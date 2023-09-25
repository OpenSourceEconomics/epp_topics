# Script: Principles for Good Functions

## Why functions are important slide

Make one example for each point:

- Help to re-use code and avoid duplication -> example of not writing out the formula
  for CRRA utility multiple times
- Help to structure code and reduce cognitive load -> You can forget the formula for
  CRRA utility when you are done implementing the function and and function calls are
  much more readable than looking at the formula
- Make individual code snippets testable -> Say that pytest requires functions
- Help to make your projects more reproducible -> pytask
- Unlock the power of functional programming concepts -> Mention some of the crazy
  things we are doing with jax in lcm
- Are also the basis for good object oriented code -> methods are just like functions

## Pass all variables slide

- Mention that both alternatives to global variables are ok.
- Which one to use depends on whether the variable is just needed in one place or in
  multiple places.
