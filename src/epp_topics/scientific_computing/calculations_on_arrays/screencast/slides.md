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

### Calculations on arrays

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Mathematical functions

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([1, 1.5, 2])
>>> np.exp(a)
array([2.71828183, 4.48168907, 7.3890561 ])
```

```python
>>> np.log(a)
array([0.        , 0.40546511, 0.69314718])
```

```python
>>> np.sqrt(a)
array([1.        , 1.22474487, 1.41421356])
```

```python
>>> np.sin(a)
array([0.84147098, 0.99749499, 0.90929743])
```

</div>
<div>

- Numpy functions usually apply elementwise
- Faster and more readable than looping
- For more functions see the [docs](https://numpy.org/doc/stable/reference/routines.math.html)


</div>
</div>


---

# Reductions


<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([[1, 2], [3, 4]])
>>> a.mean()
2.5
```

```python
>>> a.prod()
24
```

```python
>>> a.sum()
10
```

```python
>>> a.std()
1.118033988749895
```

```python
>>> a.sum(axis=1)
array([3, 7])
```

</div>
<div>

- Reductions take an array of numbers and reduce it to fewer numbers
- Again, faster and more readable than loops
- All reductions support axis arguments

</div>
</div>


---

# Vectorization

- The above functions are all vectorized

<br/>

> Vectorization is the process of converting an algorithm from operating on a single
> value at a time to operating on a set of values (vector) at a time.
> Hence, we can use these techniques to perform operations on Numpy arrays without
> using loops.

<br/>

- The loops are still there, but now in a compiled language
- Faster than Python loops, list comprehensions, ...
- Sometimes vectorization makes code more readable


---

# Linear algebra

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([[1, 0], [0, 4]])
>>> np.linalg.inv(a)
```
```txt
array([[1.  , 0.  ],
       [0.  , 0.25]])
```
```python
>>> np.linalg.cholesky(a)
```
```txt
array([[1., 0.],
       [0., 2.]])
```

</div>
<div>

- All matrix decompositions you'll ever need are implemented
- Check out the [documentation](https://numpy.org/doc/stable/reference/routines.linalg.html)
for an overview

</div>
</div>
