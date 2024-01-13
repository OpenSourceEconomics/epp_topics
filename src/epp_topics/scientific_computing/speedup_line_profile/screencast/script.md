# Script: Line Profiling

The screencast will be a live demo

## Introduction

open `line_profile_example.ipynb`

## Production function example

- Quick recap of the production function example
- Say that it is important to use realistic inputs (more on that in the previous
  screencast)
- Re-write the function to use:

```python
weighted = factors**weights
product = np.prod(weighted)
return a * product
```

- Run the code until (but not including the lprun cell)

## Explain the invocation of lprun

`%lprun` is the jupyter magic for the `line_profiler -f _cobb_douglas`. Says that we
want to line-profile the `_cobb_douglas` function.
`array_cobb_douglas(factors, weights, a)` is the code snippet that is actually ran to
generate the profile.

## Explain the output

Most time is spent on `np.prod(weighted)`

This might look like we are already efficient because all time is spent in numpy.

However, every numpy function call does a few things

- Check the input and potentially convert it to an array
- Check the dtypes of all arrays
- Call a fast low-level function
- Potentially do something with the output

In our case, the code is far from optimal because `np.prod` is called many times on tiny
inputs so the overhead dominates the runtime
