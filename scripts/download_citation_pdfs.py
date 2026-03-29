#!/usr/bin/env python3

import json
import xml.etree.ElementTree as ET
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path("/home/daniel/git/vidiq")
INDEX_PATH = ROOT / "lit-survey" / "citation-index.md"
OUTPUT_DIR = ROOT / "lit-survey" / "pdfs"
REPORT_PATH = OUTPUT_DIR / "download-report.md"

USER_AGENT = "vidiq-pdf-downloader/1.0 (+local automation)"
TIMEOUT = 30

BLOCKED_DOMAINS = {
    "researchgate.net",
    "www.researchgate.net",
    "academia.edu",
    "www.academia.edu",
}


@dataclass
class Citation:
    number: int
    raw: str
    normalized: str
    title: Optional[str]
    expected_year: Optional[int]
    year_range: Optional[Tuple[int, int]]


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def title_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()


def slugify_title(title: str, max_words: int = 8) -> str:
    words = [w for w in normalize_text(title).split() if w not in {"the", "a", "an", "of", "for", "and", "to", "in"}]
    words = words[:max_words] or normalize_text(title).split()[:max_words]
    return "-".join(words[:max_words])[:80].strip("-") or "paper"


def http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        return json.load(response)


def verify_pdf_url(url: str) -> Tuple[bool, str]:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            content_type = response.headers.get_content_type()
            if response.status == 200 and content_type == "application/pdf":
                return True, "verified with HEAD"
    except Exception:
        pass

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Range": "bytes=0-15",
            },
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            content_type = response.headers.get_content_type()
            chunk = response.read(16)
            if response.status in {200, 206} and (content_type == "application/pdf" or chunk.startswith(b"%PDF")):
                return True, "verified with ranged GET"
            return False, f"unexpected content type {content_type}"
    except Exception as exc:
        return False, str(exc)


def download_file(url: str, path: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
        content_type = response.headers.get_content_type()
        if content_type != "application/pdf":
            raise ValueError(f"expected application/pdf, got {content_type}")
        data = response.read()
    if not data.startswith(b"%PDF"):
        raise ValueError("response did not look like a PDF")
    path.write_bytes(data)


def parse_citations(index_text: str) -> List[Citation]:
    lines = index_text.splitlines()
    in_section = False
    citations: List[Citation] = []
    for line in lines:
        if line.strip() == "## Consolidated citations":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        match = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if not match:
            continue
        number = int(match.group(1))
        raw = match.group(2).strip()
        title_match = re.search(r'"([^"]+)"', raw)
        title = title_match.group(1).strip() if title_match else None
        year_range = None
        expected_year = None
        year_match = re.search(r"\((\d{4})(?:/(\d{4}))?\)", raw)
        if year_match:
            expected_year = int(year_match.group(1))
            if year_match.group(2):
                year_range = (expected_year, int(year_match.group(2)))
            else:
                year_range = (expected_year, expected_year)
        citations.append(
            Citation(
                number=number,
                raw=raw,
                normalized=normalize_text(raw),
                title=title,
                expected_year=expected_year,
                year_range=year_range,
            )
        )
    return citations


def year_ok(candidate_year: Optional[int], citation: Citation) -> bool:
    if citation.year_range is None or candidate_year is None:
        return True
    start, end = citation.year_range
    return start <= candidate_year <= end


def domain_allowed(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    if not host:
        return False
    return host not in BLOCKED_DOMAINS


def match_score(candidate_title: str, candidate_year: Optional[int], citation: Citation) -> float:
    if not citation.title:
        return 0.0
    score = title_similarity(candidate_title, citation.title)
    if citation.expected_year and candidate_year:
        if year_ok(candidate_year, citation):
            score += 0.05
        elif abs(candidate_year - citation.expected_year) == 1:
            score -= 0.02
        else:
            score -= 0.3
    return score


def fetch_semantic_scholar(citation: Citation) -> Optional[dict]:
    if not citation.title:
        return None
    query = urllib.parse.quote(citation.title)
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search/match"
        f"?query={query}"
        "&fields=title,year,venue,openAccessPdf,externalIds,isOpenAccess,url"
    )
    try:
        data = http_json(url)
    except Exception:
        return None
    papers = data.get("data") or []
    if not papers:
        return None
    paper = papers[0]
    if match_score(paper.get("title", ""), paper.get("year"), citation) < 0.9:
        return None
    return build_semantic_scholar_candidate(paper)


def build_semantic_scholar_candidate(paper: dict) -> dict:
    external_ids = paper.get("externalIds") or {}
    pdf_url = (paper.get("openAccessPdf") or {}).get("url")
    if not pdf_url and external_ids.get("ArXiv"):
        pdf_url = f"https://arxiv.org/pdf/{external_ids['ArXiv']}.pdf"
    if not pdf_url and external_ids.get("ACL"):
        pdf_url = f"https://aclanthology.org/{external_ids['ACL']}.pdf"
    if not pdf_url and external_ids.get("DBLP"):
        dblp_pdf = fetch_dblp_pdf(external_ids["DBLP"])
        if dblp_pdf:
            pdf_url = dblp_pdf
    return {
        "resolver": "Semantic Scholar",
        "title": paper.get("title"),
        "year": paper.get("year"),
        "pdf_url": pdf_url,
        "landing_url": paper.get("url"),
        "external_ids": external_ids,
    }


def fetch_semantic_scholar_search(citation: Citation) -> Optional[dict]:
    if not citation.title:
        return None
    query = urllib.parse.quote(citation.title)
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={query}&limit=10"
        "&fields=title,year,venue,openAccessPdf,externalIds,isOpenAccess,url"
    )
    try:
        data = http_json(url)
    except Exception:
        return None
    papers = data.get("data") or []
    best = None
    best_score = 0.0
    for paper in papers:
        score = match_score(paper.get("title", ""), paper.get("year"), citation)
        if score > best_score:
            best = paper
            best_score = score
    if best is None or best_score < 0.82:
        return None
    candidate = build_semantic_scholar_candidate(best)
    candidate["resolver"] = "Semantic Scholar Search"
    return candidate


