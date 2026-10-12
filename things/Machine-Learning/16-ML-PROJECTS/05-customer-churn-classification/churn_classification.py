"""Project 5: imbalanced synthetic churn classification.

Synthetic data is for learning metric interpretation only.
"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    X, y = make_classification(
        n_samples=1200,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        weights=[0.9, 0.1],
        class_sep=0.8,
        random_state=42,
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(class_weight="balanced", max_iter=1000),
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
    print("Precision:", round(precision_score(y_test, predictions, zero_division=0), 3))
    print("Recall:", round(recall_score(y_test, predictions, zero_division=0), 3))
    print("F1:", round(f1_score(y_test, predictions, zero_division=0), 3))
    print("Confusion matrix (rows=true [0,1], cols=predicted [0,1]):")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))
    print(classification_report(y_test, predictions, zero_division=0))


if __name__ == "__main__":
    main()
