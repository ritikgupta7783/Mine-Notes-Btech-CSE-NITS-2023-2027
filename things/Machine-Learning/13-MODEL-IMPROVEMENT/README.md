# Module 13 — Model Improvement

**Prerequisites:** model fundamentals, preprocessing, supervised algorithms and evaluation.
**Goal:** improve models through controlled experiments, not random parameter guessing.

## Learning order
1. [Baseline, hypotheses and error analysis](01-baselines-and-error-analysis.md)
2. [Hyperparameter search and learning curves](02-tuning-and-learning-curves.md)

## Improvement workflow
1. Record the baseline and metric.
2. Inspect errors and data splits.
3. Write a hypothesis about the current limitation.
4. Change one major factor or use a controlled experiment.
5. Use the same validation procedure to compare fairly.
6. Keep a change only when the gain is meaningful and trade-offs acceptable.
7. Evaluate final choices once on the held-out test set.
8. Record data version, seed, parameters, scores and remaining risks.

Never invent score improvements. Treat an expected effect as a hypothesis until the experiment is run.
