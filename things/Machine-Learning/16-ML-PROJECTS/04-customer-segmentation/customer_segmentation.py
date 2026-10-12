"""Project 4: reproducible synthetic customer segmentation."""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    X, _ = make_blobs(
        n_samples=240,
        centers=[[-2, -1], [0, 2], [2, -1]],
        cluster_std=0.8,
        random_state=42,
    )
    data = pd.DataFrame(X, columns=["annual_spend_index", "visits_index"])

    pipeline = make_pipeline(
        StandardScaler(),
        KMeans(n_clusters=3, n_init=10, random_state=42),
    )
    labels = pipeline.fit_predict(data)
    scaled_data = pipeline.named_steps["standardscaler"].transform(data)
    score = silhouette_score(scaled_data, labels)

    print("Cluster counts:", pd.Series(labels).value_counts().sort_index().to_dict())
    print("Silhouette:", round(float(score), 3))

    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=labels)
    plt.xlabel("Annual spend index (synthetic)")
    plt.ylabel("Visits index (synthetic)")
    plt.title("K-means clusters on synthetic data")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
