# Lesson 11.1 — Regression Metrics

## 1. A tiny example
True values y=[3,5,7], predictions ŷ=[2,5,10]. Residuals (y−ŷ) are [1,0,−3]. A residual is an error under the chosen sign convention; metrics commonly use absolute/squared values so positive/negative errors don't simply cancel.

## 2. Mean Absolute Error (MAE)
\[
MAE=\frac{1}{n}\sum_i|y_i-\hat y_i|
\]
Absolute errors are [1,0,3], sum to 4, then divide by 3, so MAE = 1.333…. It tells the mean size of the miss in the target's original units.

## 3. Mean Squared Error (MSE) and RMSE
\[
MSE=\frac{1}{n}\sum_i(y_i-\hat y_i)^2
\]
Squared errors are [1,0,9], sum to 10, so MSE=10/3≈3.333. RMSE is square root of MSE, approximately 1.826. Because errors are squared, big errors receive extra weight. RMSE returns to the target's units.

## 4. R-squared
R² compares squared prediction error with the variation around the target mean under its formula. It is often described as the proportion of target variance accounted for relative to a mean baseline on the evaluated data. It can be negative on test data when the model performs worse than predicting the evaluated target mean, and it is not a universal percentage of “accuracy.”

## 5. Python
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = [3, 5, 7]
y_pred = [2, 5, 10]

print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mean_squared_error(y_true, y_pred))
print("R2:", round(r2_score(y_true, y_pred), 3))
```

**Output**
```text
MAE: 1.3333333333333333
MSE: 3.3333333333333335
R2: -0.25
```

The R² is negative for these values; predictions are worse than the mean baseline under the R² definition. RMSE can be calculated with mean_squared_error(... ) ** 0.5 for broad version compatibility, or with root_mean_squared_error in versions that provide it.

## Choosing between them
- Use MAE when the average absolute miss is easy to explain and you want less sensitivity to large residuals than squared error.
- Use RMSE when large misses deserve extra penalty.
- R² helps compare explained variation relative to a mean baseline but must be interpreted with the dataset and split.
- Check residual plots and errors by subgroup; one overall metric can hide systematic failures.

## Practice
1. Compute MAE for y=[10,20] and predictions [8,23].
2. Why is RMSE more sensitive to large errors than MAE?
3. Can test R² be negative?
4. Why can an average metric hide poor performance for one region?

**Answers:** (2+3)/2=2.5; it squares errors before averaging; yes; groups may have different sample sizes or error distributions, so inspect subgroup metrics.
