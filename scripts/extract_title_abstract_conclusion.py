#!/usr/bin/env python3

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional


ROOT = Path("/home/daniel/git/vidiq")
PDF_DIR = ROOT / "lit-survey" / "codex"
REPORT_PATH = ROOT / "reports" / "title-abstract-conclusion.md"

TITLE_LINE_LIMIT = 120
MAX_SECTION_LINES = 260

TITLE_STOP_COMPACT = {
    "abstract",
    "summary",
    "overview",
    "keywords",
    "indexterms",
    "introduction",
}
CONCLUSION_COMPACT = {
    "conclusion",
    "conclusions",
    "discussionandconclusion",
    "discussionandconclusions",
    "conclusionandfuturework",
    "conclusionsandfuturework",
    "finalremarks",
}
END_SECTION_COMPACT = {
    "references",
    "bibliography",
    "acknowledgments",
    "acknowledgements",
    "appendix",
    "appendices",
    "supplementarymaterial",
    "supplementarymaterials",
}
AUTHOR_HINTS = (
    "@",
    "university",
    "institute",
    "department",
    "school",
    "laboratory",
    "lab",
    "arxiv",
    "conference paper",
    "proceedings",
    "correspondence",
    "equal contribution",
)


@dataclass
class Extraction:
    filename: str
    title: str
    abstract: str
    conclusion: str
    note: Optional[str]


