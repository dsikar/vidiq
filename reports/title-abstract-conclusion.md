# Title, Abstract, and Conclusion Report

Generated from PDFs in `lit-survey/codex`.

## Summary

- Total PDFs processed: 82
- Abstracts found: 82 (78 originally + 4 added by Claude)
- Conclusions found: 82 (33 originally + 49 added by Claude)
- Entries missing either field: 0

*Updated by Claude after extraction pass. All missing fields filled using permissive extraction: Discussion, Limitations, Concluding Remarks, Outlook sections accepted as Conclusion equivalents.*

## Papers

### 1. 2008-representational-similarity-analysis-connecting-branches-systems-neuroscience.pdf

**Title**

2C_fnsys-02-004.indd

**Abstract**

ing from the activity patterns themselves and computing Functional Imaging Methods, Laboratory of Brain and Cognition, representational dissimilarity matrices (RDMs), which characterize the information carried by National Institute of Mental Health, a given representation in a brain or model. Building on a rich psychological and mathematical National Institutes of Health, Building literature on similarity analysis, we propose a new experimental and data-analytical framework 10, Room 1D80B, 10 Center Dr. MSC called representational similarity analysis (RSA), in which multi-channel measures of neural activity 1148, Bethesda, MD 20892-1148, USA. e-mail: kriegeskorten@mail.nih.gov are quantitatively related to each other and to computational theory and behavior by comparing RDMs. We demonstrate RSA by relating representations of visual objects as measured with fMRI in early visual cortex and the fusiform face area to computational models spanning a wide range of complexities. The RDMs are simultaneously related via second-level application of multidimensional scaling and tested using randomization and bootstrap techniques. We discuss the broad potential of RSA, including novel approaches to experimental design, and argue that these ideas, which have deep roots in psychology and neuroscience, will allow the integrated quantitative analysis of data from all three branches, thus contributing to a more unified systems neuroscience.

**Conclusion**

A fundamental question in systems neuroscience is to what extent brain-activity patterns measured with different techniques reflect neuronal pattern information. RSA characterizes pattern information in terms of pattern similarity and, thus, provides one attractive avenue for addressing this issue. We used RSA to relate neuronal patterns recorded in monkey IT to fMRI patterns elicited by the same set of 92 object images in human IT. Despite the confounding species difference, results show a surprising match between the two dissimilarity matrices (linear correlation = 0.49, p < 0.0001). This indicates not only that monkey and human IT represent similar object-image information, but also that this information is similarly reflected in single-cell recordings and high-resolution fMRI, when analyzed with massively multivariate information-based techniques. RSA lends itself to a broad spectrum of analyses from data-driven to hypothesis-driven, and the RDM at the front end of RSA provides a more data-driven, richer representation than a scalar measure of model fit. It appears likely that high-resolution fMRI and cell recording will turn out to convey overlapping but non-identical components of the underlying neuronal pattern information. RSA appears attractive for relating modalities and also for use in each modality, no matter what their relationship turns out to be.

*Conclusion added by Claude*

**Note**

Extracted from "DISCUSSION" section.

### 2. 2013-sinkhorn-distances-lightspeed-computation-optimal-transport.pdf

**Title**

SINKHORN DISTANCES: LIGHTSPEED COMPUTATION OF OPTIMAL TRANSPORTATION DISTANCES MARCO CUTURI

**Abstract**

Optimal transportation distances are a fundamental family of parameterized distances for histograms. Despite their appealing theoretical properties, excellent performance in retrieval tasks and intuitive formulation, their computation involves the resolution of a linear program whose cost is prohibitive whenever the histograms’ dimension exceeds a few hundreds. We propose in this work a new family of optimal transportation distances that look at transportation problems from a maximum-entropy perspective. We smooth the classical optimal transportation problem with an entropic regularization term, and show that the resulting optimum is also a distance which can be computed through Sinkhorn-Knopp’s matrix scaling algorithm at a speed that is several orders of magnitude faster than that of transportation solvers. We also report improved performance over classical optimal transportation distances on the MNIST benchmark problem.

**Conclusion**

We have shown that regularizing the optimal transportation problem with an intuitive entropic penalty opens the door for new research directions and potential applications at the intersection of optimal transportation theory and machine learning. This regularization guarantees speed-ups that are effective whatever the structure of the ground metric M . Based on preliminary evidence, it seems that Sinkhorn distances do not perform worse than the EMD, and may in fact perform better in applications. Sinkhorn distances are parameterized by a regularization weight λ which should be tuned having both computational and performance objectives in mind, but we have not observed a need to establish a trade-off between both. Indeed, reasonably small values of λ seem to perform better than large ones.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 3. 2014-understanding-image-representations-by-measuring-their-equivariance-equivalence.pdf

**Title**

Understanding Image Representations by Measuring Their Equivariance and Equivalence

**Abstract**

Despite the importance of image representations such as histograms of oriented gradients and deep Convolutional Neural Networks (CNN), our theoretical understanding of them remains limited. Aimed at filling this gap, we investigate two key mathematical properties of representations: equivariance and equivalence. Equivariance studies how transformations of the input image are encoded by the representation, invariance being a special case where a transformation has no effect. Equivalence studies whether two representations, for example two different parameterizations of a CNN, two different layers, or two different CNN architectures, share the same visual information or not. A number of methods to establish these properties empirically are proposed, including introducing transformation and stitching layers in CNNs. These methods are then applied to popular representations to reveal insightful aspects of their structure, including clarifying at which layers in a CNN certain geometric invariances are achieved and how various CNN architectures differ. We identify several predictors of geometric and architectural compatibility, including the spatial resolution of the representation and the complexity and depth of the models. While the focus of the paper is theoretical, direct applications to structured-output regression are demonstrated too.

Keywords Image representations · Geometric equivariance · Equivalent representations · Convolutional neural networks

**Conclusion**

This paper introduced the idea of studying representations by learning their equivariant and coverage/equivalence properties empirically. It was shown that shallow representations and the first several layers of deep state-of-the-art CNNs transform in an easily predictable manner with image warps. It was also shown that many representations tend to be interchangeable, and hence equivalent, despite differences, even substantial ones, in the architectures. Deeper layers share some of these properties but to a lesser degree, being more task-specific. A similarity of spatial resolution is a key predictor of representations compatibility; having a sufficiently-large spatial resolution is also predictive of the equivariance properties to geometric warps. Furthermore, deeper and larger representations tend to cover well for shallower and smaller ones. In addition the usage as analytical tools, these methods have practical applications such as accelerating structured-output regressors classifier in a simple and elegant manner.

*Conclusion added by Claude*

**Note**

Extracted from Section 7 "Summary".

### 4. 2014-word-representations-via-gaussian-embedding.pdf

**Title**

WORD REPRESENTATIONS VIA GAUSSIAN EMBEDDING Luke Vilnis, Andrew McCallum

**Abstract**

Current work in lexical distributed representations maps each word to a point vector in low-dimensional space. Mapping instead to a density provides many interesting advantages, including better capturing uncertainty about a representation and its relationships, expressing asymmetries more naturally than dot product or cosine similarity, and enabling more expressive parameterization of decision boundaries. This paper advocates for density-based distributed embeddings and presents a method for learning representations in the space of Gaussian distributions. We compare performance on various word embedding benchmarks, investigate the ability of these embeddings to model entailment and other asymmetric relationships, and explore novel properties of the representation.

**Conclusion**

In this work we introduced a method to embed word types into the space of Gaussian distributions, and learn the embeddings directly in that space. This allows us to represent words not as low-dimensional vectors, but as densities over a latent space, directly representing notions of uncertainty and enabling a richer geometry in the embedded space. We demonstrated the effectiveness of these embeddings on a linguistic task requiring asymmetric comparisons, as well as standard word similarity benchmarks, learning of synthetic hierarchies, and several qualitative examinations. In future work, we hope to move beyond spherical or diagonal covariances and into combinations of low rank and diagonal matrices. Efficient updates and scalable learning is still possible due to the Sherman-Woodbury-Morrison formula. Additionally, going beyond diagonal covariances will enable us to keep our semantics from being axis-aligned, which will increase model capacity and expressivity. We also hope to move past stochastic gradient descent and warm starting and be able to learn the Gaussian representations robustly in one pass from scratch by using e.g. proximal or block coordinate descent methods. Improved optimization strategies will also be helpful on the highly nonconvex problem of training supervised hierarchies with KL divergence. Representing words and concepts as different types of distributions (including other elliptic distributions such as the Student’s t) is an exciting direction – Gaussians concentrate their density on a thin spherical ellipsoidal shell, which can lead to counterintuitive behavior in high dimensions. Multimodal distributions represent another clear avenue for future work. Combining ideas from

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 5. 2015-from-word-embeddings-document-distances.pdf

**Title**

From Word Embeddings To Document Distances

**Abstract**

document 1 ‘greets’ document 2 We present the Word Mover’s Distance (WMD), Obama ‘Obama’ The a novel distance function between text docu- speaks ‘speaks’ President to ‘President’ greets ments. Our work is based on recent results in the the word embeddings that learn semantically mean- media ‘Chicago’ press in ‘media’ in ingful representations for words from local co- Illinois Chicago ‘Illinois’ ‘press’ occurrences in sentences. The WMD distance measures the dissimilarity between two text doc- word2vec embedding uments as the minimum amount of distance that Figure 1. An illustration of the word mover’s distance. All the embedded words of one document need to non-stop words (bold) of both documents are embedded into a “travel” to reach the embedded words of another word2vec space. The distance between the two documents is the document. We show that this distance metric can minimum cumulative distance that all words in document 1 need be cast as an instance of the Earth Mover’s Dis- to travel to exactly match document 2. (Best viewed in color.) tance, a well studied transportation problem for which several highly efficient solvers have been their frequent near-orthogonality (Schölkopf et al., 2002; developed. Our metric has no hyperparameters Greene & Cunningham, 2006). Another significant drawand is straight-forward to implement. Further, we back of these representations are that they do not capture demonstrate on eight real world document classi- the distance between individual words. Take for example fication data sets, in comparison with seven state- the two sentences in different documents: Obama speaks of-the-art baselines, that the WMD metric leads to the media in Illinois and: The President greets the press to unprecedented low k-nearest neighbor docu- in Chicago. While these sentences have no words in comment classification error rates. mon, they convey nearly the same information, a fact that cannot be represented by the BOW model. In this case, the closeness of the word pairs: (Obama, President); (speaks, greets); (media, press); and (Illinois, Chicago) is not fac-

**Conclusion**

It is worthwhile considering why the WMD metric leads to such low error rates across all data sets. We attribute this to its ability to utilize the high quality of the word2vec embedding. Trained on billions of words, the word2vec embedding captures knowledge about text documents in the English language that may not be obtainable from the training set alone. As pointed out by Mikolov et al. (2013a), other algorithms (such as LDA or LSI) do not scale naturally to data sets of such scale without special approximations which often counteract the benefit of large-scale data (although it is a worthy area of future work). Surprisingly, this "latent" supervision benefits tasks that are different from the data used to learn the word embedding.

One attractive feature of the WMD, that we would like to explore in the future, is its interpretability. Document distances can be dissected into sparse distances between words, which can be visualized and explained to humans. Another interesting direction will be to incorporate document structure into the distances between words by adding penalty terms if two words occur in different sections of similarly structured documents. If for example the WMD metric is used to measure the distance between academic papers, it might make sense to penalize word movements between the introduction and method section more than word movements from one introduction to another.

*Conclusion added by Claude*

**Note**

Extracted from Section 6 "Discussion and Conclusion".

### 6. 2015-vilnis-gaussian-embedding.pdf

**Title**

WORD REPRESENTATIONS VIA GAUSSIAN EMBEDDING Luke Vilnis, Andrew McCallum

**Abstract**

Current work in lexical distributed representations maps each word to a point vector in low-dimensional space. Mapping instead to a density provides many interesting advantages, including better capturing uncertainty about a representation and its relationships, expressing asymmetries more naturally than dot product or cosine similarity, and enabling more expressive parameterization of decision boundaries. This paper advocates for density-based distributed embeddings and presents a method for learning representations in the space of Gaussian distributions. We compare performance on various word embedding benchmarks, investigate the ability of these embeddings to model entailment and other asymmetric relationships, and explore novel properties of the representation.

**Conclusion**

In this work we introduced a method to embed word types into the space of Gaussian distributions, and learn the embeddings directly in that space. This allows us to represent words not as low-dimensional vectors, but as densities over a latent space, directly representing notions of uncertainty and enabling a richer geometry in the embedded space. We demonstrated the effectiveness of these embeddings on a linguistic task requiring asymmetric comparisons, as well as standard word similarity benchmarks, learning of synthetic hierarchies, and several qualitative examinations. In future work, we hope to move beyond spherical or diagonal covariances and into combinations of low rank and diagonal matrices. Efficient updates and scalable learning is still possible due to the Sherman-Woodbury-Morrison formula. Additionally, going beyond diagonal covariances will enable us to keep our semantics from being axis-aligned, which will increase model capacity and expressivity. We also hope to move past stochastic gradient descent and warm starting and be able to learn the Gaussian representations robustly in one pass from scratch by using e.g. proximal or block coordinate descent methods. Improved optimization strategies will also be helpful on the highly nonconvex problem of training supervised hierarchies with KL divergence. Representing words and concepts as different types of distributions (including other elliptic distributions such as the Student’s t) is an exciting direction – Gaussians concentrate their density on a thin spherical ellipsoidal shell, which can lead to counterintuitive behavior in high dimensions. Multimodal distributions represent another clear avenue for future work. Combining ideas from

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 7. 2016-diachronic-word-embeddings-reveal-statistical-laws-semantic-change.pdf

**Title**

Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change

**Abstract**

But many core questions about semantic change remain unanswered. One is the role of freUnderstanding how words change their quency. Frequency plays a key role in other linmeanings over time is key to models of guistic changes, associated sometimes with faster language and cultural evolution, but his- change—sound changes like lenition occur in torical data on meaning is scarce, mak- more frequent words—and sometimes with slower ing theories hard to develop and test. change—high frequency words are more resistant Word embeddings show promise as a di- to morphological regularization (Bybee, 2007; achronic tool, but have not been carefully Pagel et al., 2007; Lieberman et al., 2007). What evaluated. We develop a robust method- is the role of word frequency in meaning change? ology for quantifying semantic change Another unanswered question is the relationship by evaluating word embeddings (PPMI, between semantic change and polysemy. Words SVD, word2vec) against known historical gain senses over time as they semantically drift changes. We then use this methodology (Bréal, 1897; Wilkins, 1993; Hopper and Trauto reveal statistical laws of semantic evo- gott, 2003), and polysemous words1 occur in lution. Using six historical corpora span- more diverse contexts, affecting lexical access ning four languages and two centuries, we speed (Adelman et al., 2006) and rates of L2 propose two quantitative laws of seman- learning (Crossley et al., 2010). But we don’t tic change: (i) the law of conformity—the know whether the diverse contextual use of polrate of semantic change scales with an in- ysemous words makes them more or less likely verse power-law of word frequency; (ii) to undergo change (Geeraerts, 1997; Winter et the law of innovation—independent of fre- al., 2014; Xu et al., 2015). Furthermore, polyquency, words that are more polysemous semy is strongly correlated with frequency—high have higher rates of semantic change. frequency words have more senses (Zipf, 1945; İlgen and Karaoglan, 2007)—so understanding

**Conclusion**

We show how distributional methods can reveal statistical laws of semantic change and offer a robust methodology for future work in this area. The two statistical laws we propose have strong implications for future work in historical semantics. The law of conformity—frequent words change more slowly—clarifies frequency's role in semantic change. Future studies of semantic change must account for frequency's conforming effect. The law of innovation—polysemous words change more quickly—quantifies the central role polysemy plays in semantic change, an issue that has concerned linguists for more than 100 years. Overall, these two factors—frequency and polysemy—explain between 48% and 88% of the variance in rates of semantic change. This remarkable degree of explanatory power indicates that frequency and polysemy are perhaps the two most crucial linguistic factors that explain rates of semantic change over time.

*Conclusion added by Claude*

**Note**

Extracted from Section 5 "Discussion".

### 8. 2016-man-is-computer-programmer-as-woman-is-homemaker.pdf

**Title**

Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings Tolga Bolukbasi1 , Kai-Wei Chang2 , James Zou2 , Venkatesh Saligrama1,2 , Adam Kalai2

**Abstract**

The blind application of machine learning runs the risk of amplifying biases present in data. Such a danger is facing us with word embedding, a popular framework to represent text data as vectors which has been used in many machine learning and natural language processing tasks. We show that even word embeddings trained on Google News articles exhibit female/male gender stereotypes to a disturbing extent. This raises concerns because their widespread use, as we describe, often tends to amplify these biases. Geometrically, gender bias is first shown to be captured by a direction in the word embedding. Second, gender neutral words are shown to be linearly separable from gender definition words in the word embedding. Using these properties, we provide a methodology for modifying an embedding to remove gender stereotypes, such as the association between between the words receptionist and female, while maintaining desired associations such as between the words queen and female. We define metrics to quantify both direct and indirect gender biases in embeddings, and develop algorithms to “debias” the embedding. Using crowd-worker evaluation as well as standard benchmarks, we empirically demonstrate that our algorithms significantly reduce gender bias in embeddings while preserving the its useful properties such as the ability to cluster related concepts and to solve analogy tasks. The resulting embeddings can be used in applications without amplifying gender bias.

**Conclusion**

Word embeddings help us further our understanding of bias in language. We find a single direction that largely captures gender, that helps us capture associations between gender neutral words and gender as well as indirect inequality. The projection of gender neutral words on this direction enables us to quantify their degree of female- or male-bias. To reduce the bias in an embedding, we change the embeddings of gender neutral words, by removing their gender associations. Through empirical evaluations, we show that our hard-debiasing algorithm significantly reduces both direct and indirect gender bias while preserving the utility of the embedding. We have also developed a soft-embedding algorithm which balances reducing bias with preserving the original distances, and could be appropriate in specific settings. Corpus of documents often contain other undesirable stereotypes and these can also be reflected in the embedding vectors. An important direction of future work would be to quantify and remove these biases.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 9 "Discussion".

### 9. 2017-all-but-top-simple-effective-postprocessing-word-representations.pdf

**Title**

ALL-BUT-THE-TOP : SIMPLE AND EFFECTIVE POST-PROCESSING FOR WORD REPRESENTATIONS Jiaqi Mu, Pramod Viswanath

**Abstract**

arXiv:1702.01417v2 [cs.CL] 19 Mar 2018

Real-valued word representations have transformed NLP applications; popular examples are word2vec and GloVe, recognized for their ability to capture linguistic regularities. In this paper, we demonstrate a very simple, and yet counter-intuitive, postprocessing technique – eliminate the common mean vector and a few top dominating directions from the word vectors – that renders off-the-shelf representations even stronger. The postprocessing is empirically validated on a variety of lexical-level intrinsic tasks (word similarity, concept categorization, word analogy) and sentence-level tasks (semantic textural similarity and text classification) on multiple datasets and with a variety of representation methods and hyperparameter choices in multiple languages; in each case, the processed representations are consistently better than the original ones.

**Conclusion**

We present a simple postprocessing operation that renders word representations even stronger, by eliminating the top principal components of all words. Such an simple operation could be used for word embeddings in downstream tasks or as intializations for training task-specific embeddings. Due to their popularity, we have used the published representations of WORD2VEC and GLOVE in English in the main text of this paper; postprocessing continues to be successful for other representations and in multilingual settings – the detailed empirical results are tabulated in Appendix C.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 10. 2017-poincare-embeddings-learning-hierarchical-representations.pdf

**Title**

Poincaré Embeddings for Learning Hierarchical Representations

**Abstract**

Representation learning has become an invaluable approach for learning from symbolic data such as text and graphs. However, while complex symbolic datasets often exhibit a latent hierarchical structure, state-of-the-art methods typically learn embeddings in Euclidean vector spaces, which do not account for this property. For this purpose, we introduce a new approach for learning hierarchical representations of symbolic data by embedding them into hyperbolic space – or more precisely into an n-dimensional Poincaré ball. Due to the underlying hyperbolic geometry, this allows us to learn parsimonious representations of symbolic data by simultaneously capturing hierarchy and similarity. We introduce an efficient algorithm to learn the embeddings based on Riemannian optimization and show experimentally that Poincaré embeddings outperform Euclidean embeddings significantly on data with latent hierarchies, both in terms of representation capacity and in terms of generalization ability.

**Conclusion**

In this paper, we introduced Poincaré embeddings for learning representations of symbolic data and showed how they can simultaneously learn the similarity and the hierarchy of objects. Furthermore, we proposed an efficient algorithm to compute the embeddings and showed experimentally, that Poincaré embeddings provide important advantages over Euclidean embeddings on hierarchical data: First, Poincaré embeddings enable very parsimonious representations whats allows us to learn high-quality embeddings of large-scale taxonomies. Second, excellent link prediction results indicate that hyperbolic geometry can introduce an important structural bias for the embedding of complex symbolic data. Third, state-of-the-art results for predicting lexical entailment suggest that the hierarchy in the embedding space corresponds well to the underlying semantics of the data.

The main focus of this work was to evaluate the general properties of hyperbolic geometry for the embedding of symbolic data. In future work, we intend, to both expand the applications of Poincaré embeddings – for instance to multi-relational data – and also to derive models that are tailored to specific applications such as word embeddings. Furthermore, we have shown that natural gradient based optimization already produces very good embeddings and scales to large datasets. We expect that a full Riemannian optimization approach can further increase the quality of the embeddings and lead to faster convergence.

*Conclusion added by Claude*

**Note**

Extracted from Section 5 "Discussion and Future Work".

### 11. 2017-semantics-derived-automatically-from-language-corpora-contain-human.pdf

**Title**

This is an early draft. Please read/cite the published version instead: Caliskan, Aylin, Joanna J. Bryson, and Arvind Narayanan. “Semantics de-rived automatically from language corpora contain human-like biases.” Science

**Abstract**

Artificial intelligence and machine learning are in a period of astounding growth. However, there are concerns that these technologies may be used, either with or without intention, to perpetuate the prejudice and unfairness that unfortunately characterizes many human institutions. Here we show for the first time that human-like semantic biases result from the application of standard machine learning to ordinary language—the same sort of language humans are exposed to every day. We replicate a spectrum of standard human biases as exposed by the Implicit Association Test and other well-known psychological studies. We replicate these using a widely used, purely statistical machine-learning model—namely, the GloVe word embedding—trained on a corpus of text from the Web. Our results indicate that language itself contains recoverable and accurate imprints of our historic biases, whether these are morally neutral as towards insects or flowers, problematic as towards race or gender, or even simply veridical, reflecting the status quo for the distribution of gender with respect to careers or first names. These regularities are captured by machine learning along with the rest of semantics. In addition to our empirical findings concerning language, we also contribute new methods for evaluating bias in text, the Word Embedding Association Test (WEAT) and the Word Embedding Factual Association Test (WEFAT). Our results have implications not only for AI and machine learning, but also for the fields of psychology, sociology, and human ethics, since they raise the possibility that mere exposure to everyday language can account for the biases we replicate here.

**Conclusion**

We have shown that machine learning can acquire prejudicial biases from training data that reflect historical injustice. Unlike prior work on fairness in machine learning that tries to minimize or avoid such biases, our setting is not a particular, explicit decision-making task (known as "classification" in machine learning), but rather the often unconscious consequences of all of language. We show for the first time that if AI is to exploit via our language the vast knowledge that culture has compiled, it will inevitably inherit human-like prejudices. In other words, if AI learns enough about the properties of language to be able to understand and produce it, it also acquires cultural associations that can be offensive, objectionable, or harmful. We view the approach of "debiasing" word embeddings with skepticism, as debiasing alters the AI's perception (and model) of the world, rather than how it acts on that perception. Instead, we recommend continuing the program of research examining behavior that does and does not correlate to human subject performance in the IAT, and using our text processing tools to check pilot predictions for likely IAT performance on comparisons where none is currently known.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from "Discussion" section.

