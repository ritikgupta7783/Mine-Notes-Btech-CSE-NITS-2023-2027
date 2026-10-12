# Lesson 13.1 — Baselines and Error Analysis

## 1. Why begin with a baseline?
A baseline is a simple reference method with a known rule. It tells us whether a more complex model adds value. For regression, DummyRegressor can predict a mean or median; for classification, DummyClassifier can use simple class-frequency rules.

## 2. Inspect errors, not only the overall score
For numeric predictions, inspect residuals, absolute error by target range and error by useful subgroup. For classification, inspect false positives and false negatives. A model may have a respectable average metric while systematically failing on an important group or region.

## 3. Example: mean baseline
```python
from sklearn.datasets import load_diabetes
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42
)
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)
baseline_pred = baseline.predict(X_test)

model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
model.fit(X_train, y_train)
model_pred = model.predict(X_test)

print("Baseline MAE:", round(mean_absolute_error(y_test, baseline_pred), 2))
print("Ridge MAE:", round(mean_absolute_error(y_test, model_pred), 2))
```

Run this comparison to record the actual values in your environment. Do not assume Ridge must win; the split and data characteristics determine the result. The same test split is used for comparison here for a teaching demonstration, but repeated tuning should happen with validation/cross-validation rather than choosing a model from the test set.

## 4. Form hypotheses
Example: “Large error for high-price houses may occur because the linear model cannot represent a curved relationship.” A reasonable experiment may compare a polynomial or tree model under the same development split and metric. It is not enough to try many approaches and report only the winner without noting comparisons and validation method.

## Practice
1. Why is a baseline required?
2. Give one error analysis for a false-negative fraud case.
3. What would you record in an experiment log?
4. Why should the held-out test score not be used repeatedly to make changes?

**Answers:** establishes reference value; inspect transaction features/threshold and fraud costs; hypothesis, change, split/seed, metric, score, trade-offs and notes; repeated adaptation overfits the test set.
