# Interview Set 17.2 — Mathematics and Metrics

## Numerical question 1: Mean and standard deviation
For x=[2,4,6], mean=(2+4+6)/3=4. Population squared deviations are 4,0,4; population variance=8/3, population standard deviation=√(8/3)≈1.633. Sample variance divides by n−1, yielding 4; sample standard deviation is 2. Always state which convention you use.

## Numerical question 2: Regression errors
True y=[3,5,7], prediction ŷ=[2,5,10]. Absolute errors are [1,0,3], so MAE=4/3≈1.333. Squared errors are [1,0,9], so MSE=10/3≈3.333 and RMSE≈1.826. A single large residual has greater effect on MSE/RMSE than on MAE.

## Numerical question 3: Confusion matrix
Suppose TP=40, TN=50, FP=10, FN=20.
- Accuracy=(40+50)/120=0.75.
- Precision=40/(40+10)=0.80.
- Recall=40/(40+20)≈0.667.
- Specificity=50/(50+10)≈0.833.
- F1=2×0.80×0.667/(0.80+0.667)≈0.727.

Interpret the metrics in words and discuss which error is costly before recommending a model.

## Numerical question 4: Gradient descent
Let J(w)=(w−3)², so J'(w)=2(w−3). Start w=0 with η=0.1:
gradient=−6, updated w=0−0.1×(−6)=0.6. J moves from 9 to 5.76. This one step works for this simple objective; it does not prove all learning rates work for every objective.

## Numerical question 5: Distance
Euclidean distance between (1,2) and (4,6) is √(3²+4²)=5. Manhattan distance is |3|+|4|=7. If feature one is in thousands and feature two in single digits, one feature might dominate Euclidean distance; scaling and feature meaning matter.

## Concept questions
**Why square errors?** To avoid positive/negative cancellation, penalise larger misses more and get a convenient differentiable objective. This also increases sensitivity to outliers.

**Why is sigmoid used in logistic regression?** It maps a real linear score to a number in (0,1), which is used as the model's binary class probability estimate under the model assumptions.

**Why is the gradient negative in the update?** The gradient points toward greatest local increase; subtracting it aims to move downhill. Learning rate determines step size.

**Does a lower loss always mean a better model?** Only under the chosen training objective. Generalisation, metric relevance, subgroup errors, calibration and operational costs still matter.

**What does R² < 0 mean on test data?** Under its usual formula, the model's squared error is worse than the test-set mean baseline. It does not mean the model explains a negative physical fraction of reality.

## Practice
Solve the examples without looking, then explain one limitation for each formula. If arithmetic is wrong, show your steps rather than memorising a corrected final number.
