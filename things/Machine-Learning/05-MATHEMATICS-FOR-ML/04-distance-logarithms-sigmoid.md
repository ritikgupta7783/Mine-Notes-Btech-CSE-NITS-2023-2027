# Lesson 05.4 — Distance, Logarithms and Sigmoid Intuition

## 1. Euclidean distance
For two feature vectors, Euclidean distance is the straight-line distance:
\[
d(\mathbf{x},\mathbf{y})=\sqrt{\sum_j(x_j-y_j)^2}
\]
Example: distance between (1,2) and (4,6) is √((4−1)²+(6−2)²)=√(9+16)=5.

Manhattan distance sums absolute differences: |1−4|+|2−6|=7. Cosine similarity compares the angle between vectors and is commonly used with text vectors. These measures answer different notions of similarity.

## 2. Why scaling matters
If one feature is salary in thousands and another feature is age in years, raw Euclidean distance may be dominated by salary. Standardisation or another scaling method can make distance-based methods more balanced, but the right choice depends on feature meaning and the algorithm.

## 3. Exponentials and sigmoid
The sigmoid function is:
\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]
It maps any finite real score z to a value between 0 and 1. For z=0, sigmoid is 0.5. For a large positive z, it approaches 1; for a large negative z, it approaches 0. Logistic regression uses this function to model the probability of one class in a binary classification setting.

The number is not automatically a well-calibrated real-world probability; calibration and model assumptions still matter.

## 4. Log loss intuition
Logarithms penalise confident wrong probability estimates strongly. If the true class is 1, assigning probability 0.99 gives a small negative log-likelihood loss, while assigning 0.01 gives a much larger loss. The probability should be clipped carefully only for numerical computations; conceptually, confident wrong predictions deserve strong penalties under log loss.

## Practice
1. Compute Euclidean distance between (0,0) and (3,4).
2. What is sigmoid(0)?
3. Why can KNN predictions change when a feature is measured in dollars rather than thousands of dollars?
4. Why isn't a predicted probability automatically guaranteed to be calibrated?

**Answers:** 5; 0.5; its numeric scale can dominate distance; calibration must be checked on relevant held-out data.
