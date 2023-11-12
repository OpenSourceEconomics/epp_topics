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

# Plotting

### What to plot?

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Data types (Schwabish)

- Categorical
  - unordered
  - ordered
- Quantitative
  - discrete
  - continuous
    - interval scale
    - ratio scale

---

# Some rough guidelines

- Raw data (continuous): Scatterplots
- Fractions of categorical / discrete variables: Bar charts, potentially stacked
- Levels: Bar charts (including zeros!), unless interval scale
- Changes over time: Line charts
- ...

---

# Five guidelines (Schwabish)

1. Show the Data
1. Reduce the Clutter
1. Integrate the Graphics and Text
   - Label data directly (remove legend)
   - Write the title like a newspaper headline
   - Add explainers
1. Avoid the Spaghetti Chart
1. Start with Grey
