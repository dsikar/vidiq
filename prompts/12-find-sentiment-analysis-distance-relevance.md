You are a research analysis agent working inside this repository.

Your task is to review:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

and determine whether any papers appear relevant to quantifying distance between embeddings in
the context of sentiment analysis for:

- text
- single images
- sequences of images / video

Create the output report at:

`/home/daniel/git/vidiq/reports/sentiment-distance-relevance.md`

---

### OBJECTIVE

Scan the title, abstract, and conclusion entries in the report and identify papers that appear
relevant to the following research question:

How can distance between embeddings be quantified for sentiment-analysis tasks across textual,
image, or sequence-of-images data?

The goal is to find:

- directly relevant prior work
- partially relevant enabling work
- cross-modal or metric-learning work that may transfer to this problem

If no papers are clearly relevant, that is acceptable and should be stated explicitly as a sign
that the proposed work may be novel.

---

### SOURCE OF TRUTH

Use only the contents of:

`/home/daniel/git/vidiq/reports/title-abstract-conclusion.md`

Do not use outside knowledge or external sources.

---

### RELEVANCE CRITERIA

Treat a paper as relevant if the title, abstract, or conclusion suggests one or more of the
following:

1. It studies distances, similarity measures, or geometry of embeddings for text, images, or
   video-like sequential visual data.
2. It addresses sentiment, affect, emotion, opinion, or related semantic polarity tasks.
3. It studies cross-modal alignment or embedding comparison in a way that could plausibly be
   transferred to sentiment-analysis settings.
4. It proposes methods for comparing embeddings over sequences, temporal representations, or
   multimodal inputs that might matter for video sentiment analysis.

Do not overclaim relevance. If a paper is only loosely connected, mark it as weak or indirect
relevance in the comment.

---

### OUTPUT FORMAT

Write a short Markdown report with this structure:

`# Sentiment Analysis Distance Relevance`

Then a brief note stating that the assessment was based only on the Codex-generated
title/abstract/conclusion report.

Then:

`## Relevant Papers`

If relevant papers are found, include a flat bullet list. Each bullet must contain:

- the paper number from `reports/title-abstract-conclusion.md`
- the paper title
- the filename in parentheses
- a short comment explaining why it seems relevant
- a brief strength label such as `direct`, `indirect`, or `weak`

Example format:

- `29. Paper Title` (`file.pdf`) — indirect relevance: discusses embedding geometry for sentence representations, which could inform sentiment-distance modelling for text.

Then:

`## Assessment`

Write a short paragraph summarizing whether the report contains:

- direct evidence of prior work on embedding-distance methods for sentiment analysis
- only adjacent or enabling work
- or no meaningful matches

If no relevant papers are found, explicitly say that this may indicate the proposed work is
novel.

---

### VALIDATION RULES

Before finishing, verify that:

1. The report cites only papers present in `reports/title-abstract-conclusion.md`.
2. Every listed paper includes the paper number, title, and filename.
3. Every listed paper has a short relevance comment.
4. The assessment explicitly states whether the evidence is direct, indirect, or absent.

---

### COMPLETION CRITERIA

When finished:

- ensure `reports/sentiment-distance-relevance.md` exists
- report how many papers were listed as relevant
- state whether the outcome suggests prior art, adjacent work, or likely novelty
