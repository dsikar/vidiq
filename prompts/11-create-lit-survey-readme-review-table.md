You are a repository editing agent working inside this repository.

Your task is to create:

`/home/daniel/git/vidiq/lit-survey/README.md`

---

### OBJECTIVE

Create a README for Daniel and Pritish that explains their review task and provides a table
for scoring all papers listed in the Codex-generated report.

The task is:

- Daniel and Pritish should read the title, abstract, and conclusion for every paper in:
  `/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`
- They should quantify how relevant each paper is to the task of quantifying distance between
  embeddings for:
  - text
  - single images
  - multiple images / sequences of images

---

### SOURCE OF TRUTH

Use:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

as the source of truth for:

- the paper index
- the filename
- the total number of papers

Do not invent filenames. Extract them from the numbered paper headings in that report.

---

### README CONTENT

The README should contain:

1. A short title, for example:

`# Literature Survey Review`

2. A short instruction section stating that Daniel and Pritish should read the title,
   abstract, and conclusion of every paper in the Codex report and assess relevance to the
   embedding-distance task.

3. A scoring guide that explains:

- `0` = irrelevant
- `1` = somewhat relevant
- `2` = relevant

4. A short block immediately above the table explaining the columns.

This block must explain at least:

- `Paper` = paper index from the Codex report
- `Filename` = PDF filename
- `Rev.` = reviewer
- `D` = Daniel
- `P` = Pritish
- `Score` = relevance score from `0` to `2`
- `Notes` = short justification or comments

5. A Markdown table with these exact columns:

- `Paper`
- `Filename`
- `Rev.`
- `Score`
- `Notes`

---

### TABLE REQUIREMENTS

1. The table must have exactly 82 data rows, plus the header row and separator row.
2. The `Paper` column must contain the paper index from the report (`1` through `82`).
3. The `Filename` column must contain the corresponding PDF filename from the report.
4. The `Rev.` column must be assigned as follows:
   - rows `1` through `42`: `D`
   - rows `43` through `82`: `P`
5. The `Score` column should be left blank for manual completion.
6. The `Notes` column should be left blank for manual completion.
7. Preserve the ordering from `reports/title-abstract-conclusion.md`.
8. The column-explanation block must appear immediately above the table.

---

### OUTPUT FORMAT

The table should look like this:

`| Paper | Filename | Rev. | Score | Notes |`

`| --- | --- | --- | --- | --- |`

`| 1 | example-paper.pdf | D |  |  |`

Continue until paper `82`.

---

### VALIDATION RULES

Before finishing, verify that:

1. `lit-survey/README.md` exists.
2. The table has exactly 82 data rows.
3. Paper indices run contiguously from `1` to `82`.
4. Filenames exactly match the numbered entries in `reports/title-abstract-conclusion.md`.
5. Reviewer assignments are `D` for `1` to `42` and `P` for `43` to `82`.
6. A column-explanation block appears immediately above the table and defines the reviewer abbreviations.

---

### COMPLETION CRITERIA

When finished:

- save `lit-survey/README.md`
- report that the README was created
- report that 82 paper rows were added
