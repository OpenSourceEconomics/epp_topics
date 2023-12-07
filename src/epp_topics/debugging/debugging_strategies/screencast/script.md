# Script: Strategies for debugging

- Mention that we will go much deeper on some of the rules in later videos. This is just
  an introduction.

# Rule 3:

- Each experiment becomes a test case:
  - So that you can re-run all of them with a single command
  - How else are you going to know that the bug has actually been fixed?
  - Then at least your debugging has a long-term value and is not just pure suffering

# Rule 5:

- Make a git commit: People hesitate to commit code that is not running. It is so
  important that you start from a fresh git commit when debugging. Tim has learned it
  the hard way several times in tranquilo and lcm and does it religiously now.

- "Undo changes that were not helpful": Say that The more things you change at once, the
  harder it is to know what is responsible for what. If they committed before starting
  to debug, git reset --hard can be their friend.
