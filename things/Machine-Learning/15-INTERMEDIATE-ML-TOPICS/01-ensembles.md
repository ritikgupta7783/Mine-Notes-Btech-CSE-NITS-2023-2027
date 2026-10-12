# Lesson 15.1 — Ensembles, Bagging and Boosting

## Ensemble
An ensemble combines multiple models. It helps when individual models make complementary errors and the combination reduces error under the chosen metric. More models do not guarantee better results.

## Bagging
Bootstrap aggregating trains models on different resampled versions of the training data and combines their predictions. Random forests add feature randomness when building trees. Bagging often reduces variance of unstable learners.

## Boosting
Boosting builds models sequentially. Each stage focuses on correcting errors or following gradients of a chosen loss. Gradient boosting often achieves strong tabular performance but depends on learning rate, tree complexity, number of stages and suitable validation.

## Stacking
Stacking learns how to combine base-model predictions using a second-level model. The meta-model must be trained on predictions from appropriate out-of-fold/held-out samples, not the base models' in-sample predictions, or it can overfit via leakage.

## Choose carefully
- Bagging: reduce variance and stabilise high-variance learners.
- Boosting: add sequential corrections to improve a loss.
- Stacking: learn a combination of heterogeneous model outputs.
- Simple baseline: may outperform complex ensemble when data are small/noisy or the task is easy.

## Practice
1. Why can averaging diverse tree outputs help?
2. What is the key difference between random forest and gradient boosting training?
3. What leakage issue can occur when training a stacking meta-model?
4. Why should the ensemble still be compared with a simple baseline?

**Answers:** reduces impact of individual tree variability; forests grow varied trees then aggregate, boosting adds sequential learners; using in-sample base predictions gives the meta-model unrealistically easy signals; added complexity may not improve appropriate held-out performance.
