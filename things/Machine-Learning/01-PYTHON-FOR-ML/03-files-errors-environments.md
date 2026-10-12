# Lesson 01.3 — Files, Exceptions, Imports and Environments

## 1. Read a CSV file with the standard library
CSV stores tabular text. Before Pandas is introduced, Python's csv module can show how rows and columns are read.

```python
import csv
from pathlib import Path

path = Path("scores.csv")

with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Asha", "score": 82})
    writer.writerow({"name": "Dev", "score": 91})

with path.open(newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["name"], int(row["score"]))

path.unlink()  # clean up the example file
```

**Output**
```text
Asha 82
Dev 91
```

Values read from a CSV are usually text strings. Convert them deliberately; int(row["score"]) turns the score into an integer. The with statement closes the file even if an error occurs.

## 2. Handle errors where you can respond usefully
```python
def read_score(text):
    try:
        score = int(text)
    except ValueError as error:
        raise ValueError("Score must be a whole number") from error

    if not 0 <= score <= 100:
        raise ValueError("Score must be from 0 to 100")
    return score

for raw in ["82", "many", "130"]:
    try:
        print(read_score(raw))
    except ValueError as error:
        print("Invalid:", error)
```

**Output**
```text
82
Invalid: Score must be a whole number
Invalid: Score must be from 0 to 100
```

Do not catch every error and silently continue. Catch a specific exception only when the code can recover, explain the problem or add context.

## 3. Imports and virtual environments
- An **import** makes a module's names available to the current program.
- A **package** is a way to organise reusable code; packages can include modules.
- A **virtual environment** isolates a project's installed Python packages from other projects.

Create and activate an environment using the commands in [How to Study](../HOW-TO-STUDY.md). Then install packages with python -m pip, which helps ensure pip belongs to that Python interpreter.

## 4. Debugging a traceback
Read the final line for the exception type and message, then inspect the file and line mentioned near the bottom. The earliest relevant line in your own code often shows the cause, while library stack frames show how execution got there. Fix one issue, run again, and do not hide exceptions just to make the program stop displaying red text.

## Practice
1. Convert the string "19" to an integer and explain what happens for "nineteen".
2. Read a CSV score and validate it is between 0 and 100.
3. Why should a file be opened with a with block?
4. Why can installing a package in one Python environment fail to make it importable in another?

**Answers:** int("19") is 19; int("nineteen") raises ValueError; with closes the file reliably; separate environments keep different package installations isolated.
