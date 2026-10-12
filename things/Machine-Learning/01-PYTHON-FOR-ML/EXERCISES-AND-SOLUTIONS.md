# Python for ML — Practice and Solutions

## Try first
1. Write a function that calculates the mean of a non-empty list.
2. Given records as dictionaries, create one list of feature rows and one list of labels.
3. Filter numeric values greater than or equal to 10.
4. Write a function that converts text to float and gives a clear error for invalid input.
5. Explain why a test dataset should not be used to choose a model configuration repeatedly.

## Worked solutions
```python
def mean(values):
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

records = [
    {"area": 50, "bedrooms": 1, "price": 120},
    {"area": 70, "bedrooms": 2, "price": 165},
]
X = [[row["area"], row["bedrooms"]] for row in records]
y = [row["price"] for row in records]

values = [2, 10, 12, 4, 15]
large_values = [value for value in values if value >= 10]

def parse_measurement(text):
    try:
        return float(text)
    except ValueError as error:
        raise ValueError("Measurement must be numeric") from error

print(mean([2, 4, 6]))
print(X)
print(y)
print(large_values)
print(parse_measurement("2.5"))
```

**Output**
```text
4.0
[[50, 1], [70, 2]]
[120, 165]
[10, 12, 15]
2.5
```

The last question is conceptual: use training data to fit, validation/cross-validation to guide choices, and keep the final test set for a final estimate after those choices are settled.
