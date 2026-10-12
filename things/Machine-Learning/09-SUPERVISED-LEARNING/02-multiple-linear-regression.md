# Algorithm 09.2 — Multiple Linear Regression

## What changes from simple regression?
Simple regression uses one feature. Multiple linear regression uses several features to predict one numeric target. The model adds the weighted feature contributions:
\[
\hat y=w_1x_1+w_2x_2+\dots+w_px_p+b
\]
x_j is the j-th feature, w_j its coefficient, and b the intercept. In vector notation: ŷ = x·w + b.

## Small numerical example
Suppose a score model is ŷ = 5×practice_hours + 2×previous_score + 10. For practice_hours=4 and previous_score=70:
- Practice contribution = 5×4=20.
- Previous-score contribution = 2×70=140.
- Add intercept 10.
- Prediction = 170. This is only arithmetic practice, not a realistic score scale or a trained model.

## Fit with scikit-learn
```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [1, 50],
    [2, 55],
    [3, 65],
    [4, 70],
    [5, 80],
], dtype=float)
y = np.array([52, 59, 68, 74, 83], dtype=float)

model = LinearRegression()
model.fit(X, y)
print("Number of coefficients:", len(model.coef_))
print("Prediction:", round(model.predict([[3, 70]])[0], 2))
```

The model learns one coefficient for each feature. On a tiny illustrative dataset, fitted coefficients can be unstable and this example is not an evaluation claim.

## Interpretation cautions
A coefficient represents the model's expected prediction change for a one-unit increase in that feature while other input features are held fixed. This is a conditional model interpretation, not proof of a causal effect. If features are strongly correlated, coefficients may be difficult to interpret and can vary with the training sample.

## Assumptions and limitations
- Relationship is linear in the supplied features and coefficients.
- Observations and residual patterns must be suitable for the intended inference/use.
- Outliers can strongly influence squared-error fitting.
- Collinearity can make coefficients unstable.
- Adding many irrelevant features can increase variance; regularisation or feature selection may help.

## Practice
1. Write a model with three features and intercept.
2. In a coefficient interpretation, what does “holding other features fixed” mean?
3. Why does a high coefficient not automatically mean the feature causes the target?
4. What evaluation setup helps estimate performance on new samples?

**Answers:** ŷ=w1x1+w2x2+w3x3+b; imagine varying one feature while keeping others constant in the model; association/confounding and data-generation issues remain; use a suitable train/validation/test or cross-validation procedure.
