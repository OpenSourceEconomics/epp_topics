# Script: Using the Pdb+ debugger

## Setting a breakpoint

- Examples when conditional breakpoints are useful:

  - Something breaks down for specific parameter combinations
  - Something breaks down after a certain number of iterations

- Say that in many tutorials they will only see `breakpoint()`; the import is needed to
  get a nicer debugger!

## Important commands

- I keep it deliberately simple. When I learned it I was scared by the long list of
  commands and I only started using it again when I realized I just need `n` and `s`

## Graphical alternatives

- Emphasize that `pytask` and `pytest` are our main ways of running code so it is very
  important that our debugger integrates well with them.

- The "more robust" comment refers to my experience from last year, where people used
  vscode debuggers but there were all kinds of problems (breakpoint was skipped, ...);
  I'm sure it was their fault, but the last thing you want to do is debug your debugger.

- I know people miss variable explorers they know from R, but I cannot imagine how they
  help for large datasets or arrays since you always need to filter those to see
  important bits. Maybe talk about this

## Show another life demo

I think it would be a good idea to go through the same example from before but talk a
bit more about the different command you are using to navigate. I say that without
watching your previous recording, so feel free to skip.
