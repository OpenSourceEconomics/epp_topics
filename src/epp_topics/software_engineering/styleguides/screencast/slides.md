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
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### Styleguides

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Main message

- Styleguides are important
- Styleguides do not automatically make code good
- Styleguides should be automated!

---

# Naming conventions

- Functions and methods are `lowercase_with_underscores`
- Local variables are `lowercase_with_underscores`
- Global variables ar `UPPERCASE_WITH_UNDERSCORES`
- Classes are `CamelCase`, instances are `lowercase_with_underscores`
- Private functions start with `_underscores`

---

# Why naming conventions are important

- Help to communicate information without extra characters
- Make it easier to read code written by others
- Reduce your mental load when deciding about variable names
- Do not cost any time to implement

---

# Examples of formatting rules

- Loop and function bodys are indented by four spaces (mandatory)
- Maximum line length of 88 characters
- Two blank lines between function definitions, one between method definitions
- Whitespaces around operators
- ...

---

# Why formatting is important

- Many formatting rules are based on rigorous research about code readability
- Indentation helps to prevent bugs!
- Familiar formatting makes it easier to read code written by others


---

# Why styleguides should be automated

- Code style is important, so it has to be enforced
- Formatting is boring, so it should be automated
- Manual formatting and discussions about it distract from important things

---

# How to automate styleguides?

- Linters in your editor
- Formatters in your editor
- Pre-commit hooks
