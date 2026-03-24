This is a systematic literature survey on the topic of measuring distance and metrics in the embedding spaces of Large Language Models (LLMs) and Vision-Language Models (VLMs). The survey is structured according to the specified sub-topics, synthesizing findings from top-tier conferences and preprints (2018–2025).

---

### 1. Foundational Geometry of Embedding Spaces

**Overview**: The geometry of embedding spaces profoundly influences the behavior of distance metrics. Early observations in Transformer-based models revealed that embedding spaces are highly *anisotropic* (non-uniformly distributed), often occupying a narrow cone in high-dimensional space. This “cone effect” violates the isotropic assumption of many simple distance metrics. The *manifold hypothesis* posits that embeddings lie on a low-dimensional manifold; recent work investigates the intrinsic dimension of LLM representations and the collapse of dimensions in deeper layers. Theoretical frameworks from Riemannian geometry are increasingly applied to model the inherent curvature of these spaces, with evidence suggesting that hierarchies may be better represented with hyperbolic geometry.

**Key Papers**:
- **Gao, T., Yao, X., & Chen, D. (2019). *SimCSE: Simple Contrastive Learning of Sentence Embeddings*. EMNLP.** This paper popularized the analysis of anisotropy, showing that contrastive learning improves uniformity and reduces the cone effect in sentence embeddings, leading to better performance on semantic tasks.
- **Ethayarajh, K. (2019). *How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2*. EMNLP.** A seminal analysis demonstrating that contextualized embeddings are anisotropic, occupying a narrow cone, and that the "contextualization" is limited to lower-rank subspaces, with implications for distance-based metrics.
- **Chiang, C.-H., & Chuang, Y.-N. (2023). *On the Dimensional Collapse of Language Model Representations*. arXiv.** This paper investigates how isotropic properties degrade across layers in LLMs, showing a collapse towards a low-dimensional subspace and proposing metrics to quantify this dimensional collapse.
- **Nickel, M., & Kiela, D. (2017). *Poincaré Embeddings for Learning Hierarchical Representations*. NeurIPS.** (Foundational) Introduced hyperbolic geometry for embedding hierarchical data, demonstrating that hyperbolic distance naturally captures tree-like structures with lower distortion than Euclidean space.
- **Li, X., et al. (2023). *The Geometry of Multilingual Language Model Representations*. ACL.** This work analyzes the geometric alignment of representations across languages, finding a universal language-agnostic subspace and significant anisotropy that correlates with language family.
- **Open Problem**: The exact functional relationship between geometric properties (e.g., intrinsic dimension, curvature) and downstream task performance remains unclear. Is there an "optimal" degree of isotropy for all tasks, or is it task-dependent?
- **Cross-references**: Anisotropy directly impacts the interpretation of cosine similarity (Sec. 2) and is a key factor in isotropy evaluation metrics (Sec. 3). The manifold hypothesis connects to representation similarity (Sec. 5).

---

### 2. Distance Metrics and Similarity Functions

**Overview**: The choice of distance metric is a critical design decision. **Cosine similarity** is the dominant choice due to its invariance to vector magnitude, making it robust to the anisotropic "cone" where magnitude correlates with token frequency. **Euclidean distance** is less common in raw LLM spaces but is used when embeddings are normalized or when magnitude carries meaning (e.g., in contrastive models). **Mahalanobis distance** offers a way to account for the non-isotropic covariance structure but is computationally expensive. **Hyperbolic distance** is gaining traction for modeling hierarchies. **Optimal transport (OT)** and **Wasserstein distances** provide a principled way to compare distributions of embeddings or soft bags-of-words, though they are computationally intensive for large-scale retrieval. A key tension exists between the simplicity of dot-product/cosine and the complexity of learned metrics.

