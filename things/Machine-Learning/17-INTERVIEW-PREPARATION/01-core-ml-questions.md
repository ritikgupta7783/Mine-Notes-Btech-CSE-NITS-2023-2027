# Interview Set 17.1 — Core ML Questions and Answers

## Beginner

**1. What is Machine Learning?**  
ML is a set of methods that fit a model from data so it can make predictions or decisions under a defined objective. A learned mapping can find patterns, but it does not guarantee truth, fairness or correct generalisation.

**2. AI vs ML vs Deep Learning?**  
AI is the broader field of intelligent systems. ML is one approach inside AI that learns from data. Deep Learning is a branch of ML that uses multi-layer neural networks.

**3. Supervised vs unsupervised learning?**  
Supervised learning trains with known target labels/values; unsupervised learning explores structure without supplied target labels. Regression and classification are supervised task types; clustering is a common unsupervised task.

**4. Feature vs target?**  
A feature is an input used for prediction. The target is the value/category we want to predict. A target column must not accidentally be included as an input.

**5. Algorithm vs model?**  
The algorithm is a learning procedure; the model is the fitted result used to map input to prediction.

**6. Training vs inference?**  
Training estimates model parameters from examples. Inference applies the fitted model to new inputs.

**7. Parameter vs hyperparameter?**  
Parameters are learned during fit, such as regression coefficients. Hyperparameters configure the process, such as tree depth or K in KNN, and are normally selected on development validation.

## Intermediate

**8. What is overfitting?**  
The fitted model captures training-specific patterns/noise, so training performance is much better than relevant unseen-data performance. Use appropriate splits, regularisation, simpler models, more representative data and error analysis as applicable.

**9. What is underfitting?**  
The model cannot capture important patterns even on training data. Investigate features, model capacity, objective and training procedure rather than automatically adding data or tuning every parameter.

**10. Explain bias–variance trade-off.**  
In a common conceptual view, overly simple assumptions can cause systematic error (bias), while a model very sensitive to training samples has high variance. Balancing them supports generalisation, but the terms also have formal decompositions under particular assumptions.

**11. What is data leakage?**  
Training or model-selection decisions use information that would not legitimately be available at that stage or at prediction time. Examples include target-derived features, scaling before splitting, or letting future records enter training for a forecasting task.

**12. Why split into train/validation/test?**  
Train fits model parameters; validation compares designs/hyperparameters; test gives a final held-out evaluation after decisions are complete. Cross-validation can provide more stable development comparisons.

**13. Why use a baseline?**  
A simple reference tells whether added model complexity improves a suitable metric under the same evaluation procedure. A complicated model with no benefit is harder to maintain.

**14. Explain regularisation.**  
Regularisation adds a penalty or constraint that discourages overly complex parameter values. It can improve generalisation but excessive regularisation may underfit.

**15. Why use a Pipeline?**  
It binds preprocessing and the estimator into one reproducible object and helps ensure transformations are fitted inside training folds during cross-validation. It also keeps inference preprocessing consistent.

**16. Why is correlation not causation?**  
Variables may move together because of confounding, reverse causality, selection effects or coincidence. Predictive usefulness alone does not tell us what would happen after an intervention.

**17. What is generalisation?**  
Performance on relevant unseen data drawn from the intended use setting. A random held-out score can still be misleading if deployment data differ or the split violates time/group constraints.

## Algorithm comparisons

**18. Linear vs logistic regression?**  
Linear regression predicts numeric values, often by least squares. Logistic regression commonly models class probability with a sigmoid of a linear score and is used for classification.

**19. Decision tree vs random forest?**  
One tree is a sequence of splits and is relatively easy to inspect, but can be unstable. A random forest aggregates many randomised trees, often reducing variance at the expense of interpretability and compute.

**20. Random forest vs gradient boosting?**  
Forests typically combine trees trained with data/feature randomness; boosting adds learners sequentially to improve the current model's loss. Both need fair validation.

**21. KNN vs linear model?**  
KNN predicts from nearby stored examples and is sensitive to scale/distance and inference cost. Linear models fit coefficients for a global linear relationship and may be simpler to inspect.

**22. K-means vs classification?**  
K-means groups data without target labels by a distance/objective rule. Classification learns to predict supplied labels. Cluster IDs aren't automatically semantic categories.

**23. What is PCA?**  
Principal Component Analysis builds orthogonal directions that capture decreasing amounts of variation in the data. It is unsupervised; high variance is not the same as high predictive usefulness.

## Data and evaluation

**24. What is imputation?**  
Filling missing feature values by a defined rule, such as training-set median. The choice should reflect feature meaning and missingness mechanisms.

**25. One-hot vs ordinal encoding?**  
One-hot creates indicator columns without imposing numeric order; ordinal encoding assigns codes and is appropriate when an order exists or the chosen model supports the representation.

**26. Why scale features?**  
It makes scales more comparable for distance-based methods and often helps numerical optimisation/regularisation. Trees usually do not need standard scaling in the same way.

**27. What is precision?**  
TP/(TP+FP): among predicted positives, fraction actually positive.

**28. What is recall?**  
TP/(TP+FN): among actual positives, fraction detected.

**29. Why can accuracy mislead?**  
With rare positives, predicting the majority class can yield high accuracy while missing every positive. Inspect precision, recall, F1, PR curves and error cost.

**30. What does cross-validation do?**  
It repeatedly fits and validates on different folds of development data to estimate variability and compare choices. The fold strategy must respect grouping, time and leakage constraints.

## Answer practice
Pick any question and answer aloud using four steps: definition, reason, example, limitation. Keep the first answer under 60 seconds, then elaborate if asked.
