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

<br>

# Numerical Optimization

### Derivative-Based Trust Region Algorithms

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

1. Set initial trust region radius.

2. Construct a quadratic Taylor approximation of the function based on function value, gradient,
   and (approximation to) the Hessian.

    The Taylor approximation:

    - approximates the function well within the trust region if radius is not too large

    - is a quadratic function that it easy to optimize.

3. Minimize the Taylor approximation within the trust region.

4. Evaluate the function again at the argument that minimized the Taylor approximation.

---

5. Compare expected and actual improvement.

    - Expected improvement is the decrease in the criterion according to the Taylor
      approximation.
    - Actual improvement is the decrease in the actual function value.

6. Accept the new parameters if actual improvement is good enough.

7. Modify the trust region radius (**important and complex step**).

8. Construct a new Taylor approximation ...


---

# Smaller radii lead to better approximations

- For a step $s$, the Taylor expansion of $f(x + s)$ around $x$ satisfies:

  $f(x + s) = f(x) + f'(x)^\top s + \frac{1}{2} s^\top f''(x) s + o(\|s\|^2)$.

- The step $s$ is bounded by the trust region radius $\Delta$: $\|s\| \leq \Delta$.

- And therefore, as $\Delta$ decreases the approximation error $o(\|s\|^2)$ decreases.

- (Holds for any function $f$ that is at least twice continuously differentiable.)


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

### Iteration 5

<img src="./iteration_5.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>


---

### A real algorithm: fides

<img src="./illustration_db_trust_region_real_algo.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
