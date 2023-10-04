# Script: Definition of reproducibility

This definition is much stricter than what is usually required by journals

We expect all of this for a good grade in final projects

# Availability

Miklos Koren's guidelines are more detailed and in some regards stricter than ours. As I
see, we only really deviate in point 3:

"Analysis data is provided as part of the replication package unless they can be fully
reproduced from accessible data within a reasonable time frame. Exceptions are explained
under Rule 1."

As far as I understand, analyisis data refers to generated outputs.

I will make a suggestion on a later slide of how to reconcile the two approaches

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

The purpose of makig results available is not reproducibility but ease of inspecting
details that were not mentioned in the paper

# Automation

This command is typicall `pytask`

Talk about the implications

- No notebooks that need to be executed manually
- There is no clicking or manual copy-pasting
- There is no commenting out code and running again
- There is no need to run multiple files in the correct order
- ...

I suggest the following recommandation:

- Do not keep analysis data under version control
- Make sure that any kind of analysis data could be safely deleted because it can be
  reproduced
- If the analyisis is very time consuming, make your generated files available
  separately from the source code
