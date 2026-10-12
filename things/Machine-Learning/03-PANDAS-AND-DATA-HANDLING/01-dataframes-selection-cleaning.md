# Lesson 03.1 — DataFrames, Selection and Cleaning

## 1. A DataFrame is a labelled table

```python
import pandas as pd

data = pd.DataFrame({
    "area": [50, 70, 90, 110],
    "bedrooms": [1, 2, 3, 3],
    "price": [120, 165, 215, 250],
})
print(data.shape)
print(data.head(2))
print(data.dtypes)
```

**Output**
```text
(4, 3)
   area  bedrooms  price
0    50         1    120
1    70         2    165
area        int64
bedrooms    int64
price       int64
dtype: object
```

Output formatting can vary by Pandas version/platform, but shape is four rows and three columns. head(2) shows the first two rows. dtypes reports the type Pandas inferred for each column.

## 2. Select columns, rows and filters

```python
import pandas as pd
data = pd.DataFrame({
    "area": [50, 70, 90, 110],
    "bedrooms": [1, 2, 3, 3],
    "price": [120, 165, 215, 250],
})

print(data["price"].tolist())
print(data.loc[0, "area"])
print(data.loc[data["area"] >= 90, ["area", "price"]].to_dict("records"))
```

**Output**
```text
[120, 165, 215, 250]
50
[{'area': 90, 'price': 215}, {'area': 110, 'price': 250}]
```

data["price"] selects one Series. A list of column names selects multiple columns as a DataFrame. loc uses row/column labels. Filtering creates a boolean mask and keeps rows for which the mask is true.

## 3. Missing values and duplicates

Missing data can have many meanings: not collected, not applicable, sensor failure, or deliberate omission. Don't replace all missing values with zero without considering the meaning.

```python
import pandas as pd

data = pd.DataFrame({
    "age": [20, None, 22, 22],
    "city": ["Silchar", "Silchar", None, None],
})
print(data.isna().sum().to_dict())
print(data.duplicated().sum())
clean = data.drop_duplicates()
print(len(clean))
```

**Output**
```text
{'age': 1, 'city': 2}
1
3
```

isna().sum() counts missing values per column. duplicated() marks rows that match earlier row values under Pandas duplicate rules. Dropping a duplicate row is appropriate only if it is genuinely a duplicate, not a separate event with identical values.

## 4. Data types can mislead
CSV files often begin as strings because CSV is a text format. Inspect columns before calculations. Convert with pd.to_numeric or astype only after deciding how invalid values should be handled. Never assume a date or numeric-looking identifier was parsed correctly by automatic inference.

## Beginner questions
**Why do row indexes start at 0?** Pandas creates an index, often 0-based for a new DataFrame, but indexes can be labels and aren't always a simple range.  
**What's the difference between loc and iloc?** loc selects by labels; iloc selects by integer position.  
**Should missing target labels be imputed?** Usually not by ordinary feature imputation. If the supervised target is missing, the sample often cannot directly contribute to standard supervised training; the correct handling depends on the problem.

## Practice
1. Select only the columns area and bedrooms.
2. Filter records where price is greater than 180.
3. Count missing entries by column.
4. Explain why duplicates should be investigated before being dropped.

**Answers:** use data[["area","bedrooms"]]; use data.loc[data["price"] > 180]; use data.isna().sum(); identical-looking rows may represent separate legitimate observations.
