# Lesson 10.3 — Principal Component Analysis (PCA)

## 1. Why reduce dimensions?
A dataset can have many features, some correlated. PCA creates new axes (principal components) that are orthogonal directions capturing decreasing amounts of variance in the data. A projection onto the first few components can provide a compact representation for visualisation or preprocessing.

PCA is unsupervised: it does not use target labels to choose directions. A component capturing the most variance is not guaranteed to be the most predictive for a target.

## 2. Intuition
If points lie close to a diagonal line in a two-feature plot, much of their variation may be summarised by one direction along that line. PCA rotates the coordinate system toward directions that capture variance, then projects values onto selected directions.

Typical steps include centering features, computing a decomposition of their covariance/data matrix, ranking components by explained variance, and projecting onto the selected components. Scaling before PCA is often useful when numeric features have different units; the decision depends on the problem.

## 3. Example
```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

iris = load_iris()
pca_model = make_pipeline(
    StandardScaler(),
    PCA(n_components=2),
)
X_2d = pca_model.fit_transform(iris.data)
pca = pca_model.named_steps["pca"]
print("New shape:", X_2d.shape)
print("Explained variance ratios:", pca.explained_variance_ratio_.round(3))
print("Total shown variance:", round(pca.explained_variance_ratio_.sum(), 3))
```

This transforms 4 Iris features into 2 components. The explained variance ratio indicates the fraction of variance captured by each component under the fitted representation; it is not a classification accuracy measure.

## 4. Limitations
- Components may be difficult to interpret as individual real-world features.
- Variance is not identical to predictive information.
- Results depend on scaling and training data.
- When supervised target information matters, feature selection/model evaluation should be carried out with a leakage-safe pipeline.

## Practice
1. Does PCA use y labels to find its components?
2. Why might scaling come before PCA?
3. What does an explained variance ratio measure?
4. Does preserving 95% of variance guarantee 95% predictive accuracy?

**Answers:** no; to keep one large-scale feature from dominating distance/variance; the share of variance attributed to a component; no, variance retention and predictive performance are different.
