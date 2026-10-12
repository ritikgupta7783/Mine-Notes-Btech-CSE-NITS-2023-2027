# Lesson 01.1 — Variables, Types, Conditions and Loops

## 1. Variables are names for values
A variable lets a program refer to a value by a name. Python determines the type from the value assigned at runtime, though the type still affects which operations are valid.

```python
age = 21                    # int
height_m = 1.72             # float
name = "Riya"               # str
has_experience = False      # bool
not_recorded = None         # NoneType

print(age, type(age).__name__)
print(height_m, type(height_m).__name__)
print(name, type(name).__name__)
print(has_experience, type(has_experience).__name__)
print(not_recorded)
```

**Output**
```text
21 int
1.72 float
Riya str
False bool
None
```

The equals sign assigns a value; it does not mean “these two values are mathematically equal.” Use == to compare two values. None is commonly used to represent a missing/not-yet-provided value, but in a real dataset you must understand why a value is missing.

## 2. Conditions choose a path

```python
score = 74

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C or below"

print(grade)
```

**Output:** `B`

Python uses indentation to mark blocks. The elif branch is checked only if the earlier if condition was false. Here, a score of 74 is not at least 90 but is at least 70.

## 3. Loops repeat work

```python
scores = [70, 80, 90]
total = 0

for score in scores:
    total += score

print(total)
print(total / len(scores))
```

**Output**
```text
240
80.0
```

Dry run: total starts at 0, then becomes 70, 150 and 240. len(scores) is 3, so the average is 240/3 = 80.0. Using sum(scores) is simpler for this example; the loop shows the repetition explicitly.

## 4. Common mistakes
- Using = when you need ==.
- Comparing strings and numbers without converting them intentionally.
- Forgetting that a list index starts at 0.
- Using a variable before it has been assigned.
- Incorrect indentation.
- Dividing by zero when a list may be empty.
- Treating missing values as zero without checking what missing means.

## Questions a beginner might ask
**Why does 5 / 2 return 2.5?** Python's / operator performs division and returns a float in this case. // performs floor division.  
**Can a variable change type?** Python permits rebinding a name to a value of another type, but mixing types unexpectedly often causes bugs.  
**When should I use a loop instead of sum()?** Use sum() for a direct sum; a loop is useful when each item needs extra logic or you are learning the underlying steps.

## Practice
1. Create variables for a sample ID, a feature value and a boolean flag.
2. Print whether a score is at least 50.
3. Calculate the total of [3, 7, 10] using a loop.
4. What does this output?

```python
values = [2, 4, 6]
print(values[1])
```

**Answers:** 1. Choose clear variable names and matching values. 2. A boolean result, True or False. 3. 20. 4. 4, because indexing starts at zero.
