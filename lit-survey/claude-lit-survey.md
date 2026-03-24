# Measuring Distance and Metrics in Embedding Spaces of Large Language Models and Vision-Language Models

**A Systematic Literature Survey**

*Prepared: March 2025 | Scope: 2018–2025 | Venues: NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, ECCV, arXiv*

---

## Table of Contents

1. Foundational Geometry of Embedding Spaces
2. Distance Metrics and Similarity Functions
3. Evaluation Benchmarks and Intrinsic Metrics
4. Cross-Modal Distance in VLMs
5. Representation Similarity Across Models
6. Semantic and Contextual Distance
7. Applications and Downstream Implications
8. Synthesis
9. Gap Analysis
10. Suggested Reading Order

---

## Section 1: Foundational Geometry of Embedding Spaces

### Overview

The geometric properties of embedding spaces produced by neural language and vision models are far from random or uniform — they exhibit systematic structure that profoundly affects how distances should be interpreted and computed. Two interrelated phenomena dominate the literature: **anisotropy** (the tendency of learned representations to occupy a narrow cone rather than the full hypersphere) and **dimensional collapse** (the tendency for representations to span far fewer effective dimensions than the nominal embedding size). These properties were first systematically documented for static word embeddings and have since been confirmed, in modified forms, for contextualised encoders such as BERT and for decoder-only language models.

Ethayarajh (2019) showed that BERT, GPT-2, and ELMo all produce highly anisotropic representations: randomly sampled token vectors have unexpectedly high cosine similarity even when semantically unrelated, a phenomenon sometimes called the **cone effect**. This is theoretically problematic because it compresses the effective representational capacity of the space and inflates cosine similarity scores between arbitrary pairs. Mu & Viswanath (2018) demonstrated an analogous effect in word2vec and GloVe, proposing a post-hoc "all-but-the-top" correction that subtracts the dominant principal components to restore isotropy.

The **manifold hypothesis** — the assumption that natural data, including text and images, lies on or near a low-dimensional manifold embedded in a high-dimensional ambient space — provides a theoretical basis for why high-dimensional embeddings can still be compact. However, the precise geometry of this manifold (curvature, topology, dimensionality) is model- and layer-dependent. Fang et al. (2022) demonstrated that the intrinsic dimensionality of BERT representations varies substantially across layers, with middle layers often exhibiting the highest effective dimension.

More recently, the **uniformity–alignment** framework (Wang & Isola, 2020) has provided a cleaner normative lens: a good representation should be *aligned* (semantically similar inputs map to nearby points) and *uniform* (feature vectors spread evenly over the unit hypersphere). These two objectives are often in tension. Contrastive learning methods such as SimCSE and CLIP push toward both properties but rarely achieve them simultaneously.

There is also an important distinction between **encoder models** (e.g., BERT, RoBERTa) and **decoder-only LLMs** (e.g., GPT-3, LLaMA). In decoder-only models, embeddings extracted from intermediate layers are not trained with explicit representation objectives; their geometry is therefore less well-characterised. Cai et al. (2021) found that last-token representations in decoder models tend to be even more anisotropic than encoder models, likely due to the autoregressive training objective.

### Key Papers

**1. Ethayarajh, K. (2019). "How Contextual Are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings." EMNLP 2019.**
Quantified anisotropy in BERT, ELMo, and GPT-2 by measuring the average cosine similarity of random vector pairs across layers. Found that upper layers of all three models produce increasingly anisotropic, context-specific representations; demonstrated that the "cone effect" means naive cosine similarity is an unreliable semantic proxy without correction.

**2. Mu, J., & Viswanath, P. (2018). "All-but-the-Top: Simple and Effective Postprocessing for Word Representations." ICLR 2018.**
Showed that static word embeddings (word2vec, GloVe) have a small number of dominant directions that artificially inflate pairwise cosine similarity. Proposed subtracting the top principal components as a simple post-processing step; demonstrated consistent improvements on word similarity and analogy benchmarks.

**3. Wang, T., & Isola, P. (2020). "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere." ICML 2020.**
Formalised alignment (proximity of positive pairs) and uniformity (entropy of the distribution over the unit sphere) as two complementary objectives for representation quality. Provided closed-form expressions for both metrics and showed they explain the success of contrastive learning methods including SimCLR and MoCo.

**4. Gao, T., Yao, X., & Chen, D. (2021). "SimCSE: Simple Contrastive Learning of Sentence Embeddings." EMNLP 2021.**
Introduced dropout-based data augmentation for contrastive sentence embedding, achieving state-of-the-art on STS benchmarks by explicitly optimising alignment and uniformity. Demonstrated that anisotropy in BERT's pooled CLS representations is the primary bottleneck for semantic similarity tasks.

**5. Cai, X., Huang, J., Bian, Y., & Church, K. (2021). "Isotropy in the Contextual Embedding Space: Clusters and Manifolds." ICLR 2021.**
Revealed that contextual embeddings are not uniformly anisotropic but cluster into distinct local cones, one per WordPiece token. This "local isotropy within global anisotropy" structure challenges both the uniform-cone model and naive uniformity-restoration approaches.

**6. Bis, D., Macháček, M., & Žabokrtský, Z. (2021). "Too Much in Common: Shifting of Embeddings in Transformer Language Models and its Implications." NAACL 2021.**
Demonstrated that across-layer averaging (mean pooling) exacerbates anisotropy in transformer models by up-weighting the dominant constant component. Showed that layer-wise normalisation strategies partially mitigate this effect for downstream retrieval tasks.

**7. Fang, H., Wang, S., Zhou, M., Ding, J., & Xie, P. (2022). "CERT: Contrastive Self-supervised Learning for Language Understanding." arXiv 2022.**
Measured effective intrinsic dimensionality across transformer layers using the participation ratio metric; found that self-supervised contrastive fine-tuning substantially increases effective dimensionality in upper layers, correlating with improved downstream performance.

**8. Rudman, W., Gillman, N., Talmor, A., & Eickhoff, C. (2022). "IsoScore: Measuring the Uniformity of Embedding Space Utilization." ACL Findings 2022.**
Introduced IsoScore, a metric for measuring how uniformly an embedding space is used based on the eigenvalue distribution of the covariance matrix; showed that IsoScore correlates with downstream task performance better than average cosine similarity anisotropy measures.

### Open Problems

1. **Layer-selection for geometry analysis.** Most analyses focus on a single layer (last, first, or mean), but embedding geometry changes dramatically across layers. No principled theory explains which layer's geometry is most predictive of downstream task performance for different model architectures.

2. **Geometry in decoder-only LLMs at scale.** The geometric characterisation of embeddings from models such as GPT-4, LLaMA-3, or Mixtral remains largely unexplored, partly due to access constraints. It is unclear whether the anisotropy documented in earlier, smaller models persists, worsens, or diminishes with scale.

3. **The relationship between training objective and emergent geometry.** While contrastive objectives provably improve uniformity, the precise mechanism by which masked language modelling produces anisotropic spaces is not fully understood. Theoretical accounts (e.g., spectral arguments) exist but have not been experimentally validated at scale.

### Cross-References

