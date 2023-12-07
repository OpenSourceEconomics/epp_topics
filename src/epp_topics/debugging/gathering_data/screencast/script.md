# Script: Gathering data efficiently

This will be an interactive screencast, based on the file `example.py`

The goal of the screencast is to show the usefulness of a debugger compared to print
statements, without talking too much about the mechanics of using a debugger yet.

The code plots a cobb douglas function for several levels of x1, given a fixed level of
x2 and bounds.

The bug is a trailing comma at the end of the cobb douglas function.

## Show the code

- Show the code
- Explain that `plot_cobb_douglas` should plot the output values for various levels of
  x1, given a level of x2. Mention that `partial` creates a function of only one input.
- Explain that they already know the `cobb_douglas` function from assignments
- Explain that `_create_plotting_data` sets up grids and creates a series for plotting

## Run for the first time

- Run the script and show the plot (in the \`epp\`\` environment)
- I don't get an error but weird plot. (not what I would have expected but actually
  nice)
- Explain that it is hard to form a hypothesis about what is wrong just from the plot
  and say we pretend we did not see the problem when reading the code either. So we need
  to collect data.

## Do it via print statements

- Add print statements after every line of `_create_plotting_data`. Do add context like
  f"value of x1_grid": \{x1_grid}" for now. Maybe even add print statements in other
  functions.
- Run and show the output
- Show how we can find the bug in the output
- Make clear that with print statements you always have at least some of the following
  problem:
  - Time consuming to write or not very informative
  - A lot of output or the risk that you miss the important bit

## Do it with the debugger

- Add `import pdbp; breakpoint()` to the first line of plot_cobb_douglas
- press n to go over the partial line
- step into \_create_plotting_data
- press n a bunch of times until `data` is defined
- Look at data; confirm by looking at data.dtype and evaluations\[0\]

## Summary

- Gathering data can help us to find bugs that we could not find by thinking alone
- It is almost always needed to confirm a hypothesis
- Using a debugger instead of print statements can make a huge difference in efficiency
- Learning to use a debugger is one of the easiest ways to double your productivity
