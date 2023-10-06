# Script: Definition of reproducibility

This definition is much stricter than what is usually required by journals

We expect all of this for a good grade in final projects

# Version control

The points imply that git is used throughout the project and not just in the end (last
year some people thought, it is enough to commit in the end)

- **Published results** here refers to anything that is shared, e.g. conference slides,
  working papers also count as published

# Separation of source files and output

About the reasons not to put outputs under version control

- Make an example of committing without running the code and how this leads to out of
  date outputs if they are under version control

- Mention that outputs are often binary; since git cannot handle binaries efficiently
  the repo size explodes

- Make very clear that just because you stored and output, it does not mean you can
  reproduce it!

The purpose of making results available is not reproducibility but ease of inspecting
details that were not mentioned in the paper

# Automation

This command is typically `pytask`

Talk about the implications

- No notebooks that need to be executed manually
- There is no clicking or manual copy-pasting
- There is no commenting out code and running again
- There is no need to run multiple files in the correct order
- ...

# Summing up

- Availability
- Version Control
- Separation of source and output
- Automation
- Documentation and readability
