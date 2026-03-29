You are a senior research scientist. Your task is to perform a meta-analysis and comparative synthesis of the multiple literature surveys provided in the `lit-survey/` directory.

The goal of this project is to **investigate metrics in the embedding space of LLMs and VLMs to understand "truth" and "trust" in videos.**

---

### INPUT FILES

Analyze and compare the following files:
1. `lit-survey/claude-lit-survey.md`
2. `lit-survey/deepseek-lit-review.md`
3. `lit-survey/gemini-lit-survey.md`
4. `lit-survey/grok-lit-review.md`
5. `lit-survey/mistral-lit-review.md`

Refer to `lit-survey/citation-index.md` for the consolidated list of references.

---

### OBJECTIVES

1. **Identify Consensus**: Pinpoint the metrics, methodologies, and foundational papers that appear across all or most surveys. Establish the "standard model" of embedding space analysis.
2. **Analyze Divergences**: Highlight areas where the surveys differ in their focus, recommendations, or conclusions. Do any models prioritize specific metrics (e.g., hyperbolic distance vs. cosine similarity) or theoretical frameworks (e.g., manifold hypothesis vs. platonic representation)?
3. **Unique Contributions**: For each survey, identify at least one unique insight, paper, or research direction that was not covered by the others.
4. **Thematic Mapping**: Group findings into high-level themes (e.g., Geometry, Cross-Modal Alignment, Probing, Applications) and compare the depth of coverage for each.
5. **Gap Analysis (Project-Specific)**: Evaluate how well the combined surveys address the specific problem of "truth" and "trust" in video representations. What is missing?
6. **Actionable Synthesis**: Propose a prioritized list of metrics and methodologies that should be carried forward into the implementation and experiment phase.

---

### OUTPUT FORMAT

Your report should be structured as follows:

1. **Executive Summary** (1 paragraph): The state of the field as synthesized from all sources.
2. **Consensus Matrix**: A table or list showing concepts/papers with high agreement across surveys.
3. **Divergence & Tension Analysis**: Detailed breakdown of where the surveys disagree or offer competing perspectives.
4. **Survey-Specific Value-Add**: A section briefly summarizing the "unique flavor" or specific strength of each model's survey.
5. **Missing Links**: A gap analysis focusing on the transition from general LLM/VLM metrics to video-specific "truth and trust" metrics.
6. **Final Recommendations**: A "Top 5" list of metrics/approaches to prioritize for the next phase of the project, with brief justifications based on the meta-analysis.

---

### CONSTRAINTS

- Be critical: If a survey contains vague or likely hallucinated citations (check against `citation-index.md`), note this as a limitation.
- Stay focused: Ensure the synthesis always points back to the ultimate goal of video truth and trust.
- Be precise: Use the specific LaTeX or mathematical terminology found in the surveys.
