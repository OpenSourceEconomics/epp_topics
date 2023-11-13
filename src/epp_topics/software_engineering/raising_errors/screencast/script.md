# Script: How to raise errors

## Raising a built-in exception

- Say that the `# ...` stands for the actual implementation of the function

## Common built-in exceptions

- Make it clear that most of the built-in exceptions are relevant for library authors
  and they will only get them as users. When they do their own error handling they can
  get very far with TypeError and ValueError.

## fail functions

- This example is equivalent to the previous one
- Say again that the `# ...` stands for the actual implementation of the function

## Collect multiple errors before raising

- If you need to combine a report across multiple fail functions you are probably going
  too far. Reason:If early functions failed (e.g. we don't have a dict where we need
  one), later check functions might produce errors where we don't want it (e.g. when
  accessing keys)
