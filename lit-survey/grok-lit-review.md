**1. Foundational Geometry of Embedding Spaces**

**Overview paragraph**: Embedding spaces in LLMs and VLMs are typically high-dimensional and exhibit pronounced anisotropy, where representations concentrate in a narrow cone around a dominant direction rather than uniformly filling the space; this "narrow cone effect" arises early (even at random initialization in some cases) and is linked to dimensional collapse and outlier dimensions that dominate variance. Decoder-only LLMs (e.g., GPT-style) and encoder models (e.g., BERT) both show this, though the former may preserve more hierarchical structure due to autoregressive training, while CLIP-style VLMs display additional modality-specific clustering. Theoretical frameworks emphasize the manifold hypothesis (embeddings lie on low-dimensional manifolds within ambient space) and Riemannian geometry for curved spaces; isotropy debates persist, with early views claiming it boosts expressivity (by avoiding collapse) contested by recent work showing anisotropy can encode useful structure without inherent harm.

**Key papers**:
- Ethayarajh (2019), EMNLP: "How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings" — Introduced the narrow-cone phenomenon in contextual embeddings, showing average cosine similarity near 1 forces representations into a low-dimensional cone and quantifies anisotropy across model families.
- Rudman et al. (2022), ICLR: "IsoScore: Measuring the Uniformity of Embedding Space Utilization" — Proposed IsoScore, a covariance-based metric superior to average cosine similarity for quantifying isotropy; demonstrated prior metrics were flawed and that embeddings are anisotropic but locally uniform.
- Timkey & van Schijndel (2021), EMNLP: "All Bark and No Bite: Rogue Dimensions in Transformer Language Models" — Identified "rogue" dimensions dominating variance in BERT/GPT-2 embeddings, linking anisotropy to training dynamics and proposing post-processing to mitigate.
- Gao et al. (2019), ICLR: "Representation Degeneration Problem in Training Natural Language Generation Models" — Analyzed degeneration into anisotropic cones during training; introduced CosReg regularization to encourage isotropy and improve generation quality.
- Machina et al. (2024), NAACL: "Anisotropy is Not Inherent to Transformers" — Showed anisotropy emerges from training objectives rather than architecture; demonstrated isotropic embeddings are achievable and sometimes beneficial without performance loss.
- Tyshchuk et al. (2023), Information: "On Isotropy of Multimodal Embeddings" — Extended analysis to CLIP VLMs, finding both image/text embeddings form cones at initialization but are locally isotropic; multilingual text embeddings show language-independent geometry.
- Rajaee & Pilehvar (2021), Findings EMNLP: "How Does Fine-tuning Affect the Geometry of Embedding Space?" — Found fine-tuning can exacerbate or alleviate anisotropy depending on task; distinguished effects in encoder vs. decoder LLMs.

**Open problems**: (1) Whether anisotropy is detrimental or encodes beneficial low-rank structure (debated and model-class dependent); (2) Scalable, differentiable isotropy regularization stable on mini-batches for large decoder-only LLMs; (3) Manifold dimensionality collapse in trillion-parameter models and its relation to the manifold hypothesis.

**Cross-references**: Directly informs distance metric choice (Section 2), evaluation benchmarks (Section 3), and modality gaps in VLMs (Section 4).

**2. Distance Metrics and Similarity Functions**

**Overview paragraph**: Cosine similarity is the de-facto standard for LLM/VLM embeddings because it ignores magnitude (aligning with normalized, direction-focused representations from contrastive or next-token prediction training), while Euclidean distance is equivalent on unit-norm vectors but sensitive to magnitude in unnormalized spaces and suffers curse-of-dimensionality collapse in high-d spaces; dot product is interchangeable with cosine on normalized vectors but retains scale information when relevant (e.g., some retrieval). Mahalanobis or learned metrics adapt to covariance but are rare due to compute; hyperbolic distances (Poincaré/Lorentz) better capture hierarchical structures in taxonomies or knowledge graphs within LLMs; optimal transport/Wasserstein distances treat embeddings as distributions for robust semantic alignment but scale poorly without embeddings or slicing approximations. Findings hold across decoder-only LLMs (where magnitude encodes confidence) and CLIP VLMs (directional alignment dominant).