- The alignment/uniformity framework is directly operationalised in **Section 3** (evaluation benchmarks).
- Anisotropy has major implications for cosine similarity as a distance metric (**Section 2**).
- Layer-dependent geometry is relevant to contextualised vs. static embeddings (**Section 6**).

---

## Section 2: Distance Metrics and Similarity Functions

### Overview

Choosing an appropriate distance or similarity function for embedding spaces is not merely an engineering detail — it encodes an implicit assumption about the geometry of the space. The dominant choice in the NLP and information retrieval literature has been **cosine similarity**, motivated by its invariance to vector magnitude and its robustness under anisotropy (to some degree). However, cosine similarity is not a metric in the formal sense (it violates the triangle inequality when converted naively to a distance), and its appropriateness depends critically on the isotropy and normalisation of the embedding space.

**Euclidean distance** (L2) is theoretically well-motivated in isotropic, normalised spaces but becomes unreliable in high-dimensional anisotropic spaces due to concentration of measure and the curse of dimensionality. When embeddings are L2-normalised onto the unit hypersphere, cosine similarity and Euclidean distance are monotonically related, making the choice between them moot in well-normalised settings. However, most pre-trained models do not produce L2-normalised outputs, and the norms of contextual embeddings carry meaningful information (e.g., rare tokens tend to have larger norms in some models).

The **dot product** (unnormalised inner product) is used extensively in large-scale retrieval systems (e.g., dense passage retrieval for RAG) and is the basis for attention mechanisms. It is sensitive to vector magnitude and is not symmetric in the same way as cosine similarity, but it is computationally efficient for approximate nearest-neighbour search using FAISS or ScaNN. The Maximum Inner Product Search (MIPS) problem is distinct from nearest-neighbour search under Euclidean distance and requires different algorithmic approaches.

**Mahalanobis distance** accounts for the covariance structure of the embedding distribution, effectively "whitening" the space before computing Euclidean distance. It has been used successfully for out-of-distribution detection (Lee et al., 2018) and for computing semantically-adjusted distances in anisotropic spaces. Its practical limitation is that estimating the full covariance matrix is O(d²) in space and requires a sufficient number of reference samples.

**Hyperbolic distance metrics** (specifically, the Poincaré disk or Lorentz model) offer a principled way to represent hierarchical structure in embeddings. Nickel & Kiela (2017) demonstrated that word hyponymy hierarchies can be embedded with exponentially lower distortion in hyperbolic space than in Euclidean space of the same dimension. Subsequent work has extended this to sentences and knowledge graph entities, though integrating hyperbolic geometry into transformer architectures remains technically challenging.

