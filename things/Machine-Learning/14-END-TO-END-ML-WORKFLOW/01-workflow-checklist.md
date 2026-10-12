# Lesson 14.1 — End-to-End Workflow Checklist

## 1. Define the task before coding
Write:
- What decision or estimate is needed?
- What is one prediction sample?
- What is the target?
- When is the prediction made?
- Which features are available at that moment?
- What is the cost of errors?
- What simple baseline can be compared?

An ambiguous target can make even technically correct code useless. “Predict churn” must define which customers, which time horizon, and what event counts as churn.

## 2. A valid build sequence
1. Inspect schema, missingness, duplicates, class balance and target.
2. Split data according to the deployment setting (random, stratified, grouped or time-aware).
3. Establish a baseline.
4. Put imputation, encoding, scaling and model in a Pipeline.
5. Compare configurations with validation/CV on development data.
6. Record metrics and inspect false/large-error cases.
7. Make model choices, then measure final performance on untouched test data.
8. Fit the final pipeline using the allowed development data, document the final test result, then persist the chosen pipeline.
9. Define the exact input columns/order/types for inference.
10. Monitor for changing data distributions and update the model only using a controlled procedure.

## 3. Persist preprocessing with the model
Saving only a classifier while forgetting the scaler or encoder can make later predictions wrong or impossible. Saving a complete Pipeline preserves the learned preprocessing and estimator together. Model files should be loaded only from trusted sources, because pickle/joblib based formats can execute code during loading.

## 4. Acceptance checklist
- [ ] A problem/target statement exists.
- [ ] Every input is available at prediction time.
- [ ] Split and random seed/group/time logic are documented.
- [ ] Preprocessing fits only within training folds.
- [ ] Baseline and selected model are compared fairly.
- [ ] Metrics align with the task/cost of mistakes.
- [ ] Error analysis and limitations are documented.
- [ ] The fitted pipeline is saved and can be loaded for inference.
- [ ] Feature schema and package requirements are documented.
