# Lesson 01.2 — Collections and Functions

## 1. Lists, tuples, dictionaries and sets
- A **list** is an ordered, mutable sequence: elements can be changed.
- A **tuple** is an ordered sequence that cannot be reassigned element-by-element after creation.
- A **dictionary** maps keys to values.
- A **set** stores unique elements and is useful for membership/uniqueness; it should not be used when sequence order is the main requirement.

```python
scores = [80, 92, 75]
student = ("Riya", 21)
record = {"name": "Riya", "score": 92}
unique_scores = {80, 92, 75, 92}

print(scores[0])
print(student[0])
print(record["score"])
print(sorted(unique_scores))
```

**Output**
```text
80
Riya
92
[75, 80, 92]
```

The output from sorted() is a list; set display order is not a reliable way to present sorted data.

## 2. Functions package a task

A function receives input through parameters and may return a result. Calling a function is different from defining it.

```python
def mean(values):
    if len(values) == 0:
        raise ValueError("mean needs at least one value")
    return sum(values) / len(values)

print(mean([2, 4, 6]))
```

**Output**
```text
4.0
```

values is a parameter. [2, 4, 6] is the argument supplied when mean is called. return sends the answer to the caller; print displays it. Raising an exception for an empty list is safer than dividing by zero or returning a pretend mean.

## 3. Dictionaries help inspect individual records

```python
row = {"area": 70, "bedrooms": 2, "price": 165}
features = [row["area"], row["bedrooms"]]
target = row["price"]
print(features, target)
```

**Output**
```text
[70, 2] 165
```

This previews the X/y idea from Module 00. The target should not accidentally be included in the feature list when the goal is to predict it.

## 4. List comprehensions
A comprehension builds a list from an iterable, optionally filtering items. Use it when it makes the code clearer; an ordinary loop is often easier to debug for complex logic.

```python
scores = [42, 81, 67, 95]
passed = [score for score in scores if score >= 50]
doubled = [score * 2 for score in scores]
print(passed)
print(doubled)
```

**Output**
```text
[81, 67, 95]
[84, 162, 134, 190]
```

## 5. Avoid changing shared lists unexpectedly
Lists are mutable. If two variables refer to the same list, modifying it through one reference affects what the other name sees.

```python
first = [1, 2]
second = first
second.append(3)
print(first)
```

**Output:** `[1, 2, 3]`

Assignment does not copy the list; it binds another name to the same object. When you require a shallow copy, first consider list(first) or first.copy(); nested mutable structures need extra thought.

## Practice
1. Store a user's city and age in a dictionary.
2. Write a function that returns the largest of two numbers.
3. Use a comprehension to keep only positive values.
4. Explain why y = record["price"] and X = [record["area"], record["bedrooms"]] have different roles.

**Answers:** Use a dictionary such as {"city":"Silchar","age":21}; max(a, b) or a comparison can return the larger; [x for x in values if x > 0]; X contains inputs while y is the target to predict.
