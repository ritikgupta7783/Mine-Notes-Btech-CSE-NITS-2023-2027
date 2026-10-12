# Module 03 — Pandas and Data Handling

**Prerequisite:** Python collections (Module 01) and basic arrays (Module 02).  
**Goal:** load and inspect structured data, clean common issues, create features X and target y, and understand why splitting comes before fitted preprocessing.

## Lessons
1. [DataFrames, selection, filtering and missing values](01-dataframes-selection-cleaning.md)
2. [Group, join, and define X/y](02-grouping-joins-features-target.md)
3. [Runnable example](pandas_basics.py)

## Why Pandas
A CSV is a table stored as text. Pandas represents that table as a DataFrame with labelled rows and columns. Labels are useful when you want to select a feature by name, inspect missing values, group data and prepare a model input.

## Checkpoint
- Read a CSV and inspect shape, columns, dtypes and sample rows.
- Select a Series or a DataFrame intentionally.
- Filter with a boolean condition.
- Detect and handle missing/duplicate records with a stated rule.
- Separate X from y and avoid accidentally leaving the target in X.
- Explain why preprocessing parameters must be learned only from training data.
