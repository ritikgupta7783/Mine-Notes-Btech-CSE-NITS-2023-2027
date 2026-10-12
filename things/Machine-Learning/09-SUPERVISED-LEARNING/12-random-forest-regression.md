# Algorithm 09.12 — Random Forest Regression

## Intuition
A random forest regressor combines predictions from many regression trees. Training uses samples/features randomisation to create diversity; predictions are generally averaged. This can reduce the high variance of one decision tree while preserving nonlinear feature interactions.

## Example
```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42
)
model = RandomForestRegressor(
    n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=-1
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
```

The metric is produced at runtime. Use the same development split/metric as a baseline and alternative models when comparing. Do not report a performance gain unless it was actually measured.

## Hyperparameters
- n_estimators: number of trees.
- max_depth: maximum tree depth.
- min_samples_leaf: minimum observations in a leaf.
- max_features: number/proportion of features considered at a split, according to supported settings.
- random_state: repeatability of randomised fitting.

## Strengths and limitations
It can capture nonlinear interactions and usually doesn't require standard scaling. It consumes more memory/compute than one small tree and is less directly interpretable. Impurity-based feature importance has limitations and does not establish causality. Tree averaging does not naturally extrapolate numeric trends well outside the training target range.

## Questions
1. Why can a forest outperform one tree? Averaging diverse trees can reduce variance.
2. Why can more trees cost more without fixing bad features? They increase compute/memory but can't remove target leakage or irrelevant data.
3. Does feature importance imply cause? No.
4. Why compare to a mean baseline? To test whether extra complexity adds value.
