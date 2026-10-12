# Lesson 15.2 — Calibration, Thresholds and Imbalanced Data

## Imbalanced classes
If only 1% of examples are positive, a model can reach 99% accuracy by predicting all negatives. Inspect precision, recall, PR curve, cost of each error and the prevalence of the positive class. Options such as class weights, threshold adjustment or resampling can help, but must be tuned within a valid development process.

## Thresholds
For a binary score/probability, the decision threshold converts the score into a label. A lower threshold often increases recall and can reduce precision. Choose the threshold based on development validation, costs/constraints, and expected operational load—not by repeatedly checking final test labels.

## Calibration
A model is calibrated when predicted probabilities correspond to observed outcome frequencies under the relevant evaluation setting. For example, among many events predicted near 0.7, roughly 70% should occur if calibration holds. Calibration can vary across populations and over time. Good discrimination/ranking does not guarantee good calibration.

## Resampling caution
Resampling such as oversampling must be performed inside each training fold, not before a split that allows duplicates to appear in both training and test. Synthetic oversampling may create implausible samples and is not automatically superior to class weighting or threshold adjustment.

## Practice
1. Why can accuracy mislead when positives are rare?
2. Who chooses a decision threshold?
3. Does ROC-AUC measure calibration?
4. Why should oversampling not happen before a train/test split?

**Answers:** the majority-class baseline dominates; choose it on development data based on costs/constraints; no, it primarily measures ranking; duplicate/synthetic relatives could leak across train/test and distort evaluation.