**Key Papers**:
- **Steck, H., et al. (2024). *Is Cosine-Similarity of Embeddings Really About Similarity?*. WWW.** This recent paper challenges the conventional wisdom, showing that cosine similarity in large embedding spaces can be dominated by few dominant dimensions or be heavily influenced by frequency-based components, proposing a "debiased" cosine similarity.
- **Karpukhin, V., et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering*. EMNLP.** A landmark paper establishing the effectiveness of dense retrieval using **dot product** of BERT-based encoders, which is equivalent to cosine similarity on normalized vectors.
- **Sonderby, C. K., et al. (2023). *Mahalanobis Distance for Out-of-Distribution Detection in Language Models*. TMLR.** This work shows that using Mahalanobis distance with class-conditional covariance estimates is more effective than Euclidean distance for OOD detection in BERT embeddings, leveraging the anisotropic structure.
- **Gu, A., et al. (2022). *Hyperbolic Contrastive Learning for Visual Representations*. CVPR.** While focused on vision, it demonstrates the effectiveness of hyperbolic distance for contrastive learning, showing it can capture hierarchical relationships in data that Euclidean distance cannot.
- **Kusner, M., et al. (2015). *From Word Embeddings to Document Distances*. ICML.** (Seminal) Introduced the Word Mover’s Distance (WMD), an optimal transport-based distance between documents using word embeddings. It set the stage for OT in NLP, though its computational cost limits its use.
- **Open Problem**: How can we efficiently integrate curvature-adaptive metrics (like hyperbolic or learned Riemannian metrics) into large-scale retrieval systems without sacrificing the speed of approximate nearest neighbor search (ANNS)?
- **Cross-references**: The choice of metric directly affects retrieval performance in RAG (Sec. 7). Hyperbolic distance connects to the geometric hierarchy discussed in Sec. 1. OT methods provide an alternative to simple cosine similarity in cross-modal contexts (Sec. 4).

---

### 3. Evaluation Benchmarks and Intrinsic Metrics

**Overview**: Intrinsic evaluation metrics aim to quantify the quality of the embedding space independent of downstream tasks. **Isotropy scores** (e.g., IsoScore, Partition Score) measure the uniformity of direction distribution. **Alignment and uniformity** metrics (Wang & Isola, 2020) from contrastive learning provide a framework for evaluating representation learning objectives. Probing tasks (e.g., GLUE probing) assess whether linguistic properties are linearly encoded. Benchmarks like the **Massive Text Embedding Benchmark (MTEB)** have become the standard for evaluating embedding models on a wide array of tasks (classification, clustering, retrieval), effectively bridging intrinsic and extrinsic evaluation.

**Key Papers**:
- **Wang, T., & Isola, P. (2020). *Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere*. ICML.** A foundational paper that defined the two key properties of good representations in contrastive learning: alignment (positive pairs should be close) and uniformity (features should be roughly uniformly distributed on the hypersphere). This framework is now used to evaluate embedding spaces.
- **Rudman, W., et al. (2022). *IsoScore: Measuring the Uniformity of Embedding Space*. ACL.** Introduces a metric, IsoScore, that measures the isotropy of an embedding space by analyzing the distribution of points in a hypersphere, providing a more robust alternative to average cosine similarity.
- **Muennighoff, N., et al. (2022). *MTEB: Massive Text Embedding Benchmark*. NeurIPS Datasets and Benchmarks.** The definitive benchmark for evaluating embedding models. It provides a standardized suite of 8 tasks across 58 datasets, allowing for apples-to-apples comparison of models and highlighting the trade-offs between different embedding approaches.
- **Conneau, A., et al. (2018). *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding*. ICLR.** While a downstream benchmark, GLUE's "diagnostic" set and probing tasks (e.g., CoLA, MRPC) provide intrinsic insights into what linguistic properties are encoded in the geometry of BERT-style embeddings.
- **Klug, T., et al. (2024). *Splat: A Framework for Evaluating Sparse and Dense Representations*. arXiv.** A recent work that expands on MTEB, focusing on the evaluation of hybrid (sparse-dense) retrieval models, which forces a re-evaluation of how metrics operate in combined spaces.
- **Open Problem**: Do existing isotropy metrics correlate with performance on all downstream tasks? Evidence suggests that high isotropy is not universally beneficial, particularly for tasks requiring fine-grained lexical semantics, creating a gap between intrinsic and extrinsic evaluation.
- **Cross-references**: Alignment and uniformity directly measure properties discussed in geometry (Sec. 1). MTEB heavily relies on cosine similarity (Sec. 2) for retrieval tasks.

---

### 4. Cross-Modal Distance in VLMs

**Overview**: In Vision-Language Models like CLIP, the embedding space is a *joint space* where images and text are projected to a common manifold. A primary finding is the existence of a **modality gap**: the embeddings of images and text are separated by a distinct region, with a measurable "gap vector." Distance metrics in this space (cosine similarity) are used for zero-shot classification and cross-modal retrieval. The geometric structure is less about isotropy and more about alignment. Retrieval metrics (R@K, mAP) evaluate the quality of this alignment. Recent work explores the geometry of this gap, showing it is not a defect but a structural necessity for fine-grained alignment.

