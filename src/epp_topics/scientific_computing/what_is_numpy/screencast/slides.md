---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### What is numpy?

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is numpy?

- Library providing:
  - Multidimensional arrays
  - Fast elementwise calculations
  - Fast linear algebra
- The mother of all tensor libraries

---

# What is an array?

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> import numpy as np
>>> arr = np.array([[1, 2], [3, 4.0]])
>>> arr
```
```txt
array([[1., 2.],
       [3., 4.]])
```
```python
>>> arr.dtype
dtype('float64')
```


</div>
<div>

- Mental models:
  - 1d array: A vector
  - 2d array: A matrix
  - 3d array: A "list" of matrices
  - ...
- All array entries have the same type


</div>
</div>



---

# Why are calculations on arrays fast?

1. Homogeneous datatype:
   - The datatype of all array elements is known
   - Numpy can get same performance as statically type languages
2. Contiguous memory layout:
   - All array elements are physically stored next to each other in memory
   - This can create enormous performance gains!

This holds for any language!
