"""Small, self-contained Pandas example.
Install: python -m pip install pandas
Run: python pandas_basics.py
"""

import pandas as pd


def main():
    data = pd.DataFrame({
        "area": [50, 70, 90, 110],
        "bedrooms": [1, 2, 3, 3],
        "price": [120, 165, 215, 250],
    })

    print("Shape:", data.shape)
    print("Average price:", data["price"].mean())

    X = data[["area", "bedrooms"]]
    y = data["price"]
    print("X columns:", list(X.columns))
    print("X shape:", X.shape)
    print("y shape:", y.shape)

    larger_houses = data.loc[data["area"] >= 90, ["area", "price"]]
    print("Large houses:", larger_houses.to_dict("records"))


if __name__ == "__main__":
    main()
