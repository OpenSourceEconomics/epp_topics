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

### Derivative-Based (DB) Line Search Algorithm(s)

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

1. Evaluate function at initial point.
2. Use first derivative to get search direction.
3. Use approximated second derivative to guess step length.
4. Use a line search algorithm to see how far to go in the search direction.
  - Line search stays a 1d problem even with many parameters;
  - Only solved approximately;
  - Quite complicated if you really want to understand it;
  - Most of the time accepts the first guess.
5. Accept the new parameter and go back to 1.

---

### Initial Evaluation

<img src="iteration_0.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 1

<img src="iteration_1.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 2

<img src="iteration_2.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 3

<img src="iteration_3.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 4

<img src="iteration_4.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 5

<img src="iteration_5.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

### Iteration 6

<img src="iteration_6.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

### Iteration 7

<img src="iteration_7.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

# Some Remarks

- A big advantage over algorithms you will see later is that this has no tuning parameters.
- Using hessian for step length is much better than standard gradient descent.
- In very high dimensional problems, standard gradient descent can nevertheless be computationally better.


---

### A Real Algorithm: L-BFGS-B

<img src="illustration_db_line_search_real_algo.png" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
