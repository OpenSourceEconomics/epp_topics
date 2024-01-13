# Script: Profiling code with snakeviz

This screencast is a combination of a live demo and slides

**Start with the live demo**

## Introduction

open `snakeviz_example.ipynb` in a browser and explain that snakeviz does not work if
the notebook is opened in vscode

## Production function example

- Quick recap on the production function example
- Say that it is important to use realistic inputs (more on that in the previous
  screencast)
- Run the code until the snakeviz profile is generated

Explain the output:

- **First and second row** are always the same and can be ignored

- **Third row** says that the entire time is spent on executing `array_cobb_douglas`,
  which makes sense since this is all we do

- **Fourth row** (hover over it) shows that only very little of that time is actually
  spent in that function and most of it is spent into `_cobb_douglas` which we call from
  `array_cobb_douglas`

  - Below that level we quickly get into numpy internals we don't understand
  - The white parts means that there are no further function calls we could analyze

Say that here we did not learn all that much from the profile because we only have a
tiny code snippet. True power shows when we apply snakeviz to large code bases.

## Switch back to slides

### Non obvious outputs

- Last remark: This is exactly what happens in the tiny production function example. It
  looks like we are already efficient because all time is spent in numpy operations but
  we are very far from the optimum.
