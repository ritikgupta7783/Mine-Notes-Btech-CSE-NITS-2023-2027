# Lesson 07.2 — Generalisation, Overfitting and Regularisation

## 1. Generalisation is the true goal
A model is useful when it performs on relevant unseen cases, not only on data it already saw. Performance on training samples is an incomplete measure because the model was specifically fitted to them.

## 2. Underfitting vs overfitting
- **Underfitting:** the model is too limited or poorly trained to capture important patterns even in training data.
- **Overfitting:** the model captures accidental training-specific detail/noise and performs worse on new data.
- **Generalisation gap:** difference between a training metric and a held-out metric; interpret its direction based on whether the metric is a score to maximise or loss to minimise.

Typical pattern for a loss:
| Situation | Training loss | Validation loss |
|---|---|---|
| Underfitting | High | High |
| Good fit (relative to task) | Low/moderate | Low/moderate and similar |
| Overfitting | Very low | Much higher |

These are diagnostic patterns, not perfect rules. Data shift, split error or different metric definitions can also cause a gap.

## 3. Regularisation
Regularisation discourages overly complex fits or very large parameter values. In linear models, Ridge adds a penalty proportional to squared weights; Lasso adds a penalty based on absolute weights. The penalty is combined with a data-fitting loss. Stronger regularisation can reduce variance but may increase bias and cause underfitting if too strong.

## 4. Cross-validation
In k-fold cross-validation, development data is split into k folds. The model is fitted on k−1 folds and validated on the remaining fold, repeating until each fold has served as validation. Results are averaged or otherwise summarised. The method provides a more stable estimate than one arbitrary split in many small-data settings, but it can be costly and must respect grouping/time constraints.

## 5. Learning curves
A learning curve studies how a training/validation metric changes as the amount of training data increases. If training is good and validation remains poor, more data may help if representative; if both scores are poor, a more suitable model/features or better training may be needed.

## Practice
1. What does overfitting look like in train and validation losses?
2. How can regularisation help?
3. Does stronger regularisation always improve the test score?
4. Why might random k-fold cross-validation be inappropriate for forecasting next month?

**Answers:** low train loss and much higher validation loss; discourages overly complex parameter fits; no, excessive regularisation can underfit; a random split can allow future information into training and break the temporal order.
