You are an ML researcher designing a rigorous but lightweight experiment. 
Your task is to produce a complete, reproducible experimental protocol for the following study:

**Studying Embedding Space Geometry and Cluster Structure in a Small LLM 
Fine-tuned on a Binary Sentiment Classification Task (Happy / Sad)**

---

### RESEARCH OBJECTIVE

Design an end-to-end experiment that:
1. Selects and prepares a small LLM suitable for research-scale compute
2. Constructs or curates a minimal, controlled sentiment dataset (binary: happy / sad)
3. Fine-tunes the model on this dataset
4. Extracts embeddings at multiple layers
5. Analyzes the geometry and cluster structure of the resulting embedding space
6. Produces interpretable visualizations and quantitative metrics

The experiment should be fully reproducible on a single consumer GPU (≤24GB VRAM) 
or a free-tier cloud instance (e.g., Colab A100).

---

### SECTION 1 — MODEL SELECTION

Recommend a specific small LLM for this experiment. Address:

- **Candidate models**: Consider GPT-2 (small/medium), DistilBERT, BERT-base, 
  RoBERTa-base, Pythia-160M/410M, Phi-1.5, or similar. Justify your choice.
- **Architecture considerations**: encoder-only vs. decoder-only — how does this 
  affect which layers and token positions to extract embeddings from?
- **Tokenizer**: Note any tokenizer quirks relevant to short sentiment sentences
- **Baseline embedding quality**: Does the pre-trained model already encode 
  sentiment signal? How would you verify this before fine-tuning?

---

### SECTION 2 — DATASET CONSTRUCTION

Design a controlled synthetic + curated dataset. Specify:

- **Size**: How many examples per class? Justify the minimum viable size for 
  meaningful cluster analysis (consider: 200, 500, 1000 per class)
- **Construction strategy**: 
  - Option A: Curate from existing datasets (SST-2, IMDB, EmotionLines) — 
    describe exact filtering criteria to isolate clean happy/sad examples
  - Option B: Generate synthetically using a prompted LLM — provide the exact 
    generation prompt, and describe quality filtering steps
  - Option C: Hybrid — specify the ratio and rationale
- **Controlled variables**: 
  - Sentence length distribution (short: 5–10 tokens, medium: 10–20 tokens)
  - Vocabulary overlap between classes — should it be high or low, and why?
  - Presence/absence of explicit sentiment words (e.g., "happy", "sad") — 
    consider having a split with and without these words to test implicit vs. 
    explicit sentiment encoding
- **Train / val / test splits**: Specify ratios and any stratification strategy
- **Dataset quality checks**: Inter-annotator agreement proxy, class balance 
  verification, duplicate detection

Produce 10 example sentences per class to illustrate the target distribution.

---

### SECTION 3 — FINE-TUNING PROTOCOL

Specify the full training setup:

- **Task formulation**: classification head on [CLS] token vs. mean pooling vs. 
  causal LM with sentiment prompt — justify the choice
- **Hyperparameters**: learning rate, batch size, epochs, warmup, weight decay. 
  Provide a sweep range and the single recommended default.
- **Regularization**: dropout, label smoothing — what values, and why?
- **Optimizer**: AdamW with specific β values; justify
- **Evaluation during training**: what metric to track on val set (accuracy, F1, 
  loss)? At what interval?
- **Stopping criterion**: early stopping patience, minimum delta
- **Checkpointing**: save best model by which metric?
- **Compute estimate**: approximate training time on a T4 / A100 GPU
- **Reproducibility**: specify random seeds, torch.backends settings, 
  and any non-determinism sources to control

---

### SECTION 4 — EMBEDDING EXTRACTION

Define exactly what to extract and how:

- **Which layers**: Extract from at least 3 points — early (layer 1–2), 
  middle, and final layer. Specify exact layer indices for the chosen model.
- **Which token position**: [CLS], last token, mean pool over all tokens, 
  or mean pool over non-padding tokens — specify per architecture type
- **When to extract**: 
  - Before fine-tuning (frozen pre-trained model)
  - After fine-tuning
  - Optionally: at intermediate checkpoints during training
- **What inputs to embed**: 
  - Full test set (for cluster analysis)
  - A matched probe set: identical sentence templates with only the sentiment 
    word swapped (e.g., "I feel [happy/sad] today") — for controlled comparison
- **Storage format**: shape of embedding tensor, dtype (float32 vs float16), 
  file format (numpy .npy, HDF5, or PyTorch .pt)
- **Normalization**: should embeddings be L2-normalized before analysis? 
  Justify based on the metric you plan to use.

---

### SECTION 5 — EMBEDDING SPACE ANALYSIS

Specify the full analysis pipeline across three levels:

#### 5a. Geometric / Global Structure
- **Isotropy**: compute IsoScore or average pairwise cosine similarity — 
  what does a high vs. low score indicate here?
