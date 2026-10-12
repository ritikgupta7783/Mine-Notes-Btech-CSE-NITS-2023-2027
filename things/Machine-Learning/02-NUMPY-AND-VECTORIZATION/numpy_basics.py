"""Runnable NumPy basics example.

Install NumPy first:
    python -m pip install numpy
Run:
    python numpy_basics.py
"""

import numpy as np


def main():
    values = np.array([1, 2, 3])
    table = np.array([[1, 2, 3], [4, 5, 6]])

    print("Element-wise * 2:", values * 2)
    print("Vector shape:", values.shape)
    print("Table shape:", table.shape)
    print("Column sums:", table.sum(axis=0))
    print("Row sums:", table.sum(axis=1))

    feature_matrix = np.array([[1, 2], [3, 4], [5, 6]])
    weights = np.array([2, 10])
    predictions = feature_matrix @ weights
    print("Predictions:", predictions)


if __name__ == "__main__":
    main()