**Optimal transport (OT) distances**, particularly the **Wasserstein distance** (earth mover's distance), treat a sentence or document as a distribution over word or token embeddings and measure the minimum "transport cost" to morph one distribution into another. Kusner et al. (2015) introduced Word Mover's Distance (WMD), which was the seminal application. More recent work uses Sinkhorn regularisation for computational tractability and has shown strong performance on semantic similarity and retrieval tasks where word order matters less than bag-of-words composition. OT distances are expensive to compute exactly (O(n³)) but practical approximations exist.

A growing line of work learns **metric functions** directly from data. Approaches include Siamese networks with contrastive or triplet loss, metric meta-learning (Prototypical Networks), and more recently learning a full bilinear form (generalised Mahalanobis) jointly with the encoder. These learned metrics can outperform fixed functions when in-domain training data is available but tend to overfit in low-data regimes.

### Key Papers

**1. Reimers, N., & Gurevych, I. (2019). "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks." EMNLP 2019.**
Fine-tuned BERT with a siamese architecture using a regression objective over cosine similarity for NLI pairs, producing sentence embeddings optimised for cosine-based semantic similarity. Showed that pooled BERT representations without fine-tuning are poor for cosine ranking and require explicit training for the metric to be meaningful.

**2. Kusner, M., Sun, Y., Kolkin, N., & Weinberger, K. (2015). "From Word Embeddings to Document Distances." ICML 2015.**
Introduced Word Mover's Distance (WMD), computing the minimum cost to transport one document's word embedding distribution to another's using Earth Mover's Distance. Achieved state-of-the-art on text classification without supervision; established OT as a viable document distance framework.

**3. Nickel, M., & Kiela, D. (2017). "Poincaré Embeddings for Learning Hierarchical Representations." NeurIPS 2017.**
Demonstrated that embedding lexical hierarchies (WordNet) in the Poincaré disk model of hyperbolic space achieves dramatically lower distortion than Euclidean embeddings of comparable dimension. Introduced the first practical gradient descent procedure for learning hyperbolic embeddings; foundational paper for geometric NLP.

**4. Nickel, M., & Kiela, D. (2018). "Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry." ICML 2018.**
Extended hyperbolic embeddings to the Lorentz (hyperboloid) model, which has numerical advantages over the Poincaré disk. Demonstrated faster convergence and better accuracy on transitive closure prediction for large hierarchies.

**5. Lee, K., Lee, K., Lee, H., & Shin, J. (2018). "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks." NeurIPS 2018.**
Applied Mahalanobis distance in feature space (computed class-conditionally) as an OOD detector, showing it outperforms confidence-based baselines across multiple architectures. Established the class-conditional Mahalanobis distance as a standard OOD detection baseline.

**6. Kolouri, S., Park, S. R., Thorpe, M., Slepcev, D., & Rohde, G. K. (2017). "Optimal Mass Transport: Signal Processing and Machine-Learning Applications." IEEE Signal Processing Magazine.**
Comprehensive tutorial on Wasserstein/optimal transport distances and their computational variants (sliced Wasserstein, Sinkhorn). Not NLP-specific but provides theoretical foundations used extensively in subsequent embedding comparison work.

**7. Cuturi, M. (2013). "Sinkhorn Distances: Lightspeed Computation of Optimal Transport." NeurIPS 2013.**
Introduced entropic regularisation of optimal transport, enabling computation of approximate Wasserstein distances in near-linear time via the Sinkhorn-Knopp algorithm. Made OT-based embedding distances computationally practical; enables all modern applications of WMD at scale.

**8. Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. (2020). "Dense Passage Retrieval for Open-Domain Question Answering." EMNLP 2020.**
Introduced the DPR framework for dense retrieval, using dot product as the similarity function between dual-encoder query and passage embeddings trained with in-batch negatives. Showed that learned dense retrieval with dot product substantially outperforms BM25 on open-domain QA; foundational RAG paper.

### Open Problems

1. **Metric selection for heterogeneous corpora.** There is no principled framework for selecting among cosine, dot product, Euclidean, and OT distances for a given dataset without empirical search. The field lacks theoretical conditions under which one metric dominates another as a function of corpus and model properties.

2. **Hyperbolic embedding at scale.** Training large transformers entirely or partially in hyperbolic space remains numerically unstable (gradient explosion on the boundary of the Poincaré disk). Hybrid Euclidean–hyperbolic architectures have been proposed but not yet adopted in production models.

3. **Asymmetric similarity.** Many semantic relationships are directionally asymmetric (hypernymy, entailment, prerequisite), but symmetric distances dominate the field. Asymmetric similarity functions (e.g., KL divergence, Bregman divergences) are underexplored for embedding-space search.

### Cross-References

- The appropriateness of cosine similarity is tied to isotropy/anisotropy conditions discussed in **Section 1**.
- Mahalanobis distance is a standard baseline for OOD detection (**Section 7**).
- OT distances have been applied to cross-modal alignment measurement (**Section 4**).

---

## Section 3: Evaluation Benchmarks and Intrinsic Metrics

### Overview

Evaluating embedding quality is a multi-faceted problem requiring both **intrinsic** metrics (measuring geometric properties of the space itself) and **extrinsic** benchmarks (measuring performance on downstream tasks). The field has progressively moved toward standardised extrinsic benchmarks — most notably **MTEB** (Massive Text Embedding Benchmark) — while also developing increasingly rigorous intrinsic metrics that go beyond simple anisotropy measurements.

For intrinsic evaluation, the most commonly used proxy has been **average cosine similarity (ACS)** between random sentence pairs: a perfectly isotropic space would have ACS ≈ 0, while anisotropic spaces have ACS near 1. This metric is simple and widely used but has documented failure modes: a space could have low ACS while still exhibiting severe dimensional collapse (Rudman et al., 2022). IsoScore (Rudman et al., 2022) improves on ACS by measuring the eigenvalue entropy of the embedding covariance matrix, penalising both low-rank structure and variance concentration in a subset of dimensions.

**Wang & Isola's (2020) alignment and uniformity metrics** have become a standard pair for evaluating contrastive sentence representations. Alignment measures the average distance between embeddings of positive pairs (semantically equivalent sentences), while uniformity measures the log of the average pairwise Gaussian kernel (a proxy for entropy). These two metrics are in tension: maximising alignment encourages collapse (all embeddings to a single point), while maximising uniformity pushes embeddings apart. The best models balance both.

**Probing tasks** evaluate whether specific linguistic properties (syntax, morphology, semantic roles) are linearly decodable from embeddings. The probing paradigm (Conneau et al., 2018; Tenney et al., 2019) has generated enormous insight into the layer-wise information content of transformer models. However, the interpretation of probing results is contested: high probing accuracy could reflect either that the information is genuinely encoded in the representation or that the probing classifier itself is performing the extraction. Hewitt & Liang (2019) proposed selectivity — comparing probing accuracy against a random-baseline control task — as a corrective measure.

For extrinsic evaluation, **MTEB** (Muennighoff et al., 2023) is the most comprehensive benchmark, covering 56 datasets across 8 task types (classification, clustering, pair classification, reranking, retrieval, STS, summarisation, bitext mining) and 112 languages. MTEB has become the de facto standard for comparing sentence embedding models, with a public leaderboard. Its main limitation is that it conflates retrieval performance (which depends on metric choice and approximate NN algorithm) with representation quality per se.

For sentence-level semantic similarity specifically, the **STS-B benchmark** (Cer et al., 2017) and its variants (STS12–STS16) remain widely used, measuring Spearman correlation between model cosine similarities and human-annotated similarity scores. Criticism has been levelled at STS benchmarks for (a) ceiling effects for recent models, (b) potential annotation artefacts, and (c) not testing retrieval at scale (Reimers, 2022).

**BERTScore** (Zhang et al., 2020), while primarily a generation evaluation metric, can be viewed as a grounded application of embedding distances: it matches token-level embeddings of candidate and reference text using greedy alignment, computing precision/recall/F1 over cosine similarities. It has been both widely used and criticised for being sensitive to the choice of embedding model and for correlating imperfectly with human judgement on certain domains.

### Key Papers

**1. Muennighoff, N., Tazi, N., Magne, L., & Reimers, N. (2023). "MTEB: Massive Text Embedding Benchmark." EACL 2023.**
Introduced a comprehensive benchmark for text embedding models covering 56 diverse tasks across 8 categories. Evaluated 33 models including OpenAI's text-embedding-ada-002 and multiple S-BERT variants; established that no single model dominates all task types, and that retrieval and STS performance are weakly correlated. Standard reference for embedding model evaluation.

**2. Conneau, A., Kruszewski, G., Lample, G., Barrault, L., & Baroni, M. (2018). "What You Can Cram into a Single Vec and What You Can't: Probing Sentence Embeddings for Linguistic Properties." ACL 2018.**
Introduced 10 probing tasks testing morphological, syntactic, and semantic properties of sentence embeddings. Demonstrated that LSTM-based encoders encode more syntactic information in upper layers; established probing as the standard methodology for interpretability of sentence representations.

**3. Tenney, I., Das, D., & Pavlick, E. (2019). "BERT Rediscovers the Classical NLP Pipeline." ACL 2019.**
Applied edge probing to BERT to show that lower layers capture morphology and syntax, middle layers capture semantic roles, and upper layers capture coreference — a rough rediscovery of the classical NLP pipeline. Important methodological paper for layer-wise analysis.

**4. Hewitt, J., & Liang, P. (2019). "Designing and Interpreting Probes with Control Tasks." EMNLP 2019.**
Proposed "selectivity" as a corrective measure for probing tasks: compare task accuracy against a control task (same input, random labels). Showed that high probing accuracy is a necessary but not sufficient condition for genuine encoding; many reported probing results were inflated by classifier capacity.

**5. Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., & Artzi, Y. (2020). "BERTScore: Evaluating Text Generation with BERT." ICLR 2020.**
Used contextual BERT embeddings and greedy token-level cosine alignment to compute precision/recall/F1 between candidate and reference text. Showed higher correlation with human judgements than BLEU/ROUGE on MT and image captioning; widely adopted but with known sensitivity to layer selection and model choice.

**6. Rudman, W., Gillman, N., Talmor, A., & Eickhoff, C. (2022). "IsoScore: Measuring the Uniformity of Embedding Space Utilization." ACL Findings 2022.**
Defined IsoScore using the participation ratio of the eigenvalue distribution of the embedding covariance matrix, providing a principled measure of how uniformly dimensions are used. Showed IsoScore better predicts downstream STS performance than ACS and is more discriminative at the high-quality end.

**7. Wang, T., & Isola, P. (2020). "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere." ICML 2020.**
*(See also Section 1)* Provided closed-form, differentiable metrics for alignment and uniformity that can be used both as diagnostic tools and training objectives; uniformity metric is defined as log mean pairwise Gaussian kernel on the unit sphere.

**8. Cer, D., Diab, M., Agirre, E., Lopez-Gazpio, I., & Specia, L. (2017). "SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Cross-Lingual Focused Evaluation." SemEval 2017.**
Established the STS-B benchmark widely used for evaluating sentence embedding quality via Spearman correlation with human similarity judgements. Despite its age, STS-B remains the most widely reported evaluation for contrastive sentence embedding methods including SimCSE.

### Open Problems

1. **Beyond correlation: causal evaluation.** Current benchmarks measure correlation between embedding distances and human-labelled similarities, but they do not measure whether the geometry of the space is causally useful — i.e., whether preserving a particular geometric property leads to better generalisation on unseen tasks and distributions.

2. **Evaluation for large-scale retrieval.** MTEB includes retrieval tasks but at relatively small scale (< 1M documents). The geometric properties that matter at billion-scale retrieval (where approximate NN methods introduce systematic errors) are poorly characterised.

3. **Compositional and relational geometry.** No standard benchmark tests whether geometric operations over embeddings (e.g., vector arithmetic, analogies, offset-based reasoning) remain valid for contextualised sentence embeddings or large LLM representations, despite these being theoretically interesting.

### Cross-References

- Isotropy metrics directly address the geometric issues from **Section 1**.
- MTEB results provide the empirical ground truth for metric choices in **Section 2**.
- Cross-modal extensions of these benchmarks appear in **Section 4**.

---

## Section 4: Cross-Modal Distance in VLMs

### Overview

Vision-Language Models (VLMs) such as CLIP (Radford et al., 2021), ALIGN (Jia et al., 2021), and BLIP (Li et al., 2022) create joint embedding spaces in which visual and textual representations are geometrically aligned, enabling zero-shot classification, cross-modal retrieval, and visual question answering. Measuring distance in these joint spaces requires attending not only to the within-modality geometry but also to the **modality gap** — the systematic offset between the cloud of image embeddings and the cloud of text embeddings in the joint space.

The seminal measurement of this gap was provided by Liang et al. (2022), who showed that in CLIP, image and text embeddings occupy largely non-overlapping antipodal cones in the joint embedding space, even after contrastive training is intended to align them. This gap is not a training failure but an emergent consequence of the InfoNCE loss and the implicit regularisation of the contrastive objective. The modality gap has practical consequences: a text embedding and its matched image embedding are closer to other within-modality embeddings than to each other in absolute Euclidean distance, even when cosine similarity of the matched pair is high.

**Cross-modal retrieval** is the primary evaluation task for VLMs, typically measuring **Recall at K (R@K)** — the fraction of queries for which the correct match is within the top K retrieved items — and **Mean Reciprocal Rank (MRR)**. Standard benchmarks include **MS-COCO Captions** and **Flickr30k** for image–text retrieval, and newer, harder benchmarks such as **Winoground** (Thrush et al., 2022), which tests compositional understanding by requiring models to match images and captions that differ only in the arrangement of the same words.

A significant finding from the Winoground evaluation is that CLIP-style models achieve near-chance performance on compositional reasoning despite high scores on standard R@K metrics, revealing that standard retrieval metrics measure distributional alignment but not compositional geometric precision. This points to a systematic limitation of cosine similarity in the joint space: models that perform well on retrieval may have learned to match global semantic features rather than precise compositional structure.

The **CLIP score** (Hessel et al., 2021) has become widely used as an automatic metric for image captioning, text-to-image generation quality, and other VLM tasks. It is computed as the cosine similarity between image and text embeddings in CLIP's joint space. Like BERTScore, it is subject to the quality of the underlying model and the known biases in CLIP's training data, including sensitivity to racial, gender, and geographic biases encoded in the joint space.

The **geometric properties** of CLIP's joint space differ markedly from those of unimodal LLMs. Shah et al. (2023) showed that CLIP's text encoder produces more isotropic embeddings than BERT-style models, likely because contrastive training with image pairs provides stronger uniformity pressure. However, the joint image+text distribution is highly anisotropic — both modality clouds are themselves anisotropic, and the inter-modality gap adds a further structural constraint.

### Key Papers

**1. Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., ... & Sutskever, I. (2021). "Learning Transferable Visual Models from Natural Language Supervision." ICML 2021.**
Introduced CLIP, training a visual and textual encoder jointly with InfoNCE contrastive loss on 400M image–text pairs. Achieved state-of-the-art zero-shot image classification by framing recognition as image–text retrieval; defined cosine similarity in the joint space as the operational distance for all downstream tasks.

**2. Liang, V. W., Zhang, Y., Kwon, Y., Yeung, S., & Zou, J. Y. (2022). "Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning." NeurIPS 2022.**
Precisely characterised the modality gap in CLIP: image and text embeddings lie in nearly antipodal cones, with the gap persisting across model sizes and training regimes. Showed that the gap is driven by the geometry of the initialisation and the implicit uniformity pressure of InfoNCE; proposed a gap-reducing fine-tuning strategy.

**3. Hessel, J., Holtzman, A., Forbes, M., Bras, R. L., & Choi, Y. (2021). "CLIPScore: A Reference-Free Evaluation Metric for Image Captioning." EMNLP 2021.**
Proposed CLIP cosine similarity as a reference-free metric for image captioning, demonstrating high correlation with human judgements. Noted that CLIPScore is sensitive to CLIP's biases and works better for content accuracy than stylistic quality.

**4. Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., & Ross, C. (2022). "Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality." CVPR 2022.**
Introduced Winoground, 400 image–caption pairs that differ only in word arrangement, requiring compositional spatial and relational reasoning. CLIP achieves ~30% accuracy (near chance), revealing that high R@K on standard benchmarks does not imply compositional geometric precision.

**5. Jia, C., Yang, Y., Xia, Y., Chen, Y. T., Parekh, Z., Pham, H., ... & Duerig, T. (2021). "Scaling Up Visual and Vision-Language Representation Learning with Noisy Text Supervision." ICML 2021.**
Introduced ALIGN, scaling contrastive vision-language pre-training to 1.8B noisy image–alt-text pairs, demonstrating that scale can compensate for data quality. Established dot product (on L2-normalised embeddings) as equivalent to cosine similarity for retrieval; confirmed CLIP's findings at a different scale and architecture.

**6. Li, J., Li, D., Xiong, C., & Hoi, S. (2022). "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation." ICML 2022.**
Extended CLIP-style contrastive training with image-text matching (binary, not cosine) and language modelling objectives, enabling both understanding and generation tasks. Demonstrated that the geometric alignment of the joint space can be improved by auxiliary losses beyond InfoNCE.

**7. Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., & Zou, J. (2023). "When and Why Vision-Language Models Behave like Bags-of-Words, and What to Do about It." ICLR 2023.**
Systematically documented that CLIP treats captions as bags of words rather than structured sentences, explaining failures on compositional benchmarks. Showed that fine-tuning with hard negative captions (differing by one word/phrase) substantially improves compositional accuracy without sacrificing R@K.

**8. Shi, W., & Suzuki, T. (2023). "Towards Understanding the Influence of the Modality Gap on CLIP Generalization." arXiv 2023.**
Theoretical analysis showing that the modality gap acts as a regulariser that prevents over-fitting to a single modality, providing a partial justification for preserving (rather than eliminating) the gap. Showed that gap-elimination strategies can harm zero-shot transfer accuracy.

### Open Problems

1. **Compositional distance in joint spaces.** Standard cosine similarity in CLIP's joint space fails on compositional reasoning. No metric has been proposed that reliably captures compositional semantic distance between images and structured text.

2. **Cross-modal OOD detection.** Detecting when an image–text pair is semantically inconsistent or out-of-distribution is important for safety-critical applications but poorly characterised geometrically. Modality gap magnitude has been proposed as a proxy but has high variance.

3. **Fine-grained alignment beyond retrieval.** R@K measures coarse alignment; it does not capture whether the geometric neighbourhood structure of the image space and the text space are consistently ordered. Rank correlation metrics across modalities are rarely reported but would provide richer information.

### Cross-References

- Modality gap geometry connects to the cone effect discussed in **Section 1**.
- CLIP score is an application of the distance metrics in **Section 2**.
- Cross-modal CKA analysis bridges to **Section 5** (representation similarity across models).

---

## Section 5: Representation Similarity Across Models

### Overview

A central question in modern deep learning is whether different neural networks, trained independently (and possibly on different modalities or tasks), converge to similar representational structures. This question has both scientific significance (illuminating what structure is inherent to the data vs. the architecture) and practical implications (model merging, distillation, and interpretability). The primary tools for answering this question are **Centered Kernel Alignment (CKA)**, **Representational Similarity Analysis (RSA)**, and more recently, methods based on **stitching** layers between models.

**CKA** (Kornblith et al., 2019) computes the normalised Hilbert-Schmidt independence criterion between the kernel matrices (typically linear or RBF) of representations from two models over the same set of inputs. It is invariant to orthogonal transformations and isotropic scaling, making it suitable for comparing representations from models with different initialisation. CKA has become the default tool for cross-model layer comparison, but it has known failure modes: Nguyen et al. (2020) showed that CKA is sensitive to the number of samples (especially with RBF kernels) and can report spuriously high similarity between models that are functionally very different if the input distribution is simple. Furthermore, Williams et al. (2021) noted that CKA's invariance to orthogonal transformations means it cannot distinguish between models whose representational geometry is equivalent but whose learned structure differs after rotation.

**RSA** (Kriegeskorte et al., 2008; originally from neuroscience) computes a representational dissimilarity matrix (RDM) for each model by measuring pairwise distances between representations of a fixed stimulus set, then computes the correlation between RDMs across models or between a model and neural recording data. RSA is model-agnostic, can use any distance function, and naturally handles the comparison of representations from very different sources (e.g., brain activations vs. model layers). However, like CKA, it is sensitive to the choice of input stimuli and distance function.

The **Platonic Representation Hypothesis** (Huh et al., 2024) extends these ideas to a striking empirical claim: as models are scaled up and trained on larger datasets, their representations (measured by CKA and RSA) converge to a common structure, regardless of modality, architecture, or training objective. This convergence is interpreted as evidence that there is a universal latent structure in the world — a "Platonic representation" — that all sufficiently capable models approximate. The claim is empirically supported for a range of models (language, vision, audio) but the theoretical mechanism is debated.

**Model stitching** (Lenc & Vedaldi, 2015; Bansal et al., 2021) provides a complementary probe: two models are "stitched" at a given layer by inserting a learned linear transformation, and performance degradation is used to measure the incompatibility of the two representations at that layer. If two models produce highly compatible representations, performance after stitching is high. This is a more functional criterion than CKA and directly measures whether representations are interchangeable, but it requires joint training.

### Key Papers

**1. Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). "Similarity of Neural Network Representations Revisited." ICML 2019.**
Introduced CKA as an improvement over prior similarity metrics (CCA, cosine similarity of activations), demonstrating invariance to orthogonal transformations and isotropic scaling. Showed that different random seeds of the same architecture trained on the same data converge to highly similar representational structure in corresponding layers.

