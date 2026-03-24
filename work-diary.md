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
- Added literature survey drafts under `/home/daniel/git/vidiq/lit-survey`:
  - `claude-lit-survey.md`
  - `deepseek-lit-review.md`
  - `gemini-lit-survey.md`
  - `grok-lit-review.md`
  - `mistral-lit-review.md`
- Reformatted `lit-survey/gemini-lit-survey.md` from a single wall of text into structured Markdown: added numbered section headers, pipe-formatted tables, bullet and numbered lists, fixed truncated LaTeX formulas (cosine similarity and hyperbolic distance), and added horizontal rules between sections.
- Committed the untracked literature survey drafts and citation prompt with git commit `64ce284` (`Add literature survey drafts and citation prompt`).
- Pushed the `main` branch to `origin`, updating `git@github.com:dsikar/vidiq.git`.

Signed,
codex
