# Module 08 — Data Preprocessing

**Prerequisites:** Pandas, statistics, splitting and data-leakage lessons.  
**Goal:** turn raw columns into model-ready features without accidentally letting test information influence training.

## Lessons
1. [Missing values, encoding and feature scaling](01-imputation-encoding-scaling.md)
2. [Pipelines, ColumnTransformer and leakage-safe fitting](02-pipelines-and-no-leakage.md)
3. [Runnable scikit-learn workflow](preprocessing_pipeline.py)

## The order matters
First define the target and the inputs, then split data. Fit data-dependent steps—imputation statistics, scaling parameters, encoders and feature selection—using training data only. Apply the fitted transformations to held-out data. Pipelines make this sequence reproducible and reduce accidental leakage.

## When scaling matters
Scaling is important for distance-based methods such as KNN and K-means and often helpful for gradient-based/regularised models. Ordinary decision trees split on feature thresholds and generally do not need standard scaling, though data quality and encodings still matter.

## Checkpoint
- Explain imputation, categorical encoding, standardisation and min-max scaling.
- Distinguish fit_transform on training data from transform on held-out data.
- Use a Pipeline and ColumnTransformer.
- Explain why a missing target is not treated like a normal missing feature.
