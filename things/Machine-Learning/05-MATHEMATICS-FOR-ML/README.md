# Module 05 — Mathematics for Machine Learning

**Prerequisites:** Python basics and the NumPy shape lessons. **Goal:** understand the simple maths used by ML rather than memorising notation.

## Learning order
1. [Numbers, functions and linear equations](01-functions-equations-and-graphs.md)
2. [Vectors, matrices and dot products](02-vectors-matrices-and-dimensions.md)
3. [Slope, derivatives and gradient descent](03-derivatives-gradients-descent.md)
4. [Distance, logarithms and sigmoid intuition](04-distance-logarithms-sigmoid.md)

## Notation used in this course
- x: input for one sample, or feature value when clearly stated.
- y: true target.
- ŷ (“y-hat”): predicted target.
- w: weight/coefficient; b: bias/intercept.
- n: number of samples; p: number of features (notation varies by text).
- J(w,b): objective/cost function.
- η: learning rate.
- Σ: summation; ∇: gradient.

Always read the definitions near a formula; the same letter can mean different things in a different context.

## Why this module matters
A linear model combines features using weights. Training tries to select weights that minimise a loss. KNN and K-means use distance. Logistic regression maps a score to a probability. These ideas are difficult to reason about if vectors, shapes, slopes and losses remain mysterious.
