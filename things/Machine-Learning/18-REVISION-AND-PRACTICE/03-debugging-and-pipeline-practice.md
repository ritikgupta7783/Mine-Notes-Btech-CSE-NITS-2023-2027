# Revision Set 18.3 — Debugging and Pipeline Practice

Identify the issue, explain the mechanism and propose a fix.

## A. Target in X
```python
X = df[["age", "income", "churn"]]
y = df["churn"]
```

## B. Full-data scaling
```python
X_scaled = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

## C. Wrong regression metric
A team reports only classification accuracy for predicting a patient's waiting time in minutes.

## D. Text vectorisation leakage
A CountVectorizer is fit on all messages before train/test split.

## E. Class imbalance
A classifier is evaluated on data where 98% of labels are negative. It predicts every example as negative and reports 98% accuracy.

## F. Overfit tree
A deep tree achieves zero training error but large validation error. The team increases max_depth again, hoping for improvement.

## G. Correlation claim
A report says “customers with feature A churn more often, so changing A will cause churn.” No experimental or causal analysis was done.

## H. Random split in a forecasting task
To predict outcomes in a future month, the team randomly mixes all years into train and test. Some of the newest records are in training.

## I. Pipeline mismatch
Training code standardises features, but inference code feeds raw values directly to a saved estimator.

## J. Unseen categories
An encoder raises an error when a new category appears. The team wants to silently label it as the most common known category without logging the event.

For each item, describe:
1. The problem.
2. Why it matters.
3. A corrected workflow.
4. One test/check that would verify the change.
