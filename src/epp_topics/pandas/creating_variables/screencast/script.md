# Script: Creating variables

## Intro

- By creating variables we mean applying transformations to existing columns in a
  DataFrame

Outline:

- Using numpy math functions
- Arithmetic with Series
- Recoding values
- Vectorized if conditions
- When is it okay to loop?

## Arithmetic with Series:

About the last bullet point: I have observed that people store even intermediate series
in a DataFrame because they don't know that they can simply assign as python variables.

## Vectorized if conditions

- The specific example could have been done by `pd.cut`. Couldn't find and example with
  gapminder data that needs full generality of `Series.where`

## When can you loop

Mention the following:

1. Even though the rule is simple it is a very very good rule of thumb and there are
   basically no exceptions
1. The exact reasons are two complicated to explain and they do not have to know them
1. List comprehensions, df.apply and similar things are basically just loops. When we
   say no loop we mean vectorized (i.e. the loop is written in a fast language)

My mental model of why loops over rows are so slow:

1. Loops over rows need to create a fresh Series, i.e. call an init method of a Series
   which will then call an init method of a numpy array.
1. When looping over rows, typically we access individual variables of that row. This
   means that there are repeated slow index lookups.
1. Typically a DataFrame has more rows than columns, so the loops are long
1. Insertion of the results into a Series are costly

In contrast, loops over columns don't have these costs

1. Only need to look up the Series, it is already created
1. Applying a function to a Series inside the loop typically dominates any loop overhead
1. Just one result needs to be inserted.
