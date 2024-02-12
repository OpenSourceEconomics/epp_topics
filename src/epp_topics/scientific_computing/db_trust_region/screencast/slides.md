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

### Derivative-Based (DB) Trust Region Algorithm(s)

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Basic Idea

1. Fix a trust region radius
2. Construct a Taylor expansion of the function based on function value, gradient, and (approximation to) Hessian

   The Taylor expansion
   - approximates the function well within trust region if radius is not too large
   - is a quadratic function that it easy to optimize

3. Minimize the Taylor expansion within the trust region
4. Evaluate function again at the argmin of the Taylor expansion
5. Compare expected and actual improvement
6. Accept the new parameters if actual improvement is good enough
7. Potentially modify the trust region radius

   **This is a very important and very complicated step**

8. Go back to 2.

---

The following is just an illustration of the principle. The trust region radius is updated manually to simulate a real algorithm.

Note that a real algorithm is quite complex to implement. You should never do that yourself. Leave it to experts unless:
- you are a very good programmer;
- you have read a few books on optimization algorithms;
- you have a very special problem that cannot be solved with existing algorithms.

---

# DB Trust Region: Illustration

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_0.png)

</div>
<div>

- orange line is the approx. model
- expected improvement: difference between f(x0) and minimum of the orange line
- actual improvement: difference beween f(x0) and f(x)
- since actual improvement / expected improvement large (>1 even)
  - accept the new point → midpoint of new trust region
  - increase trust region radius


---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_1.png)

</div>
<div>

- actual improvement / expected improvement < 1, but still large
- accept new point, increase trust region

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_2.png)

</div>
<div>

- actual improvement / expected improvement is negative
- Do not new accept point
- Decrease trust region radius

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_3.png)

</div>
<div>

- actual improvement / expected improvement around 1
- accept new point, increase trust region

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_4.png)

</div>
<div>

- actual improvement / expected improvement around 1
- accept new point, increase trust region

---

<div class="grid grid-cols-2 gap-4">
<div>
![](../../plots/db_trust_region/iteration_5.png)

</div>
<div>

- Convergence somewhere here

---

# Some Remarks

- Most of the time, the approximation was not very good but sent us in the right direction
- After a successful iteration, the trust region radius is increased
- At some point it becomes too large and needs to be decreased
- From now on the algorithm would converge soon because of a zero gradient
- Even when it converges, the trust region radius does not shrink to zero


---

# A real algorithm: Trust-NCG

![](../../plots/db_trust_region/illustration_db_trust_region_real_algo.png)
