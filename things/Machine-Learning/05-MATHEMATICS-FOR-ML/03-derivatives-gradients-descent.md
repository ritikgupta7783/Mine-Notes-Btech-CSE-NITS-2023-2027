# Lesson 05.3 — Derivatives, Gradients and Gradient Descent

## 1. Slope as a rate of change
A derivative describes how a function changes when its input changes a little. For f(w)=w², the derivative is f'(w)=2w. At w=3, f'(3)=6: the local slope is positive, and the function increases as w increases in that neighbourhood.

A gradient generalises a derivative to a function with several parameters. It is a vector containing partial derivatives with respect to each parameter.

## 2. What is an objective/loss?
A model produces predictions ŷ and compares them with known y values. A loss assigns a numeric penalty to prediction errors. An objective J is the quantity the training algorithm tries to minimise (it may include both data loss and a regularisation term).

For one sample, squared error is (y−ŷ)². It is non-negative and penalises large errors more heavily. Choosing a loss is part of defining the learning problem.

## 3. Gradient descent intuition
Imagine walking down a hill when the height function is known locally. The gradient points toward the direction of greatest increase, so moving in the negative-gradient direction can reduce the objective. The update is:
\[
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t)
\]
- θ: current parameter(s).
- ∇J(θ): gradient of the objective at those parameter values.
- η: learning rate or step size.
- θ next: updated parameter(s).

## 4. One numerical step
Let J(w) = (w−3)². Its derivative is 2(w−3). Start at w=0 and choose η=0.1:
- Current slope: 2(0−3)=−6.
- Updated w = 0 − 0.1×(−6) = 0.6.
- The update moves w toward 3, where this simple objective is lowest.

```python
w = 0.0
learning_rate = 0.1
gradient = 2 * (w - 3)
new_w = w - learning_rate * gradient
print(gradient)
print(new_w)
print((w - 3) ** 2, (new_w - 3) ** 2)
```

**Output**
```text
-6.0
0.6000000000000001
9.0 5.76
```

One step reduced this objective from 9 to 5.76. This doesn't mean every arbitrary learning rate or non-convex objective will behave this way. A step that's too large can overshoot or diverge; a very small step can make learning slow.

## 5. Common misconceptions
- The gradient is not always a single number; multi-parameter models have a gradient vector.
- The learning rate is usually a hyperparameter, not a learned model coefficient.
- Gradient descent minimises the chosen objective, not directly “intelligence” or business value.
- Reaching a low training loss doesn't guarantee good generalisation on new data.
- Not every ML algorithm is trained with gradient descent (e.g. a standard decision tree uses splitting criteria).

## Practice
1. If f(w)=(w−5)² at w=2, what is the derivative?
2. With w=2, gradient=−4 and learning rate=0.25, calculate the update.
3. Why can a learning rate that is too large be harmful?
4. How are loss and an objective function related?

**Answers:** −6; updated w=2−0.25×(−4)=3; it can jump past good values or diverge; objective commonly aggregates loss and may add regularisation/other terms.
