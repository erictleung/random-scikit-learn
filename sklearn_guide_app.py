import streamlit as st
import random
import requests
from bs4 import BeautifulSoup

# Comprehensive list of scikit-learn user guide topics with their URLs
# Including all subsections from the documentation (240+ guides!)
SKLEARN_GUIDES = {
    # 1.1 Linear Models subsections
    "1.1.1 Ordinary Least Squares": "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares",
    "1.1.2 Ridge Regression and Classification": "https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification",
    "1.1.3 Lasso": "https://scikit-learn.org/stable/modules/linear_model.html#lasso",
    "1.1.4 Multi-task Lasso": "https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso",
    "1.1.5 Elastic-Net": "https://scikit-learn.org/stable/modules/linear_model.html#elastic-net",
    "1.1.6 Multi-task Elastic-Net": "https://scikit-learn.org/stable/modules/linear_model.html#multi-task-elastic-net",
    "1.1.7 Least Angle Regression": "https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression",
    "1.1.8 LARS Lasso": "https://scikit-learn.org/stable/modules/linear_model.html#lars-lasso",
    "1.1.9 Orthogonal Matching Pursuit (OMP)": "https://scikit-learn.org/stable/modules/linear_model.html#orthogonal-matching-pursuit-omp",
    "1.1.10 Bayesian Regression": "https://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression",
    "1.1.11 Logistic Regression": "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression",
    "1.1.12 Generalized Linear Models": "https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-models",
    "1.1.13 Stochastic Gradient Descent - SGD": "https://scikit-learn.org/stable/modules/linear_model.html#stochastic-gradient-descent-sgd",
    "1.1.14 Robustness Regression": "https://scikit-learn.org/stable/modules/linear_model.html#robustness-regression-outliers-and-modeling-errors",
    "1.1.15 Quantile Regression": "https://scikit-learn.org/stable/modules/linear_model.html#quantile-regression",
    "1.1.16 Polynomial Regression": "https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression-extending-linear-models-with-basis-functions",
    
    # 1.2 Linear and Quadratic Discriminant Analysis
    "1.2.1 Dimensionality Reduction using LDA": "https://scikit-learn.org/stable/modules/lda_qda.html#dimensionality-reduction-using-linear-discriminant-analysis",
    "1.2.2 Mathematical Formulation of LDA and QDA": "https://scikit-learn.org/stable/modules/lda_qda.html#mathematical-formulation-of-the-lda-and-qda-classifiers",
    "1.2.3 LDA Dimensionality Reduction": "https://scikit-learn.org/stable/modules/lda_qda.html#mathematical-formulation-of-lda-dimensionality-reduction",
    "1.2.4 Shrinkage and Covariance Estimator": "https://scikit-learn.org/stable/modules/lda_qda.html#shrinkage-and-covariance-estimator",
    "1.2.5 Estimation Algorithms": "https://scikit-learn.org/stable/modules/lda_qda.html#estimation-algorithms",
    
    # 1.3 Kernel Ridge Regression
    "1.3 Kernel Ridge Regression": "https://scikit-learn.org/stable/modules/kernel_ridge.html",
    
    # 1.4 Support Vector Machines
    "1.4.1 SVM Classification": "https://scikit-learn.org/stable/modules/svm.html#classification",
    "1.4.2 SVM Regression": "https://scikit-learn.org/stable/modules/svm.html#regression",
    "1.4.3 Density Estimation, Novelty Detection": "https://scikit-learn.org/stable/modules/svm.html#density-estimation-novelty-detection",
    "1.4.4 SVM Complexity": "https://scikit-learn.org/stable/modules/svm.html#complexity",
    "1.4.5 Tips on Practical Use": "https://scikit-learn.org/stable/modules/svm.html#tips-on-practical-use",
    "1.4.6 Kernel Functions": "https://scikit-learn.org/stable/modules/svm.html#kernel-functions",
    "1.4.7 Mathematical Formulation": "https://scikit-learn.org/stable/modules/svm.html#mathematical-formulation",
    "1.4.8 Implementation Details": "https://scikit-learn.org/stable/modules/svm.html#implementation-details",
    
    # 1.5 Stochastic Gradient Descent
    "1.5.1 SGD Classification": "https://scikit-learn.org/stable/modules/sgd.html#classification",
    "1.5.2 SGD Regression": "https://scikit-learn.org/stable/modules/sgd.html#regression",
    "1.5.3 Online One-Class SVM": "https://scikit-learn.org/stable/modules/sgd.html#online-one-class-svm",
    "1.5.4 SGD for Sparse Data": "https://scikit-learn.org/stable/modules/sgd.html#stochastic-gradient-descent-for-sparse-data",
    
    # 1.6 Nearest Neighbors
    "1.6.1 Unsupervised Nearest Neighbors": "https://scikit-learn.org/stable/modules/neighbors.html#unsupervised-nearest-neighbors",
    "1.6.2 Nearest Neighbors Classification": "https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors-classification",
    "1.6.3 Nearest Neighbors Regression": "https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors-regression",
    "1.6.4 Nearest Neighbor Algorithms": "https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbor-algorithms",
    "1.6.5 Nearest Centroid Classifier": "https://scikit-learn.org/stable/modules/neighbors.html#nearest-centroid-classifier",
    "1.6.6 Nearest Neighbors Transformer": "https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors-transformer",
    "1.6.7 Neighborhood Components Analysis": "https://scikit-learn.org/stable/modules/neighbors.html#neighborhood-components-analysis",
    
    # 1.7 Gaussian Processes
    "1.7.1 Gaussian Process Regression (GPR)": "https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process-regression-gpr",
    "1.7.2 Gaussian Process Classification (GPC)": "https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process-classification-gpc",
    "1.7.3 GPC Examples": "https://scikit-learn.org/stable/modules/gaussian_process.html#gpc-examples",
    "1.7.4 Kernels for Gaussian Processes": "https://scikit-learn.org/stable/modules/gaussian_process.html#kernels-for-gaussian-processes",
    
    # 1.8 Cross Decomposition
    "1.8.1 PLSCanonical": "https://scikit-learn.org/stable/modules/cross_decomposition.html#plscanonical",
    "1.8.2 PLSSVD": "https://scikit-learn.org/stable/modules/cross_decomposition.html#plssvd",
    "1.8.3 PLSRegression": "https://scikit-learn.org/stable/modules/cross_decomposition.html#plsregression",
    "1.8.4 Canonical Correlation Analysis": "https://scikit-learn.org/stable/modules/cross_decomposition.html#canonical-correlation-analysis",
    
    # 1.9 Naive Bayes
    "1.9.1 Gaussian Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes",
    "1.9.2 Multinomial Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes",
    "1.9.3 Complement Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#complement-naive-bayes",
    "1.9.4 Bernoulli Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes",
    "1.9.5 Categorical Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#categorical-naive-bayes",
    "1.9.6 Out-of-core Naive Bayes": "https://scikit-learn.org/stable/modules/naive_bayes.html#out-of-core-naive-bayes-model-fitting",
    
    # 1.10 Decision Trees
    "1.10.1 Decision Tree Classification": "https://scikit-learn.org/stable/modules/tree.html#classification",
    "1.10.2 Decision Tree Regression": "https://scikit-learn.org/stable/modules/tree.html#regression",
    "1.10.3 Multi-output Problems": "https://scikit-learn.org/stable/modules/tree.html#multi-output-problems",
    "1.10.4 Tree Complexity": "https://scikit-learn.org/stable/modules/tree.html#complexity",
    "1.10.5 Tips on Practical Use": "https://scikit-learn.org/stable/modules/tree.html#tips-on-practical-use",
    "1.10.6 Tree Algorithms: ID3, C4.5, CART": "https://scikit-learn.org/stable/modules/tree.html#tree-algorithms-id3-c4-5-c5-0-and-cart",
    "1.10.7 Tree Mathematical Formulation": "https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation",
    "1.10.8 Missing Values Support": "https://scikit-learn.org/stable/modules/tree.html#missing-values-support",
    "1.10.9 Cost-Complexity Pruning": "https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning",
    
    # 1.11 Ensemble Methods
    "1.11.1 Gradient-boosted Trees": "https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosted-trees",
    "1.11.2 Random Forests": "https://scikit-learn.org/stable/modules/ensemble.html#random-forests-and-other-randomized-tree-ensembles",
    "1.11.3 Bagging Meta-estimator": "https://scikit-learn.org/stable/modules/ensemble.html#bagging-meta-estimator",
    "1.11.4 Voting Classifier": "https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier",
    "1.11.5 Voting Regressor": "https://scikit-learn.org/stable/modules/ensemble.html#voting-regressor",
    "1.11.6 Stacked Generalization": "https://scikit-learn.org/stable/modules/ensemble.html#stacked-generalization",
    "1.11.7 AdaBoost": "https://scikit-learn.org/stable/modules/ensemble.html#adaboost",
    
    # 1.12 Multiclass and Multioutput
    "1.12.1 Multiclass Classification": "https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification",
    "1.12.2 Multilabel Classification": "https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification",
    "1.12.3 Multiclass-multioutput Classification": "https://scikit-learn.org/stable/modules/multiclass.html#multiclass-multioutput-classification",
    "1.12.4 Multioutput Regression": "https://scikit-learn.org/stable/modules/multiclass.html#multioutput-regression",
    
    # 1.13 Feature Selection
    "1.13.1 Removing Low Variance Features": "https://scikit-learn.org/stable/modules/feature_selection.html#removing-features-with-low-variance",
    "1.13.2 Univariate Feature Selection": "https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection",
    "1.13.3 Recursive Feature Elimination": "https://scikit-learn.org/stable/modules/feature_selection.html#recursive-feature-elimination",
    "1.13.4 Feature Selection using SelectFromModel": "https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection-using-selectfrommodel",
    "1.13.5 Sequential Feature Selection": "https://scikit-learn.org/stable/modules/feature_selection.html#sequential-feature-selection",
    "1.13.6 Feature Selection in Pipeline": "https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection-as-part-of-a-pipeline",
    
    # 1.14 Semi-supervised Learning
    "1.14.1 Self Training": "https://scikit-learn.org/stable/modules/semi_supervised.html#self-training",
    "1.14.2 Label Propagation": "https://scikit-learn.org/stable/modules/semi_supervised.html#label-propagation",
    
    # 1.15 Isotonic Regression
    "1.15 Isotonic Regression": "https://scikit-learn.org/stable/modules/isotonic.html",
    
    # 1.16 Probability Calibration
    "1.16.1 Calibration Curves": "https://scikit-learn.org/stable/modules/calibration.html#calibration-curves",
    "1.16.2 Calibrating a Classifier": "https://scikit-learn.org/stable/modules/calibration.html#calibrating-a-classifier",
    "1.16.3 Calibration Usage": "https://scikit-learn.org/stable/modules/calibration.html#usage",
    
    # 1.17 Neural Networks (Supervised)
    "1.17.1 Multi-layer Perceptron": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron",
    "1.17.2 MLP Classification": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#classification",
    "1.17.3 MLP Regression": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression",
    "1.17.4 MLP Regularization": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regularization",
    "1.17.5 MLP Algorithms": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#algorithms",
    "1.17.6 MLP Complexity": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#complexity",
    "1.17.7 MLP Tips on Practical Use": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#tips-on-practical-use",
    "1.17.8 Warm Start": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html#more-control-with-warm-start",
    
    # 2.1 Gaussian Mixture Models
    "2.1.1 Gaussian Mixture": "https://scikit-learn.org/stable/modules/mixture.html#gaussian-mixture",
    "2.1.2 Variational Bayesian Gaussian Mixture": "https://scikit-learn.org/stable/modules/mixture.html#variational-bayesian-gaussian-mixture",
    
    # 2.2 Manifold Learning
    "2.2.1 Manifold Learning Introduction": "https://scikit-learn.org/stable/modules/manifold.html#introduction",
    "2.2.2 Isomap": "https://scikit-learn.org/stable/modules/manifold.html#isomap",
    "2.2.3 Locally Linear Embedding": "https://scikit-learn.org/stable/modules/manifold.html#locally-linear-embedding",
    "2.2.4 Modified Locally Linear Embedding": "https://scikit-learn.org/stable/modules/manifold.html#modified-locally-linear-embedding",
    "2.2.5 Hessian Eigenmapping": "https://scikit-learn.org/stable/modules/manifold.html#hessian-eigenmapping",
    "2.2.6 Spectral Embedding": "https://scikit-learn.org/stable/modules/manifold.html#spectral-embedding",
    "2.2.7 Local Tangent Space Alignment": "https://scikit-learn.org/stable/modules/manifold.html#local-tangent-space-alignment",
    "2.2.8 Multi-dimensional Scaling (MDS)": "https://scikit-learn.org/stable/modules/manifold.html#multi-dimensional-scaling-mds",
    "2.2.9 t-SNE": "https://scikit-learn.org/stable/modules/manifold.html#t-distributed-stochastic-neighbor-embedding-t-sne",
    "2.2.10 Manifold Learning Tips": "https://scikit-learn.org/stable/modules/manifold.html#tips-on-practical-use",
    
    # 2.3 Clustering
    "2.3.1 Overview of Clustering Methods": "https://scikit-learn.org/stable/modules/clustering.html#overview-of-clustering-methods",
    "2.3.2 K-means": "https://scikit-learn.org/stable/modules/clustering.html#k-means",
    "2.3.3 Affinity Propagation": "https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation",
    "2.3.4 Mean Shift": "https://scikit-learn.org/stable/modules/clustering.html#mean-shift",
    "2.3.5 Spectral Clustering": "https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering",
    "2.3.6 Hierarchical Clustering": "https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering",
    "2.3.7 DBSCAN": "https://scikit-learn.org/stable/modules/clustering.html#dbscan",
    "2.3.8 HDBSCAN": "https://scikit-learn.org/stable/modules/clustering.html#hdbscan",
    "2.3.9 OPTICS": "https://scikit-learn.org/stable/modules/clustering.html#optics",
    "2.3.10 BIRCH": "https://scikit-learn.org/stable/modules/clustering.html#birch",
    "2.3.11 Clustering Performance Evaluation": "https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation",
    
    # 2.4 Biclustering
    "2.4.1 Spectral Co-Clustering": "https://scikit-learn.org/stable/modules/biclustering.html#spectral-co-clustering",
    "2.4.2 Spectral Biclustering": "https://scikit-learn.org/stable/modules/biclustering.html#spectral-biclustering",
    "2.4.3 Biclustering Evaluation": "https://scikit-learn.org/stable/modules/biclustering.html#biclustering-evaluation",
    
    # 2.5 Matrix Decomposition
    "2.5.1 Principal Component Analysis (PCA)": "https://scikit-learn.org/stable/modules/decomposition.html#principal-component-analysis-pca",
    "2.5.2 Kernel PCA": "https://scikit-learn.org/stable/modules/decomposition.html#kernel-principal-component-analysis-kpca",
    "2.5.3 Truncated SVD": "https://scikit-learn.org/stable/modules/decomposition.html#truncated-singular-value-decomposition-and-latent-semantic-analysis",
    "2.5.4 Dictionary Learning": "https://scikit-learn.org/stable/modules/decomposition.html#dictionary-learning",
    "2.5.5 Factor Analysis": "https://scikit-learn.org/stable/modules/decomposition.html#factor-analysis",
    "2.5.6 Independent Component Analysis (ICA)": "https://scikit-learn.org/stable/modules/decomposition.html#independent-component-analysis-ica",
    "2.5.7 Non-negative Matrix Factorization (NMF)": "https://scikit-learn.org/stable/modules/decomposition.html#non-negative-matrix-factorization-nmf-or-nnmf",
    "2.5.8 Latent Dirichlet Allocation (LDA)": "https://scikit-learn.org/stable/modules/decomposition.html#latent-dirichlet-allocation-lda",
    
    # 2.6 Covariance Estimation
    "2.6.1 Empirical Covariance": "https://scikit-learn.org/stable/modules/covariance.html#empirical-covariance",
    "2.6.2 Shrunk Covariance": "https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance",
    "2.6.3 Sparse Inverse Covariance": "https://scikit-learn.org/stable/modules/covariance.html#sparse-inverse-covariance",
    "2.6.4 Robust Covariance Estimation": "https://scikit-learn.org/stable/modules/covariance.html#robust-covariance-estimation",
    
    # 2.7 Novelty and Outlier Detection
    "2.7.1 Overview of Outlier Detection": "https://scikit-learn.org/stable/modules/outlier_detection.html#overview-of-outlier-detection-methods",
    "2.7.2 Novelty Detection": "https://scikit-learn.org/stable/modules/outlier_detection.html#novelty-detection",
    "2.7.3 Outlier Detection": "https://scikit-learn.org/stable/modules/outlier_detection.html#id1",
    "2.7.4 Local Outlier Factor": "https://scikit-learn.org/stable/modules/outlier_detection.html#novelty-detection-with-local-outlier-factor",
    
    # 2.8 Density Estimation
    "2.8.1 Density Estimation: Histograms": "https://scikit-learn.org/stable/modules/density.html#density-estimation-histograms",
    "2.8.2 Kernel Density Estimation": "https://scikit-learn.org/stable/modules/density.html#kernel-density-estimation",
    
    # 2.9 Neural Networks (Unsupervised)
    "2.9.1 Restricted Boltzmann Machines": "https://scikit-learn.org/stable/modules/neural_networks_unsupervised.html#restricted-boltzmann-machines",
    
    # 3.1 Cross-validation
    "3.1.1 Computing Cross-validated Metrics": "https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics",
    "3.1.2 Cross Validation Iterators": "https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators",
    "3.1.3 Note on Shuffling": "https://scikit-learn.org/stable/modules/cross_validation.html#a-note-on-shuffling",
    "3.1.4 Cross Validation and Model Selection": "https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-and-model-selection",
    "3.1.5 Permutation Test Score": "https://scikit-learn.org/stable/modules/cross_validation.html#permutation-test-score",
    
    # 3.2 Hyperparameter Tuning
    "3.2.1 Exhaustive Grid Search": "https://scikit-learn.org/stable/modules/grid_search.html#exhaustive-grid-search",
    "3.2.2 Randomized Parameter Optimization": "https://scikit-learn.org/stable/modules/grid_search.html#randomized-parameter-optimization",
    "3.2.3 Successive Halving": "https://scikit-learn.org/stable/modules/grid_search.html#searching-for-optimal-parameters-with-successive-halving",
    "3.2.4 Tips for Parameter Search": "https://scikit-learn.org/stable/modules/grid_search.html#tips-for-parameter-search",
    "3.2.5 Alternatives to Brute Force": "https://scikit-learn.org/stable/modules/grid_search.html#alternatives-to-brute-force-parameter-search",
    
    # 3.3 Classification Threshold Tuning
    "3.3.1 Post-tuning Decision Threshold": "https://scikit-learn.org/stable/modules/classification_threshold.html#post-tuning-the-decision-threshold",
    
    # 3.4 Metrics and Scoring
    "3.4.1 Which Scoring Function": "https://scikit-learn.org/stable/modules/model_evaluation.html#which-scoring-function-should-i-use",
    "3.4.2 Scoring API Overview": "https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview",
    "3.4.3 Scoring Parameter": "https://scikit-learn.org/stable/modules/model_evaluation.html#the-scoring-parameter-defining-model-evaluation-rules",
    "3.4.4 Classification Metrics": "https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics",
    "3.4.5 Multilabel Ranking Metrics": "https://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-ranking-metrics",
    "3.4.6 Regression Metrics": "https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics",
    "3.4.7 Clustering Metrics": "https://scikit-learn.org/stable/modules/model_evaluation.html#clustering-metrics",
    "3.4.8 Dummy Estimators": "https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators",
    
    # 3.5 Validation Curves
    "3.5.1 Validation Curve": "https://scikit-learn.org/stable/modules/learning_curve.html#validation-curve",
    "3.5.2 Learning Curve": "https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve",
    
    # 4. Metadata Routing
    "4.1 Metadata Routing Usage Examples": "https://scikit-learn.org/stable/metadata_routing.html#usage-examples",
    "4.2 Metadata Routing API Interface": "https://scikit-learn.org/stable/metadata_routing.html#api-interface",
    "4.3 Metadata Routing Support Status": "https://scikit-learn.org/stable/metadata_routing.html#metadata-routing-support-status",
    
    # 5.1 Partial Dependence
    "5.1.1 Partial Dependence Plots": "https://scikit-learn.org/stable/modules/partial_dependence.html#partial-dependence-plots",
    "5.1.2 ICE Plot": "https://scikit-learn.org/stable/modules/partial_dependence.html#individual-conditional-expectation-ice-plot",
    "5.1.3 Mathematical Definition": "https://scikit-learn.org/stable/modules/partial_dependence.html#mathematical-definition",
    "5.1.4 Computation Methods": "https://scikit-learn.org/stable/modules/partial_dependence.html#computation-methods",
    
    # 5.2 Permutation Feature Importance
    "5.2.1 Permutation Importance Algorithm": "https://scikit-learn.org/stable/modules/permutation_importance.html#outline-of-the-permutation-importance-algorithm",
    "5.2.2 Relation to Tree Importance": "https://scikit-learn.org/stable/modules/permutation_importance.html#relation-to-impurity-based-importance-in-trees",
    "5.2.3 Misleading Values on Correlated Features": "https://scikit-learn.org/stable/modules/permutation_importance.html#misleading-values-on-strongly-correlated-features",
    
    # 6. Visualizations
    "6.1 Available Plotting Utilities": "https://scikit-learn.org/stable/visualizations.html#available-plotting-utilities",
    
    # 7.1 Pipelines
    "7.1.1 Pipeline: Chaining Estimators": "https://scikit-learn.org/stable/modules/compose.html#pipeline-chaining-estimators",
    "7.1.2 Transforming Target in Regression": "https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression",
    "7.1.3 FeatureUnion": "https://scikit-learn.org/stable/modules/compose.html#featureunion-composite-feature-spaces",
    "7.1.4 ColumnTransformer": "https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data",
    "7.1.5 Visualizing Composite Estimators": "https://scikit-learn.org/stable/modules/compose.html#visualizing-composite-estimators",
    
    # 7.2 Feature Extraction
    "7.2.1 Loading Features from Dicts": "https://scikit-learn.org/stable/modules/feature_extraction.html#loading-features-from-dicts",
    "7.2.2 Feature Hashing": "https://scikit-learn.org/stable/modules/feature_extraction.html#feature-hashing",
    "7.2.3 Text Feature Extraction": "https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction",
    "7.2.4 Image Feature Extraction": "https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction",
    
    # 7.3 Preprocessing Data
    "7.3.1 Standardization": "https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling",
    "7.3.2 Non-linear Transformation": "https://scikit-learn.org/stable/modules/preprocessing.html#non-linear-transformation",
    "7.3.3 Normalization": "https://scikit-learn.org/stable/modules/preprocessing.html#normalization",
    "7.3.4 Encoding Categorical Features": "https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features",
    "7.3.5 Discretization": "https://scikit-learn.org/stable/modules/preprocessing.html#discretization",
    "7.3.6 Imputation of Missing Values": "https://scikit-learn.org/stable/modules/preprocessing.html#imputation-of-missing-values",
    "7.3.7 Generating Polynomial Features": "https://scikit-learn.org/stable/modules/preprocessing.html#generating-polynomial-features",
    "7.3.8 Custom Transformers": "https://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers",
    
    # 7.4 Imputation
    "7.4.1 Univariate vs Multivariate Imputation": "https://scikit-learn.org/stable/modules/impute.html#univariate-vs-multivariate-imputation",
    "7.4.2 Univariate Feature Imputation": "https://scikit-learn.org/stable/modules/impute.html#univariate-feature-imputation",
    "7.4.3 Multivariate Feature Imputation": "https://scikit-learn.org/stable/modules/impute.html#multivariate-feature-imputation",
    "7.4.4 Nearest Neighbors Imputation": "https://scikit-learn.org/stable/modules/impute.html#nearest-neighbors-imputation",
    "7.4.5 Keeping Number of Features Constant": "https://scikit-learn.org/stable/modules/impute.html#keeping-the-number-of-features-constant",
    "7.4.6 Marking Imputed Values": "https://scikit-learn.org/stable/modules/impute.html#marking-imputed-values",
    "7.4.7 Estimators that Handle NaN": "https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values",
    
    # 7.5 Unsupervised Dimensionality Reduction
    "7.5.1 PCA: Principal Component Analysis": "https://scikit-learn.org/stable/modules/unsupervised_reduction.html#pca-principal-component-analysis",
    "7.5.2 Random Projections": "https://scikit-learn.org/stable/modules/unsupervised_reduction.html#random-projections",
    "7.5.3 Feature Agglomeration": "https://scikit-learn.org/stable/modules/unsupervised_reduction.html#feature-agglomeration",
    
    # 7.6 Random Projection
    "7.6.1 Johnson-Lindenstrauss Lemma": "https://scikit-learn.org/stable/modules/random_projection.html#the-johnson-lindenstrauss-lemma",
    "7.6.2 Gaussian Random Projection": "https://scikit-learn.org/stable/modules/random_projection.html#gaussian-random-projection",
    "7.6.3 Sparse Random Projection": "https://scikit-learn.org/stable/modules/random_projection.html#sparse-random-projection",
    "7.6.4 Inverse Transform": "https://scikit-learn.org/stable/modules/random_projection.html#inverse-transform",
    
    # 7.7 Kernel Approximation
    "7.7.1 Nystroem Method": "https://scikit-learn.org/stable/modules/kernel_approximation.html#nystroem-method-for-kernel-approximation",
    "7.7.2 RBF Kernel": "https://scikit-learn.org/stable/modules/kernel_approximation.html#radial-basis-function-kernel",
    "7.7.3 Additive Chi Squared Kernel": "https://scikit-learn.org/stable/modules/kernel_approximation.html#additive-chi-squared-kernel",
    "7.7.4 Skewed Chi Squared Kernel": "https://scikit-learn.org/stable/modules/kernel_approximation.html#skewed-chi-squared-kernel",
    "7.7.5 Polynomial Kernel via Tensor Sketch": "https://scikit-learn.org/stable/modules/kernel_approximation.html#polynomial-kernel-approximation-via-tensor-sketch",
    "7.7.6 Mathematical Details": "https://scikit-learn.org/stable/modules/kernel_approximation.html#mathematical-details",
    
    # 7.8 Pairwise Metrics
    "7.8.1 Cosine Similarity": "https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity",
    "7.8.2 Linear Kernel": "https://scikit-learn.org/stable/modules/metrics.html#linear-kernel",
    "7.8.3 Polynomial Kernel": "https://scikit-learn.org/stable/modules/metrics.html#polynomial-kernel",
    "7.8.4 Sigmoid Kernel": "https://scikit-learn.org/stable/modules/metrics.html#sigmoid-kernel",
    "7.8.5 RBF Kernel": "https://scikit-learn.org/stable/modules/metrics.html#rbf-kernel",
    "7.8.6 Laplacian Kernel": "https://scikit-learn.org/stable/modules/metrics.html#laplacian-kernel",
    "7.8.7 Chi-squared Kernel": "https://scikit-learn.org/stable/modules/metrics.html#chi-squared-kernel",
    
    # 7.9 Transforming Targets
    "7.9.1 Label Binarization": "https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-binarization",
    "7.9.2 Label Encoding": "https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding",
    
    # 8.1 Toy Datasets
    "8.1.1 Iris Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset",
    "8.1.2 Diabetes Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset",
    "8.1.3 Digits Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#optical-recognition-of-handwritten-digits-dataset",
    "8.1.4 Linnerrud Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset",
    "8.1.5 Wine Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset",
    "8.1.6 Breast Cancer Dataset": "https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-wisconsin-diagnostic-dataset",
    
    # 8.2 Real World Datasets
    "8.2.1 Olivetti Faces Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#the-olivetti-faces-dataset",
    "8.2.2 20 Newsgroups Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#the-20-newsgroups-text-dataset",
    "8.2.3 Labeled Faces in the Wild": "https://scikit-learn.org/stable/datasets/real_world.html#the-labeled-faces-in-the-wild-face-recognition-dataset",
    "8.2.4 Forest Covertypes": "https://scikit-learn.org/stable/datasets/real_world.html#forest-covertypes",
    "8.2.5 RCV1 Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#rcv1-dataset",
    "8.2.6 Kddcup 99 Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#kddcup-99-dataset",
    "8.2.7 California Housing Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset",
    "8.2.8 Species Distribution Dataset": "https://scikit-learn.org/stable/datasets/real_world.html#species-distribution-dataset",
    
    # 8.3 Generated Datasets
    "8.3.1 Generators for Classification/Clustering": "https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-classification-and-clustering",
    "8.3.2 Generators for Regression": "https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-regression",
    "8.3.3 Generators for Manifold Learning": "https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-manifold-learning",
    "8.3.4 Generators for Decomposition": "https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-decomposition",
    
    # 8.4 Loading Other Datasets
    "8.4.1 Sample Images": "https://scikit-learn.org/stable/datasets/loading_other_datasets.html#sample-images",
    "8.4.2 SVMLight/LibSVM Format": "https://scikit-learn.org/stable/datasets/loading_other_datasets.html#datasets-in-svmlight-libsvm-format",
    "8.4.3 OpenML Repository": "https://scikit-learn.org/stable/datasets/loading_other_datasets.html#downloading-datasets-from-the-openml-org-repository",
    "8.4.4 Loading External Datasets": "https://scikit-learn.org/stable/datasets/loading_other_datasets.html#loading-from-external-datasets",
    
    # 9.1 Scaling Strategies
    "9.1.1 Out-of-core Learning": "https://scikit-learn.org/stable/computing/scaling_strategies.html#scaling-with-instances-using-out-of-core-learning",
    
    # 9.2 Computational Performance
    "9.2.1 Prediction Latency": "https://scikit-learn.org/stable/computing/computational_performance.html#prediction-latency",
    "9.2.2 Prediction Throughput": "https://scikit-learn.org/stable/computing/computational_performance.html#prediction-throughput",
    "9.2.3 Performance Tips and Tricks": "https://scikit-learn.org/stable/computing/computational_performance.html#tips-and-tricks",
    
    # 9.3 Parallelism
    "9.3.1 Parallelism": "https://scikit-learn.org/stable/computing/parallelism.html#parallelism",
    "9.3.2 Configuration Switches": "https://scikit-learn.org/stable/computing/parallelism.html#configuration-switches",
    
    # 10. Model Persistence
    "10.1 Workflow Overview": "https://scikit-learn.org/stable/model_persistence.html#workflow-overview",
    "10.2 ONNX": "https://scikit-learn.org/stable/model_persistence.html#onnx",
    "10.3 skops.io": "https://scikit-learn.org/stable/model_persistence.html#skops-io",
    "10.4 Pickle, Joblib, Cloudpickle": "https://scikit-learn.org/stable/model_persistence.html#pickle-joblib-and-cloudpickle",
    "10.5 Security & Maintainability": "https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations",
    
    # 11. Common Pitfalls
    "11.1 Inconsistent Preprocessing": "https://scikit-learn.org/stable/common_pitfalls.html#inconsistent-preprocessing",
    "11.2 Data Leakage": "https://scikit-learn.org/stable/common_pitfalls.html#data-leakage",
    "11.3 Controlling Randomness": "https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness",
    
    # 12.1 Array API
    "12.1.1 Enabling Array API": "https://scikit-learn.org/stable/modules/array_api.html#enabling-array-api-support",
    "12.1.2 Example Usage": "https://scikit-learn.org/stable/modules/array_api.html#example-usage",
    "12.1.3 Array API Compatible Inputs": "https://scikit-learn.org/stable/modules/array_api.html#support-for-array-api-compatible-inputs",
    "12.1.4 Input/Output Array Handling": "https://scikit-learn.org/stable/modules/array_api.html#input-and-output-array-type-handling",
    "12.1.5 Common Estimator Checks": "https://scikit-learn.org/stable/modules/array_api.html#common-estimator-checks",
    
    # 13. Choosing the Right Estimator
    "13. Choosing the Right Estimator": "https://scikit-learn.org/stable/machine_learning_map.html",
    
    # 14. External Resources
    "14.1 Scikit-learn MOOC": "https://scikit-learn.org/stable/presentations.html#the-scikit-learn-mooc",
    "14.2 Videos": "https://scikit-learn.org/stable/presentations.html#videos",
    "14.3 New to Scientific Python": "https://scikit-learn.org/stable/presentations.html#new-to-scientific-python",
    "14.4 External Tutorials": "https://scikit-learn.org/stable/presentations.html#external-tutorials",
}

