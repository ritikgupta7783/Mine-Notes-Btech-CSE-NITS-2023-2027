# Revision Set 18.1 — Mixed Conceptual Practice

Try these before reading [the answer key](ANSWERS.md).

## Fundamentals
1. Explain the difference between an algorithm and a fitted model.
2. Is house-price prediction usually regression or classification? Explain.
3. What is one example of a target leakage feature in churn prediction?
4. Explain why training score alone cannot establish generalisation.
5. Distinguish a parameter from a hyperparameter.

## Data and mathematics
6. X has shape (500, 12). What do the dimensions usually represent in tabular supervised learning?
7. Why does NumPy array shape matter for matrix multiplication?
8. When would you prefer the median rather than mean as a typical-value summary?
9. Does correlation prove causation? Explain using a possible confounder.
10. A KNN dataset has income measured in tens of thousands and age measured in years. What preprocessing issue arises?

## Algorithms
11. Explain the difference between linear and logistic regression.
12. Why can regularisation improve a linear model's generalisation?
13. How does a decision tree choose a split at a high level?
14. Explain how a random forest differs from gradient boosting.
15. What assumption gives Naive Bayes its name?
16. Why does K-means require a choice of K?
17. What does PCA optimise/capture, and why doesn't it guarantee predictive improvement?

## Evaluation
18. TP=30, FP=10, FN=20. Calculate precision and recall.
19. A fraud classifier has 99% accuracy but zero fraud recall. What does this suggest?
20. When should the final test set influence hyperparameter choice?
21. Why should a scaler sit inside a pipeline during cross-validation?
22. What does a negative R² on test data indicate under the usual definition?

## Engineering and reasoning
23. Why save preprocessing along with the estimator?
24. A new category appears at inference. What should an ML system do?
25. What is one limitation of built-in tree feature importance?
26. Explain the difference between data drift and concept drift.
27. State one responsible-use concern for a model that predicts loan default.
28. Design a valid evaluation strategy for forecasting next month's demand.
