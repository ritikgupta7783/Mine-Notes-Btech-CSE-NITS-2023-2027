# Lesson 10.2 — Hierarchical Clustering and DBSCAN

## Hierarchical clustering
Hierarchical methods build nested groupings. In agglomerative clustering, each sample starts alone and the algorithm repeatedly merges clusters according to a linkage rule. The result can be shown as a dendrogram. Linkage defines cluster-to-cluster distance (e.g. single, complete or average), and the choice changes the grouping.

Strength: the hierarchy can be inspected at several cuts. Limitations: naïve implementations can be expensive and results depend on distance, linkage and cut choice.

## DBSCAN
DBSCAN groups dense regions and marks points in sparse regions as noise/outliers under its density rules. Key parameters:
- eps: neighbourhood radius.
- min_samples: minimum number of nearby samples required to call a point a core point under the library's definition.

DBSCAN can find irregularly shaped clusters and does not require specifying the cluster count in advance, but a single density threshold may struggle when clusters have very different densities. Scaling and a suitable distance measure still matter.

## Code comparison
```python
from sklearn.datasets import make_moons
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler

X, _ = make_moons(n_samples=200, noise=0.08, random_state=42)
X_scaled = StandardScaler().fit_transform(X)

hierarchical_labels = AgglomerativeClustering(
    n_clusters=2, linkage="ward"
).fit_predict(X_scaled)
dbscan_labels = DBSCAN(eps=0.25, min_samples=5).fit_predict(X_scaled)

print("Hierarchical labels:", len(set(hierarchical_labels)))
print("DBSCAN labels including noise:", sorted(set(dbscan_labels)))
```

DBSCAN assigns -1 to noise points. Its number of output labels may include that noise label. The exact outcome depends on the dataset and parameters; run the code to inspect results rather than treating the displayed model design as universal.

## Questions and practice
1. Does hierarchical clustering require choosing a cut to get final flat clusters? Yes, when you want a flat partition.
2. What does DBSCAN label -1 mean in scikit-learn? Noise/unassigned as a density cluster under the chosen settings.
3. Why can DBSCAN fail with very different cluster densities? One eps may not fit every region.
4. How does agglomerative clustering differ from K-means? It merges clusters hierarchically rather than iterating centroid assignments.

Try changing eps from 0.25 to 0.1 and 0.5 and explain what changes; do not interpret every parameter setting as better or worse without inspecting the result.
