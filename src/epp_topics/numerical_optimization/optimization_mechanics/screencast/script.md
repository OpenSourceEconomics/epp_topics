# Script: Using optimagic's minimize and maximize

The goal of this screencast is to show the mechanics of using minimize and maximize in a
few variations. Then we link to the documentation for more details. Any other approach
would produce too many or too long screencasts.

## Simple usage of minimize and maximize

- Mention that two of the steps that are trivial here, can be complex in practice

  - Defining criterion function can take weeks
  - Finding good start values needs a lot of intuition and experimentation

- Mention that most packages only have minimize -> sign flip

- Optimagic has no default optimizer because there simply is no optimizer that works
  well for all problems. Mention that there will be a later screencast on choosing
  optimizers.

## Same problem — different params

- Say that this is a simplified example to focus on mechanics. However, structured
  params formats are extremely useful in practice. Examples:

  - structural model with discount factor, wage parameters, utility parameters, ...
  - skillmodels with multiple sets of production function parameters and hundreds of
    nuisance parameters

- Mention that almost any data structure they know can be used with arbitrary nesting

## Bounds for parameters

- Mention that in general lower_bounds and upper_bounds need to have the same structure
  as `params`; Exception: They can leave out unnecessary parameters

- Mention that it is a good idea for complex structural models to start with relatively
  narrow bounds around parameters and iteratively relax them

- Mention that global optimization problems are only defined if all parameters have
  finite bounds.

## Inspecting results

- "Result objects can also be plotted" -> there will be a screencast about it!

## Documentation of more features

Maybe click on a few of them to show the documentation structure
