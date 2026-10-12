# Lesson 07.1 — Training, Loss, Baselines and Data Splits

## 1. Training means fitting parameters
A supervised dataset has inputs X and known targets y. An estimator's fit(X, y) method uses the training examples to estimate model parameters. predict(X_new) applies the fitted mapping to new examples. fit() is not the same as predict().

A loss measures disagreement between a prediction and its target. For a numeric target, squared error (y−ŷ)² is a common per-example loss. An objective often averages losses over a dataset and may include a regularisation term.

## 2. Start with a baseline
Before trying a complicated model, build a simple reference prediction:
- For regression, predicting the training target mean is a common baseline.
- For classification, a most-frequent-class baseline can indicate how misleading accuracy may be on imbalanced labels.

A baseline answers: “Is the current model doing better than a simple approach under the same evaluation protocol?”

## 3. Why split the data?
- **Training set:** fit model parameters and data-dependent transformations.
- **Validation set:** compare model choices and hyperparameters during development.
- **Test set:** a final held-out estimate after decisions are finished.

For small datasets, cross-validation may be used on development data. Keep test data out of repeated model selection.

## 4. A split example

```python
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [3, 5, 7, 9, 11, 13, 15, 17]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print("Train samples:", len(X_train))
print("Test samples:", len(X_test))
```

**Output:** the split contains 6 training samples and 2 test samples. Which rows fall into each subset is controlled by the library's split algorithm and seed; inspect the values rather than relying on row order. For classification, consider stratify=y when class proportions should be maintained and the sample sizes permit it.

## 5. Parameters and hyperparameters
- **Parameters** are learned from training, e.g. slope/intercept in linear regression.
- **Hyperparameters** configure learning, e.g. tree maximum depth or number of neighbours in KNN. They are selected using validation/cross-validation, not the final test score.

## 6. Common failure patterns
- Great training score but poor validation score can indicate overfitting.
- Poor training and validation performance can indicate underfitting, data quality issues, or an unsuitable model/objective.
- A small difference between two scores may not be meaningful when evaluation variance is high.
- Train and test splits can be invalid if related entities or future data are distributed across sets incorrectly; time-based or group-aware splitting may be needed.

## Practice
1. What is the job of fit() vs predict()?
2. Why establish a baseline?
3. A complex model scores 100% train and 62% test. What would you inspect?
4. Which set should guide hyperparameter selection and why?

**Answers:** fit learns from examples; predict produces outputs; baseline checks value against a simple rule; inspect overfitting, leakage and data split; use validation/cross-validation rather than the final test set.
