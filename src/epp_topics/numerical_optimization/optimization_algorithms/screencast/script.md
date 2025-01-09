# Script: Optimization algorithms

## Relevant problem properties

Main message:

1. It is good to learn about the properties of your problem
1. No amount of theory can replace experimentation

Mention that choosing a reasonable algorithm is super important. We are talking about:

- Minutes vs. Weeks
- Reliable solution vs. painful manual intervention
- ...

## Try to make the problem simpler

- Autodiff: Lead to a 50x speedup in skillmodels and 5x in Mariam's double index code;
  Game changer if you can do it!

- Speedup: We'll have screencasts on that

- Make your function more stable: Often pays off. Simple example: evaluate log densities
  instead of densities in likelihood functions. Hopefully we'll add screencasts on that
  at some point.

- Try to make your function smooth: E.g. kernel smoothing approaches in method of
  simulated moments.can be a game changer!

## Choosing local optimizers

- We ask about nonlinear constraints first because if you have them, you have very few
  options. Ipopt typically dominates, but always check!

- We ask about ls next because it is a game changer and very common in estimation
  problems

Rest should be self explanatory. Maybe highlight fides because it is completely
underrated.

## Choosing global optimizers

Global optimization is really really hard and global optimizers have many drawbacks: -
Very slow - Imprecise solutions - No guarantees

We ask for parameter count first because brute force is the only thing with guarantees
but most of the time it is simply too expensive.

Unless function is really badly behaved, multistart is typically the better choice
