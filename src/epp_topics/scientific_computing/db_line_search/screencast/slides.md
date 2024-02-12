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

# DB Line Search: Illustration

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_0.png)

</div>
<div>

- large gradient, low curvature
- make a big step

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_1.png)

</div>
<div>


- large gradient, large curvature
- make a smaller step

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_2.png)

</div>
<div>

- very small gradient, low curvature
- make a very small step

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_3.png)

</div>
<div>

- very small gradient, low curvature
- make another very small step

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_4.png)

</div>
<div>

- medium-sized gradient, low curvature
- make a larger step again

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_5.png)

</div>
<div>

- medium-sized gradient, larger curvature
- make a small step


---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_6.png)

</div>
<div>

- reverse direction due to gradient

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_line_search/iteration_7.png)

</div>
<div>

- convergence based on gradient ≈ zero criterion

---

# Some Remarks

- A big advantage over algorithms you will see later is that this has no tuning parameters.
- Using hessian for step length is much better than standard gradient descent.
- In very high dimensional problems, standard gradient descent can nevertheless be computationally better.


---

# A Real Algorithm: L-BFGS-B

![](../../plots/db_line_search/illustration_db_line_search_real_algo.png)