### 12. 2017-semeval-2017-task-1-semantic-textual-similarity-multilingual.pdf

**Title**

SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation

**Abstract**

STS include textual entailment (Bentivogli et al., 2016; Bowman et al., 2015; Dagan et al., 2010), Semantic Textual Similarity (STS) mea- semantic relatedness (Bentivogli et al., 2016) and sures the meaning similarity of sentences. paraphrase detection (Xu et al., 2015; Ganitkevitch Applications include machine translation et al., 2013; Dolan et al., 2004). STS differs from (MT), summarization, generation, question both textual entailment and paraphrase detection answering (QA), short answer grading, se- in that it captures gradations of meaning overlap mantic search, dialog and conversational rather than making binary classifications of parsystems. The STS shared task is a venue ticular relationships. While semantic relatedness for assessing the current state-of-the-art. expresses a graded semantic relationship as well, it The 2017 task focuses on multilingual and is non-specific about the nature of the relationship cross-lingual pairs with one sub-track ex- with contradictory material still being a candidate ploring MT quality estimation (MTQE) for a high score (e.g., “night” and “day” are highly data. The task obtained strong participa- related but not particularly similar). tion from 31 teams, with 17 participating To encourage and support research in this area, in all language tracks. We summarize per- the STS shared task has been held annually since formance and review a selection of well 2012, providing a venue for evaluation of state-ofperforming methods. Analysis highlights the-art algorithms and models (Agirre et al., 2012, common errors, providing insight into the 2013, 2014, 2015, 2016). During this time, dilimitations of existing models. To support verse similarity methods and data sets1 have been ongoing work on semantic representations, explored. Early methods focused on lexical sethe STS Benchmark is introduced as a new mantics, surface form matching and basic syntacshared training and evaluation set carefully tic similarity (Bär et al., 2012; Šarić et al., 2012a; selected from the corpus of English STS Jimenez et al., 2012a). During subsequent evaluashared task data (2012-2017). tions, strong new similarity signals emerged, such as Sultan et al. (2015)’s alignment based method.

**Conclusion**

We have presented the results of the 2017 STS shared task. This year's shared task differed substantially from previous iterations of STS in that the primary emphasis of the task shifted from English to multilingual and cross-lingual STS involving four different languages: Arabic, Spanish, English and Turkish. Even with this substantial change relative to prior evaluations, the shared task obtained strong participation. 31 teams produced 84 system submissions with 17 teams producing a total of 44 system submissions that processed pairs in all of the STS 2017 languages. For languages that were part of prior STS evaluations (e.g., English and Spanish), state-of-the-art systems are able to achieve strong correlations with human judgment. However, we obtain weaker correlations from participating systems for Arabic, Arabic-English and Turkish-English. This suggests further research is necessary in order to develop robust models that can both be readily applied to new languages and perform well even when less supervised training data is available. To provide a standard benchmark for English STS, we present the STS Benchmark, a careful selection of the English data sets from previous STS tasks (2012-2017).

*Conclusion added by Claude*

**Note**

Extracted from Section 9 "Conclusion".

### 13. 2017-svcca-singular-vector-canonical-correlation-analysis-deep-learning.pdf

**Title**

SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability Maithra Raghu,1,2 Justin Gilmer,1 Jason Yosinski,3 & Jascha Sohl-Dickstein1

**Abstract**

We propose a new technique, Singular Vector Canonical Correlation Analysis (SVCCA), a tool for quickly comparing two representations in a way that is both invariant to affine transform (allowing comparison between different layers and networks) and fast to compute (allowing more comparisons to be calculated than with previous methods). We deploy this tool to measure the intrinsic dimensionality of layers, showing in some cases needless over-parameterization; to probe learning dynamics throughout training, finding that networks converge to final representations from the bottom up; to show where class-specific information in networks is formed; and to suggest new training regimes that simultaneously save computation and overfit less.

**Conclusion**

In this paper we present SVCCA, a general method which allows for comparison of the learned distributed representations between different neural network layers and architectures. Using SVCCA we obtain novel insights into the learning dynamics and learned representations of common neural network architectures. These insights motivated a new Freeze Training technique which can reduce the number of flops required to train networks and potentially even increase generalization performance. We observe that CCA similarity can be a helpful tool for interpretability, with sensitivity to different classes reflecting their semantic properties. This technique also motivates a new algorithm for model compression. Finally, the “lower layers learn first” behavior was also observed for recurrent neural networks as shown in Figure App.6 in the Appendix.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 14. 2018-deep-contextualized-word-representations.pdf

**Title**

Deep Contextualized Word Representations

**Abstract**

guage model (LM) objective on a large text corpus. For this reason, we call them ELMo (EmWe introduce a new type of deep contextual- beddings from Language Models) representations. ized word representation that models both (1) Unlike previous approaches for learning contextucomplex characteristics of word use (e.g., syntax and semantics), and (2) how these uses alized word vectors (Peters et al., 2017; McCann vary across linguistic contexts (i.e., to model et al., 2017), ELMo representations are deep, in polysemy). Our word vectors are learned func- the sense that they are a function of all of the intions of the internal states of a deep bidirec- ternal layers of the biLM. More specifically, we tional language model (biLM), which is pre- learn a linear combination of the vectors stacked trained on a large text corpus. We show that above each input word for each end task, which these representations can be easily added to markedly improves performance over just using existing models and significantly improve the state of the art across six challenging NLP the top LSTM layer. problems, including question answering, tex- Combining the internal states in this manner altual entailment and sentiment analysis. We lows for very rich word representations. Using inalso present an analysis showing that exposing trinsic evaluations, we show that the higher-level the deep internals of the pre-trained network is LSTM states capture context-dependent aspects crucial, allowing downstream models to mix of word meaning (e.g., they can be used withdifferent types of semi-supervision signals. out modification to perform well on supervised word sense disambiguation tasks) while lower-

**Conclusion**

We have introduced a general approach for learning high-quality deep context-dependent representations from biLMs, and shown large improvements when applying ELMo to a broad range of NLP tasks. Through ablations and other controlled experiments, we have also confirmed that the biLM layers efficiently encode different types of syntactic and semantic information about words-in-context, and that using all layers improves overall task performance.

*Conclusion added by Claude*

**Note**

Extracted from Section 6 "Conclusion".

### 15. 2018-diachronic-word-embeddings-semantic-shifts-survey.pdf

**Title**

Diachronic word embeddings and semantic shifts: a survey Andrey Kutuzov Lilja Øvrelid Terrence Szymanski♦ Erik Velldal

**Abstract**

Recent years have witnessed a surge of publications aimed at tracing temporal changes in lexical arXiv:1806.03537v2 [cs.CL] 13 Jun 2018

semantics using distributional methods, particularly prediction-based word embedding models. However, this vein of research lacks the cohesion, common terminology and shared practices of more established areas of natural language processing. In this paper, we survey the current state of academic research related to diachronic word embeddings and semantic shifts detection. We start with discussing the notion of semantic shifts, and then continue with an overview of the existing methods for tracing such time-related shifts with word embedding models. We propose several axes along which these methods can be compared, and outline the main challenges before this emerging subfield of NLP, as well as prospects and possible applications.

**Conclusion**

We have presented an outline of the current research related to computational detection of semantic shifts using diachronic (temporal) word embeddings. We covered the linguistic nature of semantic shifts, the typical sources of diachronic data and the distributional approaches used to model it, from frequentist methods to contemporary prediction-based models. To sum up, Figure 1 shows the timeline of events that have been influential in the development of research in this area: introducing concepts, usage of corpora and important findings.

This emerging field is still relatively new, and although recent years has seen a string of significant discoveries and academic interchange, much of the research still appears slightly fragmented, not least due to the lack of dedicated venues like workshops, special issues, or shared tasks. We hope that this survey will be useful to those who want to understand how this field has developed, and gain an overview of what defines the current state-of-the-art and what challenges lie ahead.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 8 "Summary".

### 16. 2018-glue-multi-task-benchmark-analysis-platform-natural-language.pdf

**Title**

GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding

**Abstract**

Human ability to understand language is general, flexible, and robust. In contrast, most NLU models above the word level are designed for a specific task and struggle with out-of-domain data. We present the General Language Understanding Evaluation (GLUE) benchmark: a collection of nine diverse NLU tasks, an auxiliary dataset for probing models for understanding of specific linguistic phenomena, and an online platform for evaluating and comparing models. We evaluate baselines that use ELMo and state-of-the-art sentence representation models. The best models still achieve fairly low absolute scores, and analysis with our diagnostic dataset yields similarly weak performance over all phenomena tested, with some exceptions.

*Abstract added by Claude*

**Conclusion**

We present the GLUE benchmark, consisting of: (i) a suite of nine NLU tasks, built on established annotated datasets and covering a diverse range of text genres, dataset sizes, and difficulties; (ii) an online evaluation platform and leaderboard, based primarily on private test data; (iii) an expert-constructed analysis dataset. Experiments indicate that solving GLUE is beyond the capability of current transfer learning methods.

*Conclusion added by Claude*

**Note**

Extracted from pages 1-2 of a 3-page paper.

### 17. 2018-kutuzov-diachronic-survey.pdf

**Title**

Diachronic word embeddings and semantic shifts: a survey Andrey Kutuzov Lilja Øvrelid Terrence Szymanski♦ Erik Velldal

**Abstract**

Recent years have witnessed a surge of publications aimed at tracing temporal changes in lexical arXiv:1806.03537v2 [cs.CL] 13 Jun 2018

semantics using distributional methods, particularly prediction-based word embedding models. However, this vein of research lacks the cohesion, common terminology and shared practices of more established areas of natural language processing. In this paper, we survey the current state of academic research related to diachronic word embeddings and semantic shifts detection. We start with discussing the notion of semantic shifts, and then continue with an overview of the existing methods for tracing such time-related shifts with word embedding models. We propose several axes along which these methods can be compared, and outline the main challenges before this emerging subfield of NLP, as well as prospects and possible applications.

**Conclusion**

We have presented an outline of the current research related to computational detection of semantic shifts using diachronic (temporal) word embeddings. We covered the linguistic nature of semantic shifts, the typical sources of diachronic data and the distributional approaches used to model it, from frequentist methods to contemporary prediction-based models. To sum up, Figure 1 shows the timeline of events that have been influential in the development of research in this area: introducing concepts, usage of corpora and important findings.

This emerging field is still relatively new, and although recent years has seen a string of significant discoveries and academic interchange, much of the research still appears slightly fragmented, not least due to the lack of dedicated venues like workshops, special issues, or shared tasks. We hope that this survey will be useful to those who want to understand how this field has developed, and gain an overview of what defines the current state-of-the-art and what challenges lie ahead.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 8 "Summary".

### 18. 2018-learning-continuous-hierarchies-lorentz-model-hyperbolic-geometry.pdf

**Title**

Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry

**Abstract**

systems of concepts. However, explicit information about We are concerned with the discovery of hierar- such hierarchical relationships is unavailable for many dochical relationships from large-scale unstructured mains. In this paper, we therefore consider the problem of arXiv:1806.03417v2 [cs.AI] 8 Jul 2018

similarity scores. For this purpose, we study dif- discovering concept hierarchies from unstructured observaferent models of hyperbolic space and find that tions, specifically in the following setting: learning embeddings in the Lorentz model is substantially more efficient than in the Poincaré-ball 1. We focus on discovering pairwise hierarchical relations model. We show that the proposed approach between concepts, where all superior and subordinate allows us to learn high-quality embeddings of concepts are observed. large taxonomies which yield improvements over 2. We aim to infer concept hierarchies only from pairwise Poincaré embeddings, especially in low dimensimilarity measurements, which are relatively easy and sions. Lastly, we apply our model to discover cheap to obtain in many domains. hierarchies in two real-world datasets: we show that an embedding in hyperbolic space can reveal important aspects of a company’s organizational Examples of hierarchy discovery that adhere to this setting structure as well as reveal historical relationships include the creation of taxonomies from similarity judgbetween language families. ments (e.g., genetic similarity of species or cognate similarity of languages) and the recovery of organizational hierarchies and dominance relations from social interactions.

**Conclusion**

We introduced a new method for learning continuous concept hierarchies from unstructured observations. We exploited the properties of hyperbolic geometry in such a way that we can discover hierarchies from pairwise similarity scores – under the assumption that concepts in the same subtree of the ground-truth hierarchy are more similar to each other than to concepts in different subtrees. To learn the embeddings, we developed an efficient Riemannian optimization approach based on the Lorentz model of hyperbolic space. Due to the more principled optimization approach, we were able to substantially improve the quality of the embeddings compared to the method proposed by Nickel & Kiela (2017) – especially in low dimensions. We further showed on two real-world datasets, that our method can discover meaningful hierarchies from nothing but pairwise similarity information.

*Conclusion added by Claude*

**Note**

Extracted from Section 5 "Conclusion".

### 19. 2018-simple-unified-framework-detecting-out-distribution-samples-adversarial.pdf

**Title**

A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks Kimin Lee1 , Kibok Lee2 , Honglak Lee3,2 , Jinwoo Shin1,4

**Abstract**

Detecting test samples drawn sufficiently far away from the training distribution statistically or adversarially is a fundamental requirement for deploying a good classifier in many real-world machine learning applications. However, deep neural networks with the softmax classifier are known to produce highly overconfident posterior distributions even for such abnormal samples. In this paper, we propose a simple yet effective method for detecting any abnormal samples, which is applicable to any pre-trained softmax neural classifier. We obtain the class conditional Gaussian distributions with respect to (low- and upper-level) features of the deep models under Gaussian discriminant analysis, which result in a confidence score based on the Mahalanobis distance. While most prior methods have been evaluated for detecting either out-of-distribution or adversarial samples, but not both, the proposed method achieves the state-of-the-art performances for both cases in our experiments. Moreover, we found that our proposed method is more robust in harsh cases, e.g., when the training dataset has noisy labels or small number of samples. Finally, we show that the proposed method enjoys broader usage by applying it to class-incremental learning: whenever out-of-distribution samples are detected, our classification rule can incorporate new classes well without further training deep models.

**Conclusion**

In this paper, we propose a simple yet effective method for detecting abnormal test samples including both out-of-distribution and adversarial ones. In essence, our main idea is inducing a generative classifier under LDA assumption, and defining new confidence score based on it. With calibration techniques such as input pre-processing and feature ensemble, our method performs very strongly across multiple tasks: detecting out-of-distribution samples, detecting adversarial attacks and classincremental learning. We also found that our proposed method is more robust in the choice of its hyperparameters as well as against extreme scenarios, e.g., when the training dataset has some noisy, random labels or a small number of data samples. We believe that our approach have a potential to apply to many other related machine learning tasks, e.g., active learning [8], ensemble learning [19] and few-shot learning [31].

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 20. 2018-wic-word-context-dataset-evaluating-context-sensitive-meaning.pdf

**Title**

WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations Mohammad Taher Pilehvar1,2 and Jose Camacho-Collados3

**Abstract**

contextualized word embeddings (Melamud et al., 2016; Peters et al., 2018), which instead compute arXiv:1808.09121v3 [cs.CL] 27 Apr 2019

By design, word embeddings are unable to model the dynamic nature of words’ seman- a single dynamic embedding for a given word tics, i.e., the property of words to correspond which can adapt itself to arbitrary contexts for the to potentially different meanings. To address word. this limitation, dozens of specialized mean- Despite the popularity of research on these speing representation techniques such as sense cialised embeddings, very few benchmarks exor contextualized embeddings have been proist for their evaluation. Most works in this doposed. However, despite the popularity of research on this topic, very few evaluation main either perform evaluations on word similarbenchmarks exist that specifically focus on the ity datasets (in which words are presented in isoladynamic semantics of words. In this paper we tion; hence, they are not suitable for verifying the show that existing models have surpassed the dynamic nature of word semantics) or carry out performance ceiling of the standard evaluation impact analysis in downstream NLP applications dataset for the purpose, i.e., Stanford Contex- (usually, by taking word embeddings as baseline). tual Word Similarity, and highlight its shortDespite providing a suitable means of verifying comings. To address the lack of a suitable benchmark, we put forward a large-scale Word the effectiveness of the embeddings, the downin Context dataset, called WiC, based on anno- stream evaluation cannot replace generic evaluatations curated by experts, for generic evalua- tions as it is difficult to isolate the impact of emtion of context-sensitive representations. WiC beddings from many other factors involved, inis released in https://pilehvar.github.io/wic/. cluding the algorithmic configuration and parameter setting of the system. To our knowledge,

**Conclusion**

The Stanford Contextual Word Similarity (SCWS) dataset (Huang et al., 2012) comprises In this paper we have presented a benchmark for 2003 word pairs and is analogous to stan- evaluating context-sensitive word representations. dard word similarity datasets, such as RG-65 The proposed dataset, WiC, is based on lexico(Rubenstein and Goodenough, 1965) and Sim- graphic examples, which constitute a reliable basis Lex (Hill et al., 2015), in which the task is to to validate different models in their ability to perautomatically estimate the semantic similarity ceive and discern different meanings of words. We of word pairs. Ideally, the estimated similarity tested some of the recent state-of-the-art contextuscores should have high correlation with those alized and multi-prototype embedding models on given by human annotators. However, there is a our dataset. The considerable gap between the perfundamental difference between SCWS and other formance of these models and the human-level upword similarity datasets: each word in SCWS is perbound suggests ample room for future work on associated with a context which triggers a specific modeling the semantics of words in context. meaning of the word. The unique property of the 14 Only 8% (12% if ignoring PoS) of SCWS pairs are idendataset makes it a suitable benchmark for multi- tical but their assigned scores (by average 6.8) are substanprototype and contextualized word embeddings. tially higher than the dataset average of 3.6 on a [0,10] scale.

Acknowledgments Oren Melamud, Jacob Goldberger, and Ido Dagan. 2016. context2vec: Learning generic context emWe would like to thank Luis Espinosa-Anke and bedding with bidirectional lstm. In Proceedings Carla Pérez-Almendros for their help with the of The 20th SIGNLL Conference on Computational manual evaluation and Kiamehr Rezaee for run- Natural Language Learning, pages 51–61, Berlin,

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 21. 2019-bert-rediscovers-classical-nlp-pipeline.pdf

**Title**

BERT Rediscovers the Classical NLP Pipeline Ian Tenney1 Dipanjan Das1 Ellie Pavlick1,2

**Abstract**

of the network directly, to assess whether there exist localizable regions associated with distinct Pre-trained text encoders have rapidly adtypes of linguistic decisions. Such work has provanced the state of the art on many NLP arXiv:1905.05950v2 [cs.CL] 9 Aug 2019

