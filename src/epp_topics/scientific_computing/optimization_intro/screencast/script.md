# Script: Introduction to numerical optimization

## Example problem

- Say that this is one of the simplest optimization problems you could imagine
- Introduce important terminology, where necessary with common synonyms
  - criterion function = objective function: The function to optimize
  - Parameters, params or variables = The numbers to optimize over, often represented as
    a vector
  - Bounds = Box constraints: Lower and upper bounds for some or all parameters
  - Constraints: Possibly complex conditions on parameters (e.g. parameters of cobb
    douglas function must sum up to 1)
  - Solution: Most of the time we are interested in the argmin not min

## Application of optimization in economics

I mention logit and probit separately because many are not aware that these are
estimated with maximum likelihood using numerical optimization; You can mention that in
stata the optimization might go wrong and then it's bad that it is hidden

About "solve utility maximization problems"; I mention them here because it could be
done but maybe say that the algorithms we are going to see here are not necessarily the
best for solving agent problems in a structural model.

# What is an optimization algorithm

The definition captures the essence of optimizers but unfortunately it is not always
possible to completely abstract from the details. For difficult problems we'll have to
invest a bit more time.

"possibly after a long time": Give them a feeling for how long. Over night is common.
Say that this has implications for the diagnostic tooling we need around optimizers.

# Libraries for optimization

- I would not talk much about this slide. No need to sell estimagic. Just say we use it.
