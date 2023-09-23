# Effective Programming Practices for Economists: Topics

1. Background
   - Operating systems _(Don't change, record)_
   - Graphs _(Don't change much, record)_
   - Filesystem _(Very short, Linux/MacOS vs. Windows)_
   - Floating point numbers _(Find good resource)_
1. Tools
   - Shell: Basics / background _(Short, mostly old material)_
   - Shell: Navigation _(New(ish))_
   - Shell: Installation of Mamba and course environment _(Video, text)_
   - Installation: Git, VS Code _(only text / links)_
   - Editors, comparison IDEs _(short)_
     - VS Code
     - Stata / Matlab / RStudio
     - In the end, VS Code encompasses most features of IDE + same for all languages
   - Using LLMs effectively _\[long run\]_
   - Using copilot effectively _\[long run\]_
   - Regex _\[long run\]_
   - Communicating effectively (emails vs zoom vs in-person vs zulip) _(Video)_
   - Licenses _(Look up stuff)_
1. Git and GitHub
   - Motivation and terminology _(record anew)_
   - Committing and Diffing _(Look up stuff)_
   - Pushing and Pulling _(Look up stuff)_
   - Merging _(Look up stuff)_
   - Troubleshooting _(Look up stuff)_
   - Collaboration and Teamwork _(Look up stuff)_
1. Python basics
   - Assigning variables, built-in scalar types _(record anew)_
   - Built-in container types _(record anew)_
   - Reading tracebacks _(record anew)_
   - Importing, Modules, Namespaces
   - Filesystem in Python: The `pathlib` library _(record anew)_
   - Executing Python code: .py files _(record anew)_
   - Executing Python code: Notebooks _(record anew)_
   - Executing Python code: Debuggers, pytest, pytask _(record anew)_
   - Decorators _(record anew, further material: Harrison)_
   - Custom data containers
   - Reading object-oriented code _\[long run\]_
   - More on f-strings (could also do as an exercise)
1. Best practices (any language)
   - Avoid code duplication (iteration, functions) _(record anew)_
     - Objective: Understand Concept. Do stuff, see patterns that come out
   - Pure and testable functions _(record anew)_
   - Comments should be function names _(record anew)_
   - Avoid nested if conditions _(record anew)_
   - Naming conventions / formatting / pre-commits _(record anew)_
   - Choosing container types (list / dict / custom class) _(record anew)_
   - dags _\[long run\]_ - pytrees _\[long run\]_ - Don't be too smart
     ([link](https://hackernoon.com/why-senior-devs-write-dumb-code-and-how-to-spot-a-junior-from-a-mile-away-27fa263b101a))
     _(set up examples, make scorecards / notebooks out of those, record short video)_
   - When to code up something yourself and when to use a library _\[long run\], (record
     screencast with recipes)_
1. Ensure Correctness - Testing
   - Debugging
   - Error handling
1. Workflow management
   - Definition of "reproducible" - Pytask overview
   - Tiny Pytask example
   - Generating many tasks at once
   - Templates
1. Scientific computing
   - Numpy/scipy
   - Optimisation
   - Estimagic
   - Speedup
1. Data Science
   - Data Management
   - Plotting
   - Machine learning with Scikit-learn
   - (Econometrics with ...)

## Installation

- Create the conda environment
- do `pip install jupyterquiz`

(Adding jupyterquiz directly in environment.yml leads to problems)
