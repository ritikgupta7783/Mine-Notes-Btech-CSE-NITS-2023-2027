# Algorithm 09.5 — K-Nearest Neighbours (KNN)

## Prerequisites
- [Distance and similarity](../05-MATHEMATICS-FOR-ML/04-distance-logarithms-sigmoid.md)
- [Scaling](../08-DATA-PREPROCESSING/01-imputation-encoding-scaling.md)
- [Classification metrics](../11-MODEL-EVALUATION/02-classification-metrics.md)

## 1. Intuition
KNN predicts using nearby training examples. For regression it may average the targets of the nearest samples; for classification it often uses majority vote. It is called a non-parametric or instance-based method because it stores training examples rather than fitting a small fixed set of coefficients in the usual linear-model way.

## 2. Tiny numerical example
Training samples on a one-dimensional feature:
- x=1 -> class A
- x=2 -> class A
- x=8 -> class B

For query x=2.5 and k=3, distances are 1.5, 0.5 and 5.5. The nearest three include two A samples and one B, so majority vote predicts A. With k=1 the nearest is x=2, also A. Tie handling depends on implementation and classes; inspect how your library resolves ties.

## 3. Fit with scikit-learn
```python
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=300, noise=0.18, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
```

The score is computed at runtime on a synthetic dataset; do not assume a fixed performance number without running the script in your environment. Scaling occurs inside the pipeline to avoid fitting means/scales on the test data.

## 4. Important hyperparameters
- k / n_neighbors: small k can be sensitive to noise; large k smooths the decision boundary and can underfit.
- Distance metric: Euclidean and Manhattan distance behave differently.
- weights: uniform voting vs giving closer neighbours more influence.
- p in Minkowski distance where supported: p=1 is Manhattan, p=2 Euclidean.
- Feature scaling and meaningful feature design are crucial.

## 5. Strengths and weaknesses
**Strengths:** intuitive, can model nonlinear boundaries, little explicit training time.  
**Weaknesses:** prediction can be expensive with large datasets, memory use grows with training set, distance is less meaningful in high dimensions, and irrelevant/unscaled features can dominate.

## Questions a beginner might ask
**Why is KNN called lazy learning?** Most work is deferred until a query arrives.  
**Does KNN have a training step?** Libraries store/validate training data during fit, even if no complex parameters are learned.  
**Why do scales matter?** Distance adds differences numerically; a large-range feature can dominate.

## Practice
1. A 3-neighbour vote has labels A,A,B. What class wins?
2. What can go wrong with k=1?
3. Why fit a scaler in the training pipeline?
4. Why can KNN become slow at inference?

**Answers:** A; it may be sensitive to a noisy nearest sample; prevents data leakage and ensures a consistent transformation; it may calculate distances to many stored samples per query.
