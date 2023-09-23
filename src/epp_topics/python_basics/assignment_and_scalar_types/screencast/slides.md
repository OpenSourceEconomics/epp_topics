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
---

### Effective Programming Practices for Economists

<br>

# Basic Python

### Assigning variables and built-in scalar types

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Contents

- Representing numbers: integers and floats
- Using Python like a calculator
- Comparing variables
- Representing True and False: Booleans

---

# Integers

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = 3
>>> a
3

>>> type(a)
<class 'int'>

>>> type(3)
<class 'int'>

>>> a = 5
>>> a
5
```


</div>
<div>

- Variables are assigned with a single `=` sign
- Types are inferred, not declared upfront
- Types can be inspected with `type()`
- You can re-assign variables with different values
- Ints can hold arbitrarily large numbers



</div>
</div>


---

# Floats

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> b = 3.1415
>>> b
3.1415

>>> type(b)
<class 'float'>

>>> c = 0.1 + 0.2
>>> c
0.30000000000000004
```


</div>
<div>

- Floats represent real numbers
- They are imperfect representations
  - Imperfect precision
  - Can hold values between $-10 ^ {308}$ and $10^{308}$
- Will discuss this in detail later

</div>
</div>


---

# Python as a calculator

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = 3
>>> b = 3.1415

>>> b / a
1.0471666666666668

>>> (a + b) * 3
18.424500000000002

```

</div>
<div>

- Arithmetic works as you would expect
- Brackets work as expected
- Mixing ints and floats converts everything to floats

</div>
</div>


---

# Some things you need to know

<div class="grid grid-cols-2 gap-4">
<div>


```python
>>> a**b
31.54106995953402

>>> b // a
1.0

>>> b % a
0.14150000000000018
```

</div>
<div>

- `**` is exponentiation (not `^`)
- `//` is floored quotient division
- `%` yields the remainder of a division


</div>
</div>


---

# Comparisons

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = 3
>>> b = 3
>>> a == b
True

>>> a < b
False

>>> a >= b
True
```

</div>
<div>

- Comparison operators are `==`, `<`, `>`, `<=`, `>=`
- Remember: `=` is used for assignment, not comparison
- The result of a comparison is a Boolean

</div>
</div>


---

# Booleans

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>

>>> a and b
False

>>> a or b
True

>>> not b
True
```

</div>
<div>

- Booleans can be `True` or `False` (case sensitive)
- `and`, `or` and `not` can be used to express complex conditions
- Fundamental for control flow we will see later

</div>
</div>
