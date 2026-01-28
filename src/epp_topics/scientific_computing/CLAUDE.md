# Scientific Computing with NumPy - Guidelines for AI Agents

This document provides guidance for AI coding agents on how to write effective NumPy
code based on the best practices taught in this chapter.

## Table of Contents

1. [NumPy Fundamentals](#numpy-fundamentals)
1. [Creating Arrays](#creating-arrays)
1. [Indexing Arrays](#indexing-arrays)
1. [Calculations on Arrays](#calculations-on-arrays)
1. [Calculations Between Arrays](#calculations-between-arrays)
1. [Broadcasting](#broadcasting)
1. [Random Number Generation](#random-number-generation)
1. [Performance Optimization](#performance-optimization)
1. [Using Numba](#using-numba)

______________________________________________________________________

## NumPy Fundamentals

### What is NumPy?

NumPy is a library providing multidimensional arrays, fast elementwise calculations, and
fast linear algebra. It is the foundation for all tensor libraries (PyTorch, JAX,
TensorFlow).

### Mental Models for Arrays

- 1D array: A vector
- 2D array: A matrix
- 3D array: A "list" of matrices
- Higher dimensions: Lists of lists of matrices or vectors

### DO

- Think of arrays as homogeneous collections where all elements have the same dtype
- Use NumPy when you need fast numerical calculations
- Remember that NumPy knowledge transfers to JAX, PyTorch, TensorFlow

### DON'T

- Don't assume arrays can have mixed types like Python lists
- Don't write pure Python loops over array elements for performance-critical code

______________________________________________________________________

## Creating Arrays

### Array Creation Methods

```python
import numpy as np

# From lists
arr = np.array([1, 2, 3, 4])
arr_2d = np.array([[1, 2], [3, 4]])

# Constructors
np.ones(3)  # [1., 1., 1.]
np.ones((2, 2))  # 2x2 matrix of ones
np.zeros((3, 4))  # 3x4 matrix of zeros
np.zeros_like(arr)  # Zeros with same shape as arr
np.ones_like(arr)  # Ones with same shape as arr
np.empty((2, 3))  # Uninitialized array (faster but contains garbage)
np.arange(5)  # [0, 1, 2, 3, 4]
np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
np.eye(3)  # 3x3 identity matrix
np.full((2, 3), 7)  # 2x3 array filled with 7
```

### Reshaping

```python
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape((2, 3))  # Shape (2, 3) - 2 rows, 3 columns
# Elements are arranged in row-major order
```

### DO

- Use constructors like `np.zeros`, `np.ones`, `np.arange` for creating test inputs
- Use `np.empty` when you will immediately fill the array (slightly faster)
- Use `-1` in reshape to infer one dimension: `arr.reshape(-1, 3)`
- Learn array creation functions like vocabulary

### DON'T

- Don't create arrays from ragged (unequal length) nested lists
- Don't use `np.empty` if you won't immediately fill all values

______________________________________________________________________

## Indexing Arrays

### Basic Indexing

```python
a = np.array([0, 1, 2, 3, 4])

a[2]  # Single element: 2
a[-1]  # Last element: 4
a[1:3]  # Slice: [1, 2]
a[2:]  # From index 2 to end: [2, 3, 4]
a[[0, 3]]  # Fancy indexing: [0, 3]
a[[True, False, True, False, True]]  # Boolean indexing: [0, 2, 4]
```

### 2D Indexing

```python
b = np.arange(12).reshape(4, 3)

b[2]  # Select row 2
b[:, 2]  # Select column 2
b[1, 2]  # Select element at row 1, column 2
b[:2, :2]  # Select top-left 2x2 subarray
```

### DO

- Use slicing for selecting contiguous regions
- Use boolean indexing for conditional selection
- Separate dimension indices with commas: `arr[row, col]`
- Omit later dimensions if you don't want to restrict them

### DON'T

- Don't forget that indexing starts at 0
- Don't forget that slices include the lower bound but exclude the upper bound

______________________________________________________________________

## Calculations on Arrays

### Mathematical Functions

```python
a = np.array([1, 1.5, 2])

np.exp(a)  # Elementwise exponential
np.log(a)  # Elementwise natural log
np.sqrt(a)  # Elementwise square root
np.sin(a)  # Elementwise sine
```

### Reductions

```python
a = np.array([[1, 2], [3, 4]])

a.mean()  # Mean of all elements: 2.5
a.std()  # Standard deviation
a.sum()  # Sum of all elements: 10
a.sum(axis=0)  # Sum along axis 0 (columns): [4, 6]
a.sum(axis=1)  # Sum along axis 1 (rows): [3, 7]
a.sum(axis=-1)  # Sum along last axis
```

### Vectorization

Vectorization means operating on entire arrays at once instead of looping over elements.
The loops still exist but run in compiled C code.

### DO

- Use NumPy functions instead of Python loops - they are faster and more readable
- Use the `axis` argument for reductions along specific dimensions
- Use `axis=-1` to operate along the last axis regardless of array dimensionality
- Learn to think in terms of array operations, not element-by-element operations

### DON'T

- Don't use Python loops or list comprehensions for numerical operations
- Don't forget that NumPy functions typically apply elementwise

______________________________________________________________________

## Calculations Between Arrays

### Multiplication Types

```python
a = np.arange(4).reshape(2, 2)
b = np.array([[0.1, 0.2], [0.3, 0.4]])

a * b  # Elementwise multiplication
a @ b  # Matrix multiplication
a.dot(b)  # Matrix multiplication (alternative syntax)
```

### Other Operations

```python
a + b  # Elementwise addition
a - b  # Elementwise subtraction
a / b  # Elementwise division (warning: division by zero gives inf, not error)
a**b  # Elementwise exponentiation
```

### DO

- Use `*` for elementwise multiplication
- Use `@` or `.dot()` for matrix multiplication
- Be aware that division by zero produces `inf` or `nan`, not an error

### DON'T

- Don't confuse `*` (elementwise) with `@` (matrix multiplication)
- Don't assume division by zero will raise an exception

______________________________________________________________________

## Broadcasting

Broadcasting allows operations between arrays of different shapes by automatically
expanding smaller arrays.

### Broadcasting Rule

> Two arrays are compatible for broadcasting if for each trailing dimension (starting
> from the end) the axis lengths match or if either of the lengths is 1. Broadcasting is
> then applied over the missing or length 1 dimensions.

### Examples

```python
a = np.zeros((2, 3), dtype=np.int64)

# Scalar broadcasting
a + 1  # Add 1 to every element

# Row-wise broadcasting
a + np.array([1, 2, 3])  # Shape (3,) broadcasts to (2, 3)

# Column-wise broadcasting
a + np.array([[4], [5]])  # Shape (2, 1) broadcasts to (2, 3)

# Outer product via broadcasting
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
x.reshape(3, 1) * y  # Equivalent to np.outer(x, y)
```

### DO

- Use broadcasting instead of repeating arrays - it saves memory and is faster
- Think about shapes from the trailing dimensions (right to left)
- Use reshaping to add dimensions for broadcasting: `arr.reshape(-1, 1)`
- Prefer broadcasting over explicit `np.repeat` or `np.tile`

### DON'T

- Don't use `repeat` when broadcasting can achieve the same result
- Don't be discouraged if broadcasting is confusing at first - practice with toy
  examples

______________________________________________________________________

## Random Number Generation

### Modern API (Use This)

```python
# Create a random number generator with a seed
rng = np.random.default_rng(5471)

# Generate random numbers
rng.uniform(low=0, high=1, size=3)  # Uniform distribution
rng.normal(loc=0, scale=1, size=(2, 3))  # Normal distribution
rng.integers(0, 10, size=5)  # Random integers
```

### DO

- Always create an RNG with a seed: `rng = np.random.default_rng(seed)`
- Generate seeds randomly (don't always use 123, 42, etc.)
- Verify that your main results don't change when you change the seed
- Pass the `rng` object to functions that need randomness

### DON'T

- **Never use the legacy global seed API**: `np.random.seed()` is deprecated
- **Never use `np.random.default_rng()` without a seed** - results won't be reproducible
- Don't use `np.random.rand()`, `np.random.randn()`, etc. (legacy API)

### Example of Proper Random Number Handling

```python
# GOOD
def simulate(n_samples, rng):
    return rng.normal(size=n_samples)


rng = np.random.default_rng(8374629)
results = simulate(1000, rng)

# BAD - Don't do this
np.random.seed(42)  # Legacy API
results = np.random.randn(1000)  # Legacy API
```

______________________________________________________________________

## Performance Optimization

### The Optimization Process

1. **Get it to run** - Make sure code works correctly
1. **Get it right** - Add tests to verify correctness
1. **Find the bottleneck** - Use profiling (snakeviz, line_profiler)
1. **Speed up the bottleneck on one core** - Vectorization, better algorithms
1. **Consider parallelization** - Only after single-core optimization
1. **Repeat**

### Measuring Runtime

```text
# In Jupyter notebooks - for fast functions
%timeit my_function(args)
```

```python
# For slow functions or outside notebooks
from time import perf_counter

start = perf_counter()
my_function(args)
runtime = perf_counter() - start
```

### Why NumPy Can Be Fast

1. Homogeneous dtype - all elements have known types
1. Contiguous memory layout - efficient CPU cache usage
1. Python overhead incurred once per array, not once per element
1. Functions implemented by experts in low-level languages

### DO

- **Vectorize everything** - Use array operations instead of loops
- **Use broadcasting** instead of repeating arrays
- **Prefer few large arrays** over many small arrays
- **Use representative input sizes** when benchmarking
- **Use `time.perf_counter`** instead of `time.time` (higher resolution on Windows)
- **Profile before optimizing** - Use snakeviz to find bottlenecks

### DON'T

- **Don't use array operations inside loops** - This is typically very slow

```python
# BAD - Array operations inside a loop
def slow_function(factors, weights, a):
    out = np.empty(len(factors))
    for i in range(len(factors)):
        out[i] = a * np.prod(factors[i] ** weights)  # np.prod called many times
    return out


# GOOD - Fully vectorized
def fast_function(factors, weights, a):
    return a * np.prod(factors**weights, axis=-1)  # np.prod called once
```

- **Don't optimize prematurely** - "Premature optimization is the root of all evil"
- **Don't assume rewriting in another language will help** - Optimized Python can beat
  naive Fortran/Julia
- **Don't use DataFrames or dicts in performance-critical inner loops** - Use arrays

### Performance Anti-Patterns to Avoid

1. **Looping over rows of a DataFrame** - Extremely slow
1. **Using dicts where arrays would work** - Much slower indexing
1. **Array operations in a loop** - Incurs Python overhead repeatedly
1. **Creating many small arrays** - Array creation has overhead

### Speedup Example

```python
# SLOW: 25 ms - Array operations in a loop
def array_cobb_douglas(factors, weights, a):
    out = np.empty(len(factors))
    for i in range(len(factors)):
        out[i] = a * np.prod(factors[i] ** weights)
    return out


# FAST: 215 us - Fully vectorized (110x speedup!)
def vectorized_array_cobb_douglas(factors, weights, a):
    return a * np.prod(factors**weights, axis=-1)
```

______________________________________________________________________

## Using Numba

Numba is a just-in-time compiler that can make Python loops as fast as C/Julia.

### Basic Usage

```python
from numba import njit


@njit
def numba_function(factors, weights, a):
    out = np.empty(len(factors))
    for i in range(len(factors)):
        out_i = a
        for j in range(len(weights)):
            out_i *= factors[i, j] ** weights[j]
        out[i] = out_i
    return out
```

### When to Use Numba

- When full vectorization is difficult or impossible
- When you need to avoid intermediate arrays (memory constraints)
- When you've profiled and found a clear bottleneck

### DO

- **Write out all loops explicitly** for best performance with Numba
- **Use only scalars and arrays** inside Numba functions
- **Only apply Numba to bottlenecks**, not your entire codebase
- **Benchmark both approaches** - Numba isn't always faster than vectorized NumPy

### DON'T

- Don't use dicts, lists, or complex objects inside Numba functions
- Don't call non-compiled functions from inside Numba functions
- Don't expect Numba to magically speed up already-vectorized NumPy code
- Don't use `@njit` on all functions - only on identified bottlenecks

### Numba vs Vectorized NumPy

- Vectorized NumPy: Often fastest for operations that map well to existing functions
- Numba: Better when you need custom loop logic or want to avoid intermediate arrays
- **Either full vectorization OR full loops** - mixing is usually slow

```python
# Comparison for Cobb-Douglas example:
# Original with loop:        ~25 ms
# Naive Numba (partial):     ~1.2 ms  (20x speedup)
# Numba with full loops:     ~600 us  (40x speedup)
# Fully vectorized NumPy:    ~215 us  (110x speedup)
```

______________________________________________________________________

## Quick Reference: Common Patterns

### Normalize rows of a matrix

```python
# Each row sums to 1
normalized = arr / arr.sum(axis=1, keepdims=True)
```

### Apply function along an axis

```python
# Mean of each row
row_means = arr.mean(axis=1)

# Mean of each column
col_means = arr.mean(axis=0)
```

### Conditional operations

```python
# Set negative values to zero
arr[arr < 0] = 0

# Or use np.where
result = np.where(arr < 0, 0, arr)
```

### Outer operations via broadcasting

```python
# Pairwise differences
a = np.array([1, 2, 3])
b = np.array([4, 5])
diff = a.reshape(-1, 1) - b  # Shape (3, 2)
```

### Weighted sum/product along axis

```python
# Weighted sum
weights = np.array([0.2, 0.3, 0.5])
data = np.random.rand(100, 3)
weighted_sum = (data * weights).sum(axis=1)

# Or using matrix multiplication
weighted_sum = data @ weights
```
