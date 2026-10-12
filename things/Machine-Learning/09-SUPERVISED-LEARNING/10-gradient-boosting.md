# Algorithm 09.10 — Gradient Boosting

## 1. Intuition
Gradient boosting builds an additive model in stages. A new weak learner (often a shallow tree) focuses on improving the current model's errors according to a loss/gradient. The final prediction combines contributions from many learners.

Unlike a random forest, whose trees are typically fitted with bootstrap randomness and combined in parallel-style aggregation, boosting builds learners sequentially so each stage responds to the current model.

## 2. Why it can work well
Many small corrections can represent complex nonlinear patterns. But sequential fitting, learning rate, tree depth and number of estimators must be controlled to avoid overfitting. Boosting is a powerful family, not a guarantee of the best score on every dataset.

## 3. Introductory example
```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42
)
model = HistGradientBoostingRegressor(
    max_iter=100, learning_rate=0.1, max_leaf_nodes=15, random_state=42
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
```

This demonstrates fitting and held-out evaluation on scikit-learn's built-in diabetes dataset. It does not imply a medical decision tool or clinical suitability; dataset and metric context matter.

## 4. Important hyperparameters
- learning_rate: scales each boosting stage's contribution. Smaller values often need more stages.
- max_iter / n_estimators: number of boosting stages.
- tree depth or max_leaf_nodes: complexity of each weak learner.
- regularisation and early stopping settings where supported.
- loss: defines the objective; choose it for the target and task.

## 5. Compare methods
- Single tree: simple to inspect, but often unstable/high variance.
- Random forest: combines many independently grown/randomised trees, commonly reduces variance.
- Gradient boosting: grows learners sequentially to correct the current model, often can reduce bias but needs careful tuning.

## Practice
1. Why are boosting learners trained sequentially?
2. What is the typical trade-off with a lower learning rate?
3. How does a random forest differ in overall training strategy?
4. Why evaluate against a baseline?

**Answers:** each learner responds to current errors/gradients; slower progress may require more stages; forest trees are fit with randomisation and combined rather than each sequentially correcting the current model; score comparison establishes whether the complexity helps.
