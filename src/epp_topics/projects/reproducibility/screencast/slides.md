---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Reproducible Research


### Definition of reproducibility

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Availability

- Source data:
  - If possible, include all datets in a common format
  - Else, add a detailed description on how to obtain it and where to store it
- Source code:
  - Include any code that is needed to produce your results
- Programs:
  - Document all programs that need to be installed to run your code
  - Automate the installation as much as possible with environments
- More detailed guidelines: [https://datacodestandard.org/](https://datacodestandard.org/)

---

# Version control

- Source data and source code are under version control
- Published results are created from the main branch with no uncommitted changes
- Use tags / releases to mark submissions, revisions, etc.

---

# Separation of source files and output

- All generated files are in a separate folder that can be safely deleted
- Generated files are not under version control
  - Can easily be out of date
  - Size of the GitHub repository explodes
  - Does not help with reproducibility
- You can make your results available separately from your source code, e.g. via
Dropbox

---

# Automation

There is one command that converts your source data into the paper


---

# Documentation and readability

- You strive for readability in your source code
- There is a README file that documents
  - Your directory structure
  - How to install packages
  - How to run your code
- Docstrins and comments explain the code where necessary
