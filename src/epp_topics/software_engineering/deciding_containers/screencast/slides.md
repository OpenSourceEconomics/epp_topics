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
title: EPP — Software Engineering — When to use custom containers?
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### When to use custom containers?

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Fixed or free fields

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> from typing import NamedTuple

>>> class Student(NamedTuple):
...     first_name: str
...     last_name: str
...     email: str

>>> students = {
...    "janosg": Student(
...       first_name="Janos",
...       last_name="Gabler",
...       email="janos@uni-bonn.de",
...     )
...     "timmens": Student(
...       first_name="Tim",
...       last_name="Mensinger",
...       email="tim@uni-bonn.de",
...     )
... }
```

</div>
<div>

- `Student` has the same fixed fields every year
  - Use a NamedTuple or dataclass
- `students` has variable length and keys each year
  - Use a dictionary
- Fixed vs. free fields is the most important aspect when deciding about data structures

</div>
</div>

---

# Immutable or mutable?

> Immutability changes everything (Pat Helland)

<br/>

> Where it is not necessary to change, it is necessary not to change (Lucius Cary)

<br/>

- Immutable objects can avoid many bugs
- Your team members might not be trained in avoiding side-effects
- Unless you have reason to make something mutable, prefer immutable objects