tasks. We focus on one such model, BERT, duced evidence that deep language models can enand aim to quantify where linguistic informa- code a range of syntactic and semantic information is captured within the network. We find tion (e.g. Shi et al., 2016; Belinkov, 2018; Tenthat the model represents the steps of the tra- ney et al., 2019), and that more complex structures ditional NLP pipeline in an interpretable and are represented hierarchically in the higher layers localizable way, and that the regions respon- of the model (Peters et al., 2018b; Blevins et al., sible for each step appear in the expected se2018). quence: POS tagging, parsing, NER, semantic roles, then coreference. Qualitative analysis We build on this latter line of work, focusing reveals that the model can and often does ad- on the BERT model (Devlin et al., 2019), and use just this pipeline dynamically, revising lower- a suite of probing tasks (Tenney et al., 2019) delevel decisions on the basis of disambiguating rived from the traditional NLP pipeline to quantify information from higher-level representations. where specific types of linguistic information are encoded. Building on observations (Peters et al.,

**Conclusion**

We employ the edge probing task suite to explore how the different layers of the BERT network can resolve syntactic and semantic structure within a sentence. We present two complementary measurements: scalar mixing weights, learned from a training corpus, and cumulative scoring, measured on an evaluation set, and show that a consistent ordering emerges. We find that while this traditional pipeline order holds in the aggregate, on individual examples the network can resolve out-of-order, using high-level information like predicate-argument relations to help disambiguate low-level decisions like part-of-speech. This provides new evidence corroborating that deep language models can represent the types of syntactic and semantic abstractions traditionally believed necessary for language processing, and moreover that they can model complex interactions between different levels of hierarchical information.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 5 "Conclusion".

### 22. 2019-bertscore-evaluating-text-generation-with-bert.pdf

**Title**

BERTS CORE : EVALUATING TEXT GENERATION WITH BERT Tianyi Zhang∗†‡, Varsha Kishore∗‡, Felix Wu∗‡, Kilian Q. Weinberger†‡, and Yoav Artzi‡§ ‡

**Abstract**

We propose BERTS CORE, an automatic evaluation metric for text generation. Analogously to common metrics, BERTS CORE computes a similarity score for each token in the candidate sentence with each token in the reference sentence. However, instead of exact matches, we compute token similarity using contextual embeddings. We evaluate using the outputs of 363 machine translation and image captioning systems. BERTS CORE correlates better with human judgments and provides stronger model selection performance than existing metrics. Finally, we use an adversarial paraphrase detection task to show that BERTS CORE is more robust to challenging examples when compared to existing metrics.

**Conclusion**

We propose BERTSCORE, a new metric for evaluating generated text against gold standard references. BERTSCORE is purposely designed to be simple, task agnostic, and easy to use. Our analysis illustrates how BERTSCORE resolves some of the limitations of commonly used metrics, especially on challenging adversarial examples. We conduct extensive experiments with various configuration choices for BERTSCORE, including the contextual embedding model used and the use of importance weighting. Overall, our extensive experiments show that BERTSCORE achieves better correlation than common metrics, and is effective for model selection. However, there is no one configuration of BERTSCORE that clearly outperforms all others. While the differences between the top configurations are often small, it is important for the user to be aware of the different trade-offs, and consider the domain and languages when selecting the exact configuration to use. In general, for machine translation evaluation, we suggest using F_BERT, which we find the most reliable. In future work, we look forward to designing new task-specific metrics that use BERTSCORE as a subroutine and accommodate task-specific needs.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 7 "Discussion".

### 23. 2019-billion-scale-similarity-search-with-gpus.pdf

**Title**

Billion-scale similarity search with GPUs Jeff Johnson Matthijs Douze Hervé Jégou Facebook AI Research Facebook AI Research Facebook AI Research New York Paris Paris

**Abstract**

as the underlying processes either have high arithmetic comarXiv:1702.08734v1 [cs.CV] 28 Feb 2017

Similarity search finds application in specialized database plexity and/or high data bandwidth demands [28], or cannot systems handling complex data such as images or videos, be effectively partitioned without failing due to communiwhich are typically represented by high-dimensional features cation overhead or representation quality [38]. Once proand require specific indexing structures. This paper tackles duced, their manipulation is itself arithmetically intensive. the problem of better utilizing GPUs for this task. While However, how to utilize GPU assets is not straightforward. GPUs excel at data-parallel tasks, prior approaches are bot- More generally, how to exploit new heterogeneous architectlenecked by algorithms that expose less parallelism, such as tures is a key subject for the database community [9]. k-min selection, or make poor use of the memory hierarchy. In this context, searching by numerical similarity rather We propose a design for k-selection that operates at up than via structured relations is more suitable. This could be to 55% of theoretical peak performance, enabling a nearest to find the most similar content to a picture, or to find the neighbor implementation that is 8.5× faster than prior GPU vectors that have the highest response to a linear classifier state of the art. We apply it in different similarity search on all vectors of a collection. scenarios, by proposing optimized design for brute-force, ap- One of the most expensive operations to be performed on proximate and compressed-domain search based on product large collections is to compute a k-NN graph. It is a directed quantization. In all these setups, we outperform the state of graph where each vector of the database is a node and each the art by large margins. Our implementation enables the edge connects a node to its k nearest neighbors. This is construction of a high accuracy k-NN graph on 95 million our flagship application. Note, state of the art methods like images from the Yfcc100M dataset in 35 minutes, and of NN-Descent [15] have a large memory overhead on top of a graph connecting 1 billion vectors in less than 12 hours the dataset itself and cannot readily scale to the billion-sized on 4 Maxwell Titan X GPUs. We have open-sourced our databases we consider. approach1 for the sake of comparison and reproducibility. Such applications must deal with the curse of dimensionality [46], rendering both exhaustive search or exact indexing for non-exhaustive search impractical on billion-scale

**Conclusion**

The arithmetic throughput and memory bandwidth of GPUs are well into the teraflops and hundreds of gigabytes per second. However, implementing algorithms that approach these performance levels is complex and counter-intuitive. In this paper, we presented the algorithmic structure of similarity search methods that achieves near-optimal performance on GPUs. This work enables applications that needed complex approximate algorithms before. For example, the approaches presented here make it possible to do exact k-means clustering or to compute the k-NN graph with simple brute-force approaches in less time than a CPU (or a cluster of them) would take to do this approximately. GPU hardware is now very common on scientific workstations, due to their popularity for machine learning algorithms. We believe that our work further demonstrates their interest for database applications, and we are publishing a carefully engineered implementation of this paper's algorithms, so that these GPUs can now also be used for efficient similarity search.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 7 "Conclusion".

### 24. 2019-designing-interpreting-probes-with-control-tasks.pdf

**Title**

Designing and Interpreting Probes with Control Tasks

**Abstract**

Probes, supervised models trained to predict properties (like parts-of-speech) from representations (like ELMo), have achieved Sentence 1 The cat ran quickly . high accuracy on a range of linguistic tasks. Part-of-speech DT NN VBD RB . But does this mean that the representations Control task 10 37 10 15 3 encode linguistic structure or just that the Sentence 2 The dog ran after ! probe has learned the linguistic task? In Part-of-speech DT NN VBD IN . this paper, we propose control tasks, which Control task 10 15 10 42 42 associate word types with random outputs, to complement linguistic tasks. By construction, Figure 1: Our control tasks define random behavior (like a random output, top) for each word type in the vocabulary. these tasks can only be learned by the probe Each word token is assigned its type’s output, regardless of itself. So a good probe, (one that reflects the context (middle, bottom.) Control tasks have the same input representation), should be selective, achieving and output space as a linguistic task (e.g., parts-of-speech) but high linguistic task accuracy and low control can only be learned if the probe memorizes the mapping. task accuracy. The selectivity of a probe puts linguistic task accuracy in context with the probe’s capacity to memorize from word predict a property (like parts-of-speech) from a contypes. We construct control tasks for English strained view of the representation. Probes trained part-of-speech tagging and dependency edge on various representations have obtained high prediction, and show that popular probes on accuracy on tasks requiring part-of-speech and ELMo representations are not selective. We morphological information (Belinkov et al., 2017), also find that dropout, commonly used to control probe complexity, is ineffective for syntactic and semantic information (Peters et al., improving selectivity of MLPs, but that other 2018b; Tenney et al., 2019), among other properforms of regularization are effective. Finally, ties (Conneau et al., 2018), providing evidence that we find that while probes on the first layer deep representations trained on large datasets are of ELMo yield slightly better part-of-speech predictive of a broad range of linguistic properties. tagging accuracy than the second, probes But when a probe achieves high accuracy on on the second layer are substantially more a linguistic task using a representation, can we selective, which raises the question of which layer better represents parts-of-speech. conclude that the representation encodes linguistic structure, or has the probe just learned the task? Probing papers tend to acknowledge this

**Conclusion**

Through probing methods, it has been shown that a broad range of supervised learning tasks can be turned into tools for understanding the properties of contextual word representations (Conneau et al., 2018; Tenney et al., 2019). Alain and Bengio (2016) suggested we may think of probes as “thermometers used to measure the temperature simultaneously at many different locations”. We instead emphasize the joint roles of representations and probes together in achieving high accuracy on a task; we suggest that probes be thought of as craftspeople; their performance depends not only on the materials they’re given, but also on their expressivity.

To explore the relationship between representations, probes, and task accuracies, we defined control tasks, which by construction can only be learned by the probe itself. We’ve suggested that a probe which provides insights into the properties of the representation should be selective, achieving high linguistic task accuracy and low control task accuracy. We’ve found that linear and bilinear models achieve higher selectivity at similar accuracy to MLP probes on part-of-speech tagging. MLP probes, achieving higher accuracy on the more complex task of dependency edge prediction, can be re-designed to achieve higher selectivity at a relatively small cost to dependency edge accuracy, but often not through dropout, the most popular MLP probe regularization method.

*Conclusion added by Claude*

**Note**

Extracted from Section 6 “Conclusion”.

### 25. 2019-how-contextual-are-contextualized-word-representations-comparing-geometry.pdf

**Title**

How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings

**Abstract**

have successfully created contextualized word representations, word vectors that are sensitive to Replacing static word embeddings with con- the context in which they appear. Replacing textualized word representations has yielded static embeddings with contextualized representasignificant improvements on many NLP tasks. tions has yielded significant improvements on a diHowever, just how contextual are the contextualized representations produced by models verse array of NLP tasks, ranging from questionsuch as ELMo and BERT? Are there infinitely answering to coreference resolution. many context-specific representations for each The success of contextualized word represenword, or are words essentially assigned one of tations suggests that despite being trained with a finite number of word-sense representations? only a language modelling task, they learn highly For one, we find that the contextualized rep- transferable and task-agnostic properties of lanresentations of all words are not isotropic in guage. In fact, linear probing models trained on any layer of the contextualizing model. While representations of the same word in differfrozen contextualized representations can predict ent contexts still have a greater cosine simi- linguistic properties of words (e.g., part-of-speech larity than those of two different words, this tags) almost as well as state-of-the-art models (Liu self-similarity is much lower in upper layers. et al., 2019a; Hewitt and Manning, 2019). Still, This suggests that upper layers of contextu- these representations remain poorly understood. alizing models produce more context-specific For one, just how contextual are these contexturepresentations, much like how upper layers alized word representations? Are there infinitely of LSTMs produce more task-specific repremany context-specific representations that BERT sentations. In all layers of ELMo, BERT, and GPT-2, on average, less than 5% of the vari- and ELMo can assign to each word, or are words ance in a word’s contextualized representa- essentially assigned one of a finite number of tions can be explained by a static embedding word-sense representations? for that word, providing some justification for We answer this question by studying the geomthe success of contextualized representations. etry of the representation space for each layer of ELMo, BERT, and GPT-2. Our analysis yields

**Conclusion**

In this paper, we investigated how contextual contextualized word representations truly are. For one, we found that upper layers of ELMo, BERT, and GPT-2 produce more context-specific representations than lower layers. This increased context-specificity is always accompanied by increased anisotropy. However, context-specificity also manifests differently across the three models; the anisotropy-adjusted similarity between words in the same sentence is highest in ELMo but almost non-existent in GPT-2. We ultimately found that after adjusting for anisotropy, on average, less than 5% of the variance in a word’s contextualized representations could be explained by a static embedding. This means that even in the best-case scenario, in all layers of all models, static word embeddings would be a poor replacement for contextualized ones. These insights help explain some of the remarkable success that contextualized representations have had on a diverse array of NLP tasks.

*Conclusion added by Claude*

**Note**

Extracted from Section 6 "Conclusion".

### 26. 2019-lipstick-on-pig-debiasing-methods-cover-up-systematic.pdf

**Title**

Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them Hila Gonen1 and Yoav Goldberg1,2

**Abstract**

swer the analogy “man is to computer programWord embeddings are widely used in NLP mer as woman is to x” with “x = homemaker”. for a vast range of tasks. It was shown that Caliskan et al. (2017) further demonstrate associarXiv:1903.03862v2 [cs.CL] 24 Sep 2019

word embeddings derived from text corpora ation between female/male names and groups of reflect gender biases in society. This phe- words stereotypically assigned to females/males nomenon is pervasive and consistent across (e.g. arts vs. science). In addition, they demondifferent word embedding models, causing se- strate that word embeddings reflect actual gender rious concern. Several recent works tackle gaps in reality by showing the correlation between this problem, and propose methods for signifithe gender association of occupation words and cantly reducing this gender bias in word embeddings, demonstrating convincing results. labor-force participation data. However, we argue that this removal is super- Recently, some work has been done to reduce ficial. While the bias is indeed substantially the gender bias in word embeddings, both as a reduced according to the provided bias defi- post-processing step (Bolukbasi et al., 2016b) and nition, the actual effect is mostly hiding the as part of the training procedure (Zhao et al., bias, not removing it. The gender bias infor- 2018). Both works substantially reduce the bias mation is still reflected in the distances bewith respect to the same definition: the projection tween “gender-neutralized” words in the debi- − → −→ ased embeddings, and can be recovered from on the gender direction (i.e. he − she), introduced them. We present a series of experiments to in the former. They also show that performance on support this claim, for two debiasing meth- word similarity tasks is not hurt. ods. We conclude that existing bias removal We argue that current debiasing methods, which techniques are insufficient, and should not be lean on the above definition for gender bias and trusted for providing gender-neutral modeling. directly target it, are mostly hiding the bias rather

**Conclusion**

The experiments described in the previous section reveal a systematic bias found in the embeddings, which is independent of the gender direction. We observe that semantically related words still maintain gender bias both in their similarities, and in their representation. Words with strong previous gender bias (with the same direction) are easy to cluster together. Words that receive implicit gender from social stereotypes still tend to group with other implicit-gender words of the same gender. The implicit gender of words with prevalent previous bias is easy to predict based on their vectors alone. The implications are alarming: while suggested debiasing methods work well at removing the gender direction, the debiasing is mostly superficial. The bias stemming from world stereotypes and learned from the corpus is ingrained much more deeply in the embeddings space. Debiasing methods which directly target the gender-direction are for the most part merely hiding the gender bias and not removing it. The popular definitions used for quantifying and removing bias are insufficient, and other aspects of the bias should be taken into consideration as well.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 5 "Discussion and Conclusion".

### 27. 2019-pilehvar-wic.pdf

**Title**

WiC: the Word-in-Context Dataset for Evaluating Context-Sensitive Meaning Representations Mohammad Taher Pilehvar1,2 and Jose Camacho-Collados3

**Abstract**

contextualized word embeddings (Melamud et al., 2016; Peters et al., 2018), which instead compute arXiv:1808.09121v3 [cs.CL] 27 Apr 2019

By design, word embeddings are unable to model the dynamic nature of words’ seman- a single dynamic embedding for a given word tics, i.e., the property of words to correspond which can adapt itself to arbitrary contexts for the to potentially different meanings. To address word. this limitation, dozens of specialized mean- Despite the popularity of research on these speing representation techniques such as sense cialised embeddings, very few benchmarks exor contextualized embeddings have been proist for their evaluation. Most works in this doposed. However, despite the popularity of research on this topic, very few evaluation main either perform evaluations on word similarbenchmarks exist that specifically focus on the ity datasets (in which words are presented in isoladynamic semantics of words. In this paper we tion; hence, they are not suitable for verifying the show that existing models have surpassed the dynamic nature of word semantics) or carry out performance ceiling of the standard evaluation impact analysis in downstream NLP applications dataset for the purpose, i.e., Stanford Contex- (usually, by taking word embeddings as baseline). tual Word Similarity, and highlight its shortDespite providing a suitable means of verifying comings. To address the lack of a suitable benchmark, we put forward a large-scale Word the effectiveness of the embeddings, the downin Context dataset, called WiC, based on anno- stream evaluation cannot replace generic evaluatations curated by experts, for generic evalua- tions as it is difficult to isolate the impact of emtion of context-sensitive representations. WiC beddings from many other factors involved, inis released in https://pilehvar.github.io/wic/. cluding the algorithmic configuration and parameter setting of the system. To our knowledge,

**Conclusion**

The Stanford Contextual Word Similarity (SCWS) dataset (Huang et al., 2012) comprises In this paper we have presented a benchmark for 2003 word pairs and is analogous to stan- evaluating context-sensitive word representations. dard word similarity datasets, such as RG-65 The proposed dataset, WiC, is based on lexico(Rubenstein and Goodenough, 1965) and Sim- graphic examples, which constitute a reliable basis Lex (Hill et al., 2015), in which the task is to to validate different models in their ability to perautomatically estimate the semantic similarity ceive and discern different meanings of words. We of word pairs. Ideally, the estimated similarity tested some of the recent state-of-the-art contextuscores should have high correlation with those alized and multi-prototype embedding models on given by human annotators. However, there is a our dataset. The considerable gap between the perfundamental difference between SCWS and other formance of these models and the human-level upword similarity datasets: each word in SCWS is perbound suggests ample room for future work on associated with a context which triggers a specific modeling the semantics of words in context. meaning of the word. The unique property of the 14 Only 8% (12% if ignoring PoS) of SCWS pairs are idendataset makes it a suitable benchmark for multi- tical but their assigned scores (by average 6.8) are substanprototype and contextualized word embeddings. tially higher than the dataset average of 3.6 on a [0,10] scale.

Acknowledgments Oren Melamud, Jacob Goldberger, and Ido Dagan. 2016. context2vec: Learning generic context emWe would like to thank Luis Espinosa-Anke and bedding with bidirectional lstm. In Proceedings Carla Pérez-Almendros for their help with the of The 20th SIGNLL Conference on Computational manual evaluation and Kiamehr Rezaee for run- Natural Language Learning, pages 51–61, Berlin,

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 28. 2019-representation-degeneration-problem-training-natural-language-generation-models.pdf

**Title**

REPRESENTATION DEGENERATION PROBLEM IN TRAINING NATURAL LANGUAGE GENERATION MOD-ELS Jun Gao1,2,∗ †, Di He3,∗ , Xu Tan4 , Tao Qin4 , Liwei Wang3,5 & Tie-Yan Liu4

**Abstract**

We study an interesting problem in training neural network-based models for natural language generation tasks, which we call the representation degeneration problem. We observe that when training a model for natural language generation tasks through likelihood maximization with the weight tying trick, especially with big training datasets, most of the learnt word embeddings tend to degenerate and be distributed into a narrow cone, which largely limits the representation power of word embeddings. We analyze the conditions and causes of this problem and propose a novel regularization method to address it. Experiments on language modeling and machine translation show that our method can largely mitigate the representation degeneration problem and achieve better performance than baseline algorithms.

**Conclusion**

In this work, we described and analyzed the representation degeneration problem in training neural network models for natural language generation tasks both empirically and theoretically. We proposed a novel regularization method to increase the representation power of word embeddings explicitly. Experiments on language modeling and machine translation demonstrated the effectiveness of our method. In the future, we will apply our method to more language generation tasks. Our proposed regularization term is based on cosine similarity. There may exist some better regularization terms. Furthermore, it is interesting to combine with other approaches, e.g. (Gong et al., 2018), to enrich the representation of word embeddings.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 29. 2019-sentence-bert-sentence-embeddings-using-siamese-bert-networks.pdf

**Title**

Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

**Abstract**

tic similarity comparison, clustering, and information retrieval via semantic search. BERT (Devlin et al., 2018) and RoBERTa (Liu BERT set new state-of-the-art performance on et al., 2019) has set a new state-of-the-art various sentence classification and sentence-pair performance on sentence-pair regression tasks regression tasks. BERT uses a cross-encoder: Two like semantic textual similarity (STS). However, it requires that both sentences are fed sentences are passed to the transformer network into the network, which causes a massive com- and the target value is predicted. However, this putational overhead: Finding the most sim- setup is unsuitable for various pair regression tasks ilar pair in a collection of 10,000 sentences due to too many possible combinations. Finding requires about 50 million inference computa- in a collection of n = 10 000 sentences the pair tions (~65 hours) with BERT. The construction with the highest similarity requires with BERT of BERT makes it unsuitable for semantic simn·(n−1)/2 = 49 995 000 inference computations. ilarity search as well as for unsupervised tasks like clustering. On a modern V100 GPU, this requires about 65 hours. Similar, finding which of the over 40 milIn this publication, we present Sentence-BERT lion existent questions of Quora is the most similar (SBERT), a modification of the pretrained for a new question could be modeled as a pair-wise BERT network that use siamese and triplet network structures to derive semantically mean- comparison with BERT, however, answering a siningful sentence embeddings that can be com- gle query would require over 50 hours. pared using cosine-similarity. This reduces the A common method to address clustering and seeffort for finding the most similar pair from 65 mantic search is to map each sentence to a vechours with BERT / RoBERTa to about 5 sec- tor space such that semantically similar sentences onds with SBERT, while maintaining the ac- are close. Researchers have started to input indicuracy from BERT. vidual sentences into BERT and to derive fixedWe evaluate SBERT and SRoBERTa on com- size sentence embeddings. The most commonly mon STS tasks and transfer learning tasks, used approach is to average the BERT output layer where it outperforms other state-of-the-art (known as BERT embeddings) or by using the outsentence embeddings methods.1 put of the first token (the [CLS] token). As we will show, this common practice yields rather bad

**Conclusion**

Sentence embeddings need potentially be computed for Millions of sentences, hence, a high We showed that BERT out-of-the-box maps sencomputation speed is desired. In this section, we tences to a vector space that is rather unsuitcompare SBERT to average GloVe embeddings, able to be used with common similarity measures InferSent (Conneau et al., 2017), and Universal like cosine-similarity. The performance for seven Sentence Encoder (Cer et al., 2018). STS tasks was below the performance of average For our comparison we use the sentences from GloVe embeddings. the STS benchmark (Cer et al., 2017). We com- To overcome this shortcoming, we presented pute average GloVe embeddings using a sim- Sentence-BERT (SBERT). SBERT fine-tunes ple for-loop with python dictionary lookups and BERT in a siamese / triplet network architecNumPy. InferSent4 is based on PyTorch. For ture. We evaluated the quality on various comUniversal Sentence Encoder, we use the Tensor- mon benchmarks, where it could achieve a sigFlow Hub version5 , which is based on Tensor- nificant improvement over state-of-the-art senFlow. SBERT is based on PyTorch. For improved tence embeddings methods. Replacing BERT with computation of sentence embeddings, we imple- RoBERTa did not yield a significant improvement mented a smart batching strategy: Sentences with in our experiments. similar lengths are grouped together and are only SBERT is computationally efficient. On a GPU, padded to the longest element in a mini-batch. it is about 9% faster than InferSent and about 55% This drastically reduces computational overhead faster than Universal Sentence Encoder. SBERT from padding tokens. can be used for tasks which are computationally Performances were measured on a server with not feasible to be modeled with BERT. For examIntel i7-5820K CPU @ 3.30GHz, Nvidia Tesla ple, clustering of 10,000 sentences with hierarchical clustering requires with BERT about 65 hours,

### 30. 2019-similarity-neural-network-representations-revisited.pdf

**Title**

Similarity of Neural Network Representations Revisited

**Abstract**

This paper investigates the problem of measuring similariRecent work has sought to understand the behav- ties between deep neural network representations. An effecior of neural networks by comparing representa- tive method for measuring representational similarity could tions between layers and between different trained help answer many interesting questions, including: (1) Do arXiv:1905.00414v4 [cs.LG] 19 Jul 2019

models. We examine methods for comparing neu- deep neural networks with the same architecture trained ral network representations based on canonical from different random initializations learn similar reprecorrelation analysis (CCA). We show that CCA sentations? (2) Can we establish correspondences between belongs to a family of statistics for measuring mul- layers of different network architectures? (3) How simitivariate similarity, but that neither CCA nor any lar are the representations learned using the same network other statistic that is invariant to invertible linear architecture from different datasets? transformation can measure meaningful similari- We build upon previous studies investigating similarity beties between representations of higher dimension tween the representations of neural networks (Laakso & than the number of data points. We introduce Cottrell, 2000; Li et al., 2015; Raghu et al., 2017; Morcos a similarity index that measures the relationship et al., 2018; Wang et al., 2018). We are also inspired by the between representational similarity matrices and extensive neuroscience literature that uses representational does not suffer from this limitation. This simi- similarity analysis (Kriegeskorte et al., 2008a; Edelman, larity index is equivalent to centered kernel align- 1998) to compare representations across brain areas (Haxby ment (CKA) and is also closely connected to CCA. et al., 2001; Freiwald & Tsao, 2010), individuals (Connolly Unlike CCA, CKA can reliably identify corre- et al., 2012), species (Kriegeskorte et al., 2008b), and bespondences between representations in networks haviors (Elsayed et al., 2016), as well as between brains trained from different initializations. and neural networks (Yamins et al., 2014; Khaligh-Razavi & Kriegeskorte, 2014; Sussillo et al., 2015).

**Conclusion**

Measuring similarity between the representations learned by neural networks is an ill-defined problem, since it is not entirely clear what aspects of the representation a similarity index should focus on. Previous work has suggested that there is little similarity between intermediate layers of neural networks trained from different random initializations. We propose CKA as a method for comparing representations of neural networks, and show that it consistently identifies correspondences between layers, not only in the same network trained from different initializations, but across entirely different architectures, whereas other methods do not. We also provide a unified framework for understanding the space of similarity indexes, as well as an empirical framework for evaluation. We show that CKA captures intuitive notions of similarity, i.e. that neural networks trained from different initializations should be similar to each other. However, it remains an open question whether there exist kernels beyond the linear and RBF kernels that would be better for analyzing neural network representations.

*Conclusion added by Claude*

**Note**

Extracted from Section 7 "Conclusion and Future Work".

### 31. 2019-structural-probe-finding-syntax-word-representations.pdf

**Title**

A Structural Probe for Finding Syntax in Word Representations

**Abstract**

In this work, we propose a structural probe, a simple model which tests whether syntax trees are Recent work has improved our ability to consistently embedded in a linear transformation detect linguistic knowledge in word repreof a neural network’s word representation space. sentations. However, current methods for detecting syntactic knowledge do not test Tree structure is embedded if the transformed space whether syntax trees are represented in their has the property that squared L2 distance between entirety. In this work, we propose a structural two words’ vectors corresponds to the number of probe, which evaluates whether syntax trees edges between the words in the parse tree. To reare embedded in a linear transformation of a construct edge directions, we hypothesize a linear neural network’s word representation space. transformation under which the squared L2 norm The probe identifies a linear transformation corresponds to the depth of the word in the parse under which squared L2 distance encodes the distance between words in the parse tree, and tree. Our probe uses supervision to find the transone in which squared L2 norm encodes depth formations under which these properties are best in the parse tree. Using our probe, we show approximated for each model. If such transforthat such transformations exist for both ELMo mations exist, they define inner products on the and BERT but not in baselines, providing original space under which squared distances and evidence that entire syntax trees are embedded norms encode syntax trees – even though the modimplicitly in deep models’ vector geometry. els being probed were never given trees as input or supervised to reconstruct them. This is a structural

**Conclusion**

In summary, through our structural probes we demonstrate that the structure of syntax trees emerges through properly defined distances and norms on two deep models' word representation spaces. Beyond this actionable insight, we suggest our probe may be useful for testing the existence of different types of graph structures on any neural representation of language, an exciting avenue for future work.

*Conclusion added by Claude*

**Note**

Extracted from Section 5 "Discussion & Conclusion".

### 32. 2019-visualizing-measuring-geometry-bert.pdf

**Title**

Visualizing and Measuring the Geometry of BERT Andy Coenen∗, Emily Reif∗, Ann Yuan∗ Been Kim, Adam Pearce, Fernanda Viégas, Martin Wattenberg Google Brain

**Abstract**

Transformer architectures show significant promise for natural language processing. Given that a single pretrained model can be fine-tuned to perform well on many different tasks, these networks appear to extract generally useful linguistic features. How do such networks represent this information internally? This paper describes qualitative and quantitative investigations of one particularly effective model, BERT. At a high level, linguistic features seem to be represented in separate semantic and syntactic subspaces. We find evidence of a fine-grained geometric representation of word senses. We also present empirical descriptions of syntactic representations in both attention matrices and individual word embeddings, as well as a mathematical argument to explain the geometry of these representations.

**Conclusion**

We have presented a series of experiments that shed light on BERT’s internal representations of linguistic information. We have found evidence of syntactic representation in attention matrices, with certain directions in space representing particular dependency relations. We have also provided a mathematical justification for the squared-distance tree embedding found by Hewitt and Manning. Meanwhile, we have shown that just as there are specific syntactic subspaces, there is evidence for subspaces that represent semantic information. We also have shown how mistakes in word sense disambiguation may correspond to changes in internal geometric representation of word meaning. Our experiments also suggest an answer to the question of how all these different representations fit together. We conjecture that the internal geometry of BERT may be broken into multiple linear subspaces, with separate spaces for different syntactic and semantic information. Investigating this kind of decomposition is a natural direction for future research. What other meaningful subspaces exist? After all, there are many types of linguistic information that we have not looked for. A second important avenue of exploration is what the internal geometry can tell us about the specifics of the transformer architecture. Can an understanding of the geometry of internal representations help us find areas for improvement, or refine BERT’s architecture? Acknowledgments: We would like to thank David Belanger, Tolga Bolukbasi, Jasper Snoek, and Ian Tenney for helpful feedback and discussions.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 33. 2020-approximate-nearest-neighbor-negative-contrastive-learning-dense-text.pdf

**Title**

Preprint APPROXIMATE NEAREST NEIGHBOR NEGATIVE CON-TRASTIVE LEARNING FOR DENSE TEXT RETRIEVAL Lee Xiong∗, Chenyan Xiong∗, Ye Li, Kwok-Fung Tang, Jialin Liu,

**Abstract**

arXiv:2007.00808v2 [cs.IR] 20 Oct 2020

Conducting text retrieval in a dense representation space has many intriguing advantages. Yet the end-to-end learned dense retrieval (DR) often underperforms word-based sparse retrieval. In this paper, we first theoretically show the learning bottleneck of dense retrieval is due to the domination of uninformative negatives sampled locally in batch, which yield diminishing gradient norms, large stochastic gradient variances, and slow learning convergence. We then propose Approximate nearest neighbor Negative Contrastive Learning (ANCE), a learning mechanism that selects hard training negatives globally from the entire corpus, using an asynchronously updated ANN index. Our experiments demonstrate the effectiveness of ANCE on web search, question answering, and in a commercial search environment, showing ANCE dot-product retrieval nearly matches the accuracy of BERT-based cascade IR pipeline, while being 100x more efficient.

**Conclusion**

In this paper, we first provide theoretical analyses on the convergence of representation learning in dense retrieval. We show that under common conditions in text retrieval, the local negatives used in DR training are uninformative, yield low gradient norms, and contribute little to the learning convergence. We then propose ANCE to eliminate this bottleneck by constructing training negatives globally from the entire corpus. Our experiments demonstrate the advantage of ANCE in web search, OpenQA, and the production system of a commercial search engine. Our studies empirically validate our theory that ANCE negatives have much bigger gradient norms, reduce the stochastic gradient variance, and improve training convergence.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 34. 2020-dense-passage-retrieval-open-domain-question-answering.pdf

**Title**

Dense Passage Retrieval for Open-Domain Question Answering

**Abstract**

Retrieval in open-domain QA is usually implemented using TF-IDF or BM25 (Robertson and Open-domain question answering relies on efficient passage retrieval to select candidate Zaragoza, 2009), which matches keywords efficontexts, where traditional sparse vector space ciently with an inverted index and can be seen models, such as TF-IDF or BM25, are the de as representing the question and context in highfacto method. In this work, we show that dimensional, sparse vectors (with weighting). Conretrieval can be practically implemented us- versely, the dense, latent semantic encoding is coming dense representations alone, where em- plementary to sparse representations by design. For beddings are learned from a small number example, synonyms or paraphrases that consist of of questions and passages by a simple dualcompletely different tokens may still be mapped to encoder framework. When evaluated on a wide range of open-domain QA datasets, our vectors close to each other. Consider the question dense retriever outperforms a strong Lucene- “Who is the bad guy in lord of the rings?”, which can BM25 system greatly by 9%-19% absolute in be answered from the context “Sala Baker is best terms of top-20 passage retrieval accuracy, and known for portraying the villain Sauron in the Lord helps our end-to-end QA system establish new of the Rings trilogy.” A term-based system would state-of-the-art on multiple open-domain QA have difficulty retrieving such a context, while benchmarks.1 a dense retrieval system would be able to better

**Conclusion**

In this work, we demonstrated that dense retrieval can outperform and potentially replace the traditional sparse retrieval component in open-domain question answering. While a simple dual-encoder approach can be made to work surprisingly well, we showed that there are some critical ingredients to training a dense retriever successfully. Moreover, our empirical analysis and ablation studies indicate that more complex model frameworks or similarity functions do not necessarily provide additional values. As a result of improved retrieval performance, we obtained new state-of-the-art results on multiple open-domain question answering benchmarks.

*Conclusion added by Claude*

**Note**

Extracted from Section 8 “Conclusion”.

### 35. 2020-do-wide-deep-networks-learn-same-things-uncovering.pdf

**Title**

DOWIDE AND DEEP NETWORKS LEARN THE SAME THINGS ? UNCOVERING HOW NEURAL NETWORK REPRESENTATIONS VARY WITH WIDTH AND DEPTH Thao Nguyen∗, Maithra Raghu, & Simon Kornblith

**Abstract**

A key factor in the success of deep neural networks is the ability to scale models to improve performance by varying the architecture depth and width. This simple property of neural network design has resulted in highly effective architectures for a variety of tasks. Nevertheless, there is limited understanding of effects of depth and width on the learned representations. In this paper, we study this fundamental question. We begin by investigating how varying depth and width affects model hidden representations, finding a characteristic block structure in the hidden representations of larger capacity (wider or deeper) models. We demonstrate that this block structure arises when model capacity is large relative to the size of the training set, and is indicative of the underlying layers preserving and propagating the dominant principal component of their representations. This discovery has important ramifications for features learned by different models, namely, representations outside the block structure are often similar across architectures with varying widths and depths, but the block structure is unique to each model. We analyze the output predictions of different model architectures, finding that even when the overall accuracy is similar, wide and deep models exhibit distinctive error patterns and variations across classes.

**Conclusion**

In this work, we study the effects of width and depth on neural network representations. Through experiments on CIFAR-10, CIFAR-100 and ImageNet, we have demonstrated that as either width or depth increases relative to the size of the dataset, analysis of hidden representations reveals the emergence of a characteristic block structure that reflects the similarity of a dominant first principal component, propagated across many network hidden layers. Further analysis finds that while the block structure is unique to each model, other learned features are shared across different initializations and architectures, particularly across relative depths of the network. Despite these similarities in representational properties and performance of wide and deep networks, we nonetheless observe that width and depth have different effects on network predictions at the example and class levels. There remain interesting open questions on how the block structure arises through training, and using the insights on network depth and width to inform optimal task-specific model design.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 36. 2020-energy-based-out-distribution-detection.pdf

**Title**

Energy-based Out-of-distribution Detection Weitang Liu Xiaoyun Wang

**Abstract**

Determining whether inputs are out-of-distribution (OOD) is an essential building block for safely deploying machine learning models in the open world. However, previous methods relying on the softmax confidence score suffer from overconfident posterior distributions for OOD data. We propose a unified framework for OOD detection that uses an energy score. We show that energy scores better distinguish in- and out-of-distribution samples than the traditional approach using the softmax scores. Unlike softmax confidence scores, energy scores are theoretically aligned with the probability density of the inputs and are less susceptible to the overconfidence issue. Within this framework, energy can be flexibly used as a scoring function for any pre-trained neural classifier as well as a trainable cost function to shape the energy surface explicitly for OOD detection. On a CIFAR-10 pre-trained WideResNet, using the energy score reduces the average FPR (at TPR 95%) by 18.03% compared to the softmax confidence score. With energy-based training, our method outperforms the state-of-the-art on common benchmarks.

**Conclusion**

In this work, we propose an energy-based framework for out-of-distribution detection. We show that energy score is a simple and promising replacement of the softmax confidence score. The key idea is to use a non-probabilistic energy function that attributes lower values to in-distribution data and higher values to out-of-distribution data. Unlike softmax confidence scores, the energy scores are less susceptible to the overconfidence problem. We further propose an energy-bounded learning objective to explicitly create an energy gap for OOD detection. Energy fine-tuning achieves state-of-the-art performance on standard OOD detection benchmarks, outperforming both softmax-based and other competitive methods.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 6 "Conclusion and Outlook".

### 37. 2020-retrieval-augmented-generation-knowledge-intensive-nlp-tasks.pdf

**Title**

Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks Patrick Lewis†‡ , Ethan Perez? , Aleksandra Piktus† , Fabio Petroni† , Vladimir Karpukhin† , Naman Goyal† , Heinrich Küttler† ,

**Abstract**

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pretrained models with a differentiable access mechanism to explicit non-parametric memory have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and another which can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledgeintensive NLP tasks and set the state of the art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

**Conclusion**

In this work, we presented hybrid generation models with access to parametric and non-parametric memory. We showed that our RAG models obtain state of the art on open-domain QA. We found that people prefer RAG's generation over purely parametric BART, finding RAG more factual and specific. We conducted an thorough investigation of the learned retrieval component, validating its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model without requiring any retraining. In future work, it may be fruitful to investigate if the two components can be jointly pre-trained from scratch. Our work opens up new research directions on how parametric and non-parametric memories interact and how to most effectively combine them, showing promise in being applied to a wide variety of NLP tasks.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Extracted from Section 6 "Discussion".

### 38. 2020-understanding-contrastive-representation-learning-through-alignment-uniformity-o.pdf

**Title**

Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere

**Abstract**

arXiv:2005.10242v10 [cs.LG] 15 Aug 2022

Contrastive representation learning has been outstandingly successful in practice. In this work, we identify two key properties related to the contrastive loss: (1) alignment (closeness) of features from positive pairs, and (2) uniformity of the induced distribution of the (normalized) features on the hypersphere. We prove that, asymptotically, the contrastive loss optimizes these properties, and analyze their positive effects on downstream tasks. Empirically, we introduce an optimizable metric to quantify each property. Extensive experiments on standard vision and language datasets Alignment: Similar samples have similar features. features confirm the strong agreement between both met- (Figure inspired by Tian et al. (2019).) rics and downstream task performance. Directly optimizing for these two metrics leads to representations with comparable or better performance at downstream tasks than contrastive learning. Project Page: ssnl.github.io/hypersphere. Code: github.com/SsnL/align uniform. github.com/SsnL/moco align uniform.

**Conclusion**

In this work, we have presented a detailed investigation on the relation between these properties and the popular paradigm of contrastive representation learning. Through theoretical analysis and extensive experiments, we are able to relate the contrastive loss with the alignment and uniformity properties, and confirm their strong connection with downstream task performances. Remarkably, we have revealed that directly optimizing our proposed metrics often leads to representations of better quality. Alignment and uniformity are indeed desirable properties for representations, for both image and text modalities, and are likely connected with general contrastive representation learning methods.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 39. 2020-zhang-bertscore.pdf

**Title**

BERTS CORE : EVALUATING TEXT GENERATION WITH BERT Tianyi Zhang∗†‡, Varsha Kishore∗‡, Felix Wu∗‡, Kilian Q. Weinberger†‡, and Yoav Artzi‡§ ‡

**Abstract**

We propose BERTS CORE, an automatic evaluation metric for text generation. Analogously to common metrics, BERTS CORE computes a similarity score for each token in the candidate sentence with each token in the reference sentence. However, instead of exact matches, we compute token similarity using contextual embeddings. We evaluate using the outputs of 363 machine translation and image captioning systems. BERTS CORE correlates better with human judgments and provides stronger model selection performance than existing metrics. Finally, we use an adversarial paraphrase detection task to show that BERTS CORE is more robust to challenging examples when compared to existing metrics.

**Conclusion**

We propose BERTSCORE, a new metric for evaluating generated text against gold standard references. BERTSCORE is purposely designed to be simple, task agnostic, and easy to use. Our analysis illustrates how BERTSCORE resolves some of the limitations of commonly used metrics, especially on challenging adversarial examples. We conduct extensive experiments with various configuration choices for BERTSCORE, including the contextual embedding model used and the use of importance weighting. Overall, our extensive experiments, including the ones in the appendix, show that BERTSCORE achieves better correlation than common metrics, and is effective for model selection. However, there is no one configuration of BERTSCORE that clearly outperforms all others. While the differences between the top configurations are often small, it is important for the user to be aware of the different trade-offs, and consider the domain and languages when selecting the exact configuration to use. In general, for machine translation evaluation, we suggest using F_BERT, which we find the most reliable. For evaluating text generation in English, we recommend using the 24-layer RoBERTa_large model to compute BERTSCORE. For non-English language, the multilingual BERT_multi is a suitable choice although BERTSCORE computed with this model has less stable performance on low-resource languages.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 40. 2021-bansal-revisiting-model-stitching.pdf

**Title**

Revisiting Model Stitching to Compare Neural Representations Yamini Bansal Preetum Nakkiran Boaz Barak

**Abstract**

We revisit and extend model stitching (Lenc & Vedaldi 2015) as a methodology to study the internal representations of neural networks. Given two trained and frozen models A and B, we consider a “stitched model” formed by connecting the bottom-layers of A to the top-layers of B, with a simple trainable layer between them. We argue that model stitching is a powerful and perhaps under-appreciated tool, which reveals aspects of representations that measures such as centered kernel alignment (CKA) cannot. Through extensive experiments, we use model stitching to obtain quantitative verifications for intuitive statements such as “good networks learn similar representations”, by demonstrating that good networks of the same architecture, but trained in very different ways (e.g.: supervised vs. self-supervised learning), can be stitched to each other without drop in performance. We also give evidence for the intuition that “more is better” by showing that representations learnt with (1) more data, (2) bigger width, or (3) more training time can be “plugged in” to weaker models to improve performance. Finally, our experiments reveal a new structural property of SGD which we call “stitching connectivity”, akin to mode-connectivity: typical minima reached by SGD can all be stitched to each other with minimal change in accuracy.

**Conclusion**

As our work demonstrates, model stitching can be a very useful tool to compare representations in interpretable units. Model stitching does have its limitations: it requires training a network, making it more expensive in computation than other measures such as CKA. Additionally, stitching representations from two different architectures can be tricky and requires a careful choice of the stitching family. While we restricted ourselves to stitching the first l layers of a network, stitching can be used to also plug in intermediate layers or parts of layers, and in general to “assemble” a new model from a collection of pre-trained components. There are various avenues for future research. All of our results are in the vision domain, but it would be interesting to compare representations in natural language processing, since language tasks tend to have more variety than vision tasks. It would also be interesting to study the representations of adversarially trained networks to diagnose why they lose performance in comparison to standard training. In general, we hope that model stitching will become a part of the standard diagnostic repertoire of the deep learning community.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 41. 2021-bis-shifting-embeddings.pdf

**Title**

Too Much in Common: Shifting of Embeddings in Transformer Language Models and its Implications

**Abstract**

and Viswanath, 2018). To address the issues, postprocessing methods (Mu and Viswanath, 2018), The success of language models based on the and regularization terms have been proposed (Gao Transformer architecture appears to be inconet al., 2019; Wang et al., 2019c, 2020). However, sistent with observed anisotropic properties of representations learned by such models. We the mechanism that leads to undesirable properresolve this by showing, contrary to previous ties remains unclear. Without understanding the studies, that the representations do not occupy mechanism, it is going to be difficult to address the a narrow cone, but rather drift in common di- fundamental issue properly. rections. At any training step, all of the em- The deficiencies are most pronounced in the repbeddings except for the ground-truth target em- resentations of rare words, as we will show in bedding are updated with gradient in the same Section 4. Performance of pretrained language direction. Compounded over the training set, the embeddings drift and share common com- models is inconsistent and tends to decrease when ponents, manifested in their shape in all the input contains rare words (Schick and Schütze, models we have empirically tested. Our ex- 2020b,a). Schick and Schütze (2020a) observe periments show that isotropy can be restored that replacing a portion of words in the MNLI using a simple transformation.1 (Williams et al., 2018) entailment data set with less frequent synonyms leads to decrease in per-

