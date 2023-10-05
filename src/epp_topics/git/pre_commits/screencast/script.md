# Script: Pre-commit hooks

The example repo is inside screencast. If you need to re-do the screenshots:

- Copy it outside of our repo
- Run git init
- Commit `.pre-commit-config.yaml`

## What are pre-commit hooks

- Reference the styleguide screencast in software engineering

## Configuring pre-commit hooks

- Main message here is that they do not need to configure pre-commit hooks themselves

## A badly formatted python file

- Single blank line between function definitions
- Inconsistent white space around operators
- Random mix of single and double quotes

## Git status

Just meant to show them where we are

## First commit fails

- Say that there is no reason to panic!
- This is the one time where simply running things a second time might help.

## Second commit

- Say that it is important here to use `-am` or re-add the files that have been changed
  by black during the first commit. Otherwise it won't work.
- Say that if the second commit also fails they need to read the error messages
  carefully. Most likely it is because the need to fix something manually and the
  messages will tell theme where and what.