- **Intrinsic dimensionality**: estimate using TwoNN or PCA explained variance 
  — how many dimensions capture 90% / 99% of variance?
- **Anisotropy**: measure the dominant direction (first PCA component) — 
  does it align with the sentiment axis?
- **Uniformity metric** (Wang & Isola, 2020): log mean pairwise Gaussian kernel — 
  compare before vs. after fine-tuning

#### 5b. Cluster Analysis
- **Clustering algorithms to apply**: 
  - K-Means (k=2) as baseline
  - DBSCAN to detect natural density-based structure
  - Gaussian Mixture Models for soft cluster assignment
- **Evaluation metrics** (using ground-truth labels as reference):
  - Silhouette score
  - Davies-Bouldin index
  - Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI) 
    vs. true sentiment labels
  - Cluster purity
- **Centroid geometry**: compute cosine similarity and Euclidean distance 
  between happy and sad cluster centroids — track this across layers and 
  before/after fine-tuning
- **Intra-class vs inter-class distance ratio**: define formally and report

#### 5c. Individual Embedding Behavior
- **Nearest neighbor analysis**: for 10 randomly sampled test points per class, 
  list the 5 nearest neighbors — are they same-class? 
- **Hard examples**: identify the embeddings closest to the decision boundary 
  (minimum inter-class distance) — what do these sentences look like?
- **Outlier detection**: identify embeddings > 2σ from their class centroid — 
  what properties do they share?

---

### SECTION 6 — VISUALIZATION

Specify the full visualization plan:

- **Dimensionality reduction methods** (apply all three, compare):
  - PCA (2D and 3D): preserves global variance structure
  - t-SNE (perplexity: 5, 30, 50 — show sensitivity): preserves local structure
  - UMAP (n_neighbors: 15, min_dist: 0.1): balances local and global
- **What to color by**: 
  - Ground-truth sentiment label
  - Model confidence / softmax probability
  - Sentence length
  - Presence of explicit sentiment word
- **Layer comparison plot**: side-by-side 2D UMAP of early, middle, and final 
  layer embeddings — show how cluster separation evolves
- **Before vs. after fine-tuning**: paired plots using the same UMAP fit 
  (fit on pre-trained, transform post-trained) to ensure comparability
- **Centroid trajectory**: if extracting embeddings at training checkpoints, 
  plot how centroid distance evolves over training steps
- **Required figure list**: enumerate all figures the final report must contain, 
  with titles, axes labels, and what insight each should convey

---

### SECTION 7 — HYPOTHESES AND EXPECTED FINDINGS

State 5 falsifiable hypotheses the experiment should test, in the form:

  H[n]: [statement of expected finding]
  Null: [what the data would look like if false]
  Measured by: [specific metric or visualization]

Example:
  H1: Fine-tuning increases inter-cluster cosine distance between happy and sad 
      centroids compared to the pre-trained baseline.
  Null: Centroid distance does not change significantly after fine-tuning.
  Measured by: Cosine distance between class centroids at the final layer, 
               pre vs. post fine-tuning.

Generate 4 more hypotheses covering layer depth, implicit vs. explicit sentiment, 
cluster compactness, and intrinsic dimensionality.

---

### SECTION 8 — ABLATIONS AND CONTROLS

Specify the minimum ablation set needed to make findings interpretable:

- **No fine-tuning baseline**: embed with frozen pre-trained model — 
  does sentiment cluster even without task supervision?
- **Random projection control**: replace model embeddings with random vectors 
  of the same dimension — what do clustering metrics look like?
- **Label shuffle control**: train with shuffled labels — does the space still 
  cluster? Rules out artifacts from training dynamics.
- **Single-layer ablation**: repeat cluster analysis at every layer — 
  plot ARI vs. layer depth curve
- **Dataset size ablation**: train on 100, 250, 500, 1000 examples per class — 
  how does cluster quality scale with data?

---

### SECTION 9 — IMPLEMENTATION CHECKLIST

Produce a step-by-step numbered checklist (no code, just precise instructions) 
covering every implementation step from environment setup to final figure export. 
Each step should be specific enough that a junior ML engineer could execute it 
without ambiguity. Include:
- Environment and dependency versions
- File/directory structure convention
- Exact function calls or API names from HuggingFace / sklearn / UMAP-learn
- Where to log metrics (W&B, TensorBoard, or CSV — specify)
- How to save and version intermediate artifacts

---

### SECTION 10 — EXPECTED OUTPUTS AND SUCCESS CRITERIA

Define what a successful experiment looks like:

- **Minimum success**: ARI > 0.6 on post-fine-tuning final-layer embeddings
- **Strong success**: Clear visual cluster separation in UMAP with ARI > 0.8, 
  monotonically increasing inter-centroid distance across layers
- **Failure modes to anticipate**: 
  - Embedding collapse (all points converge)
  - No improvement over random baseline
  - Layer-wise metrics non-monotonic — what would this suggest?
- **What to report if the experiment fails**: specify diagnostic steps
