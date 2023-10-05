# Script: Styleguides

## Main message

Say that we want to focus on the bigger picture in this screencast. The detailed
styleguides are all listed in Additional materials.

## Naming conventions

- more detailed conventions are in PEP8 (link in additional materials) and that it is
  worth to read that once
- say that it is of course easily possible to come up with a bad function name that is
  lowercase with underscores, so naming conventions do not alleviate you from thinking
  about good names
- Explain that private functions are simply small helper functions that should not be
  imported from another module

## Why naming conventions are important

About "Reduce your mental load when deciding about variable names"

Example: When deciding on a function name you can fully focus on content, not on whether
you want to use CamelCase or lowercase_with_underscores for it

## Why styleguides should be automated

Tell them about the times where we spent days on formatting code!

Mention that it is still a good idea to learn how to write roughly compliant code
yourself.

## How to automate styleguides

Pre-commit hooks are the only way to do it consistently in large projects

Linters can be a good help to learn about styleguides in the beginning
