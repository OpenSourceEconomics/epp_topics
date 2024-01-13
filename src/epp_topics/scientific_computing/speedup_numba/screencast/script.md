# Script: Writing fast code with numba

## Why numba can be fast

"Uses same technology as Julia under the hood". This means that numba will be as fast as
Julia when used as intended (loops over arrays). The selling point is that Julia can
optimize things numba cannot and still be reasonably fast. However, Julia is also
fastest if you write loops over arrays and don't use fancy data structures.

## Numba is picky

The main message here is the last point: Only use numba for bottlenecks!

## Naively jitting the example

A few years ago numba would not have made this any faster than pure Python. Now it is
much better at compiling code that does not write out all loops. However, If it is fast
enough, you can use such code. If you need maximum performance you should write out
loops.

## Full loops

Make it very clear that numba can be faster than numpy even though that is not the case
in the example. Sometimes up to 10x. It depends on the application.
