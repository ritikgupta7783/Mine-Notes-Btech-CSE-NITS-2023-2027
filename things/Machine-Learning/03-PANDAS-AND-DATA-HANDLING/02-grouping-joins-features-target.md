# Lesson 03.2 — Grouping, Joins and Features X / Target y

## 1. Grouping and aggregation
A group operation splits rows by a category and calculates a summary per group.

```python
import pandas as pd
data = pd.DataFrame({
    "city": ["A", "A", "B", "B"],
    "price": [100, 140, 200, 240],
})
print(data.groupby("city")["price"].mean().to_dict())
```

**Output:** `{'A': 120.0, 'B': 220.0}`

This answers a question about historical group averages. It does not automatically mean city causes the prices; other characteristics may differ.

## 2. Joining tables
A join combines tables using a key. Verify the key's meaning and whether it is unique. A many-to-many join can multiply rows and accidentally change the dataset.

```python
import pandas as pd
houses = pd.DataFrame({"house_id": [1, 2], "area": [50, 80]})
sales = pd.DataFrame({"house_id": [1, 2], "price": [120, 210]})
combined = houses.merge(sales, on="house_id", how="inner", validate="one_to_one")
print(combined.to_dict("records"))
```

**Output**
```text
[{'house_id': 1, 'area': 50, 'price': 120}, {'house_id': 2, 'area': 80, 'price': 210}]
```

validate="one_to_one" checks the stated key relationship. It is a useful safety measure when each house should have one matching sales record. Choose inner/left/right/outer joins according to the missing-match behaviour you need.

## 3. Separate features from target

```python
import pandas as pd

data = pd.DataFrame({
    "area": [50, 70, 90],
    "bedrooms": [1, 2, 3],
    "price": [120, 165, 215],
})
X = data[["area", "bedrooms"]]
y = data["price"]

print(X.shape)
print(y.shape)
print(list(X.columns))
```

**Output**
```text
(3, 2)
(3,)
['area', 'bedrooms']
```

X is a two-dimensional table of input features with 3 samples and 2 columns. y is a one-dimensional target Series with 3 values. Check that X and y have the same number of rows and refer to the same samples.

## 4. Split before fitting transformations
For model development, split X and y into training and test parts before fitting a scaler, imputer or feature selector. Otherwise statistics calculated from held-out test rows can leak information into training. A reusable scikit-learn Pipeline is introduced in Module 08.

## Common mistakes
- Selecting data["price"] as X when it is actually the target being predicted.
- Forgetting brackets when selecting multiple DataFrame columns.
- Merging without verifying key uniqueness.
- Dropping missing data without considering whether the missingness is meaningful.
- Using future or post-outcome columns as predictors.

## Practice
1. Create X containing only area and bedrooms; create y from price.
2. Why might a join produce more rows than expected?
3. Why should the scaler be fitted after the train/test split?
4. For customer churn, the target is whether the customer leaves next month. Name one possible leakage feature.

**Answers:** use double brackets for the two feature columns; a key may match multiple rows and create a many-to-many join; fitting before split exposes test-distribution information; a field recorded only after the customer has left, such as a post-cancellation closure code.
