You are a repository editing agent working inside this repository.

Your task is to add sequential numbering to the paper entries in:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

and update the file in place.

---

### OBJECTIVE

Make the `## Papers` section easier to scan by numbering every paper entry in order.

Apply numbering only to the per-paper headings and the source-file list. Do not change the
paper content itself.

---

### REQUIRED CHANGES

#### 1. Number the paper headings

In the `## Papers` section, each paper currently appears as:

`### <filename>.pdf`

Change each heading to:

`### <N>. <filename>.pdf`

where:

- numbering starts at `1`
- numbering increases by `1` for each paper
- numbering follows the current order of entries in the file

#### 2. Number the source-file list

In the `## Source files` section at the end of the file, convert the bullet list into a
numbered Markdown list using the same numbering and ordering as the `## Papers` section.

Example:

`1. first-paper.pdf`

`2. second-paper.pdf`

#### 3. Leave everything else unchanged

Do not modify:

- the report title
- the provenance note
- the summary counts
- titles, abstracts, conclusions, or notes inside each entry
- the ordering of papers

---

### VALIDATION RULES

Before finishing, verify that:

1. Every paper entry under `## Papers` is numbered exactly once.
2. The numbering is contiguous with no gaps or duplicates.
3. The `## Source files` list contains the same filenames in the same order.
4. The number of numbered paper headings matches the number of source-file entries.

---

### COMPLETION CRITERIA

When finished:

- save the updated file in place
- report how many paper entries were numbered
- report whether the source-file list was updated successfully
