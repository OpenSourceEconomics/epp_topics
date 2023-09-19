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

### Strings

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Topics

- Representing text: Strings
- Methods to manipulate strings
- String formatting

---


# Assigning strings

<div class="grid grid-cols-2 gap-4">
<div>

```python
a = "Hello"
type(a)
```
```python
b = 'single quote string with embedded "double" quotes'
c = "double quote string with embedded 'single' quotes"
```
```python
not_an_int = "123"
type(not_an_int)
```
```txt
str
```
```python
not_an_int * 2
```
```txt
'123123'
```


</div>
<div>

- Strings can hold arbitrary text data
- Defined with single or double quotes
- Strings containing numbers do not behave like numbers!

</div>
</div>


---

# Everything is an object == Everything has methods

- Any language has `int`, `float`, `bool` and `string`
- C, Fortran, ...:
  - low level types to store data efficiently and do fast calculations
- Python: Everything is an object
  - Objects with convenient methods
  - Trade efficiency for convenience
  - We can still get efficient when needed!

---

# Some string methods


<div class="grid grid-cols-2 gap-4">
<div>

```python
a = "Hello World!"
a.lower()
```
```txt
'hello world!'
```
```python
a.replace("!", ".")
```
```txt
"Hello World."
```
```python
a.startswith("Hello")
```
```txt
True
```

</div>
<div>

- There are many methods for string manipulation
- [Full documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

</div>
</div>


---

# String formatting


<div class="grid grid-cols-2 gap-4">
<div>

```python
a = "Hello"
b = "3"
c = 3
f"{a} {b}"
```

```txt
'Hello 3'
```

</div>
<div>

- `f-strings` allow you to puzzle together different strings
- Many useful applications:
  - Embed results of calculations in messages
  - Write good error messages
- Variables used in formatting are automatically converted to strings

</div>
</div>


---

# Strings are actually containers


<div class="grid grid-cols-2 gap-4">
<div>

```python
a = "Hello World!"
len(a)
```
```txt
12
```
```python
a[0]
```
```txt
'H'
```
```python
a[1]
```
```txt
'e'
```
```python
a[:5]
```
```txt
'Hello'
```

</div>
<div>

- Most of the time, you can think of strings as scalar variables
- They are actually containers
    - Have a length
    - Can be sliced
- More on containers in the next screencast!

</div>
</div>