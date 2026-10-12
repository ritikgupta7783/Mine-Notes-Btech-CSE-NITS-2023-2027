# Lesson 11.2 — Confusion Matrix, Precision, Recall, Specificity and F1

## 1. Start with four outcomes
For binary classification:
- **TP (true positive):** positive cases predicted positive.
- **TN (true negative):** negative cases predicted negative.
- **FP (false positive):** negative cases predicted positive.
- **FN (false negative):** positive cases predicted negative.

Consider TP=40, TN=50, FP=10, FN=20. There are 120 cases total.

## 2. Calculate metrics
\[
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}=\frac{90}{120}=0.75
\]
\[
Precision=\frac{TP}{TP+FP}=\frac{40}{50}=0.80
\]
\[
Recall=\frac{TP}{TP+FN}=\frac{40}{60}\approx0.667
\]
\[
Specificity=\frac{TN}{TN+FP}=\frac{50}{60}\approx0.833
\]
\[
F1=2\frac{Precision\cdot Recall}{Precision+Recall}\approx0.727
\]

Precision answers “when the model predicts positive, how often is it correct?” Recall answers “of all actual positives, what fraction does it find?” Specificity measures how often actual negatives are correctly identified. F1 is the harmonic mean of precision and recall.

## 3. Why accuracy can mislead
Imagine 1,000 transactions where 990 are legitimate and 10 are fraud. A model that always predicts “legitimate” has 99% accuracy but finds zero fraud cases (recall for fraud is 0). The metric must match the failure cost and target prevalence.

## 4. Threshold trade-offs
A probabilistic classifier outputs scores; thresholding maps them to classes. Lowering the positive threshold often increases recall and may reduce precision, but this is data/model-dependent. Choose thresholds using validation data and a clear cost/constraint, then report performance on test data.

## 5. Python
```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

y_true = [1, 1, 1, 0, 0, 0]
y_pred = [1, 0, 1, 1, 0, 0]

print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
print("precision:", precision_score(y_true, y_pred, zero_division=0))
print("recall:", recall_score(y_true, y_pred, zero_division=0))
print("f1:", round(f1_score(y_true, y_pred, zero_division=0), 3))
```

**Output**
```text
[[2 1]
 [1 2]]
precision: 0.6666666666666666
recall: 0.6666666666666666
f1: 0.667
```

The confusion matrix here uses actual labels as rows and predicted labels as columns under labels=[0,1]. Always check the library's matrix ordering instead of assuming it.

## Practice
1. If FP increases while TP stays the same, what happens to precision?
2. If FN decreases while TP stays the same, what happens to recall?
3. Why can a high-accuracy classifier be useless for fraud detection?
4. Which metric concerns catching as many true positives as possible?

**Answers:** precision falls; recall rises; the majority class dominates accuracy while minority positives are ignored; recall.
