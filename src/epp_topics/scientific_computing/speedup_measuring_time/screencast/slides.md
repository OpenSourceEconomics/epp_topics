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
title: EPP — Scientific Computing — Measuring runtime
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Measuring runtime

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# Example

<div class="flex gap-4">
<div>

```python
def array_cobb_douglas(factors, weights, a):
    out = np.empty(len(factors))
    for i in range(len(factors)):
        out[i] = _cobb_douglas(factors[i], weights, a)
    return out

def _cobb_douglas(factors, weights, a):
    return a * np.prod(factors**weights)
```

</div>
<div>

- Assume we want to evaluate the function multiple times

- Will be the running example for all speedup screencasts

- Possible applications

  - Structural models with production

  - Skill formation models

</div>
</div>

---

# Setting up representative inputs

<div class="flex gap-8">
<div>

```python
# number of input factors
k = 5
# number of evaluations
n = 10_000

# set up random inputs
rng = np.random.default_rng(93726483)
factors = rng.uniform(0.1, 3, size=(n, k))
weights = np.array([0.2, 0.1, 0.3, 0.2, 0.2])
a = 1.2

```

</div>
<div>

- Sizes should be representative of your real application!

  - Not all algorithms scale linearly

  - You want to optimize what you really need!

- Use random numbers for inputs

</div>
</div>

---

# Timing fast functions

```python
%timeit array_cobb_douglas(factors, weights, a)
```

```txt
25.1 ms ± 488 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

<br/>

- `%timeit` only works in notebooks!

- It does many things automatically

  - discard outliers

  - determine how often the code is evaluated

  - determine suitable units of time

---

# Timing slow functions

<div class="grid grid-cols-2 gap-4">
<div>

```python
from time import perf_counter

start = perf_counter()
array_cobb_douglas(factors, weights, a)
runtime = perf_counter() - start
runtime
```

</div>
<div>

- Use this if your function takes several seconds and you only want to evaluate it once

- Do not use `time.time` instead of `time.perf_counter` because it has very low
  resolution on windows (full seconds)

- Only interpret differences between `perf_counter` evaluations

</div>
</div>

---

# Limitations

- Measured runtime depends on background tasks

  - Try to run few applications in the background

  - Do not run timings in parallel!

- Runtime does not tell you where the time is spent

  - Need profiling
