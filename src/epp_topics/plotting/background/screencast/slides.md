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

### Background

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Typical Goals of Plotting

1. Summarize data to quickly learn about patterns in data
   - Trends over time
   - Bivariate patterns (scatterplot, regression line)
1. Highlight insights and tell stories
   - Leave out unnecessary information
   - Use accent colors for most interesting points


---

# 1. Exploration

- Goal: Find patterns in data
- Making a plot has to be fast!
- Interactivity is important
- Using clear labels always helps

---

# 2. Publication

- Goal: Communicate patterns in data/results
- Plot needs to be self-explanatory
- Aesthetics is key
- Papers need static plots

---

# Workflow

- Think: What question should the plot answer?
- Sketch the plot on paper
- Find a similar plot in the documentation of your plotting library
- Make a quick plot to see if your ideas work
- Make it pretty
- Make sure the plot is self-explanatory (ask someone else)

---

# Example

- How does life expectancy develop ...
  - ... over time since 1950?
  - ... in different countries (Americas, Europe)?
- Start by thinking about type of plot
