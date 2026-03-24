You are a research operations agent working inside this repository.

Your task is to create and execute a careful plan to download PDFs for the citations listed in:

`/home/daniel/git/vidiq/lit-survey/citation-index.md`

---

### OBJECTIVE

Build a local paper library for the citation index.

Download one PDF per citation where a legitimate PDF is available, and organize the results inside:

`/home/daniel/git/vidiq/lit-survey/pdfs`

Put the report in that same folder.

---

### PLAN

1. Read `citation-index.md`.
2. Ignore the `Incomplete citations` section on the first pass.
3. For each entry in `## Consolidated citations`, identify the best legitimate source in this order:
   - publisher or conference page
   - arXiv
   - authors' official pages or lab pages
   - ACL Anthology, OpenReview, CVF, PMLR, proceedings pages, or other recognized archives
4. Prefer direct PDF links over HTML landing pages.
5. If multiple versions exist, prefer:
   - peer-reviewed conference or journal PDF
   - otherwise arXiv PDF
   - otherwise an official author-hosted PDF
6. Before downloading, verify that the paper title and year match the citation entry closely enough to avoid false matches.
7. Save PDFs into `lit-survey/pdfs` using a consistent filename format:
   - `YEAR-short-title.pdf`
   - use lowercase
   - replace spaces with hyphens
   - keep filenames short but unambiguous
8. Create a tracking file in the same folder as the PDFs:
   - `/home/daniel/git/vidiq/lit-survey/pdfs/download-report.md`
9. In that log, record for each citation:
   - citation number
   - normalized citation text
   - download status: `downloaded`, `not found`, `needs review`, or `duplicate version skipped`
   - source URL
   - saved filename if downloaded
   - short note if there was ambiguity
10. If a PDF cannot be found safely and confidently, do not guess. Mark it `needs review` or `not found`.
11. At the very top of the report, include one-line summary counts in this exact style:
   - `successes: N`
   - `failures: N`
   - `needs review: N`
   - `duplicates skipped: N`
   - `total processed: N`
12. Add a summary section later in the log with:
   - total citations processed
   - total downloads succeeded
   - total downloads failed
   - total `needs review`
   - total duplicates skipped
13. Add two explicit report sections in the log:
   - `## Successful downloads`
   - `## Failed or unresolved downloads`
14. Under `## Failed or unresolved downloads`, group entries by:
   - `not found`
   - `needs review`
   - `duplicate version skipped`

---

### DIRECTORY RULES

- Create `lit-survey/pdfs` if it does not exist.
- Do not overwrite an existing PDF unless the new file is clearly a better version of the same paper.
- If two citations refer to the same work, keep one PDF and note the duplicate in the log.

---

### QUALITY BAR

- Be conservative about matching.
- Avoid unofficial mirrors unless no authoritative source exists.
- Do not download obvious stubs, abstracts, or citation pages pretending to be PDFs.
- Keep the log complete enough that another researcher can audit every decision.

---

### OUTPUTS

Produce:

1. `lit-survey/pdfs/` with downloaded PDFs
2. `lit-survey/pdfs/download-report.md`
3. A clear final report in the agent response summarizing:
   - successful downloads
   - failed downloads
   - unresolved downloads needing manual review

---

### COMPLETION CRITERIA

When finished:
- report how many consolidated citations were processed
- report how many PDFs were downloaded
- report how many downloads failed
- report how many entries were marked `needs review`
- report how many were `not found`
- list the failed or unresolved citation numbers in the final response
- mention any recurring issues, such as incomplete metadata or likely synthetic citations