**2. Nguyen, T., Raghu, M., & Kornblith, S. (2020). "Do Wide and Deep Networks Learn the Same Things? Uncovering How Neural Network Representations Vary with Width and Depth." ICLR 2021.**
Applied CKA to compare ResNets of varying width and depth, finding that wider networks develop more differentiated later layers. Identified failure modes of CKA (sensitivity to sample size, insensitivity to functionally important rotations) and proposed diagnostic checks.

**3. Kriegeskorte, N., Mur, M., & Bandettini, P. (2008). "Representational Similarity Analysis: Connecting the Branches of Systems Neuroscience." Frontiers in Systems Neuroscience.**
Original RSA paper from computational neuroscience; introduced the framework of comparing models and brains by their pairwise dissimilarity structure over stimuli. Foundational methodology for all subsequent cross-modal and cross-system representational comparisons.

**4. Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). "The Platonic Representation Hypothesis." ICML 2024.**
Proposed that large models across modalities and architectures converge to similar representations of the world, measurable via CKA and mutual k-NN structure. Provided evidence across language, vision, and audio models at varying scales; interpretated convergence as approximation of a universal statistical model of reality.

**5. Bansal, Y., Nakkiran, P., & Barak, B. (2021). "Revisiting Model Similarity." NeurIPS Workshop 2021.**
Examined model stitching as a functional measure of representational compatibility, showing that stitching accuracy provides a complementary and sometimes contradictory signal to CKA. Demonstrated that CKA similarity does not guarantee functional interchangeability.

