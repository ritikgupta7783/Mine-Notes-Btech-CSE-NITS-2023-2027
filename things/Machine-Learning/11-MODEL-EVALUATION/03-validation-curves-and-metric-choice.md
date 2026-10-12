# Lesson 11.3 — Cross-validation, ROC-AUC, PR Curves and Metric Selection

## Cross-validation
In k-fold cross-validation, development data is divided into k folds. Each run fits on k−1 folds and evaluates on the remaining fold. Aggregate results to understand variability across splits. The method is useful for model comparison and small datasets, but it does not repair leakage or a split strategy that violates time/group structure.

Use stratified folds for many classification problems where preserving class proportions matters and group/time constraints don't override that choice. Use grouped or time-aware strategies when the deployment question requires them.

## ROC curve and ROC-AUC
The ROC curve plots true-positive rate (recall) against false-positive rate across thresholds. ROC-AUC summarises ranking discrimination: a higher score means positives tend to receive higher scores than negatives under the metric's interpretation. AUC doesn't guarantee calibration or performance at the operating threshold.

## Precision-recall curve
A precision-recall curve shows the trade-off between precision and recall as the threshold changes. It is often informative for rare positive classes because it directly reflects positive predictions. Its baseline and interpretation depend on prevalence; do not compare PR-AUC across datasets without considering prevalence.

## Choose by decision
| Problem need | Metrics to consider | Caution |
|---|---|---|
| Numeric prediction, symmetric misses | MAE/RMSE; perhaps R² | Inspect residuals and scale |
| Rare fraud detection | Recall/precision, PR curve, cost-based threshold | False positives also have costs |
| Spam filter | Precision/recall/F1 with threshold | Error costs depend on use |
| Ranking candidates | ROC-AUC or PR-AUC as appropriate | Ranking isn't calibration |
| Probabilities used for decisions | Log loss and calibration checks | Good ranking may still be poorly calibrated |

## Avoid test-set tuning
Use development validation/cross-validation to choose model/hyperparameters/threshold. After choices are fixed, evaluate on final test data. Repeatedly tuning to test outcomes overfits the test set itself.

## Practice
1. When is stratified splitting helpful?
2. What does ROC-AUC summarise?
3. Why might a PR curve be especially helpful for rare positives?
4. Should the final test score choose the decision threshold?

**Answers:** when class proportions should be preserved; threshold-aggregated ranking discrimination; precision/recall focus on the positive class and prevalence matters; no, select the threshold using development validation and then evaluate on test.
