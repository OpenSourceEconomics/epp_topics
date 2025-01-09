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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Scientific Computing

### Introduction to making code fast

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# What do we mean by speedup

- Same calculations

- Same language

- Faster execution


---

# Speed can vary within a language

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> def my_sum(numbers):
...     out = 0
...     for number in numbers:
...         out += number
...     return out

>>> numbers = list(range(10_000))

>>> %timeit my_sum(numbers)
```

```txt
128 µs ± 1.65 µs

```

```python
>>> %timeit sum(numbers)
```

```txt
28.5 µs ± 275 ns
```

</div>
<div>


- In this simple example, the speed difference is 4.5x

- Speed differences of 100x are common, more is possible

- It gets really slow if you do not use libraries as intended

</div>
</div>

---

# Python can be really fast


- Numba uses the same technology as Julia (llvm)

- JAX uses technologies [Julia dreams of](https://discourse.julialang.org/t/what-happened-to-xla-jl/88088) and is even [developing them further](https://mlir.llvm.org/)

- State of the art AI is trained in Python

- We have beat Fortran code with Python code several times

---

# Only optimize bottlenecks

> We should forget about small efficiencies, say about 97% of the time: premature
> optimization is the root of all evil (Donald Knuth)

- Typically, runtime is concentrated in a few sections of code

- Making the rest faster will not change overall runtime

- Important: Learn how to find those sections!

---

# Process

> If it doesn’t work, it doesn’t matter how fast it doesn’t work (Mich Ravera)


- Get it to run

- Get it right

- Find the bottleneck

- Speed up the bottleneck on one core

- Think about parallelization

- Repeat
