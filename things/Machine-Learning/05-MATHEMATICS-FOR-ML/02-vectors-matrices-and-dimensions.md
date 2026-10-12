# Lesson 05.2 — Vectors, Matrices and Dimensions

## 1. Scalars, vectors and matrices
A scalar is one value, such as 4. A vector is an ordered list of values, such as [50, 2]. A matrix is a table of values, such as:
\[
X=\begin{bmatrix}50&1\\70&2\\90&3\end{bmatrix}
\]
It has shape (3,2): three samples and two features.

## 2. Dot product
The dot product multiplies matching positions and sums them:
\[
[50,2]\cdot[2,10]=50\times2+2\times10=120
\]
In a linear model with two features, each input is multiplied by its weight, the results are added and the bias is added:
\[
\hat y=\mathbf{x}\cdot\mathbf{w}+b
\]
For x=[50,2], w=[2,10], b=20, prediction = 120+20=140.

## 3. Why shapes matter
If X has shape (n,p) and weights w has shape (p,), then X @ w produces one value per row, with shape (n,). The number of features p must match the number of weights. A shape error is often a clue that we have the wrong representation, not a problem to solve by blindly reshaping.

```python
import numpy as np

X = np.array([[50, 1], [70, 2], [90, 3]])
w = np.array([2, 10])
b = 20
predictions = X @ w + b

print(X.shape)
print(w.shape)
print(predictions)
```

**Output**
```text
(3, 2)
(2,)
[130 180 230]
```

Dry run for the first row: 50×2 + 1×10 + 20 = 130. The operation repeats the same weight vector for each sample row.

## 4. Matrix multiplication
For matrices A of shape (r,k) and B of shape (k,c), A @ B results in shape (r,c). The inner dimensions k must match. It combines rows of A with columns of B via dot products. Element-wise A * B is a different operation.

## 5. Transpose and transformations
The transpose flips a matrix's rows and columns: a (2,3) matrix becomes (3,2). Linear transformations include operations such as rotation, scaling or mapping input vectors through a matrix. In ML, matrix operations represent many samples at once.

## Beginner questions
**Why does ML use matrices?** They organise many samples/features and let numerical libraries calculate many predictions efficiently.  
**Why does X often have two dimensions but y one?** X has one row per sample and one column per feature; y often contains one target per sample. Multitask targets can make y two-dimensional.  
**Does every model use a dot product?** No. A linear model does; trees partition features through rules, while other algorithms use different calculations.

## Practice
1. Find [3,4] dot [10,2].
2. What shape results from (5,3) @ (3,2)?
3. Explain why (5,3) @ (4,) fails.
4. What is the shape after transposing a (2,5) array?

**Answers:** 38; (5,2); inner dimensions 3 and 4 don't match; (5,2).
