# Lesson 12.2 — Feature Selection, Importance and Leakage

## Feature selection
Feature selection keeps a subset of predictors. Reasons include reducing noise, improving interpretability, lowering cost or controlling overfitting. Selection can use domain reasoning, model-based importance, or statistical criteria. Any data-driven selection must be fitted inside training/validation folds to avoid leakage.

## Correlated features
When features carry similar information, a linear model may distribute coefficients between them in unstable ways. A tree-based importance score may choose one of several substitutes. Correlation analysis can help diagnose redundancy, but high correlation alone does not tell us which feature should be removed; domain value and validation matter.

## Model feature importance
- Linear coefficients describe the fitted model under its representation and feature scaling.
- Tree impurity importance reflects reductions in impurity attributed to splits; it can be biased toward variables with many possible split points.
- Permutation importance measures how a chosen evaluation metric changes when a feature is shuffled. It should be computed on a relevant held-out dataset and can understate correlated features because substitutes remain.

**Importance is not causation.** A feature may predict a target because it is a proxy for another factor or because of sample-selection effects. A causal claim needs an appropriate causal design and assumptions.

## Leakage checklist
Before training, ask:
1. Did this feature exist at the prediction time?
2. Was it directly derived from the target or a later event?
3. Was a global statistic calculated using train and test together?
4. Was feature selection run before splitting?
5. Can records from the same person/device appear in both sets contrary to deployment needs?
6. Can future timestamps enter past predictions?

## Practice
1. Why must SelectKBest or another fitted selector be placed within cross-validation?
2. Why can a low permutation importance be misleading when features are highly correlated?
3. What does a large coefficient mean when features have very different scales?
4. Why doesn't feature importance imply intervention effect?

**Answers:** pre-split selection uses held-out label information; correlated substitutes can preserve performance when one feature is shuffled; coefficient units depend on feature scale/representation; prediction associations do not establish causality.
