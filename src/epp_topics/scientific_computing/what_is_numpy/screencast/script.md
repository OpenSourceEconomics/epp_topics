# Script: What is numpy?

## What is numpy

Numpy is the reason Python took off for machine learning

Knowing numpy helps you to learn jax, pytorch, tensorflow, ...

## What is an array

- There are different mental models for arrays. It's good if you can quickly switch
  between them. Sometimes, a 2d array is a matrix. Sometimes it is a "list" of vectors.

- There is no upper limit on the number of dimensions. Best way to think about them is
  as lists of lists of lists of matrices or vectors

- Make an example of dtypes (float, int, bool). Reference pandas.

## Why are calculations on arrays fast

This slide is mainly there to create motivation for the next few screencasts. But we can
also use it to say for the first time that Julia, Fortran, ... will not be faster than
optimized numpy / numba / JAX.

I would say the following:

- No programming language can reach the physical performance limit of your processor if
  it does not know types or data is not stored contiguously.
- Pure Python loops over arrays will also not be fast
- Using built-in numpy functions or using modern Python compilers together with numpy
  arrays will be about as fast as compiled languages. Optimized Python can definitely be
  faster than Julia, Fortran and other code written by economists.
