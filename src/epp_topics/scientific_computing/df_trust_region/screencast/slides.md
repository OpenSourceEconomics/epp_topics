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

### Derivative-Free Trust Region Algorithm(s)

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

- Similar to derivative based trust region algorithm.
- Instead of Taylor expansion, use a surrogate model based on interpolation or regression.
    - Interpolation: Function is evaluated at exactly as many points as you need to fit the model.
    - Regression: Function is evaluated at more points than you strictly need. Better for noisy functions.
    - In general: Evaluation points are spread further out than for numerical derivatives.
- How the evaluation points are determined is complicated. It is also crucial for the efficiency of the algorithm.

---

The following is just an illustration of the principle. The trust region radius is updated manually to simulate a real algorithm.

Note that a real algorithm is quite complex to implement. You should never do that yourself. Leave it to experts unless
- you are a very good programmer;
- you have read a few books on optimization algorithms;
- you have a very special problem that cannot be solved with existing algorithms.

---

# Initial Evaluation

![](../../plots/df_trust_region/iteration_0.png)

---

# Iteration 1

![](../../plots/df_trust_region/iteration_1.png)


---

# Iteration 2

![](../../plots/df_trust_region/iteration_2.png)


---

# Iteration 3

![](../../plots/df_trust_region/iteration_3.png)

---

# Iteration 4

![](../../plots/df_trust_region/iteration_4.png)

---

# Iteration 5+

- will continue around here until optimum is reached
- you get the idea...


---

# Some Remarks

- The fit is generally better than the gradient based trust region algorithm
- By construction especially at corners of trust region
- Choose between the two based on computation speed
    - If you have fast closed form derivatives, use the derivative based algorithm
    - If you only have numerical derivatives, use this instead
- Points at which the function has been evaluated before can be re-used to save function evaluations
- Since no gradient is available, algorithm will continue until trust region radius shrinks to zero
- It's intuitively very clear how this can work for noisy functions if enough evaluations are used for each surrogate model

---

# A real algorithm: COBYLA

![](../../plots/df_trust_region/illustration_df_trust_region_real_algo.png)
