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
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Introduction to numerical optimization

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Example problem

<div class="grid grid-cols-2 gap-4">
<div>

- **Criterion** $f(a, b) = a^2 + b^2$

- Parameters $a$, $b$

- Want: $a^*, b^* = \text{argmin} f(a, b)$

- Possible extensions:

  - Constraints

  - Bounds (a.k.a. box constraints)

- Optimum at $a^*=0$, $b^*=0$, $f(a^*,b^*) = 0$

</div>

<div>

<img src="/sphere.png" alt="sphere" width="450" class="center"/>

</div>
</div>

---

# Applications of numerical optimization

- Probit, many Logit models, ...

- Fitting machine learning models

- Estimating structural models

  - Maximum likelihood

  - Method of simulated moments

- Calculating optimal policies from a structural model

- Solving utility maximization problems

---

# What is an optimization algorithm

- **Our definition**: A function that takes a criterion function and start parameters
  and returns a solution, possibly after a long time

- There are many different optimizers

- Picking the right one can make a huge difference but is hard

- Use a mix of theory and experimentation to get there

---

# Libraries for optimization


- There are many optimization libraries in Python

- All are a bit different

- We will use [estimagic](https://estimagic.readthedocs.io/) to access all of them with
  a unified interface

- Estimagic is developed by Open Source Economics in Bonn