**6. Williams, A. H., Kunz, E., Kornblith, S., & Linderman, S. W. (2021). "Generalized Shape Metrics on Neural Representations." NeurIPS 2021.**
Introduced shape metrics (Procrustes distance and variants) that go beyond CKA by explicitly solving for the optimal rotation between representation spaces. Showed that Procrustes distance is more sensitive to functionally relevant differences than CKA and proposed a geometry-aware framework for cross-model comparison.

**7. Raghu, M., Gilmer, J., Yosinski, J., & Sohl-Dickstein, J. (2017). "SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability." NeurIPS 2017.**
Introduced SVCCA, combining dimensionality reduction via SVD with Canonical Correlation Analysis to compare neural representations. Enabled efficient comparison of very large activation matrices; predated and partially motivated CKA.

**8. Lenc, K., & Vedaldi, A. (2015). "Understanding Image Representations by Measuring Their Equivariance and Equivalence." CVPR 2015.**
Early work on measuring representational equivalence between models via the quality of linear transformations between their activation spaces. Introduced the "equivalence" concept that motivates modern stitching methods.

### Open Problems

1. **What does CKA convergence actually mean?** The Platonic Representation Hypothesis is a striking empirical claim, but it is unclear whether convergence in CKA implies convergence in downstream task performance, generalisation behaviour, or failure modes. Models can have similar CKA but systematically different errors.

2. **Causal direction of convergence.** Is representational convergence driven by the structure of the data, the architecture inductive biases, or training scale? Disentangling these factors requires controlled experiments across architectures that are rarely conducted.

3. **Rotational invariance as a feature or a bug.** CKA's invariance to orthogonal transformations is both a strength (robustness to arbitrary alignment) and a weakness (insensitivity to potentially meaningful rotational structure). The field lacks consensus on whether rotational alignment should be sought or ignored when comparing representations.

### Cross-References

- CKA is computed over the same representation spaces whose intrinsic geometry is analysed in **Section 1**.
- RSA extends naturally to cross-modal comparison in VLMs (**Section 4**).
- Stitching methods implicitly test the linearity of the manifold structure (**Section 1**).

---

## Section 6: Semantic and Contextual Distance

### Overview

The transition from static word embeddings (word2vec, GloVe) to contextualised representations (ELMo, BERT, GPT) fundamentally changed the meaning of distance in embedding spaces. In static embeddings, each word type has a single representation, and distance reflects typical semantic association. In contextualised models, each word **token** receives a different representation depending on its context, meaning that distance is now a relation between specific usages rather than word types. This creates both opportunities and challenges for semantic distance measurement.

