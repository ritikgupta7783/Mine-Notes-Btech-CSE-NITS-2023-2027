"""Project 1: student score regression with reproducible synthetic data."""

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main():
    rng = np.random.default_rng(42)
    n = 120
    practice_questions = rng.integers(0, 101, size=n)
    previous_score = rng.integers(30, 96, size=n)
    noise = rng.normal(0, 5, size=n)
    final_score = np.clip(
        0.35 * practice_questions + 0.55 * previous_score + noise,
        0,
        100,
    )

    data = pd.DataFrame({
        "practice_questions": practice_questions,
        "previous_score": previous_score,
        "final_score": final_score,
    })
    X = data[["practice_questions", "previous_score"]]
    y = data["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)
    baseline_pred = baseline.predict(X_test)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Dataset rows:", len(data))
    print("Feature columns:", list(X.columns))
    print("Baseline MAE:", round(mean_absolute_error(y_test, baseline_pred), 2))
    print("Linear regression MAE:", round(mean_absolute_error(y_test, predictions), 2))
    print("Linear regression RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 2))


if __name__ == "__main__":
    main()
