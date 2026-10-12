# Lesson 05.1 — Functions, Equations and Graphs

## 1. A function maps input to output
A mathematical function takes an input and returns an output according to a rule. Example: f(x) = 2x + 3. If x = 4, then f(4) = 2×4 + 3 = 11.

In a regression model, a prediction is a function of input features. A simple one-feature linear model is:
\[
\hat y = wx+b
\]
Here x is the feature; w is the coefficient/slope; b is the intercept; ŷ is the prediction. The model uses the input to calculate a predicted output.

## 2. Solve one example
Suppose w=2 and b=20. For x=50:
1. Multiply the input by its coefficient: 2×50=100.
2. Add the intercept: 100+20=120.
3. Prediction is ŷ=120.

These values are given by us in this exercise; they have not been learned from data.

```python
def predict_area(area, weight, bias):
    return weight * area + bias

print(predict_area(50, weight=2, bias=20))
```

**Output:** `120`

## 3. What do slope and intercept mean?
For a line y=wx+b, slope w describes how much y changes for a one-unit increase in x when the line represents the relationship. Intercept b is the predicted y when x=0. That mathematical interpretation may or may not be meaningful in the real domain—for a house dataset, area zero may be outside the range of realistic observations.

## 4. Percentages, ratios and logarithms
Percent changes are useful for interpreting metrics and relative differences. A ratio compares two quantities; confirm units before dividing. A logarithm answers “what exponent produces this value?” For example, log base 10 of 100 is 2 because 10²=100. Natural log ln uses base e and appears in likelihood/loss formulas.

## Practice
1. Calculate 3x+5 for x=4.
2. For ŷ=4x+10, what is the predicted change for a one-unit increase in x?
3. Why can the intercept be mathematically valid but unhelpful in a real-world interpretation?
4. What value does log10(1000) equal?

**Answers:** 17; 4 output units under the model; x=0 may lie outside the real data range; 3.
