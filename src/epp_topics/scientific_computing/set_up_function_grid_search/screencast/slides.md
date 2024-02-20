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

### Grid Search

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Function Set-up

In these lectures we will use the following function as a target for our
optimization:

$$
f(\mathbf{x}) = \sum_{i=1}^n w_i x_i^{\exp_i}
$$

where $\mathbf{x} = (x_1, \dots, x_n)$ is a vector of length $n$ and
$\mathbf{w} = (w_1, \dots, w_n)$ and $\mathbf{e} = (\exp_1, \dots, \exp_n)$ are
vectors of length $n$. Exponentiation is element-wise.


---

Set of parameters:

```python
    WEIGHTS = [
        9.003014962148157,
        -3.383000146393776,
        -0.6037887934635748,
        1.6984454347036886,
        -0.9447426232680957,
        0.2669069434366247,
        -0.04446368897497234,
        0.00460781796708519,
        -0.0003000790127508276,
        1.1934114174145725e-05,
        -2.6471293419570505e-07,
        2.5090819960943964e-09,
    ]
    exponents = np.arange(len(WEIGHTS))
```



---

<img src="function_plot.png" class="rounded" style="width: 90%; height: 90%"/>

---

# Grid Search

- Grid search is a simple optimization algorithm that searches for the best
  combination of parameters by evaluating the function at a given set of
  parameter values.
- Needs bounds on the parameter (0 to 20 in our case).
- Desired precision determines number of grid points.
- Very feasible in one dimension.

---

<img src="history_grid_search.png" class="rounded" style="width: 90%; height: 90%"/>
