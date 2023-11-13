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

# Reading list

- [Calling Bullshit](https://www.callingbullshit.org/) (Carl Bergstrom &
  Jevin West), Chapter 7
- [How Charts Lie](http://www.thefunctionalart.com/p/reviews.html) (Alberto Cairo).
- [Better Data
  Visualizations](https://policyviz.com/pv_books/better-data-visualizations-a-guide-for-scholars-researchers-and-wonks/)
  (Jonathan Schwabish)
- [The Functional Art](http://www.thefunctionalart.com/p/about-book.html) (Alberto
  Cairo)
- [Show Me the Numbers](http://www.perceptualedge.com/library.php) (Stephen
  Few)


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

# Some (too) simple recipes

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
