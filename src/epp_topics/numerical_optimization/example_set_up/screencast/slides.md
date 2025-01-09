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

### Set up of the example

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Function

In these lectures we will use the following function as a target for our
optimization:

$$
f(\mathbf{x}) = \sum_{j=1}^{J} w_j \cdot x^{j-1}
$$

with $J = 12$.


---

# Weights used

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
```



---

<img src="./function.svg" class="rounded" style="width: 90%; height: 90%"/>
