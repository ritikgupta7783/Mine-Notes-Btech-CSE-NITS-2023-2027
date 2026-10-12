# Module 09 — Supervised Learning Algorithms

**Prerequisites:** Features/targets, train/test split, vectors, losses, probability, preprocessing and evaluation.
**Goal:** choose, fit and interpret models for numeric targets (regression) and category targets (classification).

## Algorithm lessons
1. [Simple linear regression](01-simple-linear-regression.md)
2. [Multiple linear regression](02-multiple-linear-regression.md)
3. [Polynomial features, Ridge and Lasso](03-polynomial-ridge-lasso.md)
4. [Logistic regression](04-logistic-regression.md)
5. [K-nearest neighbours (KNN)](05-knn.md)
6. [Decision trees](06-decision-trees.md)
7. [Random forests](07-random-forests.md)
8. [Naive Bayes](08-naive-bayes.md)
9. [Support vector machines (SVM)](09-support-vector-machines.md)
10. [Gradient boosting regression](10-gradient-boosting.md)
11. [Decision tree regression](11-decision-tree-regression.md)
12. [Random forest regression](12-random-forest-regression.md)
13. [Gradient boosting classification](13-gradient-boosting-classification.md)

## A repeatable workflow for each algorithm
1. Define the target and prediction-time inputs.
2. Choose a simple baseline.
3. Split development/test samples appropriately.
4. Build a preprocessing/model pipeline.
5. Fit on training data.
6. Evaluate using the metrics from Module 11.
7. Inspect errors and limitations, not only the headline score.
8. Tune only with a valid validation/cross-validation strategy.

## Fast algorithm selection intuition
- Numeric continuous target: start with a regression baseline and often linear regression.
- Binary/categorical target: start with a simple classifier and an appropriate metric.
- Distance-based neighbourhoods: KNN, but scaling matters.
- Rule-like nonlinear structure in tabular data: a decision tree is interpretable; random forests combine many trees.
- Text classification with frequency features: Naive Bayes is a fast baseline.
- Max-margin classification or nonlinear kernels: SVM can help on suitable sized datasets.
- Strong tabular predictive performance: gradient-boosting methods are worth comparing, but require careful tuning.

These are starting points, not universal rankings. Data size, quality, feature structure, compute and failure costs all affect a choice.
