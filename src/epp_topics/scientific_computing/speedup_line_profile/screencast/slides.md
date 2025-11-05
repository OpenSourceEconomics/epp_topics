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
title: EPP — Line profiling
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Line profiling

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

## Summing up

- Line profiling is a bit harder to use than snakeviz.

- Benefit: Shows you exactly in which line the time is spent.

- Usual process:

  1. Find a slow function with snakeviz

  2. If not enough: Create a line-profile of it with `%lprun`.

- The more practice you get, the more you can learn from the output of profilers
