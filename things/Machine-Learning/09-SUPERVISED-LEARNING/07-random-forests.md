# Algorithm 09.7 — Random Forests

## 1. Intuition
A Random Forest combines many decision trees. Trees are trained on bootstrap samples (resampled training rows) and use random subsets of features for split choices under typical implementations. Classification combines votes/probabilities; regression averages tree predictions. The goal is to reduce the instability of a single tree and improve predictive performance.

## 2. Why an ensemble can help
One decision tree can change significantly when training records change. Averaging a collection of diverse trees can reduce variance. More trees cost more memory and inference time, and do not guarantee a better result on every dataset.

## 3. scikit-learn example
```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)
model = RandomForestClassifier(
    n_estimators=200, max_depth=None, random_state=42, n_jobs=-1
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions, target_names=data.target_names))
```

This uses a built-in public teaching dataset and a fixed split seed. Run it to obtain the installed-version report; the numbers are not a general guarantee or benchmark for other populations.

## 4. Important hyperparameters
- n_estimators: number of trees. More trees can stabilise predictions but increase cost.
- max_depth and min_samples_leaf: constrain each tree's complexity.
- max_features: how many features are considered at a split under the supported setting.
- class_weight: can adjust the fitting objective for imbalanced classes.
- random_state: helps reproduce the stochastic process under the same environment.

## 5. Interpretation and limitations
Random forests often work well on tabular data and need little feature scaling, but they may be less naturally interpretable than one small tree or a linear model. Built-in impurity feature importance can favour features with many potential split points and may be misleading with correlated features. Use held-out permutation importance or other appropriate methods when interpretability matters, while remembering that importance is model-dependent and not a causal effect.

## Practice
1. How does a random forest differ from one decision tree?
2. Why can averaging help?
3. Name two parameters that control tree complexity.
4. Does feature importance prove causation?

**Answers:** ensemble of varied trees vs one tree; it can reduce variance; max_depth and min_samples_leaf; no.