**Key papers**:
- Wang & Isola (2020), ICML: "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere" — Formalized why contrastive losses (common in VLMs and sentence encoders) optimize angular (cosine-like) geometry on the hypersphere; introduced metrics showing alignment + uniformity predict downstream success.
- Nickel & Kiela (2017/updated analyses), NeurIPS (foundational; extended to LLMs): Poincaré embeddings — Demonstrated hyperbolic distance superior for hierarchical data vs. Euclidean; recent extensions show LLMs benefit from hyperbolic fine-tuning for taxonomy and reasoning.
- Haviv et al. (2024), ICML: "Wasserstein Wormhole: Scalable Optimal Transport Distance with Transformer" — Proposed transformer autoencoder embedding distributions so Euclidean distances approximate Wasserstein; enables fast OT on LLM token distributions.
- Yang et al. (2025), NeurIPS: "Hyperbolic Fine-Tuning for Large Language Models" — Showed LLM token embeddings inherently hyperbolic; hyperbolic distance in fine-tuning preserves hierarchy better than Euclidean/cosine for knowledge-intensive tasks.
- Moosmüller et al. (2020), arXiv (extended applications): "Linear Optimal Transport Embedding" — Characterized settings where Wasserstein/LOT embeds distributions linearly separable; applied to contextual LLM embeddings for robust similarity.
- Practical analyses (e.g., 2023–2025 surveys in Pinecone/Milvus docs and medium articles citing arXiv): Multiple works confirm cosine = Euclidean on normalized embeddings (standard in OpenAI/CLIP), but mismatch with training objective degrades RAG/retrieval.

**Open problems**: (1) Universal learned metrics that adapt to decoder-only vs. CLIP geometry without retraining; (2) Scalable hyperbolic/Wasserstein for trillion-token LLM corpora; (3) Failure modes of cosine in magnitude-sensitive OOD or bias detection.

**Cross-references**: Builds on geometry (Section 1) and feeds into intrinsic metrics (Section 3), cross-modal alignment (Section 4), and RAG applications (Section 7).

**3. Evaluation Benchmarks and Intrinsic Metrics**

**Overview paragraph**: Intrinsic metrics like IsoScore quantify isotropy/uniformity independently of labels, while alignment/uniformity (from contrastive theory) correlate strongly with downstream quality; probing tasks reveal how well geometry encodes syntax/semantics, and extrinsic benchmarks like MTEB aggregate retrieval, clustering, and similarity across 58+ datasets. Decoder-only LLMs often score lower on isotropy than encoders due to autoregressive bias, while VLMs require cross-modal variants; known failure modes include IsoScore instability on small batches and average cosine overestimating collapse.

**Key papers**:
- Rudman et al. (2022), ICLR: IsoScore paper (as above) — Provided robust isotropy metric; benchmarked BERT/GPT showing prior scores flawed.
- Wang & Isola (2020), ICML: Alignment & uniformity paper (as above) — Metrics directly optimizable and predictive of task performance in vision/language.
- Muennighoff et al. (2022), arXiv/NeurIPS track: "MTEB: Massive Text Embedding Benchmark" — Unified 8 tasks/58 datasets/112 languages; established leaderboards distinguishing encoder vs. LLM-derived embeddings.
- Kovaleva et al. (2021), various: Works on rogue dimensions and probing — Used intrinsic geometry probes to show anisotropy limits expressivity in BERT.
- Recent extensions (2023–2025): IsoScore* differentiable variants and multilingual CLIP isotropy papers.

**Open problems**: (1) Model-class-specific MTEB variants for decoder-only LLMs and VLMs; (2) Dynamic contextual (vs. static) intrinsic metrics; (3) Replicability of isotropy–performance correlations under contested claims.

**Cross-references**: Uses metrics from Sections 1–2; informs representation similarity (Section 5) and downstream apps (Section 7).

**4. Cross-Modal Distance in VLMs**

**Overview paragraph**: CLIP-style VLMs align image/text via contrastive loss but exhibit a modality gap—image and text embeddings cluster in separate hypersphere regions despite paired training—measurable as center-distance or smallest hyperplane angle; this stems from dimension collapse and initialization cone effect, hurting fine-grained retrieval and zero-shot. Cross-modal retrieval uses R@K/MRR; gap mitigation (e.g., mean-shift, adapters) improves alignment without forgetting. Specific to joint spaces: intra-modal misalignment persists even if inter-modal is strong.

**Key papers**:
- Liang et al. (2022), NeurIPS: "Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning" — First formalized and measured the modality gap in CLIP; linked to initialization and temperature.
- Yi et al. (2024/2025), ICLR/OpenReview: "Decrypt Modality Gap in Multimodal Contrastive Learning" — Proved dimension collapse causes the gap mathematically; showed perfect alignment impossible under subspace constraints.
- Eslami et al. (2024), ICLR: "Mitigate the Gap: Investigating Approaches for Improving Cross-Modal Alignment in CLIP" — Introduced AlignCLIP; reduced gap and boosted zero-shot/fine-tuning performance.
- Mistretta et al. (2025), ICLR: "Cross the Gap: Exposing the Intra-modal Misalignment in CLIP via Modality Inversion" — Revealed intra-modal misalignment from contrastive objective; modality inversion exposes it.
- Yamaguchi et al. (2025), CVPR: "Post-pre-training for Modality Alignment in Vision-Language Foundation Models" — Lightweight post-training closes gap while preserving uniformity.

**Open problems**: (1) Theoretical bounds on gap in billion-parameter VLMs; (2) Gap in non-CLIP VLMs (e.g., decoder-only multimodal); (3) Impact on generative vs. discriminative downstream tasks.