def fetch_openalex(citation: Citation) -> Optional[dict]:
    if not citation.title:
        return None
    query = urllib.parse.quote(citation.title)
    url = f"https://api.openalex.org/works?search={query}&per-page=5"
    try:
        data = http_json(url)
    except Exception:
        return None
    results = data.get("results") or []
    best = None
    best_score = 0.0
    for item in results:
        score = match_score(item.get("display_name") or item.get("title") or "", item.get("publication_year"), citation)
        if score > best_score:
            best = item
            best_score = score
    if best is None or best_score < 0.86:
        return None
    primary = best.get("primary_location") or {}
    best_oa = best.get("best_oa_location") or {}
    pdf_url = best_oa.get("pdf_url") or primary.get("pdf_url") or (best.get("open_access") or {}).get("oa_url")
    return {
        "resolver": "OpenAlex",
        "title": best.get("display_name") or best.get("title"),
        "year": best.get("publication_year"),
        "pdf_url": pdf_url,
        "landing_url": primary.get("landing_page_url") or best.get("doi") or best.get("id"),
        "doi": best.get("doi"),
    }


def fetch_dblp_pdf(dblp_id: str) -> Optional[str]:
    url = f"https://dblp.org/rec/{dblp_id}.xml"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            data = response.read()
    except Exception:
        return None
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return None
    for ee in root.findall(".//ee"):
        link = (ee.text or "").strip()
        if link.endswith(".pdf"):
            return link
        if "aclanthology.org/" in link and not link.endswith(".pdf"):
            return link.rstrip("/") + ".pdf"
        if "arxiv.org/abs/" in link:
            return link.replace("/abs/", "/pdf/") + ".pdf"
        if "openreview.net/forum?id=" in link:
            return link.replace("/forum?id=", "/pdf?id=")
        if "proceedings.mlr.press/" in link and link.endswith(".html"):
            return link[:-5] + ".pdf"
    return None


