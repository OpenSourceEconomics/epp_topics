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

### Derivative-Free Trust Region Algorithms

<br/>

Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Basic Idea ([optimagic docs](https://optimagic.readthedocs.io/en/latest/explanation/explanation_of_numerical_optimizers.html#derivative-free-trust-region-algorithms))

- Similar to derivative based trust region algorithm.

- Instead of Taylor approximation, use a surrogate model based on interpolation or
  regression.

  - Interpolation: Function is evaluated at exactly as many points as you need to fit
    the model.

  - Regression: Function is evaluated at more points than you strictly need. Better for
    noisy functions.

  - In general: Evaluation points are spread further out than for numerical derivatives.

- How the evaluation points are determined is complicated. It is also crucial for the
  efficiency of the algorithm.

---

### Initial Evaluation

<img src="./iteration_0.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Actual $=$ expected $\Rightarrow$ accept, increase trust region radius

---

### Iteration 1

<img src="./iteration_1.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Actual $=$ expected $\Rightarrow$ accept, increase trust region radius

---

### Iteration 2

<img src="./iteration_2.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Actual $\approx$ expected, but step small $\Rightarrow$ accept, decrease trust region
radius

---

### Iteration 3

<img src="./iteration_3.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Actual $\approx$ expected, but step small $\Rightarrow$ accept, decrease trust region
radius

---

### Iteration 4

<img src="./iteration_4.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Actual $\approx$ expected, but step small $\Rightarrow$ accept, decrease trust region
radius

---

### Iteration 5

<img src="./iteration_5.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>

Converge because trust region radius shrinks to zero.

---

# Some Remarks

- Within the trust region, the fit is generally better than the gradient based trust
  region algorithm

- By construction at the boundaries of the trust region for interpolation

- Choose between the two based on computation speed

  - If you have fast closed form derivatives, use the derivative based algorithm

  - If you only have numerical derivatives, use this instead

- It is intuitively very clear how this can work for noisy functions if enough
  evaluations are used for each surrogate model

---

# A real algorithm: COBYLA

<img src="./illustration_df_trust_region_real_algo.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
