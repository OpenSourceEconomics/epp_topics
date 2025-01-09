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
---

### Effective Programming Practices for Economists

<br/>

# Numerical Optimization

### Grid Search

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Grid Search

- Very simple!

- Fix a grid of parameter values.

- Evaluate the function at each grid point.

- Pick the best.

---

<img src="./history.svg" class="rounded" style="width: 90%; height: 90%"/>

---

# Grid Search: Properties

- Needs bounds on the parameter (0 to 20 in our case).

- Desired precision determines number of grid points.

- Very feasible in one dimension.

- Else: Curse of dimensionality.

---

# Curse of Dimensionality

- Suppose we have $p > 1$ parameters.

- If we use $n$ grid points in each dimension, we require $n^p$ function evaluations.

- This grows exponentially with $p$, making grid search infeasible in higher dimensions.

- Example:
  - 5 parameters and 100 grid points per parameter
  - $100^{5} = 10^{10}$ required function evaluations
  - Assume one function evaluation takes 1 millisecond
  - $10^{10}$ milliseconds $\approx$ 115 days
