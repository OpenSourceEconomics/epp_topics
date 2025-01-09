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

# Scientific Computing

### Derivative-Based (DB) Trust Region Algorithm(s)

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

1. Fix a trust region radius.

2. Construct a Taylor approximation of the function based on function value, gradient,
   and (approximation to) the Hessian.

    The Taylor approximation:
    - approximates the function well within the trust region if radius is not too large;
    - is a quadratic function that it easy to optimize.

3. Minimize the Taylor approximation within the trust region.

4. Evaluate the function again at the argmin of the Taylor approximation.

---

5. Compare expected and actual improvement.

6. Accept the new parameters if actual improvement is good enough.

7. Potentially modify the trust region radius (**important and complex step**).

8. Go back to 2.


---

# Smaller radii lead to better approximations

- Take any function $f$ that is at least three times continuously differentiable.

- For a step $s$, the Taylor expansion of $f(x + s)$ around $x$ satisfies:

  $f(x + s) = f(x) + \nabla f(x)^\top s + \frac{1}{2} s^\top \nabla^2 f(x) s + o(\|s\|^2)$.

- The step $s$ is bounded by the trust region radius $\Delta$: $\|s\| \leq \Delta$.

- And therefore, as $\Delta$ decreases the approximation error $o(\|s\|^2)$ decreases.

---

# DB Trust Region: an Illustration

The following is just an illustration of the principle. The trust region radius is updated manually to simulate a real algorithm.

Note that a real algorithm is quite complex to implement. You should never do that yourself. Leave it to experts unless:
- you are a very good programmer;
- you have read a few books on optimization algorithms;
- you have a very special problem that cannot be solved with existing algorithms.

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

# Some Remarks

- Most of the time, the approximation was not very good but sent us in the right direction.
- After a successful iteration, the trust region radius is increased.
- At some point it becomes too large and needs to be decreased.
- From now on the algorithm would converge soon because of a zero gradient.
- Even when it converges, the trust region radius does not shrink to zero.

---

### A real algorithm: Trust-NCG

<img src="illustration_db_trust_region_real_algo.svg" class="rounded" style="width: 80%; height: 80%; margin: auto"/>
