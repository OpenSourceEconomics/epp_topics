---
# try also 'default' to start simple
theme: academic
# background: https://source.unsplash.com/collection/94734566/1920x1080
# apply any windi css classes to the current slide
class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Effective Programming Practices for Economists
# persist drawings in exports and build
drawings:
  persist: false
# page transition
transition: fade
# use UnoCSS
css: unocss
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

# Topics

- Representing numbers: integers and floats
- Using Python like a calculator
- Comparing variables
- Representing True and False: booleans
- Representing text: Strings
- Converting between types
- More string methods

---

# Integers

<div class="grid grid-cols-2 gap-4">
<div>

```python
a = 3
a
```
```txt
3
```
```python
type(a)
```
```txt
int
```
```python
a = 5
a
```
```txt
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
b = 3.1415
b
```
```txt
3.1415
```
```python
type(b)
```
```txt
float
```
```python
c = 0.1 + 0.2
c
```
```txt
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
a = 3
b = 3.1415
(a + b) * 3
```
```txt
18.424500000000002
```
```python
a**b
```
```txt
31.54106995953402
```
```python
b / a
```
```txt
1.0471666666666668
```
```python
b // a
```
```txt
1.0
```
```python
b % a
```
```txt
0.14150000000000018
```


</div>
<div>

- Arithmetic works as you would expect
- Brackets work as expected
- Mixing ints and floats converts everything to floats
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
a = 3
b = 3
a == b
```
```txt
True
```
```python
a < b
```
```txt
False
```
```python
a >= b
```
```txt
True
```

</div>
<div>

- Comparison operators are `==`, `<`, `>`, `<=`, `>=`
- Remember: `=` is used for assignment, not comparison
- The result of a comparison is a boolean
- Booleans can be `True` or `False`


</div>
</div>


---

# Booleans

<div class="grid grid-cols-2 gap-4">
<div>

```python
a = True
b = False
type(a)
```
```txt
bool
```

</div>
<div>



</div>
</div>




---

# Strings



---

# Casting between types



---

# Everything is an object == Everything has methods

- Any language has `int`, `float` and `string`



---

# Some string methods



---

# String formatting
