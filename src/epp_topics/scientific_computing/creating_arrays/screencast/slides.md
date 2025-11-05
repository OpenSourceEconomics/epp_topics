---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: EPP — Scientific Computing — Creating arrays
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Creating arrays

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Creating arrays from lists

<div class="grid grid-cols-2 gap-4">
<div>

Flat list
```python
>>> np.array([1, 2, 3, 4])
array([1, 2, 3, 4])
```
Nested list
```python
>>> np.array([[1, 2], [3, 4])
array([[1, 2],
       [3, 4]])
```
Mixed dtypes in list
```python
>>> np.array([[1, 2], [3.1, 4])
array([[1. , 2. ],
       [3.1, 4. ]])
```
</div>
<div>

<br/>
<br/>
<br/>

- Can use flat or (deeply) nested lists
- Lists length cannot be rugged
- List might have mixed dtypes, arrays will not!


</div>
</div>



---

# Constructors

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> np.ones(3)
array([1., 1., 1.])
```

```python
>>> np.ones((2, 2))
array([[1., 1.],
       [1., 1.]])
```

```python
>>> np.arange(3)
array([0, 1, 2])
```

```python
>>> np.eye(2)
array([[1., 0.],
       [0., 1.]])
```

</div>
<div>

- `np.ones_like`
- `np.zeros` and `np.zeros_like`
- `np.empty`
- `np.linspace`
- `np.full`
- More in the ([documentation](https://numpy.org/doc/stable/reference/routines.array-creation.html))
- Learn them like vocabulary!


</div>
</div>

---

# Reshaping

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> b = a.reshape((2, 3))
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```
```python
>>> b.shape
(2, 3)
```

</div>
<div>

- Reshape can transform arrays from one shape to another
- Shapes are denoted as in matrices, i.e. (`n_rows`, `n_cols`)
- Number of elements must not change
- Elements aranged in row-major order


</div>
</div>


---

# Repeating arrays

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([1, 2, 3])
>>> a.repeat(2)
```
```txt
array([1, 1, 2, 2, 3, 3])
```
```python
>>> b = np.array([[1, 2], [3, 4]])
>>> b.repeat(2)
```
```txt
array([1, 1, 2, 2, 3, 3, 4, 4])
```
```python
>>> b.repeat(2, axis=1)
```
```txt
array([[1, 1, 2, 2],
       [3, 3, 4, 4]])
```
```python
>>> a.reshape(-1, 1).repeat(2, axis=1)
```
```txt
array([[1, 1],
       [2, 2],
       [3, 3]])
```
</div>
<div>

- `repeat` duplicates elements n times
- Without axis, result is flattened
- Versatile together with reshaping
- Tip for complex cases:
  - First introduce new dimensions via reshaping
  - Then repeat along these axes
- Always prefer broadcasting over repetition!

</div>
</div>
