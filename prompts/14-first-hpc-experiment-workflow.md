# Workflow: Vidiq-HPC Experiment #1 - Sentiment Embedding Geometry

## Objective
Investigate the representational geometry of sentiment in the latent space of a small-scale LLM. The goal is to quantify and visualize the separation between "Happy" and "Sad/Upset" sentiments using high-dimensional embeddings.

---

## Phase 1: Literature & Dataset Survey (Agent-Driven)
**Task:** Identify and curate current-state sentiment analysis datasets suitable for LLM embedding extraction.
1. **Source Identification:** Research datasets such as SST-2, IMDB, or Twitter Sentiment, focusing on those with clear binary or categorical labels.
2. **Metadata Extraction:** For each dataset, record:
   - Size (number of samples).
   - Average token length.
   - Domain (e.g., movie reviews, social media).
   - Label noise/reliability.
3. **Selection:** Choose a subset of data that provides a "clean" contrast between extreme positive (Happy) and extreme negative (Sad/Upset) sentiments.

---

## Phase 2: Model Selection & Embedding Characterization
**Task:** Configure a small-scale LLM to serve as the embedding engine.
1. **Model Selection:** Use an open-weights LLM with $\le 8$B parameters (e.g., Mistral-7B-v0.3, Llama-3-8B, or Gemma-2-2B).
2. **Tokenization & Inference:**
   - Implement a pipeline to tokenize queries and perform a forward pass.
   - Extract the hidden states from the final transformer layer (or the specific `CLS` token/mean-pooled output).
3. **Dimensionality Analysis:** 
   - Confirm the model's hidden dimension ($d_{model}$).
   - Log statistics on embedding norms and anisotropy (e.g., Cosine Similarity distribution across random samples).

---

## Phase 3: Experimental Execution (Sentiment Separation)
**Task:** Generate and align embeddings for the target sentiments.
1. **Query Generation:** Prepare a balanced set of queries/sentences that clearly evoke "Happy" and "Sad/Upset" emotions.
2. **Embedding Extraction:**
   - Process the "Happy" corpus to generate a set of vectors $V_{happy} \subset \mathbb{R}^{d}$.
   - Process the "Sad" corpus to generate a set of vectors $V_{sad} \subset \mathbb{R}^{d}$.
3. **Constraint:** Ensure all queries result in the same embedding dimensionality $d$ as characterized in Phase 2.

---

## Phase 4: Clustering, Visualization, and Centroid Analysis
**Task:** Quantify the geometric relationship between the sentiment clusters.
1. **Dimensionality Reduction:** Use PCA, t-SNE, or UMAP to project the $d$-dimensional embeddings into 2D or 3D for visualization.
2. **Centroid Calculation:**
   - Calculate the "Happy" centroid: $\mu_{happy} = \frac{1}{N} \sum_{i=1}^{N} v_{happy, i}$.
   - Calculate the "Sad" centroid: $\mu_{sad} = \frac{1}{M} \sum_{j=1}^{M} v_{sad, j}$.
3. **Distance Metrics:**
   - Measure the Euclidean and Cosine distance between $\mu_{happy}$ and $\mu_{sad}$.
   - Calculate the intra-cluster vs. inter-cluster variance to assess "separability."
4. **Visualization:**
   - Plot the individual embeddings as a scatter plot (color-coded by sentiment).
   - Overlay the centroids $\mu_{happy}$ and $\mu_{sad}$ as distinct markers.
   - Annotate the plot with the calculated distance metrics.

---

## Deliverables
- A technical report summarizing the dataset survey.
- Python scripts for embedding extraction and visualization (using `torch`, `transformers`, `scikit-learn`, and `matplotlib/seaborn`).
- High-resolution plots of the embedding space and centroids.
- A summary of whether the model exhibits a clear "Sentiment Axis" in its latent geometry.
