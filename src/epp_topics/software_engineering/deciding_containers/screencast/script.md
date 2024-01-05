# Script: When to use custom containers?

## Running example

- Same as before: Want to record basic data of students in this course: First name, last
  name, email
- Now store these data for each run of this course

## Fixed vs. free fields

- You know ex ante what data you want a `Student` to look like, hence you can type
  identifiers (fixed fields)
- You do not know the names / keys of students in a course when you set up the
  framework, hence you need the flexibility of free fields (here: string literals, in
  real world would read in from a file)

## Immutability

This is mainly for deciding between dataclasses and NamedTuples (or a motivation to use
frozen dataclasses).

If you need a dict (e.g. for very fast lookup in large collections or because of free
fields), you really do not want to use a NamedTuple / dataclass.
