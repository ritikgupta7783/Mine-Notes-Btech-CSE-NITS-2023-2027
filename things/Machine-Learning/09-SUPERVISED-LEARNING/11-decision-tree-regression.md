# Algorithm 09.11 — Decision Tree Regression

## What differs from a classification tree?
A regression tree predicts a numeric value at a leaf, often the mean of training targets that reached that leaf. It repeatedly divides feature space using thresholds, selecting splits that reduce a regression criterion such as squared error. It creates piecewise-constant predictions, not a smooth line.

## Example
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42
)
model = DecisionTreeRegressor(max_depth=3, min_samples_leaf=5, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
```

This is a regression task on scikit-learn's built-in diabetes dataset, used only for teaching. Run the script to get the metric for this split. A shallow depth and leaf minimum control complexity; do not infer medical suitability from the example.

## Strengths and limitations
A tree can model nonlinear interactions and is easy to explain when small. It can be unstable and overfit when deep. Predictions are piecewise constant and cannot naturally extrapolate a smooth trend beyond learned leaf values. Scaling usually is not required for standard numeric splits.

## Questions
1. What does a leaf predict in regression? A numeric summary learned from training targets in that leaf, often a mean under standard squared-error setup.
2. How does max_depth affect complexity? Larger depth permits more splits, potentially reducing train error but increasing overfit.
3. Why use a minimum leaf size? To prevent a leaf from being based on too few samples and reduce variance.
4. Why is held-out MAE required? Training performance alone doesn't estimate generalisation.
