# Script: Introduction to making code fast

## What do we mean by speedup

- Same calculations:
  - Mention that faster runtimes can also often come from algorithmic improvements
    (choose a better optimizer, avoid (non-obvious) duplicated calculations, etc.) but
    that this is not the topic right now.
- Same language
  - Say that it is a very bad idea to just rewrite an entire project in a different
    language to make it faster. To get really fast, you need to know what you are doing
    in any language
  - Same language means that we still write Python and call Python libraries. All of
    Python is implemented in C. As users we don't care if a library is also implemented
    in C, Rust, or something else under the hood.

## Speed can vary within a language

- "It gets really slow if you do not use libraries as intended".

  Example: looping over rows of a pandas DataFrame

## Python can be really fast

- Maybe mention, that it is true that in Python the range of possible speeds is very
  large. In Julia it is much smaller and in Fortran it is hard to write slow code (but
  possible)

- Numba is more restrictive than Julia in the sense that you need to write loops over
  arrays (instead of custom classes or similar) but if you do that, you get the same
  (almost optimal) speed as Julia.

- AI Training would be done in other languages if that was faster. It costs millions or
  billions to train large models.

- By beating fortran code I mean respy

- Mention again, that it is a really bad idea to blindly rewrite an application in
  another language and that they will learn much better ways here.

## Only optimize bottlenecks

- It has happened many times that you make one function 100x faster only to find out
  that the overall runtime does not change

- We need profilers for this and there will be a screencast about it

## Process

- Get it right -> testing
- Find the bottleneck -> profiling
- Speed up the bottleneck -> line-profiling, measuring runtime, use good benchmark
  inputs
- Speed up on one core:
  - Speedups of 100x and more are possible on one core
  - To get this via parallelization you would need at least 200 cores because speedup is
    never linear
- Think about parallelization -> We won't cover that
- Repeat -> If you solved one bottleneck, find the next one
