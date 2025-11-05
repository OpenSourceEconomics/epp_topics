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
title: EPP — Profiling code with snakeviz
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Profiling code with snakeviz

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Remarks

- Snakeviz is most useful if your code is structured in many small functions

- Don't obsess about the lowest levels of the output. It is enough if you find out
  which of your functions is currently a bottleneck.

---

# Non obvious outputs

- A lot of time is spent in `__getitem__` and `__setitem__` calls

  - You are using the wrong data structures

  - Replace DataFrames or dicts with numpy arrays where possible

- All time is spent in numpy operations but your code is still much slower than one
  would expect

  - You are doing array operations in a loop

  - Either use full loops with numba or full vectorization. Never a middle ground
