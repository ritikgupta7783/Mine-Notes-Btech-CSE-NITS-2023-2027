# Algorithm 09.1 — Simple Linear Regression

## Prerequisites
- [Functions and line equations](../05-MATHEMATICS-FOR-ML/01-functions-equations-and-graphs.md)
- [Vectors and shapes](../05-MATHEMATICS-FOR-ML/02-vectors-matrices-and-dimensions.md)
- [Loss and train/test splits](../07-ML-FUNDAMENTALS/01-training-loss-and-splits.md)

## 1. Beginner intuition
Suppose we want to estimate a house's price from its area. Simple linear regression tries to describe the relationship with a straight line. It chooses a slope and intercept so the line fits the training examples according to a chosen criterion, commonly squared error.

The line will not necessarily pass through every point. Real-world values vary, other variables may matter, and measurement noise exists.

## 2. Model and formula
\[
\hat y=wx+b
\]
x is the one input feature, ŷ the predicted target, w the slope/weight and b the intercept/bias.

For example, with w=2 and b=20, x=50 gives ŷ=2×50+20=120. These values are assumed for arithmetic practice; training is needed to estimate them from actual samples.

Mean squared error:
\[
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]
A common fitting objective is to find w and b that minimise this quantity on training data. Some libraries use numerical optimisation or specific solvers; the exact implementation depends on the estimator.

## 3. Fit an educational model from scratch
For one feature with nonzero variance, ordinary least squares has closed-form slope and intercept:
\[
w=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b=\bar y-w\bar x
\]
These formulas give the least-squares line for a single predictor. If all x values are identical, the denominator is zero and slope cannot be calculated from this expression.

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([3.0, 5.0, 7.0, 9.0])

x_mean = x.mean()
y_mean = y.mean()
weight = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
bias = y_mean - weight * x_mean

print("weight:", weight)
print("bias:", bias)
print("prediction for x=5:", weight * 5 + bias)
```

**Output**
```text
weight: 2.0
bias: 1.0
prediction for x=5: 11.0
```

The examples lie exactly on y=2x+1, so the fitted line recovers those values. Real data rarely has perfect alignment.

## 4. scikit-learn version
```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5], [6]], dtype=float)
y = np.array([3, 5, 7, 9, 11, 13], dtype=float)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("slope:", round(model.coef_[0], 3))
print("intercept:", round(model.intercept_, 3))
print("MAE:", mean_absolute_error(y_test, predictions))
```

The dataset lies on a line, so predictions can be exact apart from floating-point rounding, but split details and solver behaviour should be inspected if you compare output across environments. fit learns parameters; predict applies them; MAE calculates average absolute held-out error.

## 5. Strengths and weaknesses
**Strengths:** simple baseline, fast, coefficients are often interpretable, works well when a roughly linear relationship is adequate.
**Weaknesses:** sensitive to outliers under squared-error fitting; a single straight line may miss nonlinear patterns; coefficients can be unstable with highly correlated features in multiple regression; extrapolation beyond the observed data range can be unreliable.

## 6. Hyperparameters and diagnostics
Ordinary LinearRegression has fewer prominent tuning parameters than regularised models. Model choice still involves feature selection, preprocessing and validation procedure. Inspect a scatter plot, residuals, MAE/RMSE and whether errors vary systematically with input.

## Questions a beginner might ask
**Why called regression?** It estimates a numeric outcome in this common usage; the term has a historical statistical origin.  
**What does slope mean?** The predicted change per one-unit x increase in a one-feature linear model.  
**Why square errors?** Squaring keeps errors non-negative and penalises large misses more strongly, and it gives convenient mathematical properties. It also makes outliers influential.  
**Can correlation make a feature a cause?** No. A predictive association alone is not causal evidence.

## Practice
1. For ŷ=3x+4, predict x=2.
2. What happens to MSE if one residual changes from 2 to 4 while all other errors are fixed?
3. Fit the equation for x=[1,2,3], y=[3,5,7] by inspection.
4. Name two checks beyond training score.

**Answers:** 10; that contribution to the squared-error sum changes from 4 to 16; slope 2 and intercept 1; evaluate held-out performance and inspect residuals/data assumptions.