def extract_crossref_year(item: dict) -> Optional[int]:
    for key in ("published-print", "published-online", "issued", "created"):
        parts = (((item.get(key) or {}).get("date-parts") or [[None]])[0])
        year = parts[0]
        if isinstance(year, int):
            return year
    return None


def fetch_crossref(citation: Citation) -> Optional[dict]:
    if not citation.title:
        return None
    query = urllib.parse.quote(citation.title)
    url = (
        "https://api.crossref.org/works"
        f"?query.title={query}&rows=5&select=title,DOI,link,published-print,published-online,issued,URL"
    )
    try:
        data = http_json(url)
    except Exception:
        return None
    items = ((data.get("message") or {}).get("items")) or []
    best = None
    best_score = 0.0
    for item in items:
        titles = item.get("title") or []
        title = titles[0] if titles else ""
        year = extract_crossref_year(item)
        score = match_score(title, year, citation)
        if score > best_score:
            best = item
            best_score = score
    if best is None or best_score < 0.86:
        return None
    titles = best.get("title") or []
    title = titles[0] if titles else citation.title
    doi = best.get("DOI")
    pdf_url = None
    for link in best.get("link") or []:
        if link.get("content-type") == "application/pdf" and link.get("URL"):
            pdf_url = link["URL"]
            break
    if not pdf_url and doi:
        if doi.startswith("10.18653/v1/"):
            pdf_url = f"https://aclanthology.org/{doi.split('/', 1)[1]}.pdf"
        elif doi.startswith("10.48550/arXiv."):
            pdf_url = f"https://arxiv.org/pdf/{doi.split('arXiv.', 1)[1]}.pdf"
    return {
        "resolver": "Crossref",
        "title": title,
        "year": extract_crossref_year(best),
        "pdf_url": pdf_url,
        "landing_url": best.get("URL"),
        "doi": doi,
    }


def resolve_candidate(citation: Citation) -> Tuple[Optional[dict], str]:
    if not citation.title:
        return None, "citation title was not quoted and could not be normalized confidently"

    candidates = []
    sem = fetch_semantic_scholar(citation)
    if sem:
        candidates.append(sem)
    sem_search = fetch_semantic_scholar_search(citation)
    if sem_search:
        candidates.append(sem_search)
    oa = fetch_openalex(citation)
    if oa:
        candidates.append(oa)
    crossref = fetch_crossref(citation)
    if crossref:
        candidates.append(crossref)

    if not candidates:
        return None, "no confident metadata match found"

    for candidate in candidates:
        pdf_url = candidate.get("pdf_url")
        if not pdf_url or not domain_allowed(pdf_url):
            continue
        ok, verification_note = verify_pdf_url(pdf_url)
        if ok:
            return candidate, f"matched via {candidate['resolver']} ({verification_note})"

    for candidate in candidates:
        pdf_url = candidate.get("pdf_url")
        if pdf_url and not domain_allowed(pdf_url):
            return None, f"match found but PDF host was blocked: {urllib.parse.urlparse(pdf_url).netloc}"

    return None, "metadata match found, but no downloadable PDF was verified"


