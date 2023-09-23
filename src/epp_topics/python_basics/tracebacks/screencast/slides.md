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

### Tracebacks

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Topics

- What are Exceptions and Tracebacks?
- The Anatomy of a Python Traceback
- Reading long tracebacks
- Asking for help


---

# Motivation

- We sometimes told you that you cannot do certain things:
  - Example: Can only use hashable objects as dictionary keys
- Now we will discuss what happens if you do it anyways
  - Exception: What class of error?
  - Traceback: Detailed report that helps you to localize the error
- Pro tip: Read the traceback!


---

# Example Traceback

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> d = {"a" : 1}
>>> d[[1, 2, 3]] = "b"
>>> d["c"] = 3
```
<br/>

<img src="/simple_traceback.png" class="rounded" width="400"/>

</div>
<div>

- The code on the left has a problem
- Traceback tells us everything we need:
  1. What type of Exception ocurred: TypeError
  2. Where did it occur: In line 2 of some_file.py
  3. What exactly happened: Used an unhashable type where we should not
- Tracebacks can get very long!
- Always look for these three things!

</div>
</div>

---

# Common sources of errors

- ValueError: You called a function with something invalid
- KeyError: You have a typo in a variable name or a dictionary key
- TypeError: You called the function with something that has the wrong type
- ImportError: You have a typo in an import
- ModuleNotFoundError: You did not activate the environment or need to install a package


---

# How not to ask for help

- "I wanted to do the exercise but it does not work"
- "Python does not work on my computer"
- "My code does not work, here is a screenshot"

---

# What to keep in mind

- We do not remember what task 3 in exercise 5 is
- We like to see that you tried on your own
- We like to see that you tried to reduce the amount we have to read
- We like well formatted and copy pastable examples


---

# A better way (for a hypothetical task)

In the task where we should use Python to calculate the output value of a cobb douglas
production function (assignment 1, exercise 2) the following line gives me a type error:

```python
cobb_douglas(labor, capital, alpha)
```

In the task where we should query the iris dataset (exercise 2, Task 8), the following line gives me a KeyError:

```python
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'float'
```

I don't understand the error because I'm just passing in numbers.

---

# A better way (continued)

Here is a minimal example to reproduce the error:

```python
labor = 2.5,
capital = 4.5
alpha = 0.33

def cobb_douglas(labor, capital, alpha):
    return labor**alpha * capital**(1 - alpha)


cobb_douglas(labor, capital, alpha)
```

I attach the entire traceback as `txt` file ...
