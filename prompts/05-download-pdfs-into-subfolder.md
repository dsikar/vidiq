You are an execution-focused research agent. You may be Codex, Claude, or Gemini. Follow these instructions exactly.

Your task is to download PDFs for the citations listed in:

`/home/daniel/git/vidiq/lit-survey/citation-index.md`

and place both the downloaded PDFs and the download report in the same agent-specific subfolder.

Determine your agent identity first and then use exactly one of these base folders:

- Codex: `/home/daniel/git/vidiq/lit-survey/codex`
- Claude: `/home/daniel/git/vidiq/lit-survey/claude`
- Gemini: `/home/daniel/git/vidiq/lit-survey/gemini`

Inside that base folder, put both the PDFs and the report in:

`/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs`

Examples:

- Codex must use `/home/daniel/git/vidiq/lit-survey/codex/pdfs`
- Claude must use `/home/daniel/git/vidiq/lit-survey/claude/pdfs`
- Gemini must use `/home/daniel/git/vidiq/lit-survey/gemini/pdfs`

This prompt is authoritative about output locations. If any earlier prompt appears to conflict, use your own agent-specific folder for both the PDFs and the report.
Do not use a shared folder such as `/home/daniel/git/vidiq/lit-survey/pdfs`.

---

### REQUIRED OUTPUTS

Create or update:

1. `/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs/`
2. `/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs/download-report.md`

Do not write the report anywhere else.

---

### DOWNLOAD INSTRUCTIONS

1. Read `citation-index.md`.
2. Process the entries in `## Consolidated citations`.
3. Skip `## Incomplete citations` on the first pass.
4. For each citation, find the best legitimate PDF source in this priority order:
   - publisher or conference PDF
   - arXiv PDF
   - official author or lab-hosted PDF
   - trusted archival sources such as ACL Anthology, OpenReview, CVF, PMLR, or proceedings pages
5. Verify the title and year before downloading.
6. If multiple versions exist, prefer:
   - peer-reviewed venue PDF
   - otherwise arXiv PDF
   - otherwise an official author-hosted PDF
7. Save each PDF into `/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs` using:
   - `year-short-title.pdf`
   - lowercase only
   - spaces replaced by hyphens
   - concise but unambiguous names
8. If two citations map to the same paper, keep one PDF only and record the other as `duplicate version skipped`.
9. If you cannot confidently identify a correct PDF, do not guess. Mark the citation `needs review` or `not found`.

---

### REPORT FORMAT

Write the report to:

`/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs/download-report.md`

At the very top of the report, include these one-line counters:

`successes: N`

`failures: N`

`needs review: N`

`duplicates skipped: N`

`total processed: N`

After that, structure the report as follows:

1. `# PDF Download Report`
2. Short provenance note
3. `## Successful downloads`
4. `## Failed or unresolved downloads`
5. `## Summary`

For every processed citation, record:

- citation number
- normalized citation text
- status: `downloaded`, `not found`, `needs review`, or `duplicate version skipped`
- source URL
- saved filename if downloaded
- short note for ambiguity, mismatch, duplicate handling, or access issues

Under `## Failed or unresolved downloads`, group entries under:

- `### not found`
- `### needs review`
- `### duplicate version skipped`

---

### DIRECTORY RULES

- Create `/home/daniel/git/vidiq/lit-survey/<agent-name>/pdfs` if needed.
- Put both the PDFs and the report in that exact folder.
- Only write inside your own agent-specific folder.
- Never write into another agent's folder.
- Never write into the shared path `/home/daniel/git/vidiq/lit-survey/pdfs`.
- Do not overwrite an existing file unless it is clearly a better version of the same paper.
- Do not place temporary or final report files outside this folder.

---

### QUALITY BAR

- Be conservative about matching.
- Avoid unofficial mirrors unless no better source exists.
- Do not download abstract pages or non-PDF placeholders.
- Keep the report audit-friendly.

---

### FINAL RESPONSE

When you are done, respond with:

1. total processed
2. successes
3. failures
4. needs review
5. duplicates skipped
6. the citation numbers for all failed or unresolved cases
7. any recurring issue patterns
