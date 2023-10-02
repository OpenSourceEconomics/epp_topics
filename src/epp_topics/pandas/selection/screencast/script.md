# Script: Selecting rows and columns

## Selecting individual rows

- Maybe you want to mention that `.loc` returns a view, not a copy and that this can be
  used to update DataFrames inplace. But I am actually trying to not show any in-place
  changes of DataFrames and use things like `.where` in places where most people would
  use an assignment with `.loc[Boolean, "col"] = ...`
