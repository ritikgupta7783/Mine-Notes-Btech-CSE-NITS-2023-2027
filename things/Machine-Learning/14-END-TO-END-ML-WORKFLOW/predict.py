"""Load the saved teaching pipeline and make one example prediction.

First run train_model.py in this folder to create the artifact.
Only load joblib/pickle artifacts from trusted sources.
"""
from pathlib import Path

import joblib
from sklearn.datasets import load_diabetes


ARTIFACT = Path(__file__).with_name("ridge_diabetes_pipeline.joblib")


def main():
    if not ARTIFACT.exists():
        raise FileNotFoundError(
            "Pipeline is missing. Run train_model.py first."
        )

    bundle = joblib.load(ARTIFACT)
    model = bundle["pipeline"]
    dataset = load_diabetes()
    example = dataset.data[[0]]
    prediction = model.predict(example)[0]

    print("Feature count:", len(bundle["feature_names"]))
    print("Predicted target:", round(float(prediction), 2))


if __name__ == "__main__":
    main()
