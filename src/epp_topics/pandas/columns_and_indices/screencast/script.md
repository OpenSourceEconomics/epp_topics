# Script: Setting and renaming columns and indices

## Intro slide

- Why the Index is important
- Setting and resetting the index
- Renaming columns

## Why the index is important

Mention that they will see on the next slide how to set the index

Regarding "Using a meaningful index makes this even safer". Imagine you:

- Start with a DataFrame with a meaningless RangeIndex
- Drop some rows
- Reset the index
- Then go back to the original index -- subtle bugs
- If the index contains actual data, that does not happen