**Polysemy and sense disambiguation** are perhaps the most direct beneficiaries of contextualisation. A static embedding for "bank" must average over all senses (financial institution, river bank, etc.); a contextualised embedding separates them. Pilehvar & Camacho-Collados (2019) introduced the WiC (Words in Context) benchmark specifically to test whether models can judge whether two tokens of the same word are used in the same sense, a task that directly probes contextualised distance. However, representing multiple senses still requires post-hoc clustering of contextualised representations, and the appropriate distance function for this clustering is model-dependent.

**Semantic change detection** is a downstream application that uses embedding distance to track how word meanings shift over time. The standard approach (Hamilton et al., 2016; Kutuzov et al., 2018) is to train separate static embeddings on text from different time periods and measure distance after alignment (e.g., orthogonal Procrustes). With contextualised models, the approach shifts to sampling contextualised representations across time periods and computing distributional distance (JSD, Wasserstein, or mean cosine similarity within and across periods). Montariol et al. (2021) showed that contextualised embeddings achieve state-of-the-art on the SemEval-2020 semantic change task.

A key finding from the contextualised embeddings literature is that **layer depth matters**: lower layers capture surface-level morphological and syntactic information, while upper layers capture more abstract semantic and pragmatic content. For semantic distance measurement, upper layers typically perform better, but the optimal layer is task-dependent and model-dependent. This poses a practical problem for retrieval systems: which layer to use for embedding, and whether to average across layers, is often treated as a hyperparameter rather than principled choice.

**Token-level geometry** in contextualised models is complex. Reif et al. (2019) showed that BERT's contextual representations form a "neighbourhood geometry" around tokens in a way that encodes syntactic parse structure: the distance from a token to its syntactic head correlates with the depth of the dependency tree. Hewitt & Manning (2019) formalised this as the "structural probe", training a linear transformation on top of BERT to recover syntactic distance from inner products. This suggests that syntactic structure is encoded in the geometry of contextual embeddings, accessible via appropriate distance functions.

**Ambiguity and uncertainty** in embeddings are less well-studied. Standard embeddings produce point estimates, but a token's representation could be interpreted as a distribution over meanings. Vilnis & McCallum (2015) proposed Gaussian word embeddings (representing words as probability distributions rather than points), enabling asymmetric distance functions like KL divergence that respect entailment relationships. More recently, stochastic contextualised embeddings have been proposed but have not been widely adopted.

### Key Papers

**1. Peters, M. E., Neumann, M., Iyyer, M., Gardner, M., Clark, C., Lee, K., & Zettlemoyer, L. (2018). "Deep Contextualized Word Representations." NAACL 2018.**
Introduced ELMo (Embeddings from Language Models), the first widely adopted contextualised embedding model, using bidirectional LSTMs. Demonstrated that different layers capture different linguistic properties; introduced the practice of learned-weighted layer combinations for downstream tasks.

**2. Hewitt, J., & Manning, C. D. (2019). "A Structural Probe for Finding Syntax in Word Representations." NAACL 2019.**
Proposed the structural probe: a linear transformation of BERT embeddings that recovers syntactic distance (tree distance) as the L2 distance in the transformed space. Demonstrated that syntactic structure is geometrically encoded in BERT's middle layers with high fidelity.

**3. Pilehvar, M. T., & Camacho-Collados, J. (2019). "WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations." NAACL 2019.**
Introduced the WiC benchmark for polysemy-aware contextual representation evaluation. Showed that contextualised models substantially outperform static embeddings on sense disambiguation, and that cosine similarity in the contextual embedding space is a reasonable proxy for sense identity.

**4. Hamilton, W. L., Leskovec, J., & Jurafsky, D. (2016). "Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change." ACL 2016.**
Established the methodology of comparing word embedding cosine similarities across time-aligned corpora to detect semantic change. Proposed geometric regularities: words that change meaning most are often those with initially high polysemy; validated against historical linguistic records.

**5. Montariol, S., Martinc, M., & Pivovarova, L. (2021). "Scalable and Interpretable Semantic Change Detection." NAACL 2021.**
Demonstrated state-of-the-art semantic change detection using contextualised BERT embeddings clustered with Wasserstein-based methods. Showed that tracking the evolution of contextual embedding clusters (rather than mean shifts) provides more interpretable and accurate change detection.

**6. Reif, E., Yuan, A., Wattenberg, M., Viegas, F. B., Coenen, A., Pearce, A., & Kim, B. (2019). "Visualizing and Measuring the Geometry of BERT." NeurIPS 2019.**
Used dimensionality reduction and geometric analysis to show that BERT's contextual representations encode linguistic structure geometrically: syntactic parse trees correspond to distance structure in middle layers, and attention heads correspond to geometric transformations. Rich empirical survey of BERT geometry.

**7. Vilnis, L., & McCallum, A. (2015). "Word Representations via Gaussian Embedding." ICLR 2015.**
Represented words as Gaussian distributions (mean + covariance) rather than point vectors, enabling asymmetric similarity via KL divergence and modelling uncertainty/polysemy. Showed improvements on hypernymy detection and analogy tasks where entailment direction matters.

**8. Kutuzov, A., Øvrelid, L., Szymanski, T., & Velldal, E. (2018). "Diachronic Word Embeddings and Semantic Shifts: A Survey." COLING 2018.**
Comprehensive survey of methods for detecting semantic change using word embeddings, covering alignment methods, distance metrics, and evaluation corpora. Catalogues failure modes of cosine-based approaches and motivates the use of distributional distance measures.

### Open Problems

1. **Layer selection in production.** There is no principled, unsupervised method for selecting the optimal layer for contextualised distance computation on a new task or domain. Hyperparameter sweeps are expensive; learned layer weighting requires labelled data.

2. **Distributional vs. point-based distance for polysemy.** It is unclear whether distributional representations (Gaussian embeddings, mixture models) provide measurable benefits over clustering of point representations in practical NLP tasks. The two approaches have rarely been rigorously compared on the same benchmarks.

3. **Temporal geometry evolution.** Most semantic change detection work assumes a static metric (cosine similarity) and measures distributional shift in fixed-metric space. How the metric itself should change over time (as usage norms shift) is unexplored.

### Cross-References

- The structural probe (Hewitt & Manning) is a specific application of distance metrics in **Section 2** (L2 in a transformed space).
- Polysemy detection connects to probing tasks in **Section 3**.
- Distributional distance for semantic change uses Wasserstein distance (**Section 2**).

---

## Section 7: Applications and Downstream Implications

### Overview

The choice of distance metric and the geometric properties of embedding spaces have concrete, measurable downstream consequences across a range of applications. In **retrieval-augmented generation (RAG)**, the quality of retrieved context depends directly on the distance function and approximate nearest-neighbour (ANN) algorithm used at inference time. In **clustering and nearest-neighbour search**, the curse of dimensionality and anisotropy jointly determine the accuracy and efficiency of retrieval. In **bias and fairness measurement**, the geometric relationships between demographic group embeddings encode societal biases in measurable ways. In **out-of-distribution (OOD) detection**, the distance from a test example to the training distribution in embedding space provides a principled anomaly signal.

