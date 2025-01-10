# Script: Visualizing optimizer histories

The main goal ist that they understand how important it is to compare the histories of
multiple optimizers. The rest shows the mechanics.

## Motivation

Say that in practice you should always run at least two optimizers and compare them in a
criterion plot. Typically many more than that.

## Criterion plot for multiple optimizations

Explain how beautiful this example is: All three optimizers come from different
libraries. We can not only use all of them but even look at their internals (which none
of the original libraries let you do!)
