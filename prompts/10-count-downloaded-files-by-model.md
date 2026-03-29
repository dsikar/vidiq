You are a repository reporting agent working inside this repository.

Your task is to count how many files have been downloaded into the model-specific folders
and write a short Markdown report.

Create the report at:

`/home/daniel/git/vidiq/reports/download-counts-by-model.md`

---

### OBJECTIVE

Produce a concise report showing the number of files present in the download folders for:

- `claude`
- `codex`
- `gemini`

Use these directories:

- `/home/daniel/git/vidiq/lit-survey/claude`
- `/home/daniel/git/vidiq/lit-survey/codex`
- `/home/daniel/git/vidiq/lit-survey/gemini`

---

### COUNTING RULES

1. Count only regular files directly inside each folder.
2. Do not count subdirectories.
3. Do not recurse into nested folders.
4. If a folder does not exist, report that clearly and use a count of `0`.

---

### OUTPUT FORMAT

Write:

`# Download Counts By Model`

Then a short note stating that the counts were generated from the model-specific folders in
`lit-survey/`.

Then a section:

`## Counts`

Include one flat bullet per model in this format:

- `Claude: <count>`
- `Codex: <count>`
- `Gemini: <count>`

If a folder is missing, include that in parentheses. Example:

- `Codex: 0 (folder not found)`

Then add:

`## Total`

with a single bullet:

- `Total files across the three model folders: <count>`

---

### VALIDATION RULES

Before finishing, verify that:

1. All three models appear exactly once in the report.
2. The total equals the sum of the three reported counts.
3. Missing folders are explicitly identified.

---

### COMPLETION CRITERIA

When finished:

- ensure `reports/download-counts-by-model.md` exists
- report the three counts
- report the total
