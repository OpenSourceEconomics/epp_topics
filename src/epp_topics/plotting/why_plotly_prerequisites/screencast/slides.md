---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: EPP — Plotting — Why plotly? And a prerequisite
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Plotting

### Why plotly? And a prerequisite

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Python plotting landscape

Static plots:
- matplotlib
- seaborn

Interactive plots:
- vega-altair
- bokeh
- plotly

---

# Why we use plotly

- Interactive plots work out of the box

- Supports all relevant output formats:

    - Interactive dashboards

    - HTML

    - static image formats

- Also available in R and Julia

---

# Supporting static and interactive plots

- Interactive plots typically based on JavaScript

- Rely on browser functionality for static exports

- Kaleido hides that by installing a browser to export static plots

- Must run `plotly_get_chrome` (in pixi environment: `pixi run plotly_get_chrome`)
