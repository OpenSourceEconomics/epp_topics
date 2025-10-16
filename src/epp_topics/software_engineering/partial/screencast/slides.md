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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### Partialling arguments to functions

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Example

<div class="flex gap-4">
<div>

```python
>>> from functools import partial

>>> def f(x, y):
...     return x + y

>>> f(x=3)

--------------------------------------------------------
TypeError              Traceback (most recent call last)
/home/janos/file.ipynb Cell 26 line 6
----> 6 f(x=3)

TypeError: f() missing 1 required positional argument: 'y'
```

```python
>>> f_of_x = partial(f, y=3)
>>> f_of_x(x=3)
6
```

</div>
<div>

- `partial` is a higher order function

  - takes a function as argument

  - returns a new function

- Returned function has fewer arguments
  than original function

</div>
</div>

---

# Mental models

- `partial` lets you add or overwrite default values to arguments

- `partial` lets you inject data into functions
  ([closure](<https://en.wikipedia.org/wiki/Closure_(computer_programming)>))

- `partial` lets you partially evaluate a function

---

# Useful applications


- Plotting a mathematical function against one of its arguments

- Creating a function that only depends on a parameter vector

  - For numerical optimization

  - For numerical differentiation

- Keep it in mind as a problem solver!

- Do not over-use it for every function call!
