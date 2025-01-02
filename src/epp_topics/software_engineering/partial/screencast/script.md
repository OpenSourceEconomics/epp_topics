# Script: Partialling arguments to functions

## Example

Maybe remove the traceback and just say that calling f without a value for y would yield
an error

## Mental models

I learned partial as partially evaluating a function but did not find this mental model
helpful; In Python it also does not happen. partial does no calculations and simply
stores the inputs with the function. This is why I want to offer the other two mental
models.

## Useful applications

Two main messages:

1. Partial is much more powerful than people think, especially for scientific code. We
   do a lot of the magic in optimagic using partial. Often people would be surprised
   that can do so many things without object oriented programming. But:

   - "An object is just a poor man's closure" (famous quote with unknown author)
   - "partial is just the most explicit form of a closure" (me)

1. Partial can be over-used. I have mainly seen it from Tim a while ago, when he used
   partial for almost all function calls just to save a few lines here and there. Then
   the drawback was that there were many different versions of a minimize function and
   it was hard to keep track of them.
