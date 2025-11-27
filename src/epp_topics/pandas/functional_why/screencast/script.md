# Script: Functional data cleaning: The Why

## Advantages of the functional way

- The function name clearly tell us what is happening in the code, no need for comments
- Inside each function, sr is a perfectly fine name, so we save a lot of typing and
  clutter
- There is no intermediate version of df
- There is no way of executing this code in the wrong order, even though we can spread
  the function definitions across many cells
- We can re-use the code for cleaning agreement variables very easily and wherever we
  want
- All of our functions are pure and testable with with tiny examples where we know the
  correct result
- The top level function serves as a table of content to what comes next. This is why it
  is defined before the functions it calls.
