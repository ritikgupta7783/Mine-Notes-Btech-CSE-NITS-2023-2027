# Project 5 — Customer Churn Classification

**Task:** binary classification. **Skills:** imbalanced targets, preprocessing, logistic regression, confusion matrix, precision/recall/F1.

## Problem statement
Predict whether a customer will churn in a defined future window using features available before that window. In this demo, scikit-learn generates synthetic data with a minority positive class. It is not a real customer dataset and cannot support business decisions.

## Why not accuracy alone?
When positives are rare, a model that predicts all negatives can look accurate but miss the class we care about. Evaluate precision, recall, F1 and confusion matrix, then discuss the costs of false positives vs false negatives. Class weighting changes the learning objective and must be evaluated; it does not guarantee improvements.

## Run
Install: python -m pip install scikit-learn  
Run: python churn_classification.py

## Design and leakage
1. X contains only the generated input columns.
2. y is the churn label.
3. Split with stratify=y to preserve approximate class proportions.
4. Scaling and model fitting occur on training examples through a Pipeline.
5. Evaluate once on held-out test data.

## Questions
1. Why can accuracy be high while churn recall is low?
2. Which error is more costly—false positive or false negative—and who decides?
3. How could a threshold change precision and recall?
4. What is data leakage in churn prediction?
5. Why would a model trained on past churn data drift after customer/product changes?

## Extensions
- Change the data imbalance and compare metrics.
- Compare class_weight balanced vs none using validation.
- Choose a threshold based on a stated operational constraint.
- Inspect errors by customer subgroup and validate fairness/legal requirements before any real deployment.
