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

### Calculations between arrays

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Two types of multiplication

<div class="flex gap-10">
<div>

```python
>>> a = np.arange(4).reshape(2, 2)
>>> b = np.linspace(0.1, 0.4, 4).reshape(2, 2)
>>> b
array([[0.1, 0.2],
       [0.3, 0.4]])
```

```python
>>> a * b
array([[0. , 0.2],
       [0.6, 1.2]])
```

```python
>>> a @ b
array([[0.3, 0.4],
       [1.1, 1.6]])
```

```python
>>> a.dot(b)
array([[0.3, 0.4],
       [1.1, 1.6]])
```

</div>
<div>

- `*` means elementwise multiplication
- `@` and `.dot` mean matrix multiplication
- Both generalize to high dimensions
- They have different requirements on array shapes

</div>
</div>


---
layout: center
---

# Other operations between arrays

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.arange(3)
>>> b = np.ones(3)
>>> a + b
array([1., 2., 3.])
```

```python
>>> a - b
array([-1.,  0.,  1.])
```

```python
>>> a / b
array([0., 1., 2.])
```

```python
>>> b / a
RuntimeWarning: divide by zero encountered in divide
array([inf, 1. , 0.5])
```

```python
>>> (b * 2) ** a
array([1., 2., 4.])
```

</div>
<div>

- Addition, subtraction and division work as expected
- Division by zero does not raise an error
- Exponentiation uses `**`

</div>
</div>
