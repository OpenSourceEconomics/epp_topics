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

### Derivative Free Direct Search Algorithm(s)

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

- Explore parameter space around current point systematically and accept the best value
- Also called pattern search because the points at which the function is evaluated form a pattern
- Easiest example for one dimensional problems:
    - Evaluate function at current point and one other point
    - Switch direction of other point if you got a decrease
    - Make steps larger after success
    - Make steps smaller after failure

---

The following is just an illustration of the principle. The trust region radius is updated manually to simulate a real algorithm.

Note that a real algorithm is quite complex to implement. You should never do that yourself. Leave it to experts unless
- you are a very good programmer;
- you have read a few books on optimization algorithms;
- you have a very special problem that cannot be solved with existing algorithms.

---

# Initial Evaluation

![](../../plots/df_direct_search/iteration_0.png)

---

# Iteration 1

![](../../plots/df_direct_search/iteration_1.png)

---

# Iteration 2

![](../../plots/df_direct_search/iteration_1.png)

---

# Iteration 3

![](../../plots/df_direct_search/iteration_1.png)

---

# Iteration 4

![](../../plots/df_direct_search/iteration_1.png)

---

# Some Remarks

- Adjusting the step size and switching to promising directions is complicated in real algorithms
- Direct search algorithms only use the information which function value is smallest, not by how much
- Makes them slow but robust to small amounts of noise
- It does not help for large amounts of noise
- Most famous example is the Nelder-Mead algorithm which is widely used, but seldomly the best choice

---

# A real algorithm: Nelder Mead

![](../../plots/df_direct_search/illustration_df_direct_search_real_algo.png)