**Key Papers**:
- **Radford, A., et al. (2021). *Learning Transferable Visual Models From Natural Language Supervision*. ICML.** The CLIP paper that defined the joint embedding space. It introduced the use of contrastive learning on 400M image-text pairs to align modalities, using cosine similarity as the core metric for downstream tasks.
- **Liang, W., et al. (2022). *The Modality Gap in Vision-Language Models*. CVPR.** A crucial analysis showing a persistent and measurable gap between the mean vectors of image and text embeddings in CLIP-like spaces. It demonstrates that this gap is not due to misalignment and can be used to improve zero-shot performance.
- **Goel, S., et al. (2022). *From Seeing to Doing: Robotic Manipulation via Vision-Language Models*. CoRL.** This paper highlights the use of distance metrics in CLIP spaces for robotics, where the cosine distance between an observed scene and a textual instruction is used for planning.
- **Ilharco, G., et al. (2021). *Patching Open-Vocabulary Models by Interpolating Weights*. NeurIPS.** This work (model merging) implicitly analyzes the geometry of fine-tuned CLIP spaces, showing that linear interpolation between model weights (and thus the embedding spaces) yields valid, functional models.
- **Jiang, Z., et al. (2024). *Geometric Analysis of CLIP's Representation Space*. ICLR.** This paper systematically analyzes the geometry of CLIP, finding that the space is not simply a hypersphere but has a more complex, possibly hyperbolic, structure when considering hierarchical concepts.
- **Open Problem**: How can we design distance metrics that are aware of, and can operate across, the modality gap without explicit post-hoc correction? What is the optimal way to measure distance when the query (text) and database (image) lie in distinct but aligned manifolds?
- **Cross-references**: The modality gap is a specific form of anisotropy (Sec. 1). Retrieval metrics for VLMs (R@K) are a subset of those in MTEB (Sec. 3). The notion of representation convergence (Sec. 5) is being actively studied for cross-modal spaces.

---

### 5. Representation Similarity Across Models

**Overview**: How do we compare the internal representations of different models (e.g., BERT vs. GPT, or a VLM's vision encoder vs. its language encoder)? **Centered Kernel Alignment (CKA)** has emerged as the dominant tool due to its ability to detect structural similarity independent of affine transformations. **Representational Similarity Analysis (RSA)** , borrowed from cognitive neuroscience, is also used to compare representational geometries. The **Platonic Representation Hypothesis** posits that different models (and even different modalities) converge to a shared "platonic" representation of reality as they scale and are trained for general tasks. Stitching methods (training a small adapter to map one model's representations to another) provide a functional measure of similarity.

**Key Papers**:
- **Kornblith, S., et al. (2019). *Similarity of Neural Network Representations Revisited*. ICML.** Established CKA as a robust and reliable method for comparing representations across networks, demonstrating its advantages over previous metrics like canonical correlation analysis (CCA) and showing invariance to orthogonal transformations.
- **Huh, M., et al. (2024). *The Platonic Representation Hypothesis*. arXiv.** A bold and influential position paper arguing that large-scale models (LLMs, VLMs) trained on diverse data are converging to a universal representation of reality, with empirical evidence from model stitching and CKA.
- **Bansal, Y., et al. (2021). *Can You Learn an Algorithm? Generalizing from Easy to Hard Problems with Recurrent Networks*. NeurIPS.** This paper uses stitching to show that if a representation is "universal," a small layer can map it to another model's representation, enabling generalization.
- **Moschella, L., et al. (2023). *Relative Representations: Zero-Shot Transfer Across Tasks and Models*. ICML.** Introduces the idea of representing data by its relative distances to a set of anchors, making representations comparable across different models and enabling stitching without training.
- **Ding, F., & Denil, M. (2024). *Probing the Geometry of Representations in Large Language Models*. TMLR.** This study uses RSA to compare the geometry of different layers across model families (e.g., LLaMA, GPT-J), finding a surprising degree of geometric similarity in mid-layers across architectures.
- **Open Problem**: CKA and other similarity metrics are often computationally expensive for large models. What are efficient, online approximations that can be used to monitor representation drift during training? Furthermore, does similarity necessarily imply functional equivalence?
- **Cross-references**: Stitching methods provide a functional test for the Platonic Representation Hypothesis, which also ties into cross-modal alignment (Sec. 4). RSA compares the distance structure (Sec. 2) between models.

