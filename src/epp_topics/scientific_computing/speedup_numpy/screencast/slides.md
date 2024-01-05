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

### Writing fast code with numpy

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Why numpy can be fast

- Numbers are stored efficiently in arrays
  - dtype of all numbers is known
  - it is fast to read numbers from memory into registers
- numpy functions are implemented very efficiently
  - in a low-level language like C
  - by experts who really know what they are doing
- Python overhead is incurred once per array, not once per number


---

# Implications for writing fast code

- Vectorize everything!
- Use broadcasting where possible
- Prefer few large arrays over many small arrays



---

# Limits of performance with numpy

- Numpy is not a compiler, so it cannot
  - Fuse multiple operations into one (for more speed)
  - Eliminate intermediate results (for using less memory)
- Creating arrays is slower than creating list
  - Only relevant if you create many tiny arrays
- Calling array operations in a loop is typically slow but it is hard to detect this
inefficiency in a profiler


---

# Why is the example slow


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

k = 5
n = 10_000

rng = np.random.default_rng(93726483)
factors = rng.uniform(0.1, 3, size=(n, k))
weights = np.array([0.2, 0.1, 0.3, 0.2, 0.2])
a = 1.2
```
```python
%timeit array_cobb_douglas(factors, weights, a)
```
```txt
25.1 ms ± 488 µs per loop
```

</div>
<div>

- This uses array operations (e.g. np.prod) inside a loop
- This is typically slow and full vectorization should be faster
- Even writing out everything as a loop might be faster than the mix!


</div>
</div>

---

# Full vectorization

<div class="flex gap-4">
<div>

```python
def vectorized_array_cobb_douglas(factors, weights, a):
    return a * np.prod(factors**weights, axis=-1)

%timeit vectorized_array_cobb_douglas(factors, weights, a)
```
```txt
215 µs ± 1.63 µs per loop
```

</div>
<div>

- From ~25 milliseconds to ~215 microseconds
- Speedup of more than 110x
- Code is actually more readable
- Need to get good with `axis` argument!

</div>
</div>
