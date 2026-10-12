# Lesson 13.2 — Hyperparameter Tuning, Cross-validation and Learning Curves

## Grid search and randomized search
GridSearchCV evaluates combinations from a specified parameter grid using cross-validation. RandomizedSearchCV samples configurations from defined distributions/lists and can be more efficient when many settings exist. Both can overfit the validation procedure if choices and repeated experimentation become too adaptive; reserve a final test set.

## Pipeline-aware tuning
Place data preprocessing and the estimator in one Pipeline, then tune parameters in that pipeline. Parameter names often use double underscores, such as classifier__C. This lets cross-validation refit all preprocessing only on each fold's training portion.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25,
    random_state=42, stratify=data.target
)

pipeline = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(max_iter=2000)),
])
search = GridSearchCV(
    pipeline,
    param_grid={"model__C": [0.01, 0.1, 1.0, 10.0]},
    cv=5,
    scoring="roc_auc",
)
search.fit(X_train, y_train)

print("Best parameters:", search.best_params_)
print("Best CV ROC-AUC:", round(search.best_score_, 3))
print("Held-out accuracy:", round(search.best_estimator_.score(X_test, y_test), 3))
```

The best parameter and scores are computed from the run. The test accuracy shown is a separate final metric, and the model selection used ROC-AUC; this illustrates that the scoring objective and final reporting metric can differ. A real workflow should predefine which metrics matter and avoid choosing settings based on repeated test inspections.

## Learning and validation curves
- A **learning curve** studies metric performance as training-set size changes.
- A **validation curve** studies performance as a hyperparameter changes.

If train and validation scores are both poor, capacity/features/data quality or training may be insufficient. If train is much better than validation, high variance/overfitting is possible. Interpret curves based on whether the metric is maximised or minimised.

## Practice
1. Why tune inside a Pipeline?
2. When may randomized search be useful?
3. What do learning curves reveal?
4. Why is a fixed test score not the only criterion for model choice?

**Answers:** prevents preprocessing leakage across folds; large search spaces; data quantity vs fit/generalisation patterns; complexity, stability, metric trade-offs and practical limitations matter.
