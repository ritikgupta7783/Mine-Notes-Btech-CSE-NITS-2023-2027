# Revision Answers and Explanations

## Conceptual set answers
1. Algorithm is the learning procedure; model is the fitted mapping used for prediction.
2. Regression because the target is a number on a numeric scale.
3. A cancellation code recorded after cancellation can reveal the outcome.
4. A model is fitted to training data; it may memorise details that do not transfer to new data.
5. Parameter is learned during fitting; hyperparameter configures the process and is selected using development validation.
6. Usually 500 samples and 12 input features.
7. Matrix multiplication requires compatible inner dimensions; shapes reveal whether dimensions align.
8. When data are skewed or contain extreme values, median is less sensitive.
9. No. A confounder such as season can influence both variables.
10. Feature scaling; large-scale income can dominate distance.
11. Linear regression predicts a numeric outcome; logistic regression commonly models a binary class probability with a sigmoid/linear score.
12. It discourages overly large/complex coefficient fits, often trading some bias for lower variance; too much regularisation underfits.
13. It searches splits that improve an impurity/loss criterion, weighted by the resulting child samples.
14. Forests typically aggregate randomised trees; boosting builds models sequentially to improve the current objective.
15. Conditional independence of features given the class.
16. K-means partitions data into a chosen number of clusters; K is a user/model choice.
17. PCA finds directions that capture variation; target relevance and predictive performance are different questions.
18. Precision=30/(30+10)=0.75. Recall=30/(30+20)=0.60.
19. Accuracy is dominated by the majority negative class; inspect precision/recall/PR and class-specific costs.
20. It should not. Use validation/cross-validation for choices and hold the final test for final evaluation.
21. Each fold should fit preprocessing on its training portion only, avoiding leakage into the validation fold.
22. The model has larger squared error than the test-set mean baseline under the usual R² definition.
23. Inference must apply exactly the learned training transformations.
24. Define a consistent unknown-category policy, monitor it, and avoid pretending an unseen category is semantically known.
25. It can favour features with many possible split points and be distorted by correlated predictors.
26. Data drift is a changed input distribution; concept drift is a changed input-target relationship.
27. Disparate errors, representative data, explainability, legal constraints, false denial consequences or privacy.
28. Use time-aware validation; never train on future data relative to the forecast origin; compare with a seasonal/naïve baseline and evaluate on future-held-out periods.

## Numerical answers
1. Mean=4. Deviations [-2,0,2], squared deviations [4,0,4]. Population variance=8/3≈2.667; population SD≈1.633; sample variance=8/(3−1)=4.
2. 3×7+5=26. Coefficient is a model association conditional on model/data, not automatically causal.
3. 2×4 + (−1)×5 + 3×2 = 8−5+6 = 9. A linear model uses a dot product to sum weighted features.
4. Gradient=2(1−4)=−6. Next w=1−0.2×(−6)=2.2.
5. Absolute errors [2,2,5]; MAE=9/3=3. Squared errors [4,4,25]; MSE=33/3=11; RMSE=√11≈3.317.
6. Total=36+54+6+24=120. Accuracy=(36+54)/120=0.75. Precision=36/42≈0.857. Recall=36/60=0.6. Specificity=54/60=0.9. F1=2×(6/7)×(3/5)/((6/7)+(3/5))≈0.706.
7. P(A|B)=0.18/0.30=0.6. Denominator P(B) restricts the reference group to cases where B occurred.
8. Differences are 3 and 4. Euclidean=√(9+16)=5; Manhattan=3+4=7. Scaling can change distances by changing the relative contribution of each feature.

## Debugging answers
A. Target churn is inside X. Remove it; test that X.columns does not include target.  
B. Scaler learns from the full dataset. Split first and fit scaling inside a Pipeline; check that pipeline fitting occurs inside each CV fold.  
C. Regression needs numeric prediction metrics such as MAE/RMSE and error interpretation in minutes.  
D. Vectorizer learns vocabulary/IDF from test messages too. Put it in a Pipeline and fit inside the training folds.  
E. Accuracy hides minority-class failure. Inspect recall/precision/F1 and consider threshold/cost-aware choices.  
F. Increasing depth may worsen overfit. Compare training and validation curves; tune max_depth/min_samples_leaf using CV.  
G. Association does not prove intervention effect. Use causal reasoning/design and describe assumptions; avoid causal language without evidence.  
H. Time leakage. Use time-based splits that train on past and test on later periods; compare with a forecasting baseline.  
I. Training/inference preprocessing mismatch. Persist and load the complete fitted Pipeline; add an inference integration test on known rows.  
J. Define an explicit unknown-category strategy such as OneHotEncoder(handle_unknown="ignore"), log rates and assess impact. Do not silently merge categories unless that policy is justified.

Review not only the answer but the reasoning. For any question you miss, return to the linked lesson and reproduce its example.