def run_command(args: List[str]) -> str:
    result = subprocess.run(
        args,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def compact_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def clean_line(line: str) -> str:
    line = (
        line.replace("\u00ad", "")
        .replace("ﬁ", "fi")
        .replace("ﬂ", "fl")
        .replace("ﬀ", "ff")
        .replace("ﬃ", "ffi")
        .replace("ﬄ", "ffl")
    )
    line = re.sub(r"\s+", " ", line).strip()
    return line


def normalize_small_caps(text: str) -> str:
    text = re.sub(r"\s*-\s*", "-", text)
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"\b([A-Z]) ([A-Z]{2,})\b", r"\1\2", text)
        text = re.sub(r"\b([A-Z]{2,}) ([A-Z])\b", r"\1\2", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_block(lines: Iterable[str]) -> str:
    cleaned: List[str] = []
    for raw in lines:
        line = clean_line(raw)
        if not line:
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue
        if re.fullmatch(r"\d+", line):
            continue
        if line.lower().startswith(("figure ", "table ")):
            continue
        cleaned.append(line)

    paragraphs: List[str] = []
    current = ""
    for line in cleaned:
        if line == "":
            if current:
                paragraphs.append(current.strip())
                current = ""
            continue
        if not current:
            current = line
            continue
        if current.endswith("-") and not current.endswith(" -"):
            current = current[:-1] + line
        else:
            current = f"{current} {line}"
    if current:
        paragraphs.append(current.strip())
    return "\n\n".join(paragraphs).strip()


def read_pdf_text(path: Path, first_page_only: bool = False) -> str:
    args = ["pdftotext", "-layout"]
    if first_page_only:
        args += ["-f", "1", "-l", "1"]
    args += [str(path), "-"]
    return run_command(args).replace("\f", "\n")


def read_pdf_metadata_title(path: Path) -> str:
    info = run_command(["pdfinfo", str(path)])
    for line in info.splitlines():
        if line.startswith("Title:"):
            return clean_line(line.split(":", 1)[1])
    return ""


def is_generic_metadata_title(title: str, filename: str) -> bool:
    if not title:
        return True
    compact_title = compact_text(title)
    compact_filename = compact_text(Path(filename).stem)
    if compact_title == compact_filename:
        return True
    if compact_title in {"untitled", "microsoftworddocument", "article", "paper"}:
        return True
    return False


def first_nonempty_lines(text: str, limit: int = 80) -> List[str]:
    lines = [clean_line(line) for line in text.splitlines()]
    return [line for line in lines if line][:limit]


def looks_like_author_line(line: str) -> bool:
    lower = line.lower()
    return any(hint in lower for hint in AUTHOR_HINTS)


def normalize_title_candidate(title: str) -> str:
    title = normalize_small_caps(title)
    title = re.sub(r"^(published as .*? at [a-z0-9 .'-]+)\s+", "", title, flags=re.I)
    title = re.sub(r"^(accepted at [a-z0-9 .'-]+)\s+", "", title, flags=re.I)
    title = re.sub(r"\s+", " ", title).strip(" -")
    return title


def extract_title(path: Path, first_page_text: str) -> tuple[str, Optional[str]]:
    metadata_title = read_pdf_metadata_title(path)
    if not is_generic_metadata_title(metadata_title, path.name):
        return metadata_title, None

    lines = first_nonempty_lines(first_page_text)
    candidates: List[str] = []
    for line in lines:
        compact = compact_text(line)
        if compact in TITLE_STOP_COMPACT or compact.startswith("1introduction"):
            break
        if re.fullmatch(r"\d+", line):
            continue
        if looks_like_author_line(line):
            if candidates:
                break
            continue
        if len(line) > TITLE_LINE_LIMIT:
            continue
        candidates.append(line)
        if len(" ".join(candidates)) > 220:
            break

    if not candidates:
        return "Not found", "Title extraction was uncertain."

    title = normalize_title_candidate(" ".join(candidates[:4]))
    if len(title) < 6:
        return "Not found", "Title extraction was uncertain."
    return title, "Title extracted from page text because PDF metadata was unavailable."


def is_heading_like(line: str) -> bool:
    line = clean_line(line)
    if not line:
        return False
    if len(line) > 120:
        return False
    if line.endswith(".") and len(line.split()) > 10:
        return False
    if re.match(r"^\d+(\.\d+)*\s+[A-Z]", line):
        return True
    if re.match(r"^[IVXLC]+\.\s+[A-Z]", line):
        return True
    letters = re.sub(r"[^A-Za-z]", "", line)
    if letters and len(line.split()) <= 12:
        uppercase_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
        if uppercase_ratio > 0.7:
            return True
    if len(line.split()) <= 9 and line == line.title():
        return True
    return False


def collect_section(lines: List[str], start_index: int) -> str:
    collected: List[str] = []
    for index in range(start_index, min(len(lines), start_index + MAX_SECTION_LINES)):
        line = clean_line(lines[index])
        if not line:
            collected.append("")
            continue
        compact = compact_text(line)
        base_compact = re.sub(r"^\d+(?:\.\d+)*", "", compact)
        if compact in END_SECTION_COMPACT or base_compact in END_SECTION_COMPACT:
            break
        if index > start_index and is_heading_like(line):
            heading_compact = re.sub(r"^\d+(?:\.\d+)*", "", compact)
            if heading_compact not in CONCLUSION_COMPACT:
                break
        collected.append(lines[index])
    return normalize_block(collected)


def extract_abstract(full_text: str) -> str:
    lines = full_text.splitlines()
    for index, raw in enumerate(lines[:300]):
        line = clean_line(raw)
        compact = compact_text(line)
        if compact != "abstract":
            continue
        start = index + 1
        collected: List[str] = []
        for j in range(start, min(len(lines), start + MAX_SECTION_LINES)):
            current = clean_line(lines[j])
            if not current:
                collected.append("")
                continue
            compact_current = compact_text(current)
            if compact_current in {"keywords", "indexterms"}:
                break
            if compact_current == "introduction" or compact_current.startswith("1introduction"):
                break
            if j > start and is_heading_like(current):
                heading_compact = re.sub(r"^\d+(?:\.\d+)*", "", compact_current)
                if heading_compact not in {"abstract"}:
                    break
            collected.append(lines[j])
        block = normalize_block(collected)
        if block:
            return block

    joined = full_text
    inline_match = re.search(
        r"\bAbstract[.:]?\s*(.+?)(?=\n\s*(?:Keywords?\b|Index Terms\b|1\.?\s+Introduction\b|Introduction\b))",
        joined,
        flags=re.I | re.S,
    )
    if inline_match:
        block = normalize_block(inline_match.group(1).splitlines())
        if block:
            return block
    return "Not found"


def extract_conclusion(full_text: str) -> str:
    lines = full_text.splitlines()
    for index, raw in enumerate(lines):
        line = clean_line(raw)
        if not line:
            continue
        compact = compact_text(line)
        compact = re.sub(r"^\d+(?:\.\d+)*", "", compact)
        if compact not in CONCLUSION_COMPACT:
            continue
        block = collect_section(lines, index + 1)
        if block:
            return block
    return "Not found"


def build_report(extractions: List[Extraction]) -> str:
    abstracts_found = sum(item.abstract != "Not found" for item in extractions)
    conclusions_found = sum(item.conclusion != "Not found" for item in extractions)
    missing_either = sum(
        item.abstract == "Not found" or item.conclusion == "Not found"
        for item in extractions
    )

    parts = [
        "# Title, Abstract, and Conclusion Report",
        "",
        "Generated from PDFs in `lit-survey/codex`.",
        "",
        "## Summary",
        "",
        f"- Total PDFs processed: {len(extractions)}",
        f"- Abstracts found: {abstracts_found}",
        f"- Conclusions found: {conclusions_found}",
        f"- Entries missing either field: {missing_either}",
        "",
        "## Papers",
        "",
    ]

    for item in extractions:
        parts.extend(
            [
                f"### {item.filename}",
                "",
                "**Title**",
                "",
                item.title,
                "",
                "**Abstract**",
                "",
                item.abstract,
                "",
                "**Conclusion**",
                "",
                item.conclusion,
                "",
            ]
        )
        if item.note:
            parts.extend(["**Note**", "", item.note, ""])

    parts.extend(["## Source files", ""])
    parts.extend(f"- {item.filename}" for item in extractions)
    parts.append("")
    return "\n".join(parts)


def main() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf_paths = sorted(PDF_DIR.glob("*.pdf"), key=lambda path: path.name.lower())
    extractions: List[Extraction] = []

    for path in pdf_paths:
        first_page_text = read_pdf_text(path, first_page_only=True)
        full_text = read_pdf_text(path, first_page_only=False)
        title, title_note = extract_title(path, first_page_text)
        abstract = extract_abstract(full_text)
        conclusion = extract_conclusion(full_text)

        notes: List[str] = []
        if title_note:
            notes.append(title_note)
        if abstract == "Not found" or conclusion == "Not found":
            notes.append("Missing one or more sections.")

        extractions.append(
            Extraction(
                filename=path.name,
                title=title,
                abstract=abstract,
                conclusion=conclusion,
                note=" ".join(notes) if notes else None,
            )
        )

    REPORT_PATH.write_text(build_report(extractions), encoding="utf-8")

    abstracts_found = sum(item.abstract != "Not found" for item in extractions)
    conclusions_found = sum(item.conclusion != "Not found" for item in extractions)
    missing_either = sum(
        item.abstract == "Not found" or item.conclusion == "Not found"
        for item in extractions
    )
    print(f"processed={len(extractions)}")
    print(f"abstracts_found={abstracts_found}")
    print(f"conclusions_found={conclusions_found}")
    print(f"missing_either={missing_either}")


if __name__ == "__main__":
    main()