**Conclusion**

We find that the embeddings learned by GPT-2, BERT, and RoBERTa do not degenerate into a narrow cone, as has been suggested in the past, but instead drift in one shared direction. We recognize that target words produce gradients in the same direction for all the non-target words at each training step. Combined with the unbalanced distribution of word frequencies, any two words' embeddings will be repeatedly updated with gradients of the same direction. As such updates accumulate, the embeddings drift and share common components. Our experiments show that simply centering the embeddings restores a nearly perfectly isotropic distribution of tested models' embeddings and simultaneously improves embeddings' ability to reflect semantic relations. This understanding of the learning process dynamics opens exciting avenues for future work, such as improving the most affected embeddings of rare words and formulation of more computationally efficient training objectives.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 42. 2021-clipscore-reference-free-evaluation-metric-image-captioning.pdf

**Title**

CLIPScore: A Reference-free Evaluation Metric for Image Captioning Jack Hessel† Ari Holtzman‡ Maxwell Forbes‡ Ronan Le Bras† Yejin Choi†‡ †

**Abstract**

How clipScore works reference captions - Two dogs are running towards each Image captioning has conventionally relied on other across the sand. reference-based automatic evaluations, where - Two dogs run toward each other. machine captions are compared against cap- Two dogs are running towards each tions written by humans. This is in contrast other on a beach. to the reference-free manner in which humans 0.83 clip candidate assess caption quality. Two dogs run towards each cos clip sim. other on a marshy area. clipScore In this paper, we report the surprising empirical finding that CLIP (Radford et al., 2021), clipScore vs traditional image captioning metrics references a cross-modal model pretrained on 400M im- - A helmeted boy flies through the air on ❌ bleu-1 ❌ spice age+caption pairs from the web, can be used a snowboard. 33.3 0.0 - A snowboarder balancing on a wall. for robust automatic evaluation of image cap- - A snowboarder in green grinds along ❌ cider-d meteor ❌ the edge of a rail at night. tioning without the need for references. Ex- - A snowboarder wearing a green jacket 3.3 0.5

periments spanning several corpora demon- jumping a green railing. vs humans clipScore vs candidate strate that our new reference-free metric, ✓4/4 ✓74.0 Person snowboarding at a ski slope. CLIPScore, achieves the highest correlation references - A dirt biker in the forest. bleu-1 spice with human judgements, outperforming exist- - A dirt biker rides his motorcycle through the woods. ✓46.2 ✓19.4 ing reference-based metrics like CIDEr and - A motocross bike is being ridden along meteor cider-d SPICE. Information gain experiments demon- a woodland path. - A person rides a motorbike on a dirt ✓18.1 ✓10.3 strate that CLIPScore, with its tight focus path surrounded by trees. vs

on image–text compatibility, is complemen- ❌ humans ❌ Score clip vs candidate 1/4 37.4 A grey dog walks on top of a fallen tree in the woods. tary to existing reference-based metrics that emphasize text–text similarities. Thus, we also present a reference-augmented version, image-caption compatibility without using references, RefCLIPScore, which achieves even higher just like humans. Bottom: This frees CLIPScore correlation. Beyond literal description tasks, from the well-known shortcomings of n-gram matchseveral case studies reveal domains where ing metrics, which disfavor good captions with new CLIPScore performs well (clip-art images, words (top) and favor any captions with familiar words (bottom). Attribution: Paperclip, robot icons by Hasanudin, alt-text rating), but also where it is relatively Adiyogi (resp.) from the Noun Project. weaker in comparison to reference-based metrics, e.g., news captions that require richer contextual knowledge. against even multiple human-authored captions for

**Conclusion**

This research is supported in part by DARPA MCS For literal image description tasks, CLIPScore program through NIWC Pacific (N66001-19-2achieves high correlation with human judgments 4031), DARPA SemaFor program, and the Allen of caption quality without references when used in Institute for AI. We additionally thank Ximing an off-the-shelf fashion. Additional experiments Lu, Swabha Swayamdipta, Youngjae Yu, and the in divergent domains suggest that CLIP can also anonymous EMNLP reviewers for the helpful comreason about non-photographic clip-art, and serves ments, thoughts, and discussions. Finally, we thank as a reasonable option for reference-free evaluation Jin-Hwa Kim, who in March 2022, helped discover in the alt-text case. Promising future work includes a now fixed discrepancy for the Pascal-50S results, exploring 1) CLIP-S as a reinforcement learning re- see Appendix A. ward for literal caption generators; and 2) whether a small amount of labelled human rating data could help CLIP-S adapt to domains where it struggles,

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 43. 2021-generalized-shape-metrics-on-neural-representations.pdf

**Title**

Generalized Shape Metrics on Neural Representations Alex H. Williams Erin Kunz

**Abstract**

Understanding the operation of biological and artificial networks remains a difficult and important challenge. To identify general principles, researchers are increasingly interested in surveying large collections of networks that are trained on, or biologically adapted to, similar tasks. A standardized set of analysis tools is now needed to identify how network-level covariates—such as architecture, anatomical brain region, and model organism—impact neural representations (hidden layer activations). Here, we provide a rigorous foundation for these analyses by defining a broad family of metric spaces that quantify representational dissimilarity. Using this framework we modify existing representational similarity measures based on canonical correlation analysis to satisfy the triangle inequality, formulate a novel metric that respects the inductive biases in convolutional layers, and identify approximate Euclidean embeddings that enable network representations to be incorporated into essentially any off-the-shelf machine learning method. We demonstrate these methods on large-scale datasets from biology (Allen Institute Brain Observatory) and deep learning (NAS-Bench-101). In doing so, we identify relationships between neural representations that are interpretable in terms of anatomical features and model performance.

**Conclusion**

We demonstrated how to ground analyses of neural representations in proper metric spaces. By doing so, we capture a number of theoretical advantages. Further, we suggest new practical modeling approaches, such as using Euclidean embeddings to approximate the representational metric spaces. An important limitation of our work, as well as the past works we build upon, is the possibility that representational geometry is only loosely tied to higher-level algorithmic principles of network function. On the other hand, analyses of representational geometry may provide insight into lower-level implementational principles. Further, these analyses are highly scalable, as we demonstrated by analyzing thousands of networks—a much larger scale than is typically considered. We used simple metrics (extensions of regularized CCA) in these analyses, but metrics that account for nonlinear transformations across neural representations are also possible as we document in Supplement C. Finally, several of the metrics we described can be viewed as geodesic distances on Riemannian manifolds. Future work would ideally exploit methods that are rigorously adapted to such manifolds, which are being actively developed. Nonetheless, we found that optimized Euclidean embeddings, while only approximate, provide a practical off-the-shelf solution for large-scale surveys of neural representations.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 44. 2021-how-does-fine-tuning-affect-geometry-embedding-space.pdf

**Title**

How Does Fine-tuning Affect the Geometry of Embedding Space: A Case Study on Isotropy

**Abstract**

semantic expressiveness of embedding space, the latter reflects the unwanted social bias in training It is widely accepted that fine-tuning pre- data (Li et al., 2020; Garg et al., 2018; Gonen and trained language models usually brings about Goldberg, 2019). The representation degeneration performance improvements in downstream tasks. However, there are limited studies on problem is another issue that limits their linguistic the reasons behind this effectiveness, particu- capacity. Gao et al. (2019) showed that the weight larly from the viewpoint of structural changes tying trick (Inan et al., 2017) in the pre-training in the embedding space. Trying to fill this procedure is mainly responsible for the degenergap, in this paper, we analyze the extent to ation problem in the embedding space. In such which the isotropy of the embedding space a case, the embeddings occupy a narrow cone in changes after fine-tuning. We demonstrate the space (Ethayarajh, 2019). Several approaches that, even though isotropy is a desirable geometrical property, fine-tuning does not neces- have been proposed to improve the isotropy of sarily result in isotropy enhancements. More- pre-trained models, which in turn boosts the repover, local structures in pre-trained contextual resentation power and downstream performance word representations (CWRs), such as those of CWRs (Zhang et al., 2020; Wang et al., 2020). encoding token types or frequency, undergo a However, previous studies have mainly focused massive change during fine-tuning. Our ex- on the anisotropy of pre-trained language models. periments show dramatic growth in the num- Here, we investigate the impact of fine-tuning on ber of elongated directions in the embedding isotropy. Specifically, We try to answer the followspace, which, in contrast to pre-trained CWRs, carry the essential linguistic knowledge in the ing questions: fine-tuned embedding space, making existing isotropy enhancement methods ineffective. • Can the improved performance achieved by fine-tuning pre-trained language models

