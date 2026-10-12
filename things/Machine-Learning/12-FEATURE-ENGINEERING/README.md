# Module 12 — Feature Engineering

**Prerequisites:** Pandas, visualisation, preprocessing and model evaluation.
**Goal:** turn raw columns into useful model inputs while protecting evaluation from leakage.

## Lessons
1. [Features, transformations and interactions](01-feature-creation-and-transformation.md)
2. [Feature selection, importance and leakage traps](02-feature-selection-importance-leakage.md)

## Main questions
- Does the feature exist at prediction time?
- Does it encode a meaningful signal or an accidental identifier?
- Is a transformation fitted using only training data?
- Does it improve a fair validation score, not just training performance?
- Can the feature be explained to users and maintained in production?

Feature engineering is not an excuse to create features until a score looks good. Establish a baseline, form a hypothesis, validate the feature and keep a final test set untouched.
