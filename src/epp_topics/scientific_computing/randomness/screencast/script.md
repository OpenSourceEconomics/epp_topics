# Script: Randomness

I almost don't talk about the old global seeds. Better if they don't see it.

## Randomness

- You can mention that actually it is quite hard to produce high quality pseudo random
  numbers but numpy solves this problem for us and it's typically not worth to read up
  on the details of random number generators

## Creating random numbers

- The example is supposed to show that of course different calls to `rng.uniform`
  produce different realizations unless you reset the seed.

## Rules for randomness

For generating seeds randomly they can draw an integer without a seed and write it down.

Some people go very far to produce "really random seeds" but I think this is absolutely
not necessary. It is far more important to check that your main results do not depend on
the choice of seed.
