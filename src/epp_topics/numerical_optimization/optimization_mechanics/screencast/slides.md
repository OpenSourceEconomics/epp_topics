---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: EPP — Using optimagic's minimize and maximize
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Numerical Optimization

### Using optimagic's minimize and maximize

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Simple usage of **minimize** and **maximize**

<br/>

<div class="flex gap-20">

<div>

```python
import numpy as np
import optimagic as om

def sphere(x):
    return (x ** 2).sum()

start_params = np.ones(5)

res = om.minimize(
    fun=sphere,
    params=start_params,
    algorithm="scipy_lbfgsb",
)

res.params
```

```txt
array([0., 0., 0., 0., 0.])
```

</div>
<div>

<br/>

1. Import optimagic

2. Define criterion function

3. Define start params

4. Call minimize

<br/>

`maximize` works the same!

</div>
</div>

---

# Same problem — different params

<br/>

```python
>>> params = {"a": 0, "b": 1, "c": pd.Series([2, 3, 4])}

>>> def dict_sphere(x):
...     return x["a"] ** 2 + x["b"] ** 2 + (x["c"] ** 2).sum()

>>> res = om.minimize(
...     fun=dict_sphere,
...     params=params,
...     algorithm="scipy_neldermead",
... )
>>> res.params
{
  'a': 0.,
  'b': 0.,
  'c': 0    0.
       1    0.
       2    0.
  dtype: float64
}
```

---

# Bounds for parameters

<div class="grid grid-cols-2 gap-4">
<div>

```python{5}
>>> res = om.minimize(
...     fun=dict_sphere,
...     params=params,
...     algorithm="scipy_neldermead",
...     lower_bounds={"b": 0.5}
... )
```

```python
>>> res.params
{
  'a': 0.,
  'b': 0.5,
  'c': 0    0.
       1    0.
       2    0.
  dtype: float64
}
```

</div>
<div>

- Extend previous example

- Only need to specify bounds for parameters that need them

- `upper_bounds` work analogously

- Can use `np.inf` and `-np.inf` to explicitly specify no bound

</div>
</div>

---

# Inspecting results

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> res.criterion
```

```txt
0.
```

```python
>>> res.n_criterion_evaluations
```

```txt
805
```

```python
>>> res.success
```

```txt
True
```

```python
>>> res.message
```

```txt
'Optimization terminated successfully.'
```

</div>
<div>

- You already know res.params

- There are many other useful attributes

- Elements of results objects can also be plotted

</div>
</div>

<br/>

---

# Documentation of more features

- [How to specify algorithms and their options](https://optimagic.readthedocs.io/en/latest/how_to/how_to_specify_algorithm_and_algo_options.html)

- [How to use constraints](https://optimagic.readthedocs.io/en/latest/how_to/how_to_constraints.html)

- [How to do multistart optimization](https://optimagic.readthedocs.io/en/latest/how_to/how_to_multistart.html)

- [How to handle errors during optimization](https://optimagic.readthedocs.io/en/latest/how_to/how_to_errors_during_optimization.html)
