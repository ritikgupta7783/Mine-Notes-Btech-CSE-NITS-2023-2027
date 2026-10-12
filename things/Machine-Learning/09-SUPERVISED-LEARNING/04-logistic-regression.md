# Algorithm 09.4 — Logistic Regression

## Prerequisites
- [Probability and Bayes](../06-STATISTICS-AND-PROBABILITY/02-probability-and-bayes.md)
- [Vectors/matrices](../05-MATHEMATICS-FOR-ML/02-vectors-matrices-and-dimensions.md)
- [Confusion matrix and classification metrics](../11-MODEL-EVALUATION/02-classification-metrics.md)

## 1. What problem does it solve?
Linear regression predicts a number. Logistic regression is commonly used for classification, especially binary classification. It computes a linear score from features and maps that score through the sigmoid function to model a probability for a positive class.

\[
z=\mathbf{w}\cdot\mathbf{x}+b,\qquad
P(y=1\mid x)=\sigma(z)=\frac{1}{1+e^{-z}}
\]

## 2. Small numerical example
If z=0, sigmoid(0)=1/(1+1)=0.5. If a fitted model returns probability 0.8 for the positive class and our decision threshold is 0.5, we predict class 1. The threshold is a decision choice; it can be changed to reflect different costs for false positives and false negatives.

## 3. Fit a model
```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

X, y = make_classification(
    n_samples=300, n_features=6, n_informative=4,
    n_redundant=0, random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions, zero_division=0))
```

The dataset is synthetic and intended to demonstrate an API, not to imply expected real-world accuracy. Scaling is in the pipeline so it is fitted on training samples only. The report includes class precision, recall and F1; assess the metric relevant to the application.

## 4. What the model learns
Logistic regression estimates coefficients for a linear score and fits them using an objective related to log loss. A coefficient changes the score for a one-unit feature change while other features remain fixed; the effect on probability is nonlinear because of the sigmoid mapping. The model is called “regression” historically, but it is used as a classifier when a threshold maps probabilities to classes.

## 5. Strengths, weaknesses and hyperparameters
**Strengths:** fast baseline, coefficients can be inspected, outputs scores/probabilities, works well when a linear decision boundary is suitable.  
**Weaknesses:** nonlinear boundaries need feature engineering or another model; correlated/high-dimensional features and poor scaling can complicate fitting; probability calibration and class imbalance need attention.

Common parameters include C (inverse regularisation strength in scikit-learn: smaller C means stronger regularisation), penalty where supported, class_weight and max_iter. Check the installed scikit-learn version for exact supported combinations.

## Questions a beginner might ask
**Why not use linear regression for a class label?** Its outputs can be outside [0,1] and squared-error fitting doesn't model Bernoulli class probabilities in the same way.  
**Does 0.8 mean an 80% guaranteed chance?** No. It's a model estimate; calibration, data representativeness and assumptions matter.  
**Why scale features?** It commonly helps optimisation and makes regularisation behave more consistently.  
**Why is the threshold not always 0.5?** Real decision costs, prevalence and precision/recall trade-offs may favour another threshold.

## Practice
1. Calculate sigmoid(0).
2. What class would threshold 0.5 assign to probability 0.31?
3. What is the role of C in common scikit-learn logistic regression?
4. Why shouldn't the threshold be chosen by repeatedly checking the final test set?

**Answers:** 0.5; class 0; inverse regularisation strength in common sklearn settings; it uses the test set for model selection and biases the final estimate.
