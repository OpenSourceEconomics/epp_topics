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
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Comprehensions

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Common loop patterns


<div class="grid grid-cols-2 gap-4">
<div>

The mapping loop

```python
>>> squares = []
>>> for i in [1, 2, 3, 4, 5]:
...    squares.append(i ** 2)
>>> squares
[1, 4, 9, 16, 25]
```

The filtering loop

```python
>>> even = []
>>> for i in range(10):
...   if i % 2 == 0:
...      even.append(i)
[0, 2, 4, 6, 8]
```


</div>
<div>

<br/>

- Both initialize and append
- At least three lines
- Can lead to deep indentation

</div>
</div>


---


# List comprehensions

<div class="flex gap-12">
<div>

Set notation

$$
\{x^2 | x \in \{1, 2, 3, 4, 5\}\} \\

\{x | x \in \{0, 1, ..., 9\}, x \mod 2 = 0 \}
$$

List comprehension

```python
>>> [i ** 2 for i in [1, 2, 3, 4, 5]]
[1, 4, 9, 16, 25]
```

```python
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
```

```python
>>> [i if i % 2 == 0 else 0 for i in range(10)]
[0, 0, 2, 0, 4, 0, 6, 0, 8, 0]
```

</div>
<div>

<br/>

- List comprehensions are inspired by set notation
- Can call arbitrary functions
- More readable than loops as long as it fits on one line!
- Not much faster than loops

</div>
</div>


---


# Dict comprehension

<div class="flex gap-12">
<div>

```python
>>> {i: i ** 2 for i in [1, 2, 3, 4, 5]}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
>>> skills = {
...     "Raymond": 8,
...     "Guido": 10,
...     "Tim": 9,
... }
>>> {k: v for k, v in skills.items() if v >= 9}
{'Guido': 10, 'Tim': 9}
```

</div>
<div>

- Inside a dict comprehension you can loop over any iterable
- More readable than loops if it fits on one line

</div>
</div>


---

# When to use


Speed

- Comprehensions are a few percent faster than for loops
- Vectorization can be 100 x faster than for loops


<br/>

Readability

- Comprehensions are more readable if they fit on one line
- Loops are more readable if there are if conditions
