# Script: Measuring runtime

This screencast has a section on creating benchmark inputs that will also be relevant
for the profiling and line-profiling screencast. It also introduces the running example
for other speedup screencast.

## Example

- Relate the generalized cobb douglas to the generalized CES they implemented in the
  assignments

# Setting up representative inputs

- Not all algorithms scale linearly
  - Example: Matrix multiplication and Matrix inversion scale with O(N^3)

## Timing fast functions

- "%timeit only works in notebook" -> say that notebooks are the best place to time and
  optimize functions anyways. Functions don't have to be defined in the notebook, can
  also just import them.

## Timing slow functions

- The need for `perf_counter` was a hard debug experience for me because on linux it
  does not matter.

## Limitations

- You can mention that for important benchmarks people restart computers for each run or
  even set up virtual machines to make sure that timings are accurate