**Conclusion**

CWRs colored based on their frequency in BERT and In this paper, we explored the effect of fine-tuning RoBERTa (using Wikipedia dump as corpus). The more frequent words have darker colors. As can be on the structure of the embedding space of BERT observed, the embedding space is still anisotropic afterand RoBERTa. Our analysis demonstrates that the fine-tuning, while the frequency-based distribution of remarkable performance usually gained as a reCWRs has been remedied. sult of fine-tuning is not due to its enhancement of isotropy in the embedding space. Similarly to their pre-trained counterparts, fine-tuned CWRs we observe a slight drop in the performance com- have elongated directions towards different dimenpared to removing 12 top dominant directions. This sions across all layers, and the number of these suggests that the top dominant directions carry es- directions tends to increase by fine-tuning. We sential knowledge about the target task. We leave have also found that fine-tuning changes the nature further investigation of this interesting behavior to of the linguistic knowledge encoded in dominant future work. directions such that removing them hurts the performance (unlike pre-trained models for which reThe clustered structure of the embedding space moving such directions often result in performance changes during fine-tuning. The results of the improvements). Moreover, the clustered structure Clustering+ZM setting and Cluster-based approach of pre-trained models is entirely modified upon in Table 1 show that the clustered structure of the fine-tuning, producing unbiased embedding space pre-trained embedding space (Cai et al., 2021) has from the viewpoint of word frequency. faded in the fine-tuned CWRs. These two set- As future work, we plan to experiment with more tings can improve the STS performance of the target tasks and different fine-tuning strategies to pre-trained model by increasing isotropy. How- expand our knowledge about the fine-tuning proever, applying them to fine-tuned CWRs leads to cedure. Furthermore, we aim at exploring the type performance reduction. Moreover, as can be seen of linguistic knowledge encoded in specific dimenin Figure 2, the local areas that encode frequency sions or subspaces in the semantic space.

### 45. 2021-isoscore-measuring-uniformity-embedding-space-utilization.pdf

**Title**

IsoScore: Measuring the Uniformity of Embedding Space Utilization William Rudman† , Nate Gillman‡ , Taylor Rayne∗ , Carsten Eickhoff†

**Abstract**

all dimensions when embedded into three dimenThe recent success of distributed word repre- sions. sentations has led to an increased interest in analyzing the properties of their spatial distribution. Several studies have suggested that contextualized word embedding models do not isotropically project tokens into vector space. However, current methods designed to measure isotropy, such as average random cosine similarity and the partition score, have not Figure 1: From left to right, a line, disk, and ball embeen thoroughly analyzed and are not appro- bedded in 3D space. priate for measuring isotropy. We propose IsoScore: a novel tool that quantifies the de- A distribution is isotropic when variance is unigree to which a point cloud uniformly utilizes formly distributed across all dimensions. Namely, the ambient vector space. Using rigorously designed tests, we demonstrate that IsoScore is a distribution is fully isotropic when the covariance the only tool available in the literature that ac- matrix is proportional to the identity matrix. Sevcurately measures how uniformly distributed eral authors suggest that isotropy correlates with variance is across dimensions in vector space. improved performance of embedding models (Biś Additionally, we use IsoScore to challenge a et al., 2021; Wang et al., 2019; Coenen et al., 2019a; number of recent conclusions in the NLP liter- Gong et al., 2018; Hasan and Curry, 2017; Heature that have been derived using brittle metwitt and Manning, 2019; Liang et al., 2021; Zhou rics of isotropy. We caution future studies from using existing tools to measure isotropy et al., 2019, 2021). However, current methods of in contextualized embedding space as result- measuring the spatial utilization of contextualized ing conclusions will be misleading or alto- embedding models do not truly measure isotropy. gether inaccurate. The most commonly used methods for measuring spatial distribution in embedding spaces include av-

**Conclusion**

Several studies have attempted to study isotropy in contextualized embedding models. Using mathematically rigorous tests, we demonstrate that current methods do not accurately measure isotropy. This paper presents IsoScore: a novel method for measuring isotropy that corrects the current misunderstandings in the literature. IsoScore is the only tool that is mean agnostic, robust to scalar changes to the covariance matrix and rotation invariant. Furthermore, IsoScore scales linearly with the number dimensions used and is stable when distributions contain highly isotropic subspaces. Future studies should avoid using existing methods to measure isotropy as resulting conclusions will be misleading or altogether inaccurate. There are several promising directions for future work. Current studies have used inaccurate methods to claim that increasing isotropy improves the performance of contextualized embedding models. However, we believe that further decreasing isotropy could improve performance, especially in language modeling applications. IsoScore could be used as a regularizer when fine tuning word embeddings to penalize distributions that exhibit isotropy. As point clouds of data arise in nearly all deep learning applications, IsoScore presents itself as a useful tool to study and refine a variety of models beyond the domain of NLP.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 46. 2021-learning-transferable-visual-models-from-natural-language-supervision.pdf

**Title**

Learning Transferable Visual Models From Natural Language Supervision

**Abstract**

Task-agnostic objectives such as autoregressive and masked language modeling have scaled across many orders of magState-of-the-art computer vision systems are arXiv:2103.00020v1 [cs.CV] 26 Feb 2021

nitude in compute, model capacity, and data, steadily imtrained to predict a fixed set of predetermined proving capabilities. The development of “text-to-text” as object categories. This restricted form of supera standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled taskadditional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream other visual concept. Learning directly from raw datasets removing the need for specialized output heads or text about images is a promising alternative which dataset specific customization. Flagship systems like GPT-3 leverages a much broader source of supervision. (Brown et al., 2020) are now competitive across many tasks We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset of predicting which caption goes with which imspecific training data. age is an efficient and scalable way to learn SOTA image representations from scratch on a dataset These results suggest that the aggregate supervision accesof 400 million (image, text) pairs collected from sible to modern pre-training methods within web-scale colthe internet. After pre-training, natural language lections of text surpasses that of high-quality crowd-labeled is used to reference learned visual concepts (or NLP datasets. However, in other fields such as computer describe new ones) enabling zero-shot transfer vision it is still standard practice to pre-train models on of the model to downstream tasks. We study crowd-labeled datasets such as ImageNet (Deng et al., 2009). the performance of this approach by benchmark- Could scalable pre-training methods which learn directly ing on over 30 different existing computer vi- from web text result in a similar breakthrough in computer sion datasets, spanning tasks such as OCR, ac- vision? Prior work is encouraging. tion recognition in videos, geo-localization, and Over 20 years ago Mori et al. (1999) explored improving many types of fine-grained object classification. content based image retrieval by training a model to preThe model transfers non-trivially to most tasks dict the nouns and adjectives in text documents paired with and is often competitive with a fully supervised images. Quattoni et al. (2007) demonstrated it was possibaseline without the need for any dataset speble to learn more data efficient image representations via cific training. For instance, we match the acmanifold learning in the weight space of classifiers trained curacy of the original ResNet-50 on ImageNet to predict words in captions associated with images. Srizero-shot without needing to use any of the 1.28 vastava & Salakhutdinov (2012) explored deep represenmillion training examples it was trained on. We tation learning by training multimodal Deep Boltzmann release our code and pre-trained model weights at Machines on top of low-level image and text tag features. https://github.com/OpenAI/CLIP. Joulin et al. (2016) modernized this line of work and demonstrated that CNNs trained to predict words in image captions learn useful image representations. They converted

**Conclusion**

Our methodology has several significant limitations. Despite our focus on zero-shot transfer, we repeatedly queried performance on full validation sets to guide the development of CLIP. These validation sets often have thousands of examples, which is unrealistic for true zero-shot scenarios. Significant work is still needed to improve the task learning and transfer capabilities of CLIP. While scaling has so far steadily improved performance and suggests a route for continued improvement, we estimate around a 1000x increase in compute is required for zero-shot CLIP to reach overall state-of-the-art performance. This is infeasible to train with current hardware. CLIP also does not address the poor data efficiency of deep learning. Instead CLIP compensates by using a source of supervision that can be scaled to hundreds of millions of training examples. While zero-shot CLIP generalizes well to many natural image distributions, zero-shot CLIP still generalizes poorly to data that is truly out-of-distribution for it. Our studies of CLIP in a zero-shot setting show that the model displays significant promise for widely-applicable tasks like image retrieval or search. The relative ease of steering CLIP toward bespoke applications with little or no additional data or training could unlock a variety of novel applications that are hard for us to envision today, as has occurred with large language models over the past few years.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 47. 2021-scalable-interpretable-semantic-change-detection.pdf

**Title**

Scalable and Interpretable Semantic Change Detection

**Abstract**

it indicates a possible change in word’s context or even loss or gain of a word sense. Thus, the Several cluster-based methods for semantic change detection with contextual embeddings cluster-based approach offers a more intuitive inemerged recently. They allow a fine-grained terpretation of word usage change than alternative analysis of word use change by aggregating methods, which look at the neighborhood of a word embeddings into clusters that reflect the differ- in each time period to interpret the change (Gonen ent usages of the word. However, these meth- et al., 2020; Martinc et al., 2020b) and ignore the ods are unscalable in terms of memory con- fact that a word can have more than one meaning. sumption and computation time. Therefore, The main limitation of the cluster-based methods they require a limited set of target words to be picked in advance. This drastically limits the is the scalability in terms of memory consumption usability of these methods in open exploratory and time: clustering is applied to each word in the tasks, where each word from the vocabulary corpus separately and all occurrences of a word can be considered as a potential target. We pro- need to be aggregated into clusters. For large corpose a novel scalable method for word usage- pora with large vocabularies, where some words change detection that offers large gains in pro- can appear millions of times, the use of these methcessing time and significant memory savings ods is severely limited. while offering the same interpretability and better performance than unscalable methods. To avoid the scalability issue, cluster-based methWe demonstrate the applicability of the pro- ods are generally applied to a small set of less than posed method by analysing a large corpus of a hundred manually pre-selected words (Giulianelli news articles about COVID-19. et al., 2020; Martinc et al., 2020a). This drastically limits the application of the methods in scenarios

**Conclusion**

We proposed a scalable and interpretable method for word usage change detection, which outperforms the non-scalable contextual embeddings-based methods by a large margin. The new method also allows completely data-driven analysis of word sense dynamic in large corpora, which was impossible to conduct with unscalable methods. This opens new opportunities in both language change studies and text stream monitoring tasks. In this paper we focused on the latter application by analysing a large corpus of COVID-19 related news. The method is outperformed by the state-of-the-art SGNS+OP+CD method. We hypothesise that this can be connected with the fact that the sentences in all but one evaluation corpus (COHA) are shuffled, meaning that BERT models cannot leverage the usual sequence of 512 tokens as a context, but are limited to the number of tokens in the sentence. Despite achieving lower performance than the SGNS+OP+CD method, we nevertheless argue that our method offers a more fine-grained interpretation than methods based on non-contextual embeddings, since it accounts for the fact that words can have multiple meanings. The cluster-based technique returns a degree of change and a set of sentence clusters for each word in the corpus, roughly corresponding to word senses or particular usages.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 48. 2021-scaling-up-visual-vision-language-representation-learning-with.pdf

**Title**

Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

**Abstract**

Pre-trained representations are becoming crucial for many NLP and perception tasks. While representation learning in NLP has transitioned to training on raw text without human annotations, visual and vision-language representations still rely heavily on curated training datasets that are expensive or require expert knowledge. In this paper, we leverage a noisy dataset of over one billion image alt-text pairs, obtained without expensive filtering or post-processing steps in the Conceptual Captions dataset. A simple dual-encoder architecture learns to align visual and language representations of the image and text pairs using a contrastive loss. We show that the scale of our corpus can make up for its noise and leads to state-of-the-art representations even with such a simple learning scheme. Our visual representation achieves strong performance when transferred to classification tasks such as ImageNet and VTAB. The aligned visual and language representations enables zero-shot image classification and also set new state-of-the-art results on Flickr30K and MSCOCO image-text retrieval benchmarks, even when compared with more sophisticated cross-attention models. The representations also enable cross-modality search with complex text and text + image queries.

*Abstract added by Claude*

**Conclusion**

We present a simple method of leveraging large-scale noisy image-text data to scale up visual and vision-language representation learning. Our method avoids heavy work on data curation and annotation, and only requires minimal frequency-based cleaning. On this dataset, we train a simple dual-encoder model using a contrastive loss. The resulting model, named ALIGN, is capable of cross-modal retrieval and significantly outperforms SOTA VSE and cross-attention vision-language models. In visual-only downstream tasks, ALIGN is also comparable to or outperforms SOTA models trained with large-scale labeled data.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 49. 2021-simcse-simple-contrastive-learning-sentence-embeddings.pdf

**Title**

SimCSE: Simple Contrastive Learning of Sentence Embeddings

**Abstract**

embedding methods and demonstrate that a contrastive objective can be extremely effective when This paper presents SimCSE, a simple con- coupled with pre-trained language models such as trastive learning framework that greatly ad- BERT (Devlin et al., 2019) or RoBERTa (Liu et al., vances the state-of-the-art sentence embed2019). We present SimCSE, a simple contrastive dings. We first describe an unsupervised approach, which takes an input sentence and sentence embedding framework, which can propredicts itself in a contrastive objective, with duce superior sentence embeddings, from either only standard dropout used as noise. This unlabeled or labeled data. simple method works surprisingly well, per- Our unsupervised SimCSE simply predicts the forming on par with previous supervised couninput sentence itself with only dropout (Srivastava terparts. We find that dropout acts as minimal data augmentation and removing it leads et al., 2014) used as noise (Figure 1(a)). In other to a representation collapse. Then, we pro- words, we pass the same sentence to the pre-trained pose a supervised approach, which incorpo- encoder twice: by applying the standard dropout rates annotated pairs from natural language twice, we can obtain two different embeddings as inference datasets into our contrastive learn- “positive pairs”. Then we take other sentences in the ing framework, by using “entailment” pairs same mini-batch as “negatives”, and the model preas positives and “contradiction” pairs as hard dicts the positive one among negatives. Although it negatives. We evaluate SimCSE on standard may appear strikingly simple, this approach outpersemantic textual similarity (STS) tasks, and our unsupervised and supervised models using forms training objectives such as predicting next BERTbase achieve an average of 76.3% and sentences (Logeswaran and Lee, 2018) and discrete 81.6% Spearman’s correlation respectively, a data augmentation (e.g., word deletion and replace4.2% and 2.2% improvement compared to ment) by a large margin, and even matches previous previous best results. We also show—both supervised methods. Through careful analysis, we theoretically and empirically—that contrastive find that dropout acts as minimal “data augmentalearning objective regularizes pre-trained emtion” of hidden representations, while removing it beddings’ anisotropic space to be more uniform, and it better aligns positive pairs when leads to a representation collapse. 1 Our supervised SimCSE builds upon the recent supervised signals are available. success of using natural language inference (NLI)

**Conclusion**

In this work, we propose SimCSE, a simple contrastive learning framework, which greatly improves state-of-the-art sentence embeddings on semantic textual similarity tasks. We present an unsupervised approach which predicts input sentence itself with dropout noise and a supervised approach utilizing NLI datasets. We further justify the inner workings of our approach by analyzing alignment and uniformity of SimCSE along with other baseline models. We believe that our contrastive objective, especially the unsupervised one, may have a broader application in NLP. It provides a new perspective on data augmentation with text input, and can be extended to other continuous representations and integrated in language model pre-training.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 50. 2021-too-much-common-shifting-embeddings-transformer-language-models.pdf

**Title**

Too Much in Common: Shifting of Embeddings in Transformer Language Models and its Implications

**Abstract**

and Viswanath, 2018). To address the issues, postprocessing methods (Mu and Viswanath, 2018), The success of language models based on the and regularization terms have been proposed (Gao Transformer architecture appears to be inconet al., 2019; Wang et al., 2019c, 2020). However, sistent with observed anisotropic properties of representations learned by such models. We the mechanism that leads to undesirable properresolve this by showing, contrary to previous ties remains unclear. Without understanding the studies, that the representations do not occupy mechanism, it is going to be difficult to address the a narrow cone, but rather drift in common di- fundamental issue properly. rections. At any training step, all of the em- The deficiencies are most pronounced in the repbeddings except for the ground-truth target em- resentations of rare words, as we will show in bedding are updated with gradient in the same Section 4. Performance of pretrained language direction. Compounded over the training set, the embeddings drift and share common com- models is inconsistent and tends to decrease when ponents, manifested in their shape in all the input contains rare words (Schick and Schütze, models we have empirically tested. Our ex- 2020b,a). Schick and Schütze (2020a) observe periments show that isotropy can be restored that replacing a portion of words in the MNLI using a simple transformation.1 (Williams et al., 2018) entailment data set with less frequent synonyms leads to decrease in per-

**Conclusion**

We find that the embeddings learned by GPT-2, BERT, and RoBERTa do not degenerate into a narrow cone, as has been suggested in the past, but instead drift in one shared direction. We recognize that target words produce gradients in the same direction for all the non-target words at each training step. Combined with the unbalanced distribution of word frequencies, any two words' embeddings will be repeatedly updated with gradients of the same direction. As such updates accumulate, the embeddings drift and share common components. Our experiments show that simply centering the embeddings restores a nearly perfectly isotropic distribution of tested models' embeddings and simultaneously improves embeddings' ability to reflect semantic relations. This understanding of the learning process dynamics opens exciting avenues for future work, such as improving the most affected embeddings of rare words and formulation of more computationally efficient training objectives.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 51. 2022-blip-bootstrapping-language-image-pre-training-unified-vision.pdf

**Title**

BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

**Abstract**

“blue sky bakery in Filt sunset park “ Vision-Language Pre-training (VLP) has ad- “chocolate cake vanced the performance for many vision-language with cream frosting Cap and chocolate Filt tasks. However, most existing pre-trained mod- sprinkles on top” els only excel in either understanding-based tasks or generation-based tasks. Furthermore, perfor- Figure 1. We use a Captioner (Cap) to generate synthetic captions mance improvement has been largely achieved for web images, and a Filter (Filt) to remove noisy captions. by scaling up the dataset with noisy image-text pairs collected from the web, which is a subop- collected from the web. Despite the performance gain obtimal source of supervision. In this paper, we tained by scaling up the dataset, our paper shows that the propose BLIP, a new VLP framework which trans- noisy web text is suboptimal for vision-language learning. fers flexibly to both vision-language understand- To this end, we propose BLIP: Bootstrapping Languageing and generation tasks. BLIP effectively uti- Image Pre-training for unified vision-language understandlizes the noisy web data by bootstrapping the ing and generation. BLIP is a new VLP framework which captions, where a captioner generates synthetic enables a wider range of downstream tasks than existing captions and a filter removes the noisy ones. We methods. It introduces two contributions from the model achieve state-of-the-art results on a wide range of and data perspective, respectively: vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (a) Multimodal mixture of Encoder-Decoder (MED): a new (+2.8% in CIDEr), and VQA (+1.6% in VQA model architecture for effective multi-task pre-training and score). BLIP also demonstrates strong general- flexible transfer learning. An MED can operate either as ization ability when directly transferred to video- a unimodal encoder, or an image-grounded text encoder, language tasks in a zero-shot manner. Code, mod- or an image-grounded text decoder. The model is jointly els, and datasets are released. pre-trained with three vision-language objectives: imagetext contrastive learning, image-text matching, and imageconditioned language modeling.

**Conclusion**

We propose BLIP, a new VLP framework with state-of-the-art performance on a wide range of downstream vision-language tasks, including understanding-based and generation-based tasks. BLIP pre-trains a multimodal mixture of encoder-decoder model using a dataset bootstrapped from large-scale noisy image-text pairs by injecting diverse synthetic captions and removing noisy captions. Our bootstrapped dataset are released to facilitate future vision-language research. There are a few potential directions that can further enhance the performance of BLIP: (1) Multiple rounds of dataset bootstrapping; (2) Generate multiple synthetic captions per image to further enlarge the pre-training corpus; (3) Model ensemble by training multiple different captioners and filters and combining their forces in CapFilt.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 52. 2022-geometry-multilingual-language-model-representations.pdf

**Title**

The Geometry of Multilingual Language Model Representations Tyler A. Chang1,2 , Zhuowen Tu1 , Benjamin K. Bergen1

**Abstract**

We assess how multilingual language models maintain a shared multilingual representation space while still encoding language-sensitive arXiv:2205.10964v2 [cs.CL] 21 Oct 2022

information in each language. Using XLM-R as a case study, we show that languages occupy similar linear subspaces after mean-centering, evaluated based on causal effects on language modeling performance and direct comparisons between subspaces for 88 languages. The subspace means differ along language-sensitive axes that are relatively stable throughout middle layers, and these axes encode information onto a linear subspace where two axes are languagesuch as token vocabularies. Shifting represenneutral (horizontal axes), and one axis is languagetations by language means is sufficient to insensitive (vertical axis). Projecting from the side visualduce token predictions in different languages. izes the language-sensitive axis (top right). Projecting However, we also identify stable languagefrom the top down visualizes the language-neutral axes neutral axes that encode information such as encoding token position information, forming a nearly token positions and part-of-speech. We visuperfect torus in the representation space (bottom right). alize representations projected onto languagesensitive and language-neutral axes, identifying language family and part-of-speech clus- many of these assumptions have not been examined ters, along with spirals, toruses, and curves rep- in detail. For example, the models have been shown resenting token position information. These to retain language-sensitive information such as results demonstrate that multilingual language models encode information along orthogonal linguistic typological features (language-sensitive language-sensitive and language-neutral axes, representations; Choenni and Shutova, 2020; Liang allowing the models to extract a variety of fea- et al., 2021; Rama et al., 2020) despite also extures for downstream tasks and cross-lingual hibiting cross-lingual alignment of representations transfer learning. (language-neutral representations; Conneau et al., 2020b; Libovický et al., 2020; Pires et al., 2019).

**Conclusion**

In this work, we identified language subspaces and individual language-sensitive and language-neutral axes in the multilingual language model XLM-R. We assessed these subspaces and axes using a variety of methodologies, including causal effects on language modeling predictions, direct comparisons between subspaces, and low-dimensional visualizations. Our results suggest that multilingual language models encode features by projecting representations onto orthogonal axes in the representation space, enabling the efficient and simultaneous encoding of a wide variety of signals for downstream tasks and multilingual learning.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 53. 2022-hyperbolic-contrastive-learning-visual-representations-beyond-objects.pdf

**Title**

Hyperbolic Contrastive Learning for Visual Representations beyond Objects Songwei Ge∗1 , Shlok Mishra∗1 , Simon Kornblith2 , Chun-Liang Li2 , David Jacobs1,3

**Abstract**

Although self-/un-supervised methods have led to rapid progress in visual representation learning, these methods generally treat objects and scenes using the same lens. In this paper, we focus on learning representations for objects and scenes that preserve the structure among them. Motivated by the observation that visually similar objects are close in the representation space, we argue that the scenes and objects should instead follow a hierarchical structure

**Conclusion**

Self-Supervised Learning on Scenes. Self-Supervised Learning (SSL) has made great strides in closing the perfor- We present HCL, a contrastive learning framework that mance with supervised methods [13, 14, 24] when pretrained learns visual representation for both objects and scenes in on the object-centric datasets like ImageNet. However, re- the same representation space. The major novelty of our cent work has shown that SSL is limited on multi-object method is a hyperbolic contrastive objective built on an datasets like COCO [48, 59, 69] and OpenImages [38]. Sev- object-centric scene hierarchy. We show the effectiveness eral papers have tried to address this issue by proposing of HCL on several benchmarks including image classifidifferent techniques. Dense-CL [69] operates on pre-average cation, object detection, and semantic segmentation. We pool features and uses dense features on pixel level to show also demonstrate useful properties of the representations unimproved performance on dense tasks such as semantic seg- der several zero-shot settings, from detecting out-of-context mentation. DetCon [31] uses unsupervised semantic seg- objects to quantifying the label uncertainty in the datasets

