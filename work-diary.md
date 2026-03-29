# Work Diary

## March 24, 2026

- Discussed the goal for the repository: investigate metrics in the embedding space of LLMs and VLMs, with the end goal of understanding "truth" and "trust" in videos.
- Proposed an initial short memorable name: `VeritasLens`.
- Generated two name sets on request:
  - Academic-style names
  - Startup-style names
- Chosen repository name: `vidiq`.
- Created the repository folder at `/home/daniel/git/vidiq`.
- Added a starter prompt at `/home/daniel/git/vidiq/prompts/00-read-work-diary.md` instructing an AI agent to read the work diary first and then reply `Ready for work.`
- Drafted a short repository description: `Investigating embedding-space metrics for truth and trust in LLM, VLM, and video representations.`
- Added `/home/daniel/git/vidiq/README.md` describing the repository purpose, current status, and the expected agent startup workflow.
- Added `/home/daniel/git/vidiq/prompts/03-extract-citations.md`, a prompt directing an agent to extract and consolidate citations from the `lit-survey` Markdown files.
- Added `/home/daniel/git/vidiq/prompts/04-download-citation-pdfs.md`, a prompt directing an agent to download PDFs for the consolidated citation index into `lit-survey/pdfs` with an audit-friendly report.
- Added `/home/daniel/git/vidiq/prompts/05-download-pdfs-into-subfolder.md`, a follow-on prompt clarifying that both downloaded PDFs and the report must be written into the same `lit-survey/pdfs` subfolder.
- Added literature survey drafts under `/home/daniel/git/vidiq/lit-survey`:
  - `claude-lit-survey.md`
  - `deepseek-lit-review.md`
  - `gemini-lit-survey.md`
  - `grok-lit-review.md`
  - `mistral-lit-review.md`
- Generated `/home/daniel/git/vidiq/lit-survey/citation-index.md` by consolidating and deduplicating citations found across the literature survey drafts, with incomplete references separated into their own section.
- Reformatted `lit-survey/gemini-lit-survey.md` from a single wall of text into structured Markdown: added numbered section headers, pipe-formatted tables, bullet and numbered lists, fixed truncated LaTeX formulas (cosine similarity and hyperbolic distance), and added horizontal rules between sections.
- Committed the untracked literature survey drafts and citation prompt with git commit `64ce284` (`Add literature survey drafts and citation prompt`).
- Pushed the `main` branch to `origin`, updating `git@github.com:dsikar/vidiq.git`.
- Created `/home/daniel/git/vidiq/lit-survey/citation-index.md` by consolidating and deduplicating citations extracted from the Markdown files in `/home/daniel/git/vidiq/lit-survey`.
- Included a separate `Incomplete citations` section in the citation index for ambiguous, partial, or likely synthetic references that could not be normalized safely.
- Added `/home/daniel/git/vidiq/prompts/04-download-citation-pdfs.md`, a prompt directing an agent to download authoritative citation PDFs and produce a download report.
- Revised `/home/daniel/git/vidiq/prompts/04-download-citation-pdfs.md` to remove path ambiguity by requiring both the PDFs and the report to live in `/home/daniel/git/vidiq/lit-survey/pdfs`.
- Added `/home/daniel/git/vidiq/prompts/05-download-pdfs-into-subfolder.md`, an authoritative prompt instructing an agent to place both downloaded PDFs and `download-report.md` in `/home/daniel/git/vidiq/lit-survey/pdfs`.
- Required the PDF download report to begin with one-line counters for successes, failures, items needing review, duplicates skipped, and total processed.
- Created `prompts/06-compare-lit-surveys.md`, a prompt for performing a meta-analysis and comparative synthesis of the existing literature surveys, focused on identifying consensus and gaps for the "truth and trust" video objective.
- Completed the meta-analysis and comparative synthesis of the five literature surveys, resulting in the `lit-survey/meta-analysis.md` report. The analysis identified key consensus areas (anisotropy, alignment/uniformity, modality gap) and critical gaps regarding temporal dynamics and video-specific trust metrics.

Signed,
codex

## March 25, 2026

- Added `/home/daniel/git/vidiq/prompts/07-extract-title-abstract-conclusion.md`, a prompt directing an agent to read every PDF in `/home/daniel/git/vidiq/lit-survey/codex` and generate `/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`.
- Created `/home/daniel/git/vidiq/reports/` as the target directory for generated extraction reports.
- Specified in the new prompt that the report must extract, for every PDF, the paper title, abstract, and conclusion, mark missing sections as `Not found`, preserve source wording conservatively, and include a summary plus a complete processed file list.
- Prepared the new prompt and this work diary update for a dedicated commit without including the unrelated staged PDFs or other prompt changes currently present in the worktree.

## March 28, 2026

- Generated `/home/daniel/git/vidiq/reports/title-abstract-conclusion.md` from the PDFs in `/home/daniel/git/vidiq/lit-survey/codex`, then updated it so the paper entries and source-file list are numbered consistently.
- Added `/home/daniel/git/vidiq/prompts/08-reprocess-missing-extractions.md` to support a follow-up pass on missing abstracts or conclusions in the extraction report.
- Added `/home/daniel/git/vidiq/prompts/09-number-title-abstract-conclusion-entries.md` to number the entries in `reports/title-abstract-conclusion.md`.
- Added `/home/daniel/git/vidiq/prompts/10-count-downloaded-files-by-model.md` and generated `/home/daniel/git/vidiq/reports/download-counts-by-model.md` summarizing file counts in `lit-survey/claude`, `lit-survey/codex`, and `lit-survey/gemini`.
- Added `/home/daniel/git/vidiq/prompts/11-create-lit-survey-readme-review-table.md` and created `/home/daniel/git/vidiq/lit-survey/README.md`, which assigns Daniel to papers 1-42 and Pritish to papers 43-82 for manual relevance review.
- Added `/home/daniel/git/vidiq/prompts/12-find-sentiment-analysis-distance-relevance.md` and generated `/home/daniel/git/vidiq/reports/sentiment-distance-relevance.md`, a short report assessing whether the extracted papers contain prior work directly relevant to embedding-distance methods for sentiment analysis across text, images, and image sequences/video.
- Updated prompt 12 and the resulting sentiment relevance report so each listed finding includes the paper number from `reports/title-abstract-conclusion.md`.
- Pushed the recent report and README work to `origin/main` in three commits:
  - `34d6bb2` — `Add literature review README and extraction report`
  - `82ab4d9` — `Add model download counts report`
  - `9f110d1` — `Add sentiment distance relevance prompt and report`

## March 29, 2026

- Added `/home/daniel/git/vidiq/prompts/13-setup-vidiq-hpc.md` to create and initialize the `vidiq-hpc` experiments directory, which will eventually be linked to `github.com/dsikar/vidiq-hpc`.
- Actioned the prompt `13-setup-vidiq-hpc.md`:
  - Created `vidiq-hpc/` directory in the current workspace.
  - Initialized git in `vidiq-hpc/` and renamed the default branch to `main`.
  - Added the remote origin: `git@github.com:dsikar/vidiq-hpc.git`.
  - Created `vidiq-hpc/README.md` as an initial file.
  - Added `vidiq-hpc/` to the parent repository's `.gitignore`.
- Added `/home/daniel/git/vidiq/prompts/14-first-hpc-experiment-workflow.md`, an extensive workflow for the first `vidiq-hpc` experiment. This prompt guides an agent through a literature survey of datasets, model selection ($\le 8$B parameters), embedding extraction, and geometric analysis (clustering and centroid plotting) for "Happy" vs. "Sad" sentiments.
