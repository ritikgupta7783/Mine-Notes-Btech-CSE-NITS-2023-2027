# Module 11 — Model Evaluation

**Prerequisites:** supervised algorithms, splits, loss and statistics.
**Goal:** measure the kinds of mistakes a model makes, select metrics appropriate to the task, and estimate performance on unseen data fairly.

## Lessons
1. [Regression metrics: MAE, MSE, RMSE and R²](01-regression-metrics.md)
2. [Classification metrics: confusion matrix, precision, recall and F1](02-classification-metrics.md)
3. [Cross-validation, ROC-AUC, PR curves and metric selection](03-validation-curves-and-metric-choice.md)

## The most important rule
No single metric is best for every task. A metric should match the target, decision and cost of failure. Accuracy can be misleading on imbalanced data; MAE and RMSE react differently to large numeric errors; ROC-AUC and PR metrics summarise different aspects of ranking.

## Checkpoint
- Calculate MAE and RMSE for small predictions.
- Fill a binary confusion matrix.
- Calculate precision, recall, specificity and F1.
- Explain threshold effects.
- Select a metric and justify it for a scenario.
