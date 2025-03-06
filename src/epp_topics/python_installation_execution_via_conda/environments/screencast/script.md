# Script: Environment files and environments

## Environment files vs. environments

Mention:

- Adding a package to the environment file will not automatically install it
- Let conda/mamba manage your packages and never delete or modify the folder with
  installed packages yourself

## Anatomy of environment.yml

- Explain already that here we mainly list the packages we want to import at some point
  and not the low level dependencies they might have.
- I actually don't know what the nodefaults does and why it is good practice; We just
  always have it.

## Dependencies are automatically installed

- The main goal is to drive home that they should never export environments and instead
  always write them by hand.

## How to add a package

- Explain again that if you always use this way you might lose a few minutes from
  environment creation but can save hours in debugging problematic environments on your
  coauthor's machine.
- Maybe create a bit of fear that we would deduct points if the environment file in
  final projects does not work.
