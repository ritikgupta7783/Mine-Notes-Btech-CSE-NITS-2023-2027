"""Project 2: simple house-price regression on synthetic data only."""

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main():
    rng = np.random.default_rng(10)
    n = 200
    area = rng.uniform(35, 180, n)
    bedrooms = rng.integers(1, 6, n)
    age = rng.integers(0, 50, n)
    noise = rng.normal(0, 15, n)
    price = 3.0 * area + 8.0 * bedrooms - 0.7 * age + 40 + noise

    data = pd.DataFrame({
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "price": price,
    })
    X = data[["area", "bedrooms", "age"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)
    base_pred = baseline.predict(X_test)

    model = Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=1.0)),
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("Baseline MAE:", round(mean_absolute_error(y_test, base_pred), 2))
    print("Ridge MAE:", round(mean_absolute_error(y_test, pred), 2))
    print("Ridge RMSE:", round(mean_squared_error(y_test, pred) ** 0.5, 2))


if __name__ == "__main__":
    main()
