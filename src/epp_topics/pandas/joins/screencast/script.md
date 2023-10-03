# Script: Joining datasets

## Motivation

Say that all examples are tiny pieces of the gapminder dataset and we will usually show
all involved DataFrames fully.

Mention that it is always a good idea to practice using the merge functions with tiny
inputs to gain intuition

## 1:1 merge

- Explain why this is called 1:1 merge
- Mention that with merge you really rarely want to leave everything at defaults
  - e.g. inner join might not be what we want here!

I used `reset_index` here to create a situation where concat would have been
catastrophic even though it produces no error.

## How

I did not find a way to fit a proper heading on this slide
