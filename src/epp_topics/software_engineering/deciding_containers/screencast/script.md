# Script: When to use custom containers

## Fixed vs. free fields

- One could argue that in my example "students" also has fixed fields because it is
  typed in, i.e. fields are known at the time of writing the code. This is just because
  of the example. In a real application, we would read that data from some file.

## Immutability

This is mainly for deciding between dataclasses and namedtuples (or a motivation to use
frozen dataclasses).

If one needs a dict (e.g. for very fast lookup or because of free fields), they should
not use a NamedTuple.