**RAG and dense retrieval**: The performance of RAG systems is highly sensitive to the choice of similarity function. Karpukhin et al. (2020) established dot product on L2-normalised embeddings as the standard for dual-encoder retrieval, but subsequent work has shown that the optimal metric is task- and domain-dependent. For passage retrieval, cosine similarity and dot product differ significantly when passage embeddings have variable norms (which they do in practice when passages vary in length and vocabulary). Xiong et al. (2021) showed that hard negative mining during training sharpens the metric landscape, making the choice of similarity function more robust; but this requires domain-specific training.

**High-dimensional nearest-neighbour search**: As embedding dimension grows (modern LLMs produce 768-to-4096 dimensional representations), exact nearest-neighbour search becomes impractical. Approximate methods — FAISS (Johnson et al., 2019), HNSW (Malkov & Yashunin, 2018), ScaNN (Guo et al., 2020) — trade exact metric computation for speed. These algorithms have different biases: HNSW is graph-based and works well for cosine similarity; product quantisation in FAISS introduces quantisation error that interacts with the anisotropy of the embedding space. The geometric structure of the embedding space (dimensionality, anisotropy, clustering) directly determines which ANN algorithm is most suitable.

**Bias and fairness**: The WEAT (Word Embedding Association Test; Caliskan et al., 2017) measures the strength of association between concept words and attribute words (e.g., gendered terms, racial categories) using cosine similarity, adapted from the Implicit Association Test in psychology. WEAT has been widely applied to both static and contextualised embeddings, consistently finding that models encode human-like biases from training data. Subsequent work has measured the geometric "direction" of gender, race, and other social attributes as principal components of the embedding space (Bolukbasi et al., 2016), enabling explicit debiasing by projecting out these directions — though the effectiveness of such debiasing for downstream tasks has been contested (Gonen & Goldberg, 2019).

**OOD detection**: The Mahalanobis distance detector (Lee et al., 2018) applies class-conditional Mahalanobis distance in the feature space of a classifier to score test examples for OOD-ness. More recent methods use energy scores, gradient norms, and density estimates in embedding space. For LLMs, the embedding distance from a test prompt to the training distribution is a natural OOD signal, but estimating this distribution in high-dimensional space is challenging. Energy-based OOD detection (Liu et al., 2020) uses the log-sum-exp of logits as a distance proxy and does not require explicit modelling of the embedding distribution.

### Key Papers

**1. Johnson, J., Douze, M., & Jégou, H. (2019). "Billion-Scale Similarity Search with GPUs." IEEE Transactions on Big Data.**
Introduced FAISS, a library for efficient exact and approximate similarity search over dense vectors, supporting multiple index types (flat, IVFPQ, HNSW). Demonstrated billion-scale inner product and L2 search; remains the standard library for embedding-based retrieval in production systems.

**2. Malkov, Y. A., & Yashunin, D. A. (2018). "Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs." IEEE TPAMI.**
Introduced HNSW, a hierarchical graph-based ANN structure that achieves near-optimal search performance across a wide range of embedding spaces. Shows better performance than tree-based methods in high dimensions; widely used in vector databases (Weaviate, Qdrant, Pinecone).

**3. Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). "Semantics Derived Automatically from Language Corpora Contain Human-Like Biases." Science.**
Introduced WEAT, demonstrating that GloVe embeddings reproduce human implicit biases (racial, gender, age) as measured by differential cosine similarity to attribute categories. Foundational paper for bias measurement in embedding spaces; motivated years of debiasing research.

**4. Bolukbasi, T., Chang, K. W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings." NeurIPS 2016.**
Identified the "gender direction" in word2vec as a linear subspace and proposed debiasing by projecting out this direction for gender-neutral words. Widely replicated finding; however, subsequent work showed that debiasing by projection leaves residual bias detectable via non-linear probes.

**5. Gonen, H., & Goldberg, Y. (2019). "Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings but Do Not Remove Them." NAACL 2019.**
Showed that projection-based debiasing of word embeddings removes the most obvious cosine-similarity-based bias signals but leaves gender bias detectable via clustering and non-linear classifiers. Challenged the effectiveness of geometric debiasing; motivated more principled approaches.

**6. Liu, W., Wang, X., Owens, J., & Li, Y. (2020). "Energy-based Out-of-Distribution Detection." NeurIPS 2020.**
Proposed using the energy function (log-sum-exp of logits) as an OOD score, showing it better calibrates the uncertainty of deep classifiers than raw softmax confidence. Does not require explicit Gaussian modelling of feature space; simpler and competitive with Mahalanobis-based methods.

**7. Xiong, L., Xiong, C., Li, Y., Tang, K. F., Liu, J., Bennett, P., ... & Overwijk, A. (2021). "Approximate Nearest Neighbor Negative Contrastive Estimation for Dense Text Retrieval." ICLR 2021.**
Introduced ANCE (Approximate Nearest Neighbour Negative Contrastive Estimation), training dense retrievers with hard negatives from the model's own ANN index. Showed large improvements over standard in-batch negatives by sharpening the learned metric landscape around the decision boundary.

**8. Guo, R., Sun, P., Lindgren, E., Geng, Q., Simcha, D., Chern, F., & Kumar, S. (2020). "Accelerating Large-Scale Inference with Anisotropic Vector Quantization." ICML 2020.**
Introduced ScaNN, using anisotropic vector quantisation that accounts for the asymmetry of Maximum Inner Product Search. Outperforms isotropic quantisation methods precisely because it respects the non-uniform density of embedding space — a direct practical consequence of anisotropy (Section 1).

### Open Problems

1. **Dynamic metric adaptation in RAG.** RAG systems currently use a fixed similarity function determined at training time. There is no principled method for dynamically adapting the metric to the specific query distribution encountered at inference time, which may differ substantially from the training distribution.

2. **Intersectional bias in embedding geometry.** Most geometric bias measurement methods treat demographic attributes independently (gender OR race). Measuring intersectional bias (the interaction of multiple attributes simultaneously) in embedding space requires higher-order geometric tools that are computationally expensive and statistically underpowered.

3. **OOD detection under distributional shift vs. semantic novelty.** Embedding distance can signal both statistical OOD (the input is statistically unlike training data) and semantic OOD (the input raises a genuinely novel concept). These two types of OOD require different responses (re-calibration vs. abstention) but are conflated by current geometric methods.

### Cross-References

- ANN algorithm choice interacts with the dimensional structure discussed in **Section 1**.
- Bias measurement via WEAT uses cosine similarity as the core metric (**Section 2**).
- OOD detection methods connect to Mahalanobis distance (**Section 2**) and probing (**Section 3**).

---

## Section 8: Synthesis

### Overarching Themes

**1. The Anisotropy–Expressivity Tension**
The most persistent tension in the literature is between *anisotropy* (empirically pervasive in pre-trained models) and *expressivity* (the capacity of the space to represent many distinct semantic concepts). Anisotropy reduces the effective representational capacity of the space and makes naive distance functions unreliable. Attempts to correct anisotropy (e.g., whitening, projection, contrastive fine-tuning) can improve distance reliability but risk reducing the nuanced structure that the model learned. The Wang & Isola alignment–uniformity framework provides a principled basis for this tradeoff, but no training objective has been found that achieves both simultaneously at scale without additional supervision.