like ImageNet. More generally, we hope this paper will Model details of pre-training. For the optimizer setups encourage future work towards building a more holistic vi- and augmentation recipes, we follow the standard protocol sual representation space, and draw attention to the power of described in MoCo-v2 [14]. We find that a base learning rate non-Euclidean representation learning. of 0.3 works better when pre-training on COCO and OpenImage datasets as compared to 0.03. We adopt the linear learn7. Acknowledgements ing rate scaling receipt that lr = 0.3 × BatchSize/256 [26] and batch size of 128 by default on 4 NVIDIA p6000 gpus. Songwei Ge, Shlok Mishra, David Jacobs were supported To ensure fair comparison, we also pre-train the baselines in part by the National Science Foundation under grant no. with a learning rate of 0.3. We train our models on COCO IIS-1910132 and IIS-2213335. and the subset of OpenImage datasets for 200 epochs and full OpenImage dataset for 75 epochs. We also note that calA. Experiment setups culating hyperbolic loss itself takes nearly the same time as a normal contrastive loss. The only overhead in pre-training In this section, we provide additional details of our experis one additional forward pass to get scene representations. iments. In our setting, MoCo takes 0.616 sec/iter while HCL takes 0.757 sec/iter. For the hyperparameters of our hyperbolic Unsupervised object proposals. When pretraining on un- objective, we use r = 4.5, λ = 0.1, and ε = 1e−5 as our curated datasets, acquiring ground truth object bounding default setting. boxes using human annotations can be expensive. However, automatically generating unsupervised region proposals is B. Additional experimental results well-studied. We use Selective Search as the unsupervised proposal generation method. Following ORL [73] we first B.1. Robustness under Corruption. generate the proposals using selective search. Then we filter We calculate the mCE error as in Hendrycks et al. [32]. the proposals with 96 pixels as the minimal scale, maximum We compare our HCL model trained on OpenImages and IOU of 0.5 and aspect ratio between 1/3 to 3. For every im- lineval on ImageNet dataset with the baseline model withage we generate maximum of 100 proposals and randomly out using HCL loss. We see an improvement of 1.9 mCE select any image as the object image. over the baseline model, demonstrating that our HCL model learns more robust representations as compared to the vanilla OpenImages dataset. We use the full OpenImages dataset MoCo. which have bounding box annotations (∼ 1.9 million imB.2. Fine-grained class classification ages). We also use a subset proposed in [49]. This is a subset created from the OpenImages dataset where each image has at least 2 classes present and each class has at least 900 Method Cars [36] DTD [16] Food [5] instances. This subset is a balanced subset of OpenImages with an average of 12 object present in an image, making it HCL/Lhyp 31.92 68.46 58.66 a good proxy for real-world multi-object images. HCL 32.02 68.19 58.79

Object and Scene image augmentations. We find that small objects are always detrimental to performance. There- In Table 7 we show results on fine-grained classification fore, when sampling object bounding boxes, we drop bound- datasets. We can see that on fine-grained classification our ing boxes with size width × height ≤ 56 × 56. Further, model provides little performance improvement. This could when sampling objects for the Euclidean branch, if the size be due to the fact that all classes in these datasets have very of a bounding box width × height ≤ 256 × 256, we similar scene contexts, and hence the hyperbolic objective slightly expand it to either 256 × 256 or the maximal size does not help very much. allowed by the original image size. We also apply a small jittering to the width and height to include different con- B.3. More ImageNet Examples texts around the objects. Next, we apply random cropping and resizing with the same scale (0.2, 1.) as in MoCo [30]. When sampling objects for the hyperbolic branch, we do not apply jittering and random cropping, but only filter the small boxes and resize to ≤ 224 × 224. To crop the scene images, we sample another 1 to 5 bounding boxes and merge with the selected object bounding box.

Smallest norms (objects) Largest norms (scenes)

Smallest norms (objects) Largest norms (scenes)

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 54. 2022-ilharco-patching-clip.pdf

**Title**

Patching open-vocabulary models by interpolating weights Gabriel Ilharco∗ Mitchell Wortsman∗ Samir Yitzhak Gadre∗

**Abstract**

Open-vocabulary models like CLIP achieve high accuracy across many image classification tasks. However, there are still settings where their zero-shot performance is far from optimal. We study model patching, where the goal is to improve accuracy on specific tasks without degrading accuracy on tasks where performance is already adequate. Towards this goal, we introduce PAINT, a patching method that uses interpolations between the weights of a model before fine-tuning and the weights after fine-tuning on a task to be patched. On nine tasks where zeroshot CLIP performs poorly, PAINT increases accuracy by 15 to 60 percentage points while preserving accuracy on ImageNet within one percentage point of the zero-shot model. PAINT also allows a single model to be patched on multiple tasks and improves with model scale. Furthermore, we identify cases of broad transfer, where patching on one task increases accuracy on other tasks even when the tasks have disjoint classes. Finally, we investigate applications beyond common benchmarks such as counting or reducing the impact of typographic attacks on CLIP. Our findings demonstrate that it is possible to expand the set of tasks on which open-vocabulary models achieve high accuracy without re-training them from scratch.

**Conclusion**

In this work, we explore several techniques for patching open-vocabulary models with the goal of improving accuracy on new tasks without decreasing accuracy elsewhere. PAINT is effective in several scenarios, ranging from classifying digits to defending against typographic attacks. PAINT becomes more effective with scale, and can be applied on multiple tasks sequentially or simultaneously. Our findings demonstrate that in many circumstances it is possible to expand the set of tasks on which models achieve high accuracy, without introducing new parameters, without re-training them from scratch, and without catastrophic forgetting.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 55. 2022-mind-gap-understanding-modality-gap-multi-modal-contrastive.pdf

**Title**

Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning

**Abstract**

We present modality gap, an intriguing geometric phenomenon of the representation space of multi-modal models. Specifically, we show that different data modalities (e.g. images and texts) are embedded at arm’s length in their shared representation in multi-modal models such as CLIP. Our systematic analysis demonstrates that this gap is caused by a combination of model initialization and contrastive learning optimization. In model initialization, we show empirically and theoretically that the representation of a common deep neural network is restricted to a narrow cone. As a consequence, in a multi-modal model with two encoders, the representations of the two modalities are clearly apart when the model is initialized. During optimization, contrastive learning keeps the different modalities separated by a certain distance, which is influenced by the temperature parameter in the loss function. Our experiments further demonstrate that varying the modality gap distance has a significant impact in improving the model’s downstream zeroshot classification performance and fairness. Our code and data are available at https://modalitygap.readthedocs.io/

**Conclusion**

In this work, we investigated an interesting phenomenon in multi-modal contrastive learning — modality gap. We analyzed why the gap exists, i.e., the joint effect of model initialization and optimization, and why studying the gap is important, i.e., it can affect the downstream task performance and fairness. Our work raises several basic questions about representation learning, contrastive learning, and multi-modal contrastive representation learning. For contrastive learning, our embedding shifting, simulation, and fine-tuning experiments all show that the contrast loss landscape is heavily influenced by temperature. For multi-modal contrastive representational learning, we find that changing the modal gap can affect performance and fairness on downstream tasks. The main objective of our paper is to demonstrate the modality gap phenomenon and explain contraction mapping contribute to this.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 56. 2022-mteb-massive-text-embedding-benchmark.pdf

**Title**

MTEB: Massive Text Embedding Benchmark Niklas Muennighoff1 , Nouamane Tazi1 , Loïc Magne1 , Nils Reimers2 * Hugging Face 2 cohere.ai

**Abstract**

Gurevych, 2019) solely evaluate on STS and classification tasks, leaving open questions about the Text embeddings are commonly evaluated on transferability of the embedding models to search a small set of datasets from a single task not covering their possible applications to other or clustering tasks. STS is known to poorly corretasks. It is unclear whether state-of-the-art em- late with other real-world use cases (Neelakantan beddings on semantic textual similarity (STS) et al., 2022; Wang et al., 2021). Further, evaluating can be equally well applied to other tasks like embedding methods on many tasks requires impleclustering or reranking. This makes progress in menting multiple evaluation pipelines. Implementhe field difficult to track, as various models are tation details like pre-processing or hyperparamconstantly being proposed without proper evaleters may influence the results making it unclear uation. To solve this problem, we introduce the Massive Text Embedding Benchmark (MTEB). whether performance improvements simply come MTEB spans 8 embedding tasks covering a to- from a favorable evaluation pipeline. This leads to tal of 58 datasets and 112 languages. Through the “blind” application of these models to new use the benchmarking of 33 models on MTEB, we cases in industry or requires incremental work to establish the most comprehensive benchmark reevaluate them on different tasks. of text embeddings to date. We find that no The Massive Text Embedding Benchmark particular text embedding method dominates (MTEB) aims to provide clarity on how models across all tasks. This suggests that the field has yet to converge on a universal text embedding perform on a variety of embedding tasks and thus method and scale it up sufficiently to provide serves as the gateway to finding universal text emstate-of-the-art results on all embedding tasks. beddings applicable to a variety of tasks. MTEB MTEB comes with open-source code and a pub- consists of 58 datasets covering 112 languages lic leaderboard at https://github.com/ from 8 embedding tasks: Bitext mining, classiembeddings-benchmark/mteb. fication, clustering, pair classification, reranking,

**Conclusion**

In this work, we presented the Massive Text Embedding Benchmark (MTEB). Consisting of 8 text embedding tasks with up to 15 datasets each and covering 112 languages, MTEB aims to provide reliable embedding performance estimates. By open-sourcing MTEB alongside a leaderboard, we provide a foundation for further pushing the state-of-the-art of available text embeddings. Through the course of close to 5,000 experiments on over 30 different models, we have set up solid baselines for future research to build on. We found model performance on different tasks to vary strongly with no model claiming state-of-the-art on all tasks. Our studies on scaling behavior, model efficiency and multilinguality revealed various intricacies of models that should ease the decision-making process for future research or industry applications of text embeddings.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 57. 2022-patching-open-vocabulary-models-by-interpolating-weights.pdf

**Title**

Patching open-vocabulary models by interpolating weights Gabriel Ilharco∗ Mitchell Wortsman∗ Samir Yitzhak Gadre∗

**Abstract**

Open-vocabulary models like CLIP achieve high accuracy across many image classification tasks. However, there are still settings where their zero-shot performance is far from optimal. We study model patching, where the goal is to improve accuracy on specific tasks without degrading accuracy on tasks where performance is already adequate. Towards this goal, we introduce PAINT, a patching method that uses interpolations between the weights of a model before fine-tuning and the weights after fine-tuning on a task to be patched. On nine tasks where zeroshot CLIP performs poorly, PAINT increases accuracy by 15 to 60 percentage points while preserving accuracy on ImageNet within one percentage point of the zero-shot model. PAINT also allows a single model to be patched on multiple tasks and improves with model scale. Furthermore, we identify cases of broad transfer, where patching on one task increases accuracy on other tasks even when the tasks have disjoint classes. Finally, we investigate applications beyond common benchmarks such as counting or reducing the impact of typographic attacks on CLIP. Our findings demonstrate that it is possible to expand the set of tasks on which open-vocabulary models achieve high accuracy without re-training them from scratch.

**Conclusion**

In this work, we explore several techniques for patching open-vocabulary models with the goal of improving accuracy on new tasks without decreasing accuracy elsewhere. PAINT is effective in several scenarios, ranging from classifying digits to defending against typographic attacks. PAINT becomes more effective with scale, and can be applied on multiple tasks sequentially or simultaneously. Our findings demonstrate that in many circumstances it is possible to expand the set of tasks on which models achieve high accuracy, without introducing new parameters, without re-training them from scratch, and without catastrophic forgetting.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 58. 2022-rudman-isoscore.pdf

**Title**

IsoScore: Measuring the Uniformity of Embedding Space Utilization William Rudman† , Nate Gillman‡ , Taylor Rayne∗ , Carsten Eickhoff†

**Abstract**

all dimensions when embedded into three dimenThe recent success of distributed word repre- sions. sentations has led to an increased interest in analyzing the properties of their spatial distriarXiv:2108.07344v2 [cs.CL] 18 Apr 2022

bution. Several studies have suggested that contextualized word embedding models do not isotropically project tokens into vector space. However, current methods designed to measure isotropy, such as average random cosine similarity and the partition score, have not Figure 1: From left to right, a line, disk, and ball embeen thoroughly analyzed and are not appro- bedded in 3D space. priate for measuring isotropy. We propose IsoScore: a novel tool that quantifies the de- A distribution is isotropic when variance is unigree to which a point cloud uniformly utilizes formly distributed across all dimensions. Namely, the ambient vector space. Using rigorously designed tests, we demonstrate that IsoScore is a distribution is fully isotropic when the covariance the only tool available in the literature that ac- matrix is proportional to the identity matrix. Sevcurately measures how uniformly distributed eral authors suggest that isotropy correlates with variance is across dimensions in vector space. improved performance of embedding models (Biś Additionally, we use IsoScore to challenge a et al., 2021; Wang et al., 2019; Coenen et al., 2019a; number of recent conclusions in the NLP liter- Gong et al., 2018; Hasan and Curry, 2017; Heature that have been derived using brittle metwitt and Manning, 2019; Liang et al., 2021; Zhou rics of isotropy. We caution future studies from using existing tools to measure isotropy et al., 2019, 2021). However, current methods of in contextualized embedding space as result- measuring the spatial utilization of contextualized ing conclusions will be misleading or alto- embedding models do not truly measure isotropy. gether inaccurate. The most commonly used methods for measuring spatial distribution in embedding spaces include av-

**Conclusion**

Several studies have attempted to study isotropy in contextualized embedding models. Using mathematically rigorous tests, we demonstrate that current methods do not accurately measure isotropy. This paper presents IsoScore: a novel method for measuring isotropy that corrects the current misunderstandings in the literature. IsoScore is the only tool that is mean agnostic, robust to scalar changes to the covariance matrix and rotation invariant. Furthermore, IsoScore scales linearly with the number dimensions used and is stable when distributions contain highly isotropic subspaces. Future studies should avoid using existing methods to measure isotropy as resulting conclusions will be misleading or altogether inaccurate.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 59. 2022-when-why-vision-language-models-behave-like-bags.pdf

**Title**

WHEN AND WHY VISION-LANGUAGE MODELSBE-HAVE LIKE BAGS-O F-WORDS , AND WHAT TOD OABOUTIT ? Mert Yuksekgonul, Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, James Zou

**Abstract**

Despite the use of large vision and language models (VLMs) in many downstream applications, it is unclear how well they encode the compositional relationships between objects and attributes. Here, we create the Attribution, Relation, and Order (ARO) benchmark to systematically evaluate the ability of VLMs to understand different types of relationships, attributes, and order information. ARO consists of Visual Genome Attribution, to test the understanding of objects’ properties; Visual Genome Relation, to test for relational understanding; and COCO-Order & Flickr30k-Order, to test for order sensitivity in VLMs. ARO is orders of magnitude larger than previous benchmarks of compositionality, with more than 50,000 test cases. We present the settings in which state-of-the-art VLMs behave like bagsof-words—i.e. when they have poor relational understanding, can blunder when linking objects to their attributes, and demonstrate a severe lack of order sensitivity. VLMs are predominantly trained and evaluated on large scale datasets with rich compositional structure in the images and captions. Yet, training on these datasets has not been enough to address the lack of compositional understanding, and evaluating on these datasets has failed to surface this deficiency. To understand why these limitations emerge and are not represented in the standard tests, we zoom into the training and evaluation procedures. We demonstrate that it is possible to perform well on image-text retrieval over existing datasets without using the composition and order information. This further motivates the value of using ARO to benchmark VLMs. Given that contrastive pretraining optimizes for retrieval on large datasets with similar shortcuts, we hypothesize that this can explain why the models do not need to learn to represent compositional information. This finding suggests a natural solution: composition-aware hard negative mining. We show that a simple-to-implement modification of contrastive learning significantly improves the performance on tasks requiring an understanding of order and compositionality.

**Conclusion**

In this work, we evaluate the ability of VLMs to encode composition and order structure, introducing large-scale test beds to generate fine-grained and statistically strong insights. We show that models struggle with relation, attribution, and order understanding, and our datasets revealed various limitations of models. We show that models can achieve high performance on the task of crossmodal retrieval without needing to learn order and composition information. Given that contrastive pretraining optimizes models for the task of retrieval, we argue that this can explain why VLMs need not learn to encode order and compositional cues. Using these insights, we presented a simple modification to the training procedure, namely composition-aware hard negative mining. Through several evaluations, we demonstrate that by generating composition-aware hard negatives during model training, the compositional and order understanding of VLMs can be improved. Our work demonstrates the importance of the interaction between the pretraining objective and large datasets VLMs are trained on. In this work, we focused on finetuning of VLMs for demonstrating the use of the composition-aware negative mining. For future work, we are interested in further exploring composition-aware contrastive pretraining of VLMs. Given that VLMs are trained with large datasets with rich text corpora, the limited language understanding of these models are intriguing. While here we specifically focused on contrastive learning, in light of our findings, studying the interaction between different pretraining objectives and compositional understanding is an emerging future avenue. Our results further highlight the importance of rich evaluations of VLMs. We hope future VLMs will release results on these fine-grained evaluations in addition to standard tasks, and more fine-grained evaluations will be developed. Focused evaluation of state of the art models illuminates the strengths and deficiencies of these models, and is key to understanding in which contexts and for which goals these models can be used.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 60. 2022-winoground-probing-vision-language-models-visio-linguistic-compositionality.pdf

**Title**

Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality Tristan Thrush¶ *, Ryan Jiang‡ , Max Bartolo§ , Amanpreet Singh¶ , Adina Williams† , Douwe Kiela¶ , Candace Ross† *

**Abstract**

We present a novel task and dataset for evaluating the ability of vision and language models to conduct visio-linguistic compositional reasoning, which we call Winoground. Given two images and two captions, the goal is to match them correctly—but crucially, both captions contain a completely identical set of words, only in a dif- (a) some plants (b) a lightbulb surrounding some plants ferent order. The dataset was carefully hand-curated by ex- surrounding a lightbulb pert annotators and is labeled with a rich set of fine-grained tags to assist in analyzing model performance. We probe a Figure 1. An example from Winoground. The two sentences condiverse range of state-of-the-art vision and language mod- tain the same words but in a different order. The task of underels and find that, surprisingly, none of them do much better standing which image and caption match is trivial for humans but than chance. Evidently, these models are not as skilled at much harder for vision and language models. Every model that we visio-linguistic compositional reasoning as we might have tested (UNITER, ViLLA, VinVL, VisualBERT, ViLT, LXMERT, hoped. We perform an extensive analysis to obtain insights ViLBERT, UniT, FLAVA, CLIP, VSE++, and VSRN) fails to corinto how future work might try to mitigate these models’ rectly pair the images and captions, except the large checkpoint of shortcomings. We aim for Winoground to serve as a useful ViLLA by a very thin margin (0.00013 confidence). evaluation set for advancing the state of the art and driving further progress in the field. The dataset is available at https://huggingface.co/datasets/facebook/winoground. that transformers are often remarkably insensitive to word order [70]. Understanding the relationship between text in captions and corresponding visual content is a fundamental

**Conclusion**

We introduced a novel task and dataset, Winoground, aimed at measuring visio-linguistic compositional reasoning in state of the art vision and language models. We demonstrate that models fall short, in most cases performing no better than chance. Our findings highlight that there is more work to be done. Particularly, the field could investigate possible strengths of single-stream models, the compilation of more pretraining data, improving image-encoding capabilities, and pretraining objectives that emphasize similar but wrong images. We hope that our task and dataset will help guide research in this important direction.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 61. 2024-anisotropy-is-not-inherent-transformers.pdf

**Title**

Anisotropy is Not Inherent to Transformers Anemily Machina and Robert E. Mercer

**Abstract**

anisotropy. While no formal proof has been presented, due to the lack of any counterexamples, Isotropy is the property that embeddings are anisotropy is often taken as assumed for any Transuniformly distributed around the origin. Pre- former architecture. vious work has shown that Transformer em- We identify the most globally isotropic modbedding spaces are anisotropic, which is called the representation degradation problem. This els to date, the Pythia models with at least 410M degradation has been assumed to be inherent parameters (Biderman et al., 2023), a strong counto the standard language modeling tasks and to terexample to the assumption of anisotropy. These apply to all Transformer models regardless of models are trained using cross-entropy loss, ustheir architecture. In this work we identify a ing autoregressive language modeling, and with set of Transformer models with isotropic em- a final Layer Norm. Pythia model’s most unique bedding spaces, the large Pythia models. We architecture feature is their untied embedding and examine the isotropy of Pythia models and exunembedding matrices. Pythia models have 143 plore how isotropy and anisotropy develop as a model is trained. We find that anisotropic evenly spaced checkpoints from training, allowing models do not develop as previously theorized, us to explore how isotropy changes during training. using our own analysis to show that the large We explore the isotropy of Pythia models usPythia models optimize their final Layer Norm ing cosine similarity (Ethayarajh, 2019; Cai et al., for isotropy, and provide reasoning why pre- 2021), a partition function (Arora et al., 2016), vious theoretical justifications for anisotropy and our own analysis on the final Layer Norm of were insufficient. The identification of a set each model based on the theoretical work of Gao of isotropic Transformer models calls previous assumptions into question, provides a set of et al. (2019). Using multiple metrics allows us to models to contrast existing analysis, and should present a more confident conclusion when all of lead to deeper insight into isotropy. our isotropy measures agree. Contrary to previous work, which use token frequencies in the 1000s, we

**Conclusion**

We have found strong evidence that the anisotropy of Transformer models can not be assumed. We show that large Pythia models are isotropic across all large model sizes using numerous metrics. We suspect having untied embedding and unembedding matrices leads to higher isotropy, and show that, contrary to previous assumptions, Pythia models in fact optimize the final Layer Norm operation for isotropy. We have also explored how isotropy changes during training across different model scales. This work, providing a set of contrasting points, is a good first step into a deeper understanding of isotropy and its impacts.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 62. 2024-hyperbolic-fine-tuning-large-language-models.pdf

**Title**

Hyperbolic Fine-Tuning for Large Language Models

**Abstract**

Large language models (LLMs) have demonstrated remarkable performance across various tasks. However, it remains an open question whether the default Euclidean space is the most suitable choice for LLMs. In this study, we investigate the geometric characteristics of LLMs, focusing specifically on tokens and their embeddings. Our findings reveal that token frequency follows a power-law distribution, where high-frequency tokens (e.g., “the,” “that”) constitute the minority, while low-frequency tokens (e.g., “apple,” “dog”) constitute the majority. Furthermore, high-frequency tokens cluster near the origin, whereas low-frequency tokens are positioned farther away in the embedding space. Additionally, token embeddings exhibit hyperbolic characteristics, indicating a latent tree-like structure within the embedding space. Motivated by these observations, we propose HypLoRA, an efficient fine-tuning approach that operates in hyperbolic space to exploit these underlying hierarchical structures better. HypLoRA performs low-rank adaptation directly in hyperbolic space, thereby preserving hyperbolic modeling capabilities throughout the fine-tuning process. Extensive experiments across various base models and reasoning benchmarks, specifically arithmetic and commonsense reasoning tasks, demonstrate that HypLoRA substantially improves LLM performance.

**Conclusion**

In this work, we investigated the non-Euclidean geometric properties inherent in LLMs, confirming their strong hyperbolic characteristics, which suggest underlying hierarchical structures. Building on these insights, we introduced HypLoRA, a hyperbolic low-rank adaptation technique. HypLoRA performs fine-tuning directly on the hyperbolic manifold. Extensive experiments show that HypLoRA significantly improves LLM performance on arithmetic reasoning and commonsense tasks. By leveraging the hyperbolic structure of the data, HypLoRA enhances the model’s ability to capture and utilize intricate relationships, leading to better reasoning capabilities. Broader Impact. Enhancing reasoning-oriented LLMs can help education, scientific assistance, and safer decision-support systems, but the same improvements may also accelerate misuse (e.g., automating complex disinformation or amplifying biased advice) and increase energy consumption due to added hyperbolic projections. We therefore advocate releasing checkpoints and code with usage guidelines (as in our public repo), tracking compute budgets when scaling HypLoRA further.

