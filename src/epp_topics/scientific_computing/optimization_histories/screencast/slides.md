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

### Visualizing optimizer histories

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation


- You rarely have a guarantee that an optimizer will work

  - Assumptions of convergence proofs might not hold in practice

  - You might get stuck in local optima

  - Floating point calculations are never exact

- But you can compare the performance of optimizers

  - Which one finds the lower function value?

  - Which one decreases the function more quickly?

- The `criterion_plot` makes this very easy!


---

# Criterion plot

We assume you have done an optimization and the result is called `res`

---

# Criterion plot

```python
em.criterion_plot(res)
```

<div class="grid grid-cols-2 gap-12">
<div>

<img src="criterion_plot.png" alt="criterion" width="500" style="display: block;"/>

</div>
<div>

<br/>

- First argument can be:
  - `OptimizeResult`
  - path to log file
  - list or dict thereof
- Dictionary keys are used for legend

</div>
</div>

---

# Criterion plot

```python
em.criterion_plot(res, monotone=True)
```

<div class="grid grid-cols-2 gap-4">
<div>
<img src="criterion_plot_monotone.png" alt="criterion" width="500"
style="display: block;"/>

</div>
<div>

<br/>
<br/>

- **monotone=True** shows the current best value
- useful if there are extreme values in history

</div>
</div>

---

# Criterion plot

```python
em.criterion_plot(res, max_evaluations=300)
```

<div class="grid grid-cols-2 gap-4">
<div>
<img src="criterion_plot_max_evaluations.png" alt="criterion" width="500"
style="display: block;"/>

</div>
<div>

<br/>
<br/>
<br/>

- **max_evaluations** limits the x-axis

</div>
</div>

---

# Criterion plot for multiple optimizations

<br/>

<div class="flex gap-4">
<div>

<br/>
<br/>

```python
def sphere(x):
    return x @ x

results = {}
for algo in ["scipy_neldermead", "nlopt_neldermead", "fides"]:
    results[algo] = em.minimize(
        sphere,
        np.arange(10),
        algorithm=algo,
    )

em.criterion_plot(results, max_evaluations=200)
```

</div>
<div>

<img src="multi_optimization_criterion_plot.svg" class="rounded" width="300"/>

</div>
</div>
