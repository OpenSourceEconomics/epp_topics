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


### What are the project templates?

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What are the project templates?

1. An example of an empirical project that helps you learn pytask
   - All best practices are implemented
   - Convenient approach to handling file paths
1. A recommended directory structure you can customize
   - Folders for the typical steps in a research project
   - Clear separation of source files and results
1. A convenient way of starting your own project
   - Cookiecutter helps you fill in your details
   - Documentation guides you through the setup


---

# Terminology

- **Cookiecutter**: A Python library that helps you customise a project to your needs
- **Pytask**: A build system that executes the different steps of your research
project, keep track of dependencies between steps, and only execute what needs to be
executed. It can execute independent tasks in parallel.
- **Project templates**: An example project implementing best practices and a
recommended directory structure for pytask projects
