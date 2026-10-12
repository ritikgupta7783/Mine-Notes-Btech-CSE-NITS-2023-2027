# Machine Learning Formula Sheet

Every formula is meaningful only when its symbols and assumptions are understood. Notation can vary across books; follow the definitions used in the specific lesson.

## Descriptive statistics

**Mean**
\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]
The sum of n values divided by n. Example: for 2, 4, 6, the mean is (2+4+6)/3 = 4.

**Population variance**
\[
\sigma^2=\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2
\]
The average squared distance from population mean μ. Sample variance commonly uses n−1 in the denominator; know which formula a context calls for.

**Standard deviation**
\[
\sigma=\sqrt{\sigma^2}
\]
Square root of variance, in the same units as the measured variable.

## Linear regression

**Prediction**
\[
\hat y=wx+b
\]
x is an input, w is the weight/slope, b is the intercept and ŷ is the predicted output.

**Mean squared error**
\[
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]
Measures the average squared prediction error. Large errors receive disproportionate weight.

**Gradient descent (generic form)**
\[
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t)
\]
θ is the parameter vector, η is learning rate, J is the objective and its gradient indicates the direction of greatest local increase; subtracting it aims to reduce J.

## Classification

**Sigmoid**
\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]
Maps a real input to a value strictly between 0 and 1. Logistic regression uses it to model the probability of the positive class under its modelling assumptions.

**Accuracy**
\[
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
\]

**Precision**
\[
Precision=\frac{TP}{TP+FP}
\]

**Recall**
\[
Recall=\frac{TP}{TP+FN}
\]

**F1 score**
\[
F1=2\frac{Precision\cdot Recall}{Precision+Recall}
\]
These formulae need attention to zero denominators and the chosen positive class.

## Distance and clustering

**Euclidean distance**
\[
d(\mathbf{x},\mathbf{y})=\sqrt{\sum_{j=1}^{m}(x_j-y_j)^2}
\]
Measures straight-line distance between m-dimensional vectors. Features with large numeric scales can dominate this calculation.

**K-means objective**
\[
\sum_{i=1}^{n}\|x_i-\mu_{c_i}\|^2
\]
Sum of squared distances from each sample to its assigned cluster centroid. K-means seeks a locally good grouping under this objective; it is sensitive to initialization and scaling.

## Regression metrics
\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat y_i|
\]
\[
RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2}
\]

MAE is average absolute error. RMSE gives larger errors more weight and has the same units as the target.

## Probability
**Conditional probability**
\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0
\]

**Bayes' theorem**
\[
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
\]
Connects a conditional probability to a reverse conditional probability and prior information.

## Before using a formula
- Define each symbol.
- State any assumptions and denominator conventions.
- Check units and dimensions.
- Calculate one small numerical example by hand.
- Explain what the number tells you and what it does not tell you.
