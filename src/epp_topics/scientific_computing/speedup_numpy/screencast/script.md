# Script: Writing fast code with numpy

## Why numpy can be fast

- Emphasize that numpy is fast because it is implemented very efficiently, by experts.
  Not just because it is written in C. I hate it when people say "It's written in ..."
  and want me to take that as guarantee that it will be fast. Python is also written in
  C and it is slow.

## Full vectorization

Use the example to show one of the drawbacks of numpy

`return a * np.prod(factors**weights, axis=-1)`

Since numpy is not a compiler, `factors ** weights` needs to be calculated and stored in
memory before the product is taken. A compiler could fuse the two operations and save
memory.

(It does not matter that all of it is on one line)

However, this is rarely a big problem in practice. If so, use numba

Remind again that achieving this 100x speedup via parallelization would be impossible
and even if it were possible, it would be not desirable. So always optimize on one core
before you parallelize
