"""Leakage-safe preprocessing demonstration with scikit-learn.

Install: python -m pip install pandas scikit-learn
This uses a tiny synthetic dataset for learning, not for meaningful benchmarking.
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main():
    data = pd.DataFrame({
        "age": [22, 31, 25, 45, 52, 28, 39, 33, 48, 23, 41, 56],
        "income": [30, 55, None, 80, 90, 38, 65, 52, 88, 32, 72, 95],
        "channel": [
            "web", "store", "web", "store", "web", "app",
            "app", "store", "web", "app", "store", "web",
        ],
        "churn": [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    })

    X = data[["age", "income", "channel"]]
    y = data["churn"]
    X_train, X_test, y_train, _ = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocess = ColumnTransformer([
        ("numeric", numeric_pipeline, ["age", "income"]),
        ("categorical", categorical_pipeline, ["channel"]),
    ])
    model = Pipeline([
        ("preprocess", preprocess),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    model.fit(X_train, y_train)
    print("Train rows:", len(X_train))
    print("Test rows:", len(X_test))
    print("First prediction:", int(model.predict(X_test.iloc[[0]])[0]))


if __name__ == "__main__":
    main()