def get_guide_preview(url):
    """Fetch a preview of the guide content"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main content area
        main_content = soup.find('div', {'role': 'main'}) or soup.find('section')
        
        if main_content:
            # Get the first few paragraphs
            paragraphs = main_content.find_all('p', limit=3)
            preview_text = '\n\n'.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
            return preview_text[:500] + "..." if len(preview_text) > 500 else preview_text
        
        return "Preview not available"
    except Exception as e:
        return f"Could not load preview: {str(e)}"

# Streamlit App
st.set_page_config(
    page_title="Random Scikit-learn Guide",
    page_icon="🎲",
    layout="wide"
)

st.title("🎲 Random Scikit-learn Guide Generator")
st.markdown("Explore scikit-learn documentation one random topic at a time!")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    "This app randomly selects a guide from the scikit-learn User Guide. "
    "Guides are at the subsection level (e.g., 1.1.1 Ordinary Least Squares) "
    "for more focused learning. Click the button to discover a new topic!"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Total Guides Available:** {len(SKLEARN_GUIDES)}")

# Initialize session state
if 'current_guide' not in st.session_state:
    st.session_state.current_guide = None
    st.session_state.current_url = None

# Main content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎲 Get Random Guide", type="primary", use_container_width=True):
        # Select a random guide
        guide_name = random.choice(list(SKLEARN_GUIDES.keys()))
        st.session_state.current_guide = guide_name
        st.session_state.current_url = SKLEARN_GUIDES[guide_name]

# Display the selected guide
if st.session_state.current_guide:
    st.markdown("---")
    
    # Display guide title
    st.header(f"📚 {st.session_state.current_guide}")
    
    # Create columns for layout
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown(f"**Direct Link:** [{st.session_state.current_url}]({st.session_state.current_url})")
        
        # Show preview with loading spinner
        with st.spinner("Loading preview..."):
            preview = get_guide_preview(st.session_state.current_url)
            st.markdown("### Preview")
            st.info(preview)
    
    with col_right:
        st.markdown("### Quick Actions")
        st.link_button("📖 Read Full Guide", st.session_state.current_url, use_container_width=True)
        st.link_button("🏠 All Guides", "https://scikit-learn.org/stable/user_guide.html", use_container_width=True)
        
        if st.button("🔄 Get Another Random Guide", use_container_width=True):
            # Get a different guide
            available_guides = [g for g in SKLEARN_GUIDES.keys() if g != st.session_state.current_guide]
            guide_name = random.choice(available_guides)
            st.session_state.current_guide = guide_name
            st.session_state.current_url = SKLEARN_GUIDES[guide_name]
            st.rerun()

else:
    # Initial state - show a welcome message
    st.info("👆 Click the button above to get started and discover a random scikit-learn guide!")
    
    # Show some stats
    st.markdown("### Available Topics")
    st.markdown(f"There are **{len(SKLEARN_GUIDES)}** detailed guides covering specific machine learning topics at the subsection level.")
    st.markdown("**Examples include:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Linear Models**")
        st.markdown("- Ordinary Least Squares\n- Ridge Regression\n- Lasso\n- Elastic-Net")
    
    with col2:
        st.markdown("**Model Selection**")
        st.markdown("- Cross-validation\n- Hyperparameter Tuning\n- Metrics and Scoring")
    
    with col3:
        st.markdown("**Preprocessing**")
        st.markdown("- Feature Extraction\n- Data Preprocessing\n- Pipelines")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with Streamlit | Data from scikit-learn.org"
    "</div>",
    unsafe_allow_html=True
)
