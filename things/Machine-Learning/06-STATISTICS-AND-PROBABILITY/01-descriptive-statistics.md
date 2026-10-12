# Lesson 06.1 — Mean, Median, Variance and Spread

## 1. Why summarise a dataset?
A table can contain thousands of values. Descriptive statistics give compact summaries, but every summary hides some detail. It helps to inspect both a summary and the distribution plot.

Use the small scores [40, 50, 60, 70, 100].

## 2. Mean and median
**Mean** is the sum divided by the number of observations:
\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]
Here the mean is (40+50+60+70+100)/5 = 64.

**Median** is the middle value after sorting. With five sorted values, the median is 60. If there is an even number of values, the median is the average of the two middle values under the common numeric definition.

The mean is sensitive to extreme values; the median is more robust. Neither is universally best. For a highly skewed house-price distribution, median may describe a typical record better than mean; for other decisions, the mean may be exactly the quantity we need.

```python
import numpy as np
scores = np.array([40, 50, 60, 70, 100])
print(scores.mean())
print(np.median(scores))
```

**Output**
```text
64.0
60.0
```

## 3. Range, variance and standard deviation
Range = max − min = 100 − 40 = 60.

Variance measures average squared deviation from a mean. Population variance divides by n; sample variance commonly divides by n−1 when estimating population variance from a sample. The choice depends on the question and the library parameter (for NumPy, ddof=0 is the default population-style calculation).

Standard deviation is the square root of variance and therefore has the same units as the values; variance has squared units.

```python
import numpy as np
x = np.array([1, 3, 5])
print(x.mean())
print(x.var())                # ddof=0: population-style variance
print(x.std())
print(x.var(ddof=1))          # sample variance
```

**Output**
```text
3.0
2.6666666666666665
1.632993161855452
4.0
```

Population deviations from mean 3 are -2, 0, +2. Squared deviations are 4,0,4; their mean is 8/3. Sample variance divides that total 8 by n−1=2, giving 4.

## 4. Quartiles and outliers
Quartiles divide sorted data into parts under a chosen quantile convention. The interquartile range is IQR = Q3−Q1. A common box-plot rule flags values below Q1−1.5×IQR or above Q3+1.5×IQR as potential outliers. This is a flag for investigation, not proof of an error or a reason to delete the data automatically.

## 5. Covariance and correlation
Covariance describes whether two variables tend to vary together, but its magnitude depends on units. Correlation rescales the linear association to a range from −1 to 1. Strong correlation doesn't prove causation; a third variable, selection effects or reverse causality may explain an association.

## Practice
1. Find mean and median for [2,3,3,4,18].
2. Which summary is less sensitive to the final 18: mean or median?
3. If every value is multiplied by 10, what happens to standard deviation?
4. Give one reason not to delete a statistical outlier automatically.

**Answers:** mean=6, median=3; median; standard deviation multiplies by 10; it may be a valid rare case and deleting it can bias the data.
