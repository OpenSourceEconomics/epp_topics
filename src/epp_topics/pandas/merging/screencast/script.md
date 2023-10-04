# Script: Merging datasets

## Motivation

Say that all examples are tiny pieces of the gapminder dataset and we will usually show
all involved DataFrames fully.

Mention that it is always a good idea to practice using the merge functions with tiny
inputs to gain intuition

## Failing concatenation

- index 0, 1, 2 in both cases
- but country and year are different
- Use merge function to fix this

## 1:1 merge

- Explain why this is called 1:1 merge
- Mention that with merge you really rarely want to leave everything at defaults
  - e.g. inner join might not be what we want here!
