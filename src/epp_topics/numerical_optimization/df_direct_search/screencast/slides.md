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

# Numerical Optimization

### Derivative-Free Direct Search Algorithms

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

- Explore parameter space around current point systematically and accept the best value
- Also called pattern search because the points at which the function is evaluated form a pattern
- Easiest example for one dimensional problems:
    - Evaluate function at current point and one other point
    - Switch direction of other point if you got an increase in function value
    - Make steps larger after success
    - Make steps smaller after failure

---

### Initial Evaluation

<img src="./iteration_0.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

### Iteration 1

<img src="./iteration_1.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 2

<img src="./iteration_2.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 3

<img src="./iteration_3.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 4

<img src="./iteration_4.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

# Some Remarks

- Adjusting the step size and switching to promising directions is complicated in real algorithms
- These algorithms only use the information which function value is smallest, not by how much
- Makes them slow but robust to small amounts of noise
- It does not help for large amounts of noise
- Most famous example is the Nelder-Mead algorithm

  - Very widely used

  - Very seldomly the best choice

---

### A real algorithm: Nelder Mead

<img src="./illustration_df_direct_search_real_algo.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