### 63. 2024-mitigate-gap-investigating-approaches-improving-cross-modal-alignment.pdf

**Title**

Mitigate the Gap: Investigating Approaches for Improving Cross-Modal Alignment in CLIP Sedigheh Eslami Gerard de Melo

**Abstract**

Contrastive Language–Image Pre-training (CLIP) has manifested remarkable improvements in zero-shot classification and cross-modal vision-language tasks. Yet, from a geometrical point of view, the CLIP embedding space has been found to have a pronounced modality gap. This gap renders the embedding space overly sparse and disconnected, with different modalities being densely distributed in distinct subregions of the hypersphere. In this work, we aim at answering three main questions: 1. Does sharing the parameter space between the multi-modal encoders reduce the modality gap? 2. Can the gap be mitigated by pushing apart the uni-modal embeddings via intra-modality separation? 3. How do these gap reduction approaches affect the downstream performance? We design AlignCLIP, in order to answer these questions and through extensive experiments, we show that AlignCLIP achieves noticeable enhancements in the cross-modal alignment of the embeddings, and thereby, reduces the modality gap, while improving the performance across several zero-shot and fine-tuning downstream evaluations. The source code for reproducing our experiments is available at https://github.com/sarahESL/AlignCLIP.

**Conclusion**

This work investigates the potential of reducing the modality gap in CLIP by sharing the learnable parameter space of the vision and language encoders as well as enforcing a contrastive intra-modality separation objective. We further examine the effects of modality gap reduction by the aforementioned refinements in the performance of downstream tasks. Through extensive experiments, we show that SharedCLIP and AlignCLIP improve various zero-shot as well as fine-tuning downstream applications when compared to CLIP, while substantially improving the cross-modal alignment, and therefore, reducing the gap. Our work shows that it is possible to mitigate the modality gap in CLIP via parameter sharing and intra-modality separation without losing downstream performance.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 64. 2024-platonic-representation-hypothesis.pdf

**Title**

The Platonic Representation Hypothesis

**Abstract**

The Platonic Representation Hypothesis We argue that representations in AI models, particularly deep networks, are converging. First, we Neural networks, trained with different objectives arXiv:2405.07987v5 [cs.LG] 25 Jul 2024

survey many examples of convergence in the lit- on different data and modalities, are converging to a erature: over time and across multiple domains, shared statistical model of reality in their representathe ways by which different neural networks rep- tion spaces. resent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato’s concept of an ideal reality. We term such a representation the platonic representation and discuss several possible selective pressures toward it. Finally, we discuss the implications of these trends, their limitations, and counterexamples to our analysis. Project Page: phillipi.github.io/prh Code: github.com/minyoungg/platonic-rep

**Conclusion**

We argue that representations in AI models, particularly deep networks, are converging toward a shared statistical model of reality. We demonstrate this convergence across model architectures, training objectives, and data modalities — as vision and language models get larger, they measure distances between datapoints in more similar ways. We hypothesize that this convergence is driven by task generality, model capacity, and simplicity bias, all of which push models toward a platonic representation of reality. We discuss implications including that scaling is sufficient (if not efficient) for convergence, that training data can be shared across modalities, and that convergence may reduce hallucination and bias in large models.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 65. 2024-steck-cosine-similarity.pdf

**Title**

Is Cosine-Similarity of Embeddings Really About Similarity? Harald Steck Chaitanya Ekanadham

**Abstract**

Cosine-similarity is the cosine of the angle between two vectors, or equivalently the dot product between their normalizations. A popular application is to quantify semantic similarity between high-dimensional objects by applying cosine-similarity to a learned low-dimensional feature embedding. This can work better but sometimes also worse than the unnormalized dot-product between embedded vectors in practice. To gain insight into this empirical observation, we study embeddings derived from regularized linear models, where closed-form solutions facilitate analytical insights. We derive analytically how cosine-similarity can yield arbitrary and therefore meaningless ‘similarities.’ For some linear models the similarities are not even unique, while for others they are implicitly controlled by the regularization. We discuss implications beyond linear models: a combination of different regularizations are employed when learning deep models; these have implicit and unintended effects when taking cosinesimilarities of the resulting embeddings, rendering results opaque and possibly arbitrary. Based on these insights, we caution against blindly using cosine-similarity and outline alternatives.

**Conclusion**

It is common practice to use cosine-similarity between learned user and/or item embeddings as a measure of semantic similarity between these entities. We study cosine similarities in the context of linear matrix factorization models, which allow for analytical derivations, and show that cosine similarities are heavily dependent on the method and regularization technique, and in some cases can be rendered even meaningless. Our analytical derivations are complemented experimentally by qualitatively examining the output of these models applied simulated data where we have ground truth item-item similarity. Based on these insights, we caution against blindly using cosine-similarity, and proposed a couple of approaches to mitigate this issue. While this short paper is limited to linear models that allow for insights based on analytical derivations, we expect cosine-similarity of the learned embeddings in deep models to be plagued by similar problems, if not larger ones, as a combination of various regularization methods is typically applied there, and different layers in the model may be subject to different regularization—which implicitly determines a particular scaling (analogous to matrix D above) of the different latent dimensions in the learned embeddings in each layer of the deep model, and hence its effect

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 66. 2024-vision-language-models-create-cross-modal-task-representations.pdf

**Title**

Vision-Language Models Create Cross-Modal Task Representations

**Abstract**

Task

Autoregressive vision-language models (VLMs) Country-Capital Food-Color arXiv:2410.22330v2 [cs.CV] 7 May 2025

can handle many tasks within a single model, yet Text Map country to capital Match food to color

Modality Instruction the representations that enable this capability re- Text France : Paris, … Cherry : Red, … main opaque. We find that VLMs align concep- Examples

tually equivalent inputs into a shared task vector, Image : Paris, … : Red, … Examples which is invariant to modality (text, image) and format (examples, instruction), and may simplify VLM processing. We measure this alignment via cross-modal transfer–the ability of a task vector derived in one modality to trigger the correct generation in another–on a range of tasks and Latent Space of model architectures. Although the task vector is Task Representations highly compressed, we find that this single vector outperforms prompting the model with the Figure 1: VLMs map conceptually equivalent inputs into a full task information, unique to this cross-modal shared task representation. This representation is invariant case. Furthermore, we show that task vectors can to the specification, regardless of modality (image, text) and be transferred from a base language model to its format (examples, instruction). fine-tuned vision-language counterpart, and that they can be derived solely from instructions without the need for examples. Taken together, our representation. Consider the tasks shown in Figure 1, which findings shed light on how VLMs internally pro- can be equivalently expressed using instructions, text examcess task information, and how they map different ples, or image examples. One might argue that the model modalities into common semantic representations. is biased towards learning the same simple function that solves the task, for all specifications (Solomonoff, 1964; Valle-Perez et al., 2019; Lin et al., 2023; Huh et al., 2024). In this work, we provide evidence of such a shared task rep-

**Conclusion**

Despite the success of autoregressive VLMs, we lack a clear understanding of their hidden task representations. Our primary observation is that VLMs map inputs into a shared task representation space, regardless of whether the task is defined by text examples, image examples, or explicit instructions. We evaluate cross-modal transfer, where we observe that few-shot prompting can struggle with input regurgitation while patching induces the task more effectively. We show that task vectors can be transferred from a base LLM to a fine-tuned VLM, possibly indicating representational re-use of functions learned in language. We also show that task vectors can be defined with instructions, which improves the sample efficiency of example-based task vectors. We hope that our work will inspire further analysis of shared representation spaces and the internals of VLMs.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 67. 2024-wasserstein-wormhole-scalable-optimal-transport-distance-with-transformers.pdf

**Title**

Wasserstein Wormhole: Scalable Optimal Transport Distance with Transformers

**Abstract**

Optimal transport (OT) and the related Wasserstein metric (W) are powerful and ubiquitous tools for comparing distributions. However, computing pairwise Wasserstein distances rapidly becomes intractable as cohort size grows. An attractive alternative would be to find an embedding space in which pairwise Euclidean distances map to OT distances, akin to standard multidimensional scaling (MDS). We present Wasserstein Wormhole, a transformer-based autoencoder that embeds empirical distributions into a latent space wherein Euclidean distances approximate OT distances. Extending MDS theory, we show that our objective function implies a bound on the error incurred when embedding non-Euclidean distances. Empirically, distances between Wormhole embeddings closely match Wasserstein distances, enabling linear time computation of OT distances. Along with an encoder that maps distributions to embeddings, Wasserstein Wormhole includes a decoder that maps embeddings back to distributions, allowing for operations in the embedding space to generalize to OT spaces, such as Wasserstein barycenter estimation and OT interpolation.

*Abstract added by Claude*

**Conclusion**

We have introduced Wasserstein Wormhole, an approach for embedding point clouds such that OT distances are preserved and can be approximated efficiently. We applied our approach to eight different settings, ranging from 2D point clouds to massive spatial transcriptomics datasets with hundreds of genes. Across all settings, Wormhole embeddings recapitulated the Wasserstein distance, accurately encoded key aspects of the point clouds and outperformed competing approaches. Furthermore, Wormhole's decoder recovered solutions to variational Wasserstein problems such as barycenters and point cloud interpolations. Wormhole seamlessly extends to other OT metrics, such as GW, and learns from arbitrary orientations. By lending scalability and interpretability to OT approaches, Wasserstein Wormhole unlocks new avenues for data analysis in the fields of computational geometry and single-cell biology.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 68. 2025-cross-gap-exposing-intra-modal-misalignment-clip-via.pdf

**Title**

CROSS THE GAP : EXPOSING THE INTRA-MODAL MISALIGNMENT IN CLIP VIA MODALITY INVERSION Marco Mistretta1,∗ , Alberto Baldrati1,2,∗ , Lorenzo Agnolucci1,∗ Marco Bertini1 , Andrew D. Bagdanov1

**Abstract**

Pre-trained multi-modal Vision-Language Models like CLIP are widely used offthe-shelf for a variety of applications. In this paper, we show that the common practice of individually exploiting the text or image encoders of these powerful multi-modal models is highly suboptimal for intra-modal tasks like imageto-image retrieval. We argue that this is inherently due to the CLIP-style intermodal contrastive loss that does not enforce any intra-modal constraints, leading to what we call intra-modal misalignment. To demonstrate this, we leverage two optimization-based modality inversion techniques that map representations from their input modality to the complementary one without any need for auxiliary data or additional trained adapters. We empirically show that, in the intra-modal tasks of image-to-image and text-to-text retrieval, approaching these tasks inter-modally significantly improves performance with respect to intramodal baselines on more than fifteen datasets. Additionally, we demonstrate that approaching a native inter-modal task (e.g. zero-shot image classification) intra-modally decreases performance, further validating our findings. Finally, we show that incorporating an intra-modal term in the pre-training objective or narrowing the modality gap between the text and image feature embedding spaces helps reduce the intra-modal misalignment. The code is publicly available at: https://github.com/miccunifi/Cross-the-Gap.

**Conclusion**

In this work we show that relying on intra-modal similarities computed with off-the-shelf VLMs is suboptimal for intra-modal tasks like image-to-image and text-to-text retrieval. This stems from the inter-modal contrastive loss employed for pre-training these models that leads to a modality gap and intra-modal misalignment. We propose to transform intra-modal tasks to inter-modal ones via two single-feature level modality inversion techniques. We demonstrate that this strategy improves performance as it exploits the inter-modal alignment of VLMs. Finally, we show that employing an intra-modal loss component during VLM pre-training or reducing the modality gap alleviates the impact of intra-modal misalignment. Limitations. Our analyses demonstrate the significance of intra-modal misalignment when exploiting pre-trained CLIP models, but fall short of offering practical alternatives. The modality inversion techniques we propose are computationally expensive. They are based on iterative optimization of learnable input parameters (150 optimization steps for OTI and 1000 for OVI in our experiments). This limits their practical applicability and future work should concentrate on efficient methods to mitigate the intra-modal misalignment.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 69. 2025-exploring-relationship-between-features-calculated-from-contextual-embeddings.pdf

**Title**

Exploring the relationship between features calculated from contextual embeddings and EEG band power during sentence reading in Chinese

**Abstract**

Contextual embeddings — a core component of large language models (LLMs) that generate dynamic vector representations capturing words' semantic properties — have demonstrated structural similarities to brain activity patterns at the single-word level. This alignment supports the theoretical framework proposing vector-based neural coding for natural language processing in the brain, where linguistic units may be represented as context-sensitive vectors analogous to LLM-derived embeddings. Building on this framework, we hypothesize that cumulative distance metrics between contextual embeddings of adjacent linguistic units (words/Chinese characters) in sentence contexts may quantitatively reflect neural activation intensity during reading comprehension. Using large-scale EEG datasets collected during reading tasks, we systematically investigated the relationship between these computationally derived distance features and frequency-specific band power measures associated with neural activity.

*Abstract added by Claude*

**Conclusion**

This study offers preliminary evidence that features from contextual embeddings (as well as some other NLP features), particularly those capturing semantic divergence and geometric complexity, correlate with gamma band power during sentence reading. Future research should expand on these findings by integrating multimodal neural data and advanced NLP metrics to refine our understanding of the brain's vector-based language encoding.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 70. 2025-fill-gap-quantifying-reducing-modality-gap-image-text.pdf

**Title**

Fill the Gap: Quantifying and Reducing the Modality Gap in Image-Text Representation Learning François Role1,* , Sébastien Meyer2 , and Victor Amblard3

**Abstract**

Vision-language models (VLMs) allow to embed texts and images in a shared representation space. However, it has been shown that these models are subject to a “modality gap phenomenon” meaning there exists a clear separation between the embeddings from one modality and another in the embedding space. While this misalignment is detrimental for downstream tasks such as multimodal retrieval, multimodal clustering or zero-shot classification, etc. no generic and practical methods have so far been proposed to assess it precisely and even reduce it. We therefore propose novel measures and effective techniques (spectral- and optimal transportbased methods) to achieve this goal. Extensive experiments conducted on several image-text datasets and models demonstrate their effectiveness and beneficial effects on downstream tasks. Our code is available at https://code.peren.gouv.fr/open-source/modeles-multimodaux/ article-modeles-multimodaux.git.

**Conclusion**

In this paper novel measures as well as spectral- and optimal-transport-based methods have been presented to address the "modality gap" phenomenon encountered in most vision-language models. The aim of these methods is to bring the representations of images (resp. texts) closer to those of texts (resp. images) that correspond to them. We have also proposed new, specialized measures to help precisely assess the level of the gap. By using these measures as part of extensive experiments, we were able to show the effectiveness of the proposed methods, especially the spectral-based ones. In

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 71. 2025-harnessing-universal-geometry-embeddings.pdf

**Title**

Harnessing the Universal Geometry of Embeddings

**Abstract**

arXiv:2505.12540v4 [cs.LG] 26 Jan 2026

We introduce the first method for translating text embeddings from one vector space to another without any paired data, encoders, or predefined sets of matches. Our unsupervised approach translates any embedding to and from a universal latent representation (i.e., a universal semantic structure conjectured by the Platonic Representation Hypothesis). Our translations achieve high cosine similarity across model pairs with different architectures, parameter counts, and training datasets. The ability to translate unknown embeddings into a different space while preserving their geometry has serious implications for security. An adversary with access to a database of only embedding vectors can extract sensitive information about underlying documents, sufficient for classification and attribute inference.

GTE [32]) are fundamentally incomparable. Right: given unpaired embedding samples from different models on different texts, our model learns a latent representation where they are closely aligned.

**Conclusion**

The Platonic Representation Hypothesis conjectures that the representation spaces of modern neural networks are converging. We assert the Strong Platonic Representation Hypothesis: the latent universal representation can be learned and harnessed to translate between representation spaces without any encoders or paired data. We demonstrated that our vec2vec method successfully translates embeddings generated from unseen documents by unseen encoders, and the translator is robust to out-of-distribution inputs. We showed that vec2vec translations preserve sufficient input semantics to enable attribute inference, and we extracted sensitive disease information from patient records and partial content from corporate emails with access only to document embeddings. Our findings provide compelling evidence for the Strong Platonic Representation Hypothesis for text-based models, with preliminary results on CLIP suggesting the universal geometry can be harnessed in other modalities too.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 72. 2025-huang-deciphering-cross-modal.pdf

**Title**

DECIPHERING CROSS-MODAL ALIGNMENT IN LARGE VISION-LANGUAGE MODELS WITH MODALITY INTE-GRATION RATE Qidong Huang1,2 Xiaoyi Dong2,3 Pan Zhang2 Yuhang Zang2 Yuhang Cao2

**Abstract**

We present the Modality Integration Rate (MIR), an effective, robust, and generalized metric to indicate the multi-modal pre-training quality of Large Vision Language Models (LVLMs). Large-scale pre-training plays a critical role in building capable LVLMs, while evaluating its training quality without the costly supervised fine-tuning stage is under-explored. Loss, perplexity, and in-context evaluation results are commonly used pre-training metrics for Large Language Models (LLMs), while we observed that these metrics are less indicative when aligning a well-trained LLM with a new modality. Due to the lack of proper metrics, the research of LVLMs in the critical pre-training stage is hindered greatly, including the training data choice, efficient module design, etc. In this paper, we propose evaluating the pre-training quality from the inter-modal distribution distance perspective and present MIR, the Modality Integration Rate, which is 1) Effective to represent the pre-training quality and show a positive relation with the benchmark performance after supervised fine-tuning. 2) Robust toward different training/evaluation data. 3) Generalize across training configurations and architecture choices. We conduct a series of pre-training experiments to explore the effectiveness of MIR and observe satisfactory results that MIR is indicative about training data selection, training strategy schedule, and model architecture design to get better pre-training results. We hope MIR could be a helpful metric for building capable LVLMs and inspire the following research about modality alignment in different areas. Our code is at: github.com/shikiw/Modality-Integration-Rate.

**Conclusion**

This paper introduces Modality Integration Rate (MIR), a novel and effective metric for evaluating cross-modal alignment during the pre-training of LVLMs. By capturing domain differences between vision and language features across all layers of the language model, MIR provides an effective and reliable measure of pre-training quality compared to traditional metrics like loss or perplexity. It demonstrates its good robustness, generalization ability, and the strong correlation with postSFT performance, offering valuable insights for optimizing architecture designs and training setup. Complementing MIR, we propose MoCa, a lightweight, learnable calibration module that enhances the alignment of vision and text tokens, ultimately driving better multi-modal comprehension.

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 73. 2025-jha-universal-geometry.pdf

**Title**

Harnessing the Universal Geometry of Embeddings

**Abstract**

arXiv:2505.12540v4 [cs.LG] 26 Jan 2026

We introduce the first method for translating text embeddings from one vector space to another without any paired data, encoders, or predefined sets of matches. Our unsupervised approach translates any embedding to and from a universal latent representation (i.e., a universal semantic structure conjectured by the Platonic Representation Hypothesis). Our translations achieve high cosine similarity across model pairs with different architectures, parameter counts, and training datasets. The ability to translate unknown embeddings into a different space while preserving their geometry has serious implications for security. An adversary with access to a database of only embedding vectors can extract sensitive information about underlying documents, sufficient for classification and attribute inference.

GTE [32]) are fundamentally incomparable. Right: given unpaired embedding samples from different models on different texts, our model learns a latent representation where they are closely aligned.

**Conclusion**

The Platonic Representation Hypothesis conjectures that the representation spaces of modern neural networks are converging. We assert the Strong Platonic Representation Hypothesis: the latent universal representation can be learned and harnessed to translate between representation spaces without any encoders or paired data. We demonstrated that our vec2vec method successfully translates embeddings generated from unseen documents by unseen encoders, and the translator is robust to out-of-distribution inputs. We showed that vec2vec translations preserve sufficient input semantics to enable attribute inference, and we extracted sensitive disease information from patient records and partial content from corporate emails with access only to document embeddings. Our findings provide compelling evidence for the Strong Platonic Representation Hypothesis for text-based models, with preliminary results on CLIP suggesting the universal geometry can be harnessed in other modalities too.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 74. 2025-kang-spectral-rsa.pdf

**Title**

Spectral Analysis of Representational Similarity with Limited Neurons

**Abstract**

Understanding representational similarity between neural recordings and computational models is essential for neuroscience, yet remains challenging to measure reliably due to the constraints on the number of neurons that can be recorded simultaneously. In this work, we apply tools from Random Matrix Theory to investigate how such limitations affect similarity measures, focusing on Centered Kernel Alignment (CKA) and Canonical Correlation Analysis (CCA). We propose an analytical framework for representational similarity analysis that relates measured similarities to the spectral properties of the underlying representations. We demonstrate that neural similarities are systematically underestimated under finite neuron sampling, mainly due to eigenvector delocalization. Moreover, for power-law population spectra, we show that the number of localized eigenvectors scales as the square root of the number of recorded neurons, providing a simple rule of thumb for practitioners. To overcome sampling bias, we introduce a denoising method to infer population-level similarity, enabling accurate analysis even with small neuron samples. Theoretical predictions are validated on synthetic and real datasets, offering practical strategies for interpreting neural data under finite sampling constraints.

**Conclusion**

We have presented an eigencomponent-based analysis of how sampling a finite number of neurons affects similarity measures, including CCA and CKA. By applying methods from Random Matrix Theory, we established that this limited sampling systematically underestimates similarity because of eigenvector delocalization in the sample Gram matrices. Our framework provides both forward and backward procedures: predicting how limited sampling distorts measurements, and inferring true population-level similarity from limited observations. We validated our theoretical predictions on synthetic and real neural datasets, demonstrating that inferred population similarity is consistently higher than naive sample-based estimates, offering practical strategies for interpreting neural data under finite sampling constraints.

*Conclusion added by Claude*

**Note**

Missing one or more sections.

### 75. 2025-liu-distance-to-distance.pdf

**Title**

Distance-to-Distance Ratio: A Similarity Measure for Sentences Based on Rate of Change in LLM Embeddings

**Abstract**

A measure of similarity between text embeddings can be considered adequate only if it adheres to the human perception of similarity between texts. In this paper, we introduce the distanceto-distance ratio (DDR), a novel measure of similarity between LLM sentence embeddings. Inspired by Lipschitz continuity, DDR measures the rate of change in similarity between the pre-context word embeddings and the similarity between post-context LLM embeddings, thus measuring the semantic influence of context. We evaluate the performance of DDR in experiments designed as a series of perturbations applied to sentences drawn from a sentence dataset. For each sentence, we generate variants by replacing one, two, or three words with either synonyms, which constitute semantically similar text, or randomly chosen words, which constitute semantically dissimilar text. We compare the performance of DDR with other prevailing similarity metrics and demonstrate that DDR consistently provides finer discrimination between semantically similar and dissimilar texts, even under minimal, controlled edits.

**Conclusion**

Our results show that DDR is a viable and practical method for measuring semantic (dis)similarity between text embeddings and outperforms common methods that rely on context embedding alone. One limitation of the current implementation is the requirement that sequences have the same length. To broaden the applicability of DDR, future work should generalize the distance computation to handle variable-length inputs. Such extensions will expand DDR’s theoretical reach to enable practical applications. For example, DDR’s sensitivity to small textual variations suggests potential uses in information retrieval (distinguishing near-duplicate queries) and evaluating model robustness to adversarial edits (detecting if small lexical edits flip the model’s response when it shouldn’t). Overall, DDR allows for an expanded range; that is, similarity scores occupy a broader interval and discrimination at finer resolution.

### 76. 2025-post-pre-training-modality-alignment-vision-language-foundation.pdf

**Title**

Post-pre-training for Modality Alignment in Vision-Language Foundation Models Shin’ya Yamaguchi* Dewei Feng Sekitoshi Kanai Kazuki Adachi Daiki Chijiwa