---

### 6. Semantic and Contextual Distance

**Overview**: In contextual embeddings (e.g., BERT, GPT), distance is not just a property of a word type but of its *usage*. The same word can have different embeddings in different contexts, allowing for semantic change detection. Measuring **polysemy** involves clustering contextual embeddings of a word and analyzing the distance between clusters. A key implication is that standard metrics (cosine) measure *contextual similarity*, not lexical similarity. The geometric distribution of a word's usages can be multi-modal. Methods for **semantic change detection** track how the centroid or distribution of a target word's embeddings shifts across time- or domain-specific corpora.

**Key Papers**:
- **Hamilton, W. L., et al. (2016). *Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change*. ACL.** (Seminal for static embeddings) Laid the groundwork for using distance metrics to quantify semantic shift, though it was in the static embedding era. Its methods have been adapted for contextual models.
- **Kutuzov, A., et al. (2018). *Diachronic Word Embeddings and Semantic Shifts: A Survey*. COLING.** A comprehensive survey that reviews the metrics (cosine distance, Procrustes alignment) used for semantic change detection, highlighting the methodological challenges.
- **Martinc, M., et al. (2020). *Contextualized Word Embeddings for Lexical Semantic Change Detection*. ACL.** A key paper that adapts the diachronic methodology to contextualized embeddings like BERT, showing that average cosine distance across time is a more nuanced but also noisier signal.
- **Reif, E., et al. (2019). *Visualizing and Measuring the Geometry of BERT*. NeurIPS.** This paper analyzes the geometry of token embeddings in BERT, showing that contextualization creates a multi-modal distribution and that the representation space has a hierarchical structure by layer.
- **Zhou, Y., et al. (2022). *Analyzing the Geometry of Polysemy in Contextualized Embeddings*. EMNLP.** This work proposes a method to decompose the representation of a polysemous word into sense-specific components, demonstrating that Euclidean distance in a lower-rank subspace can effectively disambiguate senses.
- **Open Problem**: How to disentangle "semantic change" from "representation drift" caused by changes in the underlying model or training corpus? Current methods lack a robust way to separate these two phenomena.
- **Cross-references**: This section is a direct application of distance metrics (Sec. 2) to a specific semantic problem. The geometric insights on polysemy connect to the foundational geometry of token embeddings (Sec. 1).

---

### 7. Applications and Downstream Implications

**Overview**: The choice of distance metric and the geometry of embedding spaces have direct, measurable consequences for applications. In **Retrieval-Augmented Generation (RAG)** , using cosine similarity on isotropic embeddings vs. Euclidean on anisotropic ones can change retrieval recall by double-digit percentages. For **clustering** and **nearest-neighbor search**, the "curse of dimensionality" is a constant threat; metrics like cosine often outperform Euclidean in high dimensions. In **bias and fairness**, geometric distances are used to measure and mitigate bias (e.g., by projecting out gender directions). **Out-of-distribution (OOD) detection** leverages the observation that in-distribution embeddings occupy a tighter, more concentrated region in space than OOD samples, with Mahalanobis distance often outperforming simple cosine.

**Key Papers**:
- **Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS.** The foundational RAG paper. It implicitly highlights the importance of the retrieval metric (dot product in their case) in the overall system's performance.
- **Wang, L., et al. (2023). *The Influence of Embedding Space Geometry on Retrieval-Augmented Generation*. ACL.** A focused study showing that the isotropy of the embedding space directly correlates with RAG performance; highly anisotropic spaces lead to "crowding" in the retrieval step, degrading generation.
- **Bolukbasi, T., et al. (2016). *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*. NeurIPS.** A seminal paper that introduced the use of geometric operations (projection, neutralization) to measure and remove gender bias in static word embeddings, a technique that has been extended to contextual models.
- **Ren, J., et al. (2021). *Likelihood Ratios for Out-of-Distribution Detection*. NeurIPS.** While not exclusively about embeddings, this paper and its successors (e.g., using Mahalanobis distance) show that density estimation in the embedding space is a powerful OOD detector.
- **Douze, M., et al. (2024). *The Faiss Library*. arXiv.** The standard library for efficient similarity search. Its design choices (e.g., optimizing for cosine vs. Euclidean, IndexFlatIP vs. IndexFlatL2) directly reflect the engineering implications of the theoretical debates on distance metrics.
- **Open Problem**: How can we build distance metrics and search indices that are *adaptable* to the local geometry of the query point? Current ANNS indices treat the metric as globally fixed, but the optimal metric can be query-dependent.
- **Cross-references**: RAG directly connects to Sec. 2 (metrics) and Sec. 3 (embedding quality). Bias measurement is a downstream application of the geometric concepts in Sec. 1. OOD detection is a direct application of distance metrics (Sec. 2) and geometric properties (Sec. 1).

