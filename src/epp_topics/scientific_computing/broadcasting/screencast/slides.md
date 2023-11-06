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

### Broadcasting

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Examples of broadcasting

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.zeros((2, 3))
# element-wise addition
>>> a + 1
```
```txt
array([[1., 1., 1.],
       [1., 1., 1.]])
```
```python
# row-wise addition
>>> a + np.array([1, 2, 3])
```
```txt
array([[1., 2., 3.],
       [1., 2., 3.]])
```
```python
# column-wise addition
a + np.array([[1], [2]])
```
```txt
array([[1., 1., 1.],
       [2., 2., 2.]])
```

</div>
<div>

<br/>
<br/>

- Arrays don't have to have identical shapes to do calculations between them
- Smaller arrays are broadcasted to the larger shape
- Shapes need to be compatible as defined by the broadcasting rules
- More efficient than repeating arrays!

</div>
</div>


---

# The broadcasting rule

<br/>

> Two arrays are compatible for broadcasting if for each *trailing dimension** (i.e.,
> starting from the end) the axis lengths match or if either of the lengths is 1.
> Broadcasting is then applied over the missing or length 1 dimensions

<br/>
<br/>

More information and examples in the [documentation](https://numpy.org/doc/stable/user/basics.broadcasting.html)


---

# Advanced example: Outer product


<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.outer(a, b)
```
```txt
array([[ 4,  5,  6],
       [ 8, 10, 12],
       [12, 15, 18]])
```
```python
>>> a * b.reshape(3, 1)
```
```txt
array([[ 4,  5,  6],
       [ 8, 10, 12],
       [12, 15, 18]])
```

</div>
<div>

<br/>
<br/>

- Here, broadcasting is used to calculate an outer product without using the `np.outer`
function
- a is implicitly treated as a row vector
- b is reshaped to a column vector

</div>
</div>
