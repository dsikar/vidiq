You are a research extraction agent working inside this repository.

Your task is to read every PDF in:

`/home/daniel/git/vidiq/lit-survey/codex`

and produce a structured Markdown report at:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

Create the `reports` directory if it does not already exist.

---

### OBJECTIVE

For every PDF in `lit-survey/codex`, extract:

1. the paper title
2. the abstract
3. the conclusion

The goal is a clean audit-friendly report that lets a researcher quickly review the high-level content of the local paper set.

---

### SCOPE

- Process all `.pdf` files found directly in `lit-survey/codex`.
- Ignore non-PDF files.
- Treat each PDF as a separate paper entry.
- Use only the content available in the local PDFs. Do not invent or infer missing text from memory or external sources.

---

### EXTRACTION RULES

1. **Title**
   - Extract the paper title as it appears in the PDF.
   - Clean obvious line-break artifacts if needed.

2. **Abstract**
   - Extract the abstract verbatim when it is clearly labeled.
   - If the PDF has no clearly labeled abstract, write `Not found`.

3. **Conclusion**
   - Prefer a section explicitly titled `Conclusion` or `Conclusions`.
   - If no such section exists, use the final summary-style section only if it is clearly functioning as the paper's conclusion, such as:
     - `Discussion and Conclusion`
     - `Conclusion and Future Work`
     - `Final Remarks`
   - If there is no clear concluding section, write `Not found`.

4. **Quality bar**
   - Preserve the original wording from the PDF as closely as possible.
   - Remove obvious page-number artifacts, broken headers, and footer noise.
   - Do not paraphrase.
   - Do not merge unrelated sections.
   - If extraction is uncertain or badly garbled, include the best conservative result and add a short note.

---

### OUTPUT FORMAT

Create:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

with this structure:

1. Title
   `# Title, Abstract, and Conclusion Report`

2. Short provenance note
   State that the file was generated from PDFs in `lit-survey/codex`.

3. Summary section
   `## Summary`

   Include:
   - total PDFs processed
   - how many abstracts were found
   - how many conclusions were found
   - how many entries were missing either field

4. Main extraction section
   `## Papers`

   For each PDF, use this template:

   `### <filename>.pdf`

   `**Title**`

   `<extracted title or Not found>`

   `**Abstract**`

   `<extracted abstract or Not found>`

   `**Conclusion**`

   `<extracted conclusion or Not found>`

   Optional:

   `**Note**`

   `<brief note only if extraction was ambiguous, noisy, or incomplete>`

5. Final section
   `## Source files`

   List every processed PDF filename in alphabetical order.

---

### ORDERING RULES

- Process files in alphabetical order by filename.
- Present entries in the report in that same alphabetical order.
- Keep each paper entry together and clearly separated from the next.

---

### COMPLETION CRITERIA

When finished:

- ensure `reports/title-abstract-conclusion.md` exists
- ensure every PDF in `lit-survey/codex` is represented exactly once
- ensure missing abstracts or conclusions are marked `Not found`
- ensure the source file list matches the processed PDFs
- report completion with the number of PDFs processed and the number of missing abstracts or conclusions
