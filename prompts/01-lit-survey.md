You are an expert ML researcher conducting a systematic literature survey. 
Your task is to survey and synthesize the academic literature on the topic of:

**Measuring Distance and Metrics in Embedding Spaces of Large Language Models (LLMs) 
and Vision-Language Models (VLMs)**

---

### SCOPE

Cover the following sub-topics, treating each as a distinct section:

1. **Foundational Geometry of Embedding Spaces**
   - Structure of embedding spaces (isotropy, anisotropy, dimensional collapse)
   - How embeddings are distributed (e.g., cone effect, uniformity)
   - Relevant theoretical frameworks (Riemannian geometry, manifold hypothesis)

2. **Distance Metrics and Similarity Functions**
   - Cosine similarity vs. Euclidean distance — when each is appropriate
   - Dot product, Mahalanobis distance, and learned metrics
   - Hyperbolic distance metrics for hierarchical structure
   - Optimal transport and Wasserstein distances applied to embeddings

3. **Evaluation Benchmarks and Intrinsic Metrics**
   - Isotropy scores (e.g., IsoScore, Average Cosine Similarity)
   - Alignment and uniformity metrics (Wang & Isola, 2020)
   - Probing tasks and embedding quality measures
   - MTEB and similar benchmarks for retrieval/semantic similarity

4. **Cross-Modal Distance in VLMs**
   - Measuring alignment between visual and textual embedding spaces (CLIP-style)
   - Cross-modal retrieval metrics (R@K, mean reciprocal rank)
   - Modality gap analysis — what it means and how it is measured
   - Geometric properties specific to joint embedding spaces

5. **Representation Similarity Across Models**
   - Centered Kernel Alignment (CKA) and variants
   - Representational Similarity Analysis (RSA)
   - Platonic Representation Hypothesis and convergence across modalities
   - Stitching/patching methods as probes of space compatibility

6. **Semantic and Contextual Distance**
   - Contextualized vs. static embeddings — metric implications
   - Semantic change detection using embedding distances
   - Measuring polysemy, ambiguity, and token-level geometry

7. **Applications and Downstream Implications**
   - Retrieval-augmented generation (RAG) — metric choice impact
   - Clustering and nearest-neighbor search in high-dimensional embedding spaces
   - Bias and fairness measurement using geometric distances
   - Out-of-distribution detection via embedding distances

---

### OUTPUT FORMAT

For each section:
- **Overview paragraph**: Summarize the key ideas, debates, and findings
- **Key papers**: List 4–8 seminal or recent papers with authors, year, venue, and a 2-sentence summary of contribution
- **Open problems**: Note 1–3 unresolved questions or active research directions
- **Cross-references**: Flag connections to other sections where relevant

At the end, provide:
- A **synthesis section** identifying overarching themes, tensions (e.g., cosine vs. Euclidean, isotropy vs. expressivity), and promising directions
- A **gap analysis** — what questions remain underexplored
- A **suggested reading order** for someone new to the field

---

### CONSTRAINTS

- Prioritize papers from NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, ECCV, and top arXiv preprints (2018–2025)
- Where possible, distinguish between findings that are model-class-specific (e.g., decoder-only LLMs vs. encoder models vs. CLIP-style VLMs)
- Be precise: avoid vague claims. If a metric has known failure modes, state them
- If a paper's findings have been contested or replicated, note this