**2. Cosine vs. Euclidean: A False Binary**
The dominance of cosine similarity in NLP/VLM literature reflects practical convenience rather than theoretical optimality. When embeddings are L2-normalised (as in CLIP and many sentence embedding models), cosine similarity and Euclidean distance are monotonically equivalent. When they are not normalised, cosine similarity ignores magnitude information (which can be semantically meaningful) while Euclidean distance is sensitive to absolute scale (which can be artifactual). The real choice is not cosine vs. Euclidean but *which normalisation regime to enforce at training time* — a decision that currently lacks principled guidance.

**3. Metric Learning vs. Fixed Metrics**
There is a spectrum from purely geometric, fixed metrics (cosine similarity, Euclidean) to fully learned metrics (Siamese networks, bilinear forms, ANCE). Learned metrics can dramatically outperform fixed ones in-domain but generalise poorly. The field is converging on a hybrid approach — using pre-trained embeddings with a fixed metric for zero-shot evaluation and learned fine-tuned metrics for domain-specific deployment — but this creates a hidden assumption that the pre-trained metric is a reasonable starting point, which is not always true for out-of-domain data.

**4. Scale and Convergence**
The Platonic Representation Hypothesis suggests that at sufficient scale, architectural and training choices matter less for the geometry of the resulting space, and different models converge to common representational structures. If true, this reduces the importance of model-specific metric design but raises questions about what the common geometry actually is and whether it is well-suited for downstream applications.

**5. The Modality Gap as a First-Class Citizen**
The systematic gap between image and text embeddings in CLIP-style models is not a failure of alignment but an emergent structural feature with both costs (it means images and texts are never truly in the same space) and benefits (it provides implicit regularisation). The field is beginning to study and manipulate the modality gap explicitly rather than treating it as noise.

### Key Tensions

| Tension | Location | Status |
|---|---|---|
| Cosine similarity vs. Euclidean distance | Sec. 2, 7 | Partially resolved: equivalent when L2-normalised; problem is the normalisation choice |
| Isotropy vs. expressivity | Sec. 1, 3 | Unresolved: no training objective achieves both at scale |
| Fixed metric vs. learned metric | Sec. 2, 7 | Partially resolved: learned metrics win in-domain; fixed metrics for zero-shot |
| CKA invariance as feature vs. bug | Sec. 5 | Unresolved: depends on whether rotational structure is meaningful |
| Modality gap elimination vs. preservation | Sec. 4 | Emerging evidence that preservation is beneficial (Shi & Suzuki, 2023) |
| Probing accuracy as evidence of encoding | Sec. 3, 6 | Partially resolved: selectivity (Hewitt & Liang) provides correction |

---

## Section 9: Gap Analysis

The following research questions are substantively underexplored relative to their importance:

**1. Geometry of instruction-tuned and RLHF-trained models.** Nearly all geometric analysis focuses on pre-trained or contrastively fine-tuned models. How RLHF and instruction tuning change the geometry of the embedding space (alignment, uniformity, isotropy) is almost completely unstudied, despite being directly relevant to the quality of embeddings extracted from production LLMs for downstream tasks.

**2. Theoretical foundations of hyperbolic and Riemannian embeddings in transformers.** While hyperbolic embeddings for taxonomies are well-established, integrating curved-geometry representations into transformer architectures at scale remains unsolved. The numerical instability of Poincaré models at high precision is a practical barrier; Lorentz models are more stable but less expressive.

**3. Calibrated uncertainty in embedding distance.** Current embedding distance methods produce point estimates with no associated uncertainty. Probabilistic embeddings (Gaussian, von Mises-Fisher) exist but are not integrated into standard pre-training pipelines. For safety-critical retrieval (medical, legal), knowing the confidence of a similarity score is essential.

**4. Compositional geometry in VLMs.** How compositional semantic operations (negation, modification, relational binding) are reflected in the geometry of joint image–text spaces is poorly understood. Winoground (Section 4) exposes the failure; no current model has a geometric account of why it fails or how to fix it.

**5. Temporal dynamics of embedding geometry.** How the geometry of a model's embedding space evolves during training (not just pre- vs. post-training) is understudied. Recent work on loss landscape geometry is adjacent but distinct; understanding the training trajectory of representational geometry would enable more targeted intervention.

**6. Cross-lingual embedding geometry.** Most geometry analysis is conducted on English-only models. Whether the anisotropy, dimensional collapse, and cone effects documented for English hold for multilingual models (mBERT, XLM-R, NLLB) and whether cross-lingual alignment is geometrically well-behaved are open empirical questions.

**7. Downstream calibration of intrinsic metrics.** IsoScore, ACS, alignment, and uniformity are intrinsic metrics, but their correlation with downstream task performance has been measured only for STS and retrieval. Whether these metrics predict performance on generation, reasoning, and classification tasks (where embedding geometry is less obviously relevant) is unknown.

---

## Section 10: Suggested Reading Order

### For Readers New to the Field

**Foundations (weeks 1–2):**
1. Mu & Viswanath (2018) — *All-but-the-Top* — introduces the anisotropy problem in static embeddings; accessible entry point.
2. Ethayarajh (2019) — *How Contextual Are Contextualized Word Representations?* — extends anisotropy analysis to BERT/GPT; directly readable.
3. Wang & Isola (2020) — *Alignment and Uniformity* — provides the normative framework; moderate mathematical background required.

**Distance and Similarity (week 3):**
4. Reimers & Gurevych (2019) — *Sentence-BERT* — demonstrates why metric choice matters empirically; accessible.
5. Karpukhin et al. (2020) — *Dense Passage Retrieval* — motivates dot product for retrieval at scale; practical focus.

**Evaluation (week 4):**
6. Muennighoff et al. (2023) — *MTEB* — the state-of-the-art benchmark paper; important for understanding what "good" means empirically.
7. Hewitt & Liang (2019) — *Designing and Interpreting Probes* — methodological rigour in probing; critical for reading the probing literature.

**VLMs and Cross-Modality (week 5):**
8. Radford et al. (2021) — *CLIP* — foundational VLM paper.
9. Liang et al. (2022) — *Mind the Gap* — modality gap analysis; reads naturally after CLIP.
10. Thrush et al. (2022) — *Winoground* — exposes compositional failure of cosine distance in VLMs.

**Representation Comparison and Advanced Topics (week 6):**
11. Kornblith et al. (2019) — *CKA* — foundational cross-model comparison metric.
12. Huh et al. (2024) — *Platonic Representation Hypothesis* — big-picture synthesis; best read after familiarity with CKA.
13. Nickel & Kiela (2017) — *Poincaré Embeddings* — hyperbolic geometry; can be read independently.

**Applications (week 7):**
14. Caliskan et al. (2017) — *WEAT* — bias measurement; accessible to non-technical readers.
15. Lee et al. (2018) — *Mahalanobis OOD* — OOD detection; requires ML background.
16. Bolukbasi et al. (2016) and Gonen & Goldberg (2019) — read together for the debiasing debate.

---

*This survey covers approximately 60 primary sources. Given the rapid pace of publication in this area, readers are advised to supplement with monthly preprint monitoring on arXiv cs.CL and cs.LG, with particular attention to the ICLR 2025 and NeurIPS 2025 proceedings.*
