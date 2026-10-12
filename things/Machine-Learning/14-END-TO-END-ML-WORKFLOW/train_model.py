"""Train and save a reproducible starter ML pipeline.

Uses the bundled scikit-learn diabetes dataset; no dataset download is needed.
This is a regression teaching example, not a medical decision model.

Install: python -m pip install scikit-learn joblib
Run from this folder: python train_model.py
"""
from pathlib import Path

import joblib
from sklearn.datasets import load_diabetes
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ARTIFACT = Path(__file__).with_name("ridge_diabetes_pipeline.joblib")


def main():
    dataset = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.25,
        random_state=42,
    )

    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)

    pipeline = Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=1.0)),
    ])
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    print("Baseline MAE:", round(mean_absolute_error(y_test, baseline_predictions), 2))
    print("Ridge MAE:", round(mean_absolute_error(y_test, predictions), 2))
    print("Ridge RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 2))

    joblib.dump({
        "pipeline": pipeline,
        "feature_names": dataset.feature_names.tolist(),
        "target_description": dataset.DESCR.splitlines()[0],
    }, ARTIFACT)
    print("Saved fitted pipeline to:", ARTIFACT.name)


if __name__ == "__main__":
    main()
