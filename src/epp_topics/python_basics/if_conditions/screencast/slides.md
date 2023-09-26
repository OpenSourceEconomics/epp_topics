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
title: Effective Programming Practices for Economists
defaults:
  layout: center
themeConfig:
  paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br>

# Basic Python

### if conditions

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Contents

- `if`, `elif`, and `else`
- More on Booleans
- More complex conditions
- Filtering loops

---

# Motivation

- So far, all of our instructions in Python were very explicit
- There was no way of reacting to different situations:
  - Collecting elements of a list that fulfil a condition
  - Doing different things for different types of variables
  - ...
- This is what if-conditions are for



---

# Example: clipping a number


<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

```python
>>> number = -3.1

>>> if number < -3:
...     clipped = -3.0
... elif number > 3:
...     clipped = 3.0
... else:
...     clipped = number

>>> clipped
-3.0
```

</div>
<div class="col-span-3">

- `if`, `elif`, and `else` are special keywords
- End each condition with a `:`
- What happens if that condition is `True` needs to be indented by 4 spaces and can span
  one or multiple lines
- Code following `False` conditions is skipped
- `elif x:` is the same as <br> `else:` + nested `if x:`

</div>
</div>


---

# More on Booleans


<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> bool(0)
False

>>> bool(-1)
True

>>> bool(1)
True

>>> bool([])
False

>>> bool([1, 2, 3])
True

>>> bool("")
False

>>> bool("abc")
True
```

</div>
<div>

- What is not a Boolean can be converted to a Boolean
- This conversion happens implicitly after `if` and `elif`
- Can be useful and elegant but might compromise readability
- Rules of thumb:
  - 0 is `False`-ish
  - Other numbers are `True`-ish
  - Len-0 collections are `False`-ish
  - Len>0 collections are `True`-ish

</div>
</div>

---

# More complex conditions

- Remember operators from "Assignments and Scalar Types":
  - `and`
  - `or` (inclusive)
  - `not`

<br>

- Example:

<br>

```python
if a > b and b > some_cutoff:
    do_something()
else:
    do_something_else()
```


---

# Filtering loops

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> names = ["Guy", "Ray", "Tim"]
>>> names_with_i = []
>>> for n in names:
>>>     if "i" in n:
>>>       names_with_i.append(n)
>>> names_with_i
['Tim']
```

</div>
<div>

- Can filter lists based on properties of items
- Can filter dictionaries based on properties of keys and/or values
- Example usecases:
  - Find elements above a cutoff
  - Extract female names
  - Exclude invalid data

</div>
</div>
