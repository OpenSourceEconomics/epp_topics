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

4. Use a line search procedure to see how far to go in the search direction.

   - Line search stays a 1d problem even with many parameters;

   - Only solved approximately;

   - Quite complicated if you really want to understand it;

   - Most of the time accepts the first guess.

5. Accept the new parameter and go back to 1.


---

# The candidate step

- Start at some $x$ (initial point or during iteration)

- Compute the search direction $p$

  For gradient descent: $p = - f'(x)$

- The step length $\alpha$ is chosen to minimize $f$ along the direction $p$

- The candidate step $x_c$ is defined as: $x_c = x + \alpha \, p$


---

### Initial Evaluation

<img src="iteration_0.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 1

<img src="iteration_1.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 2

<img src="iteration_2.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 3

<img src="iteration_3.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 4

<img src="iteration_4.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### Iteration 5

<img src="iteration_5.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

### Iteration 6

<img src="iteration_6.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

### Iteration 7

<img src="iteration_7.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

---

# Some Remarks

- A big advantage over algorithms you will see later is that this has no tuning parameters.

- Using Hessian for step length is much better than standard gradient descent.

- In very high dimensional problems, standard gradient descent can nevertheless be computationally better.


---

### A Real Algorithm: L-BFGS-B

<img src="illustration_db_line_search_real_algo.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