def build_report_entries(results: List[dict]) -> str:
    successes = [r for r in results if r["status"] == "downloaded"]
    not_found = [r for r in results if r["status"] == "not found"]
    needs_review = [r for r in results if r["status"] == "needs review"]
    duplicates = [r for r in results if r["status"] == "duplicate version skipped"]

    def render_entry(entry: dict) -> List[str]:
        lines = [f"### Citation {entry['number']}"]
        lines.append(f"- normalized citation text: {entry['citation']}")
        lines.append(f"- status: {entry['status']}")
        lines.append(f"- source URL: {entry.get('source_url') or 'n/a'}")
        lines.append(f"- saved filename: {entry.get('saved_filename') or 'n/a'}")
        lines.append(f"- note: {entry['note']}")
        return lines

    lines = []
    lines.append(f"successes: {len(successes)}")
    lines.append(f"failures: {len(not_found)}")
    lines.append(f"needs review: {len(needs_review)}")
    lines.append(f"duplicates skipped: {len(duplicates)}")
    lines.append(f"total processed: {len(results)}")
    lines.append("")
    lines.append("# PDF Download Report")
    lines.append("")
    lines.append("Generated from `lit-survey/citation-index.md` using Semantic Scholar and OpenAlex metadata lookups, with direct PDF verification before download.")
    lines.append("")
    lines.append("## Successful downloads")
    lines.append("")
    if successes:
        for entry in successes:
            lines.extend(render_entry(entry))
            lines.append("")
    else:
        lines.append("None.")
        lines.append("")
    lines.append("## Failed or unresolved downloads")
    lines.append("")
    lines.append("### not found")
    lines.append("")
    if not_found:
        for entry in not_found:
            lines.extend(render_entry(entry))
            lines.append("")
    else:
        lines.append("None.")
        lines.append("")
    lines.append("### needs review")
    lines.append("")
    if needs_review:
        for entry in needs_review:
            lines.extend(render_entry(entry))
            lines.append("")
    else:
        lines.append("None.")
        lines.append("")
    lines.append("### duplicate version skipped")
    lines.append("")
    if duplicates:
        for entry in duplicates:
            lines.extend(render_entry(entry))
            lines.append("")
    else:
        lines.append("None.")
        lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Processed {len(results)} consolidated citations.")
    lines.append(f"Downloaded {len(successes)} PDFs, marked {len(not_found)} as not found, {len(needs_review)} as needs review, and skipped {len(duplicates)} duplicates.")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    citations = parse_citations(INDEX_PATH.read_text())
    seen_keys: Dict[str, dict] = {}
    results: List[dict] = []

    for citation in citations:
        title = citation.title
        dedupe_key = normalize_text(title or citation.raw)
        if dedupe_key in seen_keys:
            prior = seen_keys[dedupe_key]
            results.append(
                {
                    "number": citation.number,
                    "citation": citation.raw,
                    "status": "duplicate version skipped",
                    "source_url": prior.get("source_url"),
                    "saved_filename": prior.get("saved_filename"),
                    "note": f"duplicate of citation {prior['number']}",
                }
            )
            continue

        candidate, note = resolve_candidate(citation)
        if not candidate:
            status = "needs review" if citation.title else "needs review"
            if "no confident metadata match" in note:
                status = "not found"
            results.append(
                {
                    "number": citation.number,
                    "citation": citation.raw,
                    "status": status,
                    "source_url": None,
                    "saved_filename": None,
                    "note": note,
                }
            )
            continue

        filename = f"{candidate.get('year') or citation.expected_year or 'unknown'}-{slugify_title(candidate['title'])}.pdf"
        target = OUTPUT_DIR / filename
        source_url = candidate["pdf_url"]

        if target.exists():
            entry = {
                "number": citation.number,
                "citation": citation.raw,
                "status": "downloaded",
                "source_url": source_url,
                "saved_filename": filename,
                "note": f"existing file retained; {note}",
            }
            results.append(entry)
            seen_keys[dedupe_key] = entry
            continue

        try:
            download_file(source_url, target)
            entry = {
                "number": citation.number,
                "citation": citation.raw,
                "status": "downloaded",
                "source_url": source_url,
                "saved_filename": filename,
                "note": note,
            }
            results.append(entry)
            seen_keys[dedupe_key] = entry
        except Exception as exc:
            results.append(
                {
                    "number": citation.number,
                    "citation": citation.raw,
                    "status": "needs review",
                    "source_url": source_url,
                    "saved_filename": None,
                    "note": f"matched paper but download failed: {exc}",
                }
            )

        time.sleep(0.2)

    REPORT_PATH.write_text(build_report_entries(results))

    downloaded = sum(1 for r in results if r["status"] == "downloaded")
    not_found = sum(1 for r in results if r["status"] == "not found")
    needs_review = sum(1 for r in results if r["status"] == "needs review")
    duplicates = sum(1 for r in results if r["status"] == "duplicate version skipped")

    summary = {
        "total_processed": len(results),
        "successes": downloaded,
        "failures": not_found,
        "needs_review": needs_review,
        "duplicates_skipped": duplicates,
        "unresolved_numbers": [r["number"] for r in results if r["status"] != "downloaded"],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
