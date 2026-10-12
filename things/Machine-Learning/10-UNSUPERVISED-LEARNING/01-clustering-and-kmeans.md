# Lesson 10.1 — Clustering and K-means

## 1. What is clustering?
Clustering groups samples by similarity without given class labels. It is useful for exploratory analysis, such as finding rough customer groups or identifying patterns in sensor data. The algorithm's definition of similarity determines what “near” or “similar” means.

## 2. K-means steps
K-means is typically described with four repeating steps:
1. Choose the number of clusters K and initialise K centroids.
2. Assign each sample to its nearest centroid.
3. Recalculate each centroid as the mean of the samples assigned to it.
4. Repeat assignment and update until the assignments/centroids stabilise or a stopping rule is reached.

It minimises within-cluster squared distances locally; different initialisations can give different results. K-means tends to work best when groups can be represented by centroids and roughly compact Euclidean clusters; it struggles with some non-spherical shapes, varying density and strong outliers.

## 3. Code
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score

X, _ = make_blobs(
    n_samples=300, centers=3, cluster_std=1.2, random_state=42
)
model = make_pipeline(
    StandardScaler(),
    KMeans(n_clusters=3, n_init=10, random_state=42),
)
labels = model.fit_predict(X)
scaled_X = model.named_steps["standardscaler"].transform(X)
print("Number of assigned clusters:", len(set(labels)))
print("Silhouette:", round(silhouette_score(scaled_X, labels), 3))
```

This synthetic example creates three centres, so using K=3 is known by construction. Real data rarely tells you the correct K. Silhouette compares how close a sample is to its own cluster versus other clusters; higher is generally better under this metric but does not prove that the groups are meaningful.

## 4. Scaling and choosing K
Because K-means relies on Euclidean distances, a large-scale feature can dominate centroid assignment. Fit scaling on the data being analysed as part of a defined workflow. The elbow method plots the clustering objective for different K and searches for a point where improvements slow. The elbow may be ambiguous and should not be treated as a guaranteed truth.

## 5. Common mistakes
- Treating cluster labels 0,1,2 as meaningful ordered classes.
- Comparing unscaled features with very different units without justification.
- Assuming a cluster number chosen visually is objectively correct.
- Ignoring random initialisation.
- Interpreting clusters causally.
- Evaluating clusters using class accuracy when no ground-truth labels exist.

## Practice
1. Why update a centroid after assigning samples?
2. Why run multiple initialisations?
3. Why isn't cluster id 2 “more” than cluster id 1?
4. What is the silhouette score trying to capture?

**Answers:** to reflect the current members' mean; the objective can converge to different local solutions; labels are arbitrary identifiers; a sample's within-cluster closeness compared with separation from other clusters.
