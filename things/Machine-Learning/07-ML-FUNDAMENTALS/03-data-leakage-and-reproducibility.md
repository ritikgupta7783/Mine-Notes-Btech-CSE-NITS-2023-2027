# Lesson 07.3 — Data Leakage and Reproducibility

## 1. Data leakage
Data leakage occurs when training or model selection uses information that would not legitimately be available at prediction time or uses held-out information through a preprocessing/decision step. Leakage can make evaluation look much better than real use.

### Example: target sneaks into features
Suppose you predict whether a patient will be admitted, but one feature is a code entered only after admission. The model learns the answer from a downstream record rather than predicting it from available information.

### Example: fitting a scaler before splitting
```python
# Incorrect idea (do not use as a standard workflow):
# scaler.fit(X)                 # sees training AND test feature distribution
# X_scaled = scaler.transform(X)
# then split X_scaled
```

Even without target labels, the test set informs preprocessing parameters, so the held-out evaluation is no longer fully isolated. Split first, fit preprocessing on training data, then transform validation/test data with the fitted transformer.

## 2. Time and group leakage
- Forecasting: random splitting can train on future periods and test on the past.
- User/customer records: the same person in both train and test may make evaluation overoptimistic when deployment requires generalising to new users.
- Duplicate entities across folds can leak identifying patterns.
- Features calculated using future outcomes can leak target information.

## 3. Reproducibility
Use documented random seeds when supported, record data version and preprocessing decisions, and capture package versions for projects. A reproducible experiment is easier to debug and compare. A seed alone cannot solve data leakage, selection bias or wrong assumptions.

## 4. Correct pattern
1. Define prediction time and available features.
2. Split examples using a strategy appropriate to the data (random, stratified, group-based or time-based).
3. Build preprocessing and model as one pipeline.
4. Tune on training/development data using the correct validation protocol.
5. Evaluate once on the final held-out test set.
6. Save the fitted pipeline and the feature contract for inference.

## Practice
1. A feature records a customer's cancellation date; you use it to predict next month's cancellation. Why is this suspicious?
2. Why does scaling the full dataset before a split leak information?
3. Why is a random seed not enough to ensure a valid experiment?

**Answers:** cancellation date may only be known after the outcome; it uses statistics from test data during preprocessing; a reproducible experiment can still have leakage, a biased sample or an invalid split.
