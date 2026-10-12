# Interview Set 17.3 — Scenario-Based ML Questions

## Scenario 1: Very high training score, low test score
**Likely issues:** overfitting, leakage that is present only in training, unrepresentative or incorrectly split data, train/test preprocessing mismatch, distribution shift.
**How to investigate:** validate split logic, compare cross-validation results, inspect learning curves/error slices, simplify or regularise model, and check features were available at prediction time.
**Avoid:** “just collect more data” without testing which hypothesis explains the gap.

## Scenario 2: 98% accuracy on a 1% fraud class
A trivial all-negative classifier achieves around 99% accuracy if prevalence is exactly 1%, so 98% may still be unusable. Examine fraud recall, precision, PR curve, confusion matrix and expected costs. Define the positive class and threshold. Consider class weighting/resampling only within training folds, then validate the result.

## Scenario 3: New data has an unseen category
Use a designed encoding strategy. OneHotEncoder(handle_unknown="ignore") can avoid an encoder error, but the new category is not magically understood. Monitor unknown-category rate, revisit feature policy and retrain with representative examples when appropriate.

## Scenario 4: KNN performs poorly
Check feature scaling, irrelevant/noisy features, selected distance, value of k, dimensionality, train sample size and split. Compare a baseline and tune k only on development data.

## Scenario 5: K-means produces strange clusters
Inspect feature units/scaling, outliers, choice of K, initialisation stability and whether Euclidean-centroid clusters fit the shape. Compare silhouette/inertia and visualise the data. Do not assume that every cluster is a meaningful customer persona.

## Scenario 6: Model score fell after deployment
Check input schema, data pipeline version, missingness, distribution drift, target/label delays and whether the serving pipeline matches training. Verify metrics on newly labelled outcomes before assuming the model itself is solely responsible.

## Scenario 7: Model must be explainable
First clarify who needs explanation and what decision is at stake. Consider an intrinsically simple model if it meets the task requirements. Otherwise use relevant explanation methods, test their stability and remember that feature attribution is not causal proof.

## Scenario 8: Choose a model for predicting next month's demand
Clarify forecast horizon, time of prediction, target and business cost. Use time-aware validation instead of a random split if future data must be predicted from past data. Build a seasonal or naïve baseline, compare appropriate numeric metrics, inspect errors by horizon/segment and avoid future-derived features.

## Scenario 9: A colleague wants to tune on the test set
Explain that repeated decisions based on test outcomes adapt to the test data. Use a validation set/cross-validation for selection and keep the final test for a one-time final evaluation.

## Scenario 10: One feature has huge importance
Check units, leakage, identifier/memorisation effects, correlated substitutes, calculation time and data quality. Compare validation stability and investigate whether the feature exists before the prediction moment. Importance doesn't prove causation.

## How to answer scenarios
State assumptions first, identify failure risks, propose one controlled test, specify the metric/split, and report what evidence would change your mind.
