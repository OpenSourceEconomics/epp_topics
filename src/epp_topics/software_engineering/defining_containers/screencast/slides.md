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
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### Defining custom containers

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Some drawbacks of dictionaries

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> student = {
...   "first_name": "Janos",
...   "last_name": "Gabler",
...   "email": "janos@uni-bonn.de",
... }

>>> student["frist_name"]
------------------------------------------
KeyError Traceback (most recent call last)
...
KeyError: 'frist_name'
```

</div>
<div>

- Typos lead to runtime errors
- Mutable
- Hard to document/know which keys should be there
- No autocomplete for keys

</div>
</div>

---

# NamedTuples

<div class="flex gap-12">
<div>

```python
>>> from typing import NamedTuple

>>> class Student(NamedTuple):
...     first_name: str
...     last_name: str
...     email: str

>>> student = Student(
...     first_name="Janos",
...     last_name="Gabler",
...     email="janos@uni-bonn.de",
... )

>>> student.first_name
'Janos'
```

</div>
<div>

- Typos can be detected by an IDE
- Immutable
- Easy to document/know which attributes are there
- Autocomplete for attributes works

</div>
</div>

---

# Dataclasses

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> from dataclasses import dataclass

>>> @dataclass
... class Student:
...     first_name: str
...     last_name: str
...     email: str

>>> student = Student(
...     first_name="Janos",
...     last_name="Gabler",
...     email="janos@uni-bonn.de",
... )

>>> student.first_name
'Janos'
```

</div>
<div>

- Same advantages as as `NamedTuple`
- Mutable by default but can by made immutable
- Many powerful options: [Documentation](https://docs.python.org/3/library/dataclasses.html)

</div>
</div>

---

# Reminder

- Dictionaries are awesome! One of the most optimized data structures you can imagine.

- You'll need to learn when to use

  - dicts

  - NamedTuples

  - dataclasses