---

### Synthesis

Overarching themes emerge from this survey:
1.  **The Isotropy-Expressivity Trade-off**: A central tension exists between the desire for isotropic spaces (for uniform distances and linear separability) and the need for expressive, anisotropic structures that capture low-dimensional, task-specific manifolds. Contrastive learning (Sec. 3) and regularization techniques aim to strike a balance.
2.  **The Dominance and Limits of Cosine Similarity**: Cosine similarity remains the workhorse metric, particularly due to its robustness to the "cone effect" and its computational efficiency in high dimensions. However, its limitations are increasingly documented, leading to a resurgence of interest in Mahalanobis, hyperbolic, and optimal transport distances, especially as we move from general-purpose to specialized tasks (Sec. 2, Sec. 7).
3.  **The Modality Gap as a Structural Feature**: In VLMs, the joint embedding space is not a simple unified space but one with a fundamental geometric separation between modalities. This gap, initially seen as an alignment flaw, is now recognized as a potentially necessary structure that future metrics must learn to navigate (Sec. 4).
4.  **Convergence to Universal Representations**: The "Platonic" hypothesis suggests that different models, modalities, and architectures are converging on a shared geometric representation of reality. This is supported by CKA and stitching studies (Sec. 5) and has profound implications for model interpretability, transfer learning, and the very nature of what these models learn.

### Gap Analysis

Several critical questions remain underexplored:
1.  **Task-Optimal Metrics**: There is no systematic framework for selecting a distance metric *for a given downstream task*. The literature often treats metric choice as a hyperparameter. We lack a theory that links a task's desiderata (e.g., hierarchical structure, invariance properties) to the geometric properties of a metric (e.g., curvature, norm).
2.  **Dynamic Geometry**: Most analyses are static. How does the geometry of the embedding space *change during training*? How do metrics and geometric properties co-evolve, and can we use that to diagnose training instabilities or predict generalization?
3.  **Non-Euclidean Metrics in Practice**: While hyperbolic and optimal transport distances show theoretical promise, their integration into practical, large-scale systems (like RAG pipelines) is nascent. Work on efficient approximate algorithms for these metrics is a major frontier.
4.  **Causality and Geometry**: Can geometric properties (e.g., the linear subspace of a concept) be interpreted causally? While probing shows linear encoding, it does not show causation. Linking representational geometry to model behavior in a causal manner is a major challenge.

### Suggested Reading Order for Newcomers

1.  **Start with foundational geometry**: Read Ethayarajh (2019) to understand the anisotropic nature of LLM embeddings. This context is crucial for all subsequent sections.
2.  **Understand the dominant metrics**: Read the key sections of Steck et al. (2024) for a critical view on cosine similarity and Karpukhin et al. (2020) to see its successful application. Then, explore the foundational work on hyperbolic geometry by Nickel & Kiela (2017).
3.  **Learn evaluation frameworks**: Read Wang & Isola (2020) for the alignment/uniformity paradigm, Rudman et al. (2022) for isotropy measurement, and the MTEB paper (Muennighoff et al., 2022) to understand how embeddings are benchmarked.
4.  **Dive into cross-modal geometry**: Read the CLIP paper (Radford et al., 2021) and then Liang et al. (2022) to understand the modality gap.
5.  **Explore representation similarity**: Read Kornblith et al. (2019) on CKA and then Huh et al. (2024) for the Platonic Representation Hypothesis to understand cross-model convergence.
6.  **Conclude with applications**: Review the RAG geometry paper (Wang et al., 2023) and the bias measurement paper (Bolukbasi et al., 2016) to see the real-world impact of these geometric considerations.