**Cross-references**: Geometry (Section 1), metrics (Section 2), Platonic convergence (Section 5).

**5. Representation Similarity Across Models**

**Overview paragraph**: CKA measures linear/kernel alignment of representation matrices (scale-invariant, robust to dimensionality); RSA uses dissimilarity matrices; both show increasing similarity with scale. The Platonic Representation Hypothesis posits convergence to a shared statistical model of reality across modalities/architectures as models grow. Stitching/patching probes compatibility by linear maps between spaces. Holds for LLMs/VLMs but contested in small models.

**Key papers**:
- Kornblith et al. (2019), NeurIPS: Seminal CKA paper — Introduced CKA for comparing NN layers/models; became standard for representational similarity.
- Huh et al. (2024), arXiv: "The Platonic Representation Hypothesis" — Showed vision/language models converge in distance measurements with scale; hypothesized shared "Platonic" reality model.
- Recent CKA variants (2024–2025, e.g., attention-weighted CKA in distillation papers) — Adapted for cross-modal/LLM layers.
- Kriegeskorte et al. (2008/updated): RSA foundational; modern LLM applications compare token embeddings.
- Stitching works (e.g., 2024–2025 OpenReview papers on linear structure in VLMs).

**Open problems**: (1) Causal drivers of Platonic convergence vs. data artifacts; (2) CKA limitations in non-Euclidean or contextual spaces; (3) Similarity across vastly different modalities/scales.

**Cross-references**: Uses geometry/metrics (1–3); links to semantic distance (Section 6) and Platonic themes in synthesis.

**6. Semantic and Contextual Distance**

**Overview paragraph**: Contextual embeddings (LLMs) make distances dynamic per token/sentence (vs. static word2vec), enabling polysemy measurement via intra-word variance or clustering; semantic change detection uses distance between diachronic embeddings or prompting LLMs for shifts. Failure modes: high-dimensional collapse makes small contextual shifts hard to detect reliably. Decoder-only LLMs excel at instance-level ambiguity due to autoregression.

**Key papers**:
- Hamilton et al. (2016/updated with LLMs, e.g., 2023–2025 arXiv on lexical change with BERT/LLMs) — Classic diachronic distance; LLM prompting extensions.
- Multiple 2023–2025 papers (e.g., on LLM lexical semantic change detection) — Use contextual distances/probing for polysemy/ambiguity.
- Contextual geometry papers (ICLR 2021 "Isotropy, Clusters, Manifolds").

**Open problems**: (1) Reliable token-level polysemy metrics robust to anisotropy; (2) Temporal semantic change in streaming LLMs; (3) Contextual vs. static distance consistency.

**Cross-references**: Relies on all prior; informs bias/OOD (Section 7).

**7. Applications and Downstream Implications**

**Overview paragraph**: In RAG, cosine (vs. Euclidean) impacts retrieval precision (better for normalized embeddings); clustering/NN search suffers curse in anisotropic spaces (approximate methods help). Geometric distances detect bias (e.g., gender subspaces) and OOD (distance from manifold); fairness requires careful metric choice to avoid amplifying gaps. Decoder LLMs vs. VLMs differ in OOD sensitivity.

**Key papers**:
- MTEB/RAG analyses (2022–2025) — Show metric mismatch degrades retrieval.
- Bias/fairness geometric papers (various 2020–2025); OOD via embeddings (Ren et al. 2023 extensions).
- Practical RAG distance evaluations (2025 arXiv).

**Open problems**: (1) Metric-agnostic RAG for mixed model classes; (2) Fairness metrics in joint VLM spaces; (3) Scalable OOD in trillion-parameter embeddings.

**Cross-references**: All prior sections culminate here.

**Synthesis section**: Overarching themes include convergence toward Platonic, shared geometry despite training differences, and tension between isotropy (expressivity/uniformity) and useful anisotropy (structure/hierarchy). Cosine dominates due to hyperspherical training but Euclidean/Wasserstein offer robustness in specific regimes; modality gaps highlight CLIP-specific pathologies absent in unified architectures. Promising directions: hyperbolic/OT hybrids, differentiable intrinsic metrics, and scale-driven Platonic alignment.

**Gap analysis**: Underexplored: decoder-only LLM-specific geometry (most work on encoders/CLIP); dynamic contextual distances in long-context models; fairness/bias in multi-modal joint spaces; empirical replication of Platonic hypothesis beyond 2024 scales; and real-world RAG/OOD impact of contested isotropy claims. Theoretical gaps remain in linking Riemannian manifold geometry to autoregressive objectives.

**Suggested reading order** (for newcomers): (1) Ethayarajh (2019) + Rudman IsoScore (geometry basics); (2) Wang & Isola (2020) (metrics foundation); (3) Liang et al. (2022) modality gap + Huh et al. (2024) Platonic (cross-modal convergence); (4) MTEB (2022) + CKA papers (evaluation); (5) Recent applications (RAG/OOD) and hyperbolic/OT extensions. This builds intuition before advanced debates.
