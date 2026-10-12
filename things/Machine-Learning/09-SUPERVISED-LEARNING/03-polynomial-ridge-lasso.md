# Algorithm 09.3 — Polynomial Features, Ridge and Lasso

## Polynomial regression intuition
A straight line may not capture a curved pattern. Polynomial regression creates derived features such as x², then fits a linear model on the expanded feature set:
\[
\hat y=b+w_1x+w_2x^2
\]
It remains linear in the unknown coefficients even though the relationship to x is curved. Higher degrees can fit training data closely but also overfit.

## Regularisation
When there are many features or correlated columns, ordinary least squares can fit unstable coefficients. Regularisation adds a penalty to reduce complexity.

- **Ridge (L2):** penalises the sum of squared coefficients. Coefficients are pushed toward zero but typically not exactly zero.
- **Lasso (L1):** penalises the sum of absolute coefficients. It can drive some coefficients to exactly zero, behaving as a form of feature selection under suitable conditions.

A simplified objective view:
\[
J=\text{data loss}+\alpha\times\text{penalty}
\]
α controls the trade-off. The exact intercept/penalty handling is implementation-specific.

## Code
```python
from sklearn.linear_model import Ridge, Lasso
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Example data: output rises approximately with a curved pattern.
X = [[0], [1], [2], [3], [4], [5]]
y = [1, 2, 5, 10, 17, 26]

poly_ridge = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    StandardScaler(),
    Ridge(alpha=1.0),
)
poly_ridge.fit(X, y)
print(round(poly_ridge.predict([[6]])[0], 2))
```

This is an educational example. The predicted value should be examined against held-out evidence and domain constraints, not accepted just because the curve visually fits these points.

## When to use
Polynomial features can express curvature, but degree must be chosen with validation. Ridge/Lasso help control coefficient size; features should often be scaled for regularised linear models. Fit scaling and polynomial transformations inside a pipeline after splitting.

## Practice
1. What additional feature allows x² curvature?
2. How do Ridge and Lasso penalties differ?
3. Can higher polynomial degree increase overfitting?
4. Why put the scaler inside a pipeline?

**Answers:** x squared; squared coefficients versus absolute coefficients; yes; to fit only on training folds/samples and apply consistent transformations without leakage.