**Abstract**

Previous Pre-training Zero-shot Inference Approach w/ CLIP or Fine-tuning

Contrastive language image pre-training (CLIP) is an es- Our Pre-training Post-pre-training to Zero-shot Inference Approach w/ CLIP Align Modality Gap or Fine-tuning sential component of building modern vision-language foundation models. While CLIP demonstrates remarkable zeroshot performance on downstream tasks, the multi-modal gap in pre-trained CLIP models. We aim to address the modality feature spaces still suffer from a modality gap, which is gap and enhance the generalization performance of pre-trained a gap between image and text feature clusters and limits CLIP models through lightweight training. downstream task performance. Although existing works attempt to address the modality gap by modifying pre-training they are widely used as a foundation of many applications, or fine-tuning, they struggle with heavy training costs with including zero-shot classification [14, 42, 59], cross-modal large datasets or degradations of zero-shot performance. retrieval [16, 22], text-to-image generation [43, 47], and This paper presents CLIP-Refine, a post-pre-training method visual question answering [32, 33]. for CLIP models at a phase between pre-training and fineWhile CLIP achieves remarkable performance in broad tuning. CLIP-Refine aims to align the feature space with 1 domains and tasks, its image and text alignment is still epoch training on small image-text datasets without zeronot perfect. For example, CLIP models tend to encode shot performance degradations. To this end, we introduce images and texts into different clusters for each modality, two techniques: random feature alignment (RaFA) and hyand thus, there is a modality gap between images and text brid contrastive-distillation (HyCD). RaFA aligns the image features even after sufficiently training with the massive and text features to follow a shared prior distribution by mindatasets [30, 41, 70]. This modality gap suggests that CLIP imizing the distance to random reference vectors sampled has difficulty in precisely mapping images and text. In fact, from the prior. HyCD updates the model with hybrid soft Liang et al. [30] have shown that the modality gap largely labels generated by combining ground-truth image-text pair affects downstream task performance, especially in finelabels and outputs from the pre-trained CLIP model. This grained classification tasks, and Ray et al. [45] have demoncontributes to achieving both maintaining the past knowlstrated that CLIP models often fail to retrieve localized obedge and learning new knowledge to align features. Our jects and attributes in images from corresponding captions. extensive experiments with multiple classification and retrieval tasks show that CLIP-Refine succeeds in mitigating To address the modality gap in CLIP, existing literature the modality gap and improving the zero-shot performance1 . mainly focuses on refining the CLIP feature spaces in the pre-training or fine-tuning phases. For pre-training, one approach is multi-task learning of the contrastive objective and

**Conclusion**

This paper presented CLIP-Refine, a post-pre-training method for pre-trained CLIP models to align the modality gap between the image and text features. CLIP-Refine addresses the modality gap by penalizing the multi-modal features to follow a shared prior distribution by minimizing the distance to the random reference vectors sampled from the prior. To maintain the past knowledge in the CLIP models and promote the feature alignment simultaneously, CLIP-Refine also trains the model with knowledge distillation loss using hybrid soft labels composed of ground-truth image-text pair labels and outputs from the pre-trained CLIP model. Through extensive experiments, we show that CLIP-Refine can improve the zero-shot performance of the pre-trained CLIP by addressing the modality gap and enhancing uniformity. We believe that our work not only provides a practical method but also opens up a new research field where we refine the pre-trained CLIP models by post-pre-training with much smaller computational costs than that of pre-training.

*Conclusion added by Claude*

**Note**

Title extracted from page text because PDF metadata was unavailable. Missing one or more sections.

### 77. 2025-role-fill-the-gap.pdf

**Title**

Fill the Gap: Quantifying and Reducing the Modality Gap in Image-Text Representation Learning François Role1,* , Sébastien Meyer2 , and Victor Amblard3

**Abstract**

Vision-language models (VLMs) allow to embed texts and images in a shared representation space. However, it has been shown that these models are subject to a “modality gap phenomenon” meaning there exists a clear separation between the embeddings from one modality and another in the embedding space. While this misalignment is detrimental for downstream tasks such as multimodal retrieval, multimodal clustering or zero-shot classification, etc. no generic and practical methods have so far been proposed to assess it precisely and even reduce it. We therefore propose novel measures and effective techniques (spectral- and optimal transportbased methods) to achieve this goal. Extensive experiments conducted on several image-text datasets and models demonstrate their effectiveness and beneficial effects on downstream tasks. Our code is available at https://code.peren.gouv.fr/open-source/modeles-multimodaux/ article-modeles-multimodaux.git.

**Conclusion**

In this paper novel measures as well as spectral- and optimal-transport-based methods have been presented to address the "modality gap" phenomenon encountered in most vision-language models. The aim of these methods is to bring the representations of images (resp. texts) closer to those of texts (resp. images) that correspond to them. We have also proposed new, specialized measures to help precisely assess the level of the gap. By using these measures as part of extensive experiments, we were able to show the effectiveness of the proposed methods, especially the spectral-based ones. In

**Note**

Title extracted from page text because PDF metadata was unavailable.

### 78. 2025-semantic-structure-large-language-model-embeddings.pdf

**Title**

Semantic Structure in Large Language Model Embeddings

**Abstract**

Psychological research consistently finds that human ratings of words across diverse semantic scales can be reduced to a low-dimensional form with relatively little information loss. We find that the semantic associations encoded in the embedding matrices of large language models (LLMs) exhibit a similar structure. We show that the projections of words on semantic directions defined by antonym pairs (e.g. kind - cruel) correlate highly with human ratings, and further find that these projections effectively reduce to a 3-dimensional subspace within LLM embeddings, closely resembling the patterns derived from human survey responses. Moreover, we find that shifting tokens along one semantic direction causes off-target effects on geometrically aligned features proportional to their cosine similarity. These findings suggest that semantic features are entangled within LLMs similarly to how they are interconnected in human language, and a great deal of semantic information, despite its apparent complexity, is surprisingly low-dimensional. Furthermore, accounting for this semantic structure may prove essential for avoiding unintended consequences when steering features.

**Conclusion**

LLMs are notable for the high dimensionality of their representations, and their performance scales consistently as a power-law function of parameter counts over many orders of magnitude [34]. This phenomenon seems to imply that building an effective world model requires an enormous number of dimensions. However, prior psychological research suggests that many of the seemingly diverse axes of meaning that we use to communicate and understand the world are roughly represented as a linear combination of just three latent factors [4, 5]. Our findings suggest that, as with humans, the representation of semantic associations is relatively low-dimensional in LLM embeddings. This finding appears encouraging for technical AI safety efforts, because it suggests that many relevant semantic features (e.g. kind-cruel, safe-unsafe, us-them) may share a common low dimensional subspace, simplifying the tasks of identification, auditing, and control [3].

### 79. 2025-sevastjanova-layerflow.pdf

**Title**

LayerFlow

**Abstract**

Large language models (LLMs) represent words through contextual word embeddings encoding different language properties like semantics and syntax. Understanding these properties is crucial, especially for researchers investigating language model capabilities, employing embeddings for tasks related to text similarity, or evaluating the reasons behind token importance as measured through attribution methods. Applications for embedding exploration frequently involve dimensionality reduction techniques, which reduce high-dimensional vectors to two dimensions used as coordinates in a scatterplot. This data transformation step introduces uncertainty that can be propagated to the visual representation and influence users’ interpretation of the data. To communicate such uncertainties, we present LayerFlow – a visual analytics workspace that displays embeddings in an interlinked projection design and communicates the transformation, representation, and interpretation uncertainty. In particular, to hint at potential data distortions and uncertainties, the workspace includes several visual components, such as convex hulls showing 2D and HD clusters, data point pairwise distances, cluster summaries, and projection quality metrics. We show the usability of the presented workspace through replication and expert case studies that highlight the need to communicate uncertainty through multiple visual components and different data perspectives. CCS Concepts • Human-centered computing → Visual analytics; • Mathematics of computing → Dimensionality reduction;

**Conclusion**

warn the user of potential misrepresentation. Guidance in visual analytics systems [SJB*20] becomes more important and should In this paper, we present a workspace called LayerFlow that vibe used also to communicate visual uncertainties. sualizes word embedding vectors layer-wise and supports analysis in exploring their encoded linguistic properties. In this work, we Quality Metrics – The interpretation of the quality metric re- build on our previous work [SKB*21a] that introduced interlinked sults was mentioned as one of the most challenging aspects of the projections for embedding analysis, present a new flow-design that workspace. Although the experts mentioned that they are helpful supports the investigation of cluster changes between consecutive to assess which projections represent the HD data better than oth- layers, and integrate several visual components to communicate the ers, they would prefer to see direct impact of the different nearest uncertainty. In particular, we address the uncertainty that can occur neighbors for the metric values. Although the k-nearest neighbor within the data transformation, representation, and interpretation connections were judged useful, they do not explain the quality steps of the analysis. A demo is available under layerflow.ivia.ch. metric values. Since the FPR, FNR metrics are computed based on the minimum spanning tree of the LD space, a visual explanation Acknowledgments related to the spanning tree would ease their interpretation. This paper was funded by the Swiss National Science Foundation Scalability – The presented examples were limited to embedding (SNSF) within the project 10003068.

© 2025 The Author(s). Computer Graphics Forum published by Eurographics and John Wiley & Sons Ltd.

Rita Sevastjanova, Robin Gerling, Thilo Spinner, and Mennatallah El-Assady / LayerFlow 11 of 12

References [FWM*18] F ERNANDES, M ICHAEL, WALLS, L OGAN, M UNSON, S EAN, [Aup07] AUPETIT, M ICHAËL. “Visualizing distortions and recovering et al. “Uncertainty Displays Using Quantile Dotplots or CDFs Improve topology in continuous projection techniques”. Neurocomputing 70.7-9 Transit Decision-Making”. Proc. of the 2018 CHI Conf. on Human Fac(2007), 1304–1330. DOI: 10.1016/J.NEUCOM.2006.11.018 2– tors in Computing Systems. CHI ’18. New York, NY, USA: Associa4. tion for Computing Machinery, 2018, 1–12. ISBN: 9781450356206. DOI: 10.1145/3173574.3173718. URL: https://doi.org/10. [BBE*17] B OS, J OHAN, BASILE, VALERIO, E VANG, K ILIAN, et al. “The 1145/3173574.3173718 2. Groningen Meaning Bank”. Handbook of Linguistic Annotation. Ed. by I DE, NANCY and P USTEJOVSKY, JAMES. Dordrecht: Springer Nether- [HEF*22] H AGHIGHATKHAH, P., E L -A SSADY, M., F EKETE, J., et al. lands, 2017, 463–496. ISBN: 978-94-024-0881-2. DOI: 10 . 1007 / “Characterizing Uncertainty in the Visual Text Analysis Pipeline”. 978 - 94 - 024 - 0881 - 2 _ 18. URL: https : / / doi . org / 10 . 2022 IEEE 7th Workshop on Visualization for the Digital Humani1007/978-94-024-0881-2_18 7. ties (VIS4DH). Los Alamitos, CA, USA: IEEE Computer Society, Oct.

### 80. 2025-visualizing-llm-latent-space-geometry-through-dimensionality-reduction.pdf

**Title**

Visualizing LLM Latent Space Geometry Through Dimensionality Reduction

**Abstract**

Large language models (LLMs) achieve state-of-the-art results across many natural language tasks, but their internal mechanisms remain difficult to interpret. In this work, we extract, process, and visualize latent state geometries in Transformer-based language models through dimensionality reduction. We capture layerwise activations at multiple points within Transformer blocks and enable systematic analysis through Principal Component Analysis (PCA) and Uniform Manifold Approximation and Projection (UMAP). We demonstrate experiments on GPT-2 and LLaMa models, where we uncover interesting geometric patterns in latent space. Notably, we identify a clear separation between attention and MLP component outputs across intermediate layers, a pattern not documented in prior work to our knowledge. We also characterize the high norm of latent states at the initial sequence position and visualize the layerwise evolution of latent states. Additionally, we demonstrate the highdimensional helical structure of GPT-2’s positional embeddings and the sequence-wise geometric patterns in LLaMa. We make our code available at https://github.com/Vainateya/Feature_

**Conclusion**

We present a study on visualizing the internal representations of Transformer-based language models. Through systematic analysis of GPT-2 and LLaMa, we demonstrate how dimensionality reduction techniques can reveal geometric patterns that show how these models organize and process information. Our experiments highlight several notable phenomena. Most significantly, we identify a persistent geometric separation between attention and MLP component outputs (section 4.4), a pattern that appears consistent across the tested model architectures and has not been previously documented to our knowledge. We also noted the high norm of latent states at the initial sequence position (section 4.2), a phenomenon that extends beyond special tokens like <BOS> to many vocabulary tokens in LLaMa despite its use of relative position encodings. Additionally, we visualized the layerwise evolution of latent states (section 4.3) and the geometric effects of sequence position (section 4.5). Ultimately, we add to the growing body of interpretability research by motivating further work into analyzing feature geometry. Future work can help further our understanding of the dynamics of latent states within Transformer models across layers, models, and experimental conditions. By deepening our understanding of how these geometric structures emerge and behave, we move closer to principled, reliable interpretability methods capable of guiding the development of more transparent and understandable models.

### 81. 2026-decoding-geometry-alleviating-embedding-space-crowding-complex-reasoning.pdf

**Title**

Decoding in Geometry: Alleviating Embedding-Space Crowding for Complex Reasoning

**Abstract**

token distribution. It remains the prevailing method for Sampling-based decoding underlies complex rea- open-ended generation and reasoning (Chowdhery et al., soning in large language models (LLMs), where 2023; Guo et al., 2025). Prior work mainly falls into two arXiv:2601.22536v1 [cs.AI] 30 Jan 2026

decoding strategies critically shape model behav- categories: truncation-based sampling (e.g., top-p (Holtzior. Temperature- and truncation-based meth- man et al., 2019), top-k (Fan et al., 2018)) and temperatureods reshape the next-token distribution through based sampling (e.g., Temperature Scaling (Ackley et al., global probability reweighting or thresholding 1985), EDT (Zhang et al., 2024)). By modulating the cutto balance the quality-diversity tradeoff. How- off threshold or the temperature parameter, these methods ever, they operate solely on token probabilities, globally modify the token probability distribution through ignoring fine-grained relationships among tokens truncation, sharpening, or smoothing to better balance the in the embedding space. We uncover a novel quality-diversity tradeoff. phenomenon, embedding-space crowding, where In this work, we study decoding through a geometry-aware the next-token distribution concentrates its prob- view of the next-token distribution, and diagnose its effect ability mass on geometrically close tokens in on generation behavior. We uncover a novel and underthe embedding space. We quantify crowding explored phenomenon, which we term embedding-space at multiple granularities and find a statistical as- crowding. This phenomenon occurs when the next-token sociation with reasoning success in mathemati- distribution concentrates its probability mass in a narrow cal problem solving. Motivated by this finding, region of the embedding space. We formalize and quantify we propose CraEG, a plug-in sampling method embedding-space crowding at multiple granularities, and that mitigates crowding through geometry-guided analyze its relationship with reasoning outcomes. Specifireweighting. CraEG is training-free, single-pass, cally, we use mathematical reasoning as a controlled testbed, and compatible with standard sampling strategies. where the task is well-defined and correctness is automatExperiments on multiple models and benchmarks ically verifiable. Across the AIME benchmark with the demonstrate improved generation performance, Qwen model, our analysis shows that both sequence-level with gains in robustness and diversity metrics. and step-level crowding score are statistically associated with final answer correctness. These findings suggest a statistically significant association between embedding-space

**Conclusion**

We take a geometry-based view of LLM decoding and show that embedding-space crowding influences how probability mass concentrates among localized region. Leveraging this perspective, we quantify crowding as a diagnostic signal to analyze how decoding-time crowding is associated with success on complex reasoning. We then propose CraEG, a next-token probabilities and cosine similarity to the top-1 candidate reweights next-token probabilities to improves the quality(baseline vs. CraEG). diversity tradeoff. CraEG improves accuracy and generally strengthens diversity, with case studies revealing consistent trajectory-level shifts toward lower-crowding candidates. These results suggest that incorporating representation ge-

### 82. 2026-distance-distance-ratio-similarity-measure-sentences-based-on.pdf

**Title**

Distance-to-Distance Ratio: A Similarity Measure for Sentences Based on Rate of Change in LLM Embeddings

**Abstract**

A measure of similarity between text embeddings can be considered adequate only if it adheres to the human perception of similarity between texts. In this paper, we introduce the distanceto-distance ratio (DDR), a novel measure of similarity between LLM sentence embeddings. Inspired by Lipschitz continuity, DDR measures the rate of change in similarity between the pre-context word embeddings and the similarity between post-context LLM embeddings, thus measuring the semantic influence of context. We evaluate the performance of DDR in experiments designed as a series of perturbations applied to sentences drawn from a sentence dataset. For each sentence, we generate variants by replacing one, two, or three words with either synonyms, which constitute semantically similar text, or randomly chosen words, which constitute semantically dissimilar text. We compare the performance of DDR with other prevailing similarity metrics and demonstrate that DDR consistently provides finer discrimination between semantically similar and dissimilar texts, even under minimal, controlled edits.

**Conclusion**

Our results show that DDR is a viable and practical method for measuring semantic (dis)similarity between text embeddings and outperforms common methods that rely on context embedding alone. One limitation of the current implementation is the requirement that sequences have the same length. To broaden the applicability of DDR, future work should generalize the distance computation to handle variable-length inputs. Such extensions will expand DDR’s theoretical reach to enable practical applications. For example, DDR’s sensitivity to small textual variations suggests potential uses in information retrieval (distinguishing near-duplicate queries) and evaluating model robustness to adversarial edits (detecting if small lexical edits flip the model’s response when it shouldn’t). Overall, DDR allows for an expanded range; that is, similarity scores occupy a broader interval and discrimination at finer resolution.

## Source files

1. 2008-representational-similarity-analysis-connecting-branches-systems-neuroscience.pdf
2. 2013-sinkhorn-distances-lightspeed-computation-optimal-transport.pdf
3. 2014-understanding-image-representations-by-measuring-their-equivariance-equivalence.pdf
4. 2014-word-representations-via-gaussian-embedding.pdf
5. 2015-from-word-embeddings-document-distances.pdf
6. 2015-vilnis-gaussian-embedding.pdf
7. 2016-diachronic-word-embeddings-reveal-statistical-laws-semantic-change.pdf
8. 2016-man-is-computer-programmer-as-woman-is-homemaker.pdf
9. 2017-all-but-top-simple-effective-postprocessing-word-representations.pdf
10. 2017-poincare-embeddings-learning-hierarchical-representations.pdf
11. 2017-semantics-derived-automatically-from-language-corpora-contain-human.pdf
12. 2017-semeval-2017-task-1-semantic-textual-similarity-multilingual.pdf
13. 2017-svcca-singular-vector-canonical-correlation-analysis-deep-learning.pdf
14. 2018-deep-contextualized-word-representations.pdf
15. 2018-diachronic-word-embeddings-semantic-shifts-survey.pdf
16. 2018-glue-multi-task-benchmark-analysis-platform-natural-language.pdf
17. 2018-kutuzov-diachronic-survey.pdf
18. 2018-learning-continuous-hierarchies-lorentz-model-hyperbolic-geometry.pdf
19. 2018-simple-unified-framework-detecting-out-distribution-samples-adversarial.pdf
20. 2018-wic-word-context-dataset-evaluating-context-sensitive-meaning.pdf
21. 2019-bert-rediscovers-classical-nlp-pipeline.pdf
22. 2019-bertscore-evaluating-text-generation-with-bert.pdf
23. 2019-billion-scale-similarity-search-with-gpus.pdf
24. 2019-designing-interpreting-probes-with-control-tasks.pdf
25. 2019-how-contextual-are-contextualized-word-representations-comparing-geometry.pdf
26. 2019-lipstick-on-pig-debiasing-methods-cover-up-systematic.pdf
27. 2019-pilehvar-wic.pdf
28. 2019-representation-degeneration-problem-training-natural-language-generation-models.pdf
29. 2019-sentence-bert-sentence-embeddings-using-siamese-bert-networks.pdf
30. 2019-similarity-neural-network-representations-revisited.pdf
31. 2019-structural-probe-finding-syntax-word-representations.pdf
32. 2019-visualizing-measuring-geometry-bert.pdf
33. 2020-approximate-nearest-neighbor-negative-contrastive-learning-dense-text.pdf
34. 2020-dense-passage-retrieval-open-domain-question-answering.pdf
35. 2020-do-wide-deep-networks-learn-same-things-uncovering.pdf
36. 2020-energy-based-out-distribution-detection.pdf
37. 2020-retrieval-augmented-generation-knowledge-intensive-nlp-tasks.pdf
38. 2020-understanding-contrastive-representation-learning-through-alignment-uniformity-o.pdf
39. 2020-zhang-bertscore.pdf
40. 2021-bansal-revisiting-model-stitching.pdf
41. 2021-bis-shifting-embeddings.pdf
42. 2021-clipscore-reference-free-evaluation-metric-image-captioning.pdf
43. 2021-generalized-shape-metrics-on-neural-representations.pdf
44. 2021-how-does-fine-tuning-affect-geometry-embedding-space.pdf
45. 2021-isoscore-measuring-uniformity-embedding-space-utilization.pdf
46. 2021-learning-transferable-visual-models-from-natural-language-supervision.pdf
47. 2021-scalable-interpretable-semantic-change-detection.pdf
48. 2021-scaling-up-visual-vision-language-representation-learning-with.pdf
49. 2021-simcse-simple-contrastive-learning-sentence-embeddings.pdf
50. 2021-too-much-common-shifting-embeddings-transformer-language-models.pdf
51. 2022-blip-bootstrapping-language-image-pre-training-unified-vision.pdf
52. 2022-geometry-multilingual-language-model-representations.pdf
53. 2022-hyperbolic-contrastive-learning-visual-representations-beyond-objects.pdf
54. 2022-ilharco-patching-clip.pdf
55. 2022-mind-gap-understanding-modality-gap-multi-modal-contrastive.pdf
56. 2022-mteb-massive-text-embedding-benchmark.pdf
57. 2022-patching-open-vocabulary-models-by-interpolating-weights.pdf
58. 2022-rudman-isoscore.pdf
59. 2022-when-why-vision-language-models-behave-like-bags.pdf
60. 2022-winoground-probing-vision-language-models-visio-linguistic-compositionality.pdf
61. 2024-anisotropy-is-not-inherent-transformers.pdf
62. 2024-hyperbolic-fine-tuning-large-language-models.pdf
63. 2024-mitigate-gap-investigating-approaches-improving-cross-modal-alignment.pdf
64. 2024-platonic-representation-hypothesis.pdf
65. 2024-steck-cosine-similarity.pdf
66. 2024-vision-language-models-create-cross-modal-task-representations.pdf
67. 2024-wasserstein-wormhole-scalable-optimal-transport-distance-with-transformers.pdf
68. 2025-cross-gap-exposing-intra-modal-misalignment-clip-via.pdf
69. 2025-exploring-relationship-between-features-calculated-from-contextual-embeddings.pdf
70. 2025-fill-gap-quantifying-reducing-modality-gap-image-text.pdf
71. 2025-harnessing-universal-geometry-embeddings.pdf
72. 2025-huang-deciphering-cross-modal.pdf
73. 2025-jha-universal-geometry.pdf
74. 2025-kang-spectral-rsa.pdf
75. 2025-liu-distance-to-distance.pdf
76. 2025-post-pre-training-modality-alignment-vision-language-foundation.pdf
77. 2025-role-fill-the-gap.pdf
78. 2025-semantic-structure-large-language-model-embeddings.pdf
79. 2025-sevastjanova-layerflow.pdf
80. 2025-visualizing-llm-latent-space-geometry-through-dimensionality-reduction.pdf
81. 2026-decoding-geometry-alleviating-embedding-space-crowding-complex-reasoning.pdf
82. 2026-distance-distance-ratio-similarity-measure-sentences-based-on.pdf
