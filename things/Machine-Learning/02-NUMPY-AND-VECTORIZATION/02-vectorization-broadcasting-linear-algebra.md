# Lesson 02.2 — Vectorisation, Broadcasting and Linear Algebra

## 1. Element-wise operations

Vectorisation means applying an operation to an array as a whole instead of writing a Python loop for each element. It is usually clearer for numerical work and often faster because NumPy performs loops in compiled code.

```python
import numpy as np
features = np.array([50.0, 70.0, 90.0])
weights = np.array([2.0, 2.0, 2.0])
predictions = features * weights + 20
print(predictions)
```

**Output:** `[120. 160. 200.]`

Each position is calculated separately: 50×2+20=120, 70×2+20=160 and 90×2+20=200. This is a simplified prediction rule, not a trained model.

## 2. Aggregations and axes

```python
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.sum())
print(data.sum(axis=0))
print(data.sum(axis=1))
```

**Output**
```text
21
[5 7 9]
[ 6 15]
```

The whole-array sum is 21. axis=0 reduces rows and leaves one result for each column. axis=1 reduces columns and leaves one result for each row. The words “axis 0” and “axis 1” are easier to remember after checking the resulting shape.

## 3. Broadcasting
Broadcasting lets NumPy combine compatible shapes without manually repeating every value. A scalar broadcasts across an array. For example, adding 10 to [1,2,3] yields [11,12,13]. For higher dimensions, shapes are compared from the rightmost dimension; each pair must match or one of the dimensions must be 1 (with special rules for missing dimensions).

```python
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
offsets = np.array([10, 20, 30])
print(matrix + offsets)
```

**Output**
```text
[[11 22 33]
 [14 25 36]]
```

The shape of matrix is (2,3), and offsets is (3,). The trailing 3 dimensions match; the vector is used for each row. Adding a vector of shape (2,) here fails because its dimensions do not align with the matrix's last dimension 3.

## 4. Dot product and matrix multiplication
For vectors of the same length, the dot product multiplies matching positions and adds the products. For [1,2,3] and [10,20,30], result is 1×10 + 2×20 + 3×30 = 140.

```python
import numpy as np
x = np.array([1, 2, 3])
w = np.array([10, 20, 30])
print(np.dot(x, w))

X = np.array([[1, 2], [3, 4], [5, 6]])
weights = np.array([2, 10])
print(X @ weights)
```

**Output**
```text
140
[22 46 70]
```

X has shape (3,2); weights has shape (2,); X @ weights yields one prediction per row, shape (3,). The @ operator denotes matrix multiplication. For this input, each output is row dot weights: 1×2+2×10=22; 3×2+4×10=46; 5×2+6×10=70.

## 5. Random values reproducibly
Use a random generator with a fixed seed for repeatable examples.

```python
import numpy as np
rng = np.random.default_rng(42)
print(rng.integers(0, 10, size=4))
```

The values are reproducible in the same NumPy setup for this generator usage. Randomness in a simulation should be controlled when comparing experiments, but a fixed seed does not make an experiment scientifically valid by itself.

## Common mistakes
- Using * expecting matrix multiplication instead of element-wise multiplication.
- Forgetting shape compatibility with @ or broadcasting.
- Assuming axis numbers mean the same intuitive direction without inspecting output shape.
- Using np.dot and @ interchangeably in high dimensions without understanding their rules.
- Assuming vectorisation changes the mathematical result (it should implement the same operation, aside from floating-point details).

## Practice
1. Calculate the dot product of [2,3] and [4,5].
2. What shape results from matrix shape (5,3) multiplied by weights shape (3,) using @?
3. Predict np.array([1,2]) + 10.
4. Why will shape (2,3) plus shape (2,) fail under ordinary broadcasting?

**Answers:** 23; (5,); [11,12]; last dimensions 3 and 2 are neither equal nor 1.
