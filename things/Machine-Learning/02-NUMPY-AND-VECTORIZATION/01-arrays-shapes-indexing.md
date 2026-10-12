# Lesson 02.1 — NumPy Arrays, Shapes and Indexing

## 1. Lists versus arrays

```python
python_list = [1, 2, 3]
print(python_list * 2)
```

**Output:** `[1, 2, 3, 1, 2, 3]`

Multiplying a Python list by 2 repeats its items. In NumPy, multiplying a numeric array by 2 multiplies each element.

```python
import numpy as np

values = np.array([1, 2, 3])
print(values * 2)
```

**Output:** `[2 4 6]`

An **array** is a collection of values organised in one or more dimensions. A scalar is one number; a vector is a one-dimensional array; a matrix is a two-dimensional array. These labels describe common shapes and maths roles, while NumPy uses the general term ndarray for arrays of any supported dimensionality.

## 2. Shape and dimensions

```python
import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[10, 20, 30], [40, 50, 60]])

print(vector.shape)
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
```

**Output**
```text
(3,)
(2, 3)
2
6
```

Read shape (2, 3) as two rows and three columns. For ML tables, the common convention is shape (number of samples, number of features). For a column vector or higher-dimensional arrays, the shape contains further dimensions; always inspect it rather than guessing.

## 3. Indexing and slicing

```python
import numpy as np

x = np.array([[5, 6, 7], [8, 9, 10]])
print(x[0, 1])
print(x[1])
print(x[:, 0])
```

**Output**
```text
6
[ 8  9 10]
[5 8]
```

x[0, 1] selects row 0, column 1. x[1] selects the second row. x[:, 0] selects every row from column 0. Python indexes start at zero.

## 4. Reshape carefully
A reshape changes how the same ordered values are arranged; it does not create extra values. The new shape must have the same total number of elements.

```python
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print(x.reshape(2, 3))
```

**Output**
```text
[[1 2 3]
 [4 5 6]]
```

There are 6 values and 2×3=6 cells, so the reshape is valid. reshape(4, 2) would fail because it asks for 8 cells. A common ML gotcha is that shape (n,) and shape (n, 1) are different; methods expecting a two-dimensional feature matrix may require the latter.

## 5. dtypes
NumPy arrays normally store values using one array dtype. Inspect with arr.dtype. Mixing unlike values can result in a common type, sometimes causing numerical data to become text. Choose types intentionally when memory or precision matters.

## Questions a beginner might ask
**Why use shape instead of len()?** len() usually gives the first dimension; shape exposes all dimensions.  
**Does slicing always copy?** Many basic slices are views of the original array, so changes may be reflected in the source. Advanced indexing often produces a copy. Check when mutation matters.  
**Why does reshape fail?** The requested dimensions must be compatible with the total element count.

## Practice
1. What shape has np.array([[1,2],[3,4],[5,6]])?
2. What is x[0, 0] for [[7,8],[9,10]]?
3. Write code to create 12 values and reshape them to 3×4.
4. Explain the difference between shape (4,) and shape (4,1).

**Answers:** (3,2); 7; np.arange(12).reshape(3,4); the first is 1-D with four values, the second is 2-D with four rows and one column.
