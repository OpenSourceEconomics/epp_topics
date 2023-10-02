# Script: Inspecting and summarizing data

## Motivation

Last year people really missed Statas browse feature and if you only work in a notebook
inside vscode on a laptop screen and look at the entire df, I get why you might miss
that.

The motivation for this screencast should be that if you are good at selecting subsets
of dataframes, summarizing them and maybe using `.plot` you will have something better
than statas browse.

- Look at subsets was already covered
- Tell them that we'll cover groupby in more detail in another screencast

## Example

- In most cases, the columns will also not fit
- There are ways to display more of a large DataFrame but for real datasets the screen
  is simply not big enough

## Quick plotting

- Mention that they will understand why we set the plotly backend in our plotting
  lecture and for now they can just copy it

- I just show plotting in combination with groupby because that makes sense for my data.
  Important thing is that any Series has a `.plot` and `.hist` method and looking at the
  distribution that way can be very helpful!

- Plot is ugly, but gives you hover information in notebook -- three outliers are
  Cambodia and twice Rwanda, would conclude that unfortunately data is correct, not
  erroneous
