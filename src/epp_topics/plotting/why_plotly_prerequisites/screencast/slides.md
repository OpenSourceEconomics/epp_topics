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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Plotting

### Why plotly? And some prerequisites.

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
- Kaleido tries to get rid of that ([background](https://github.com/plotly/Kaleido#background))
- Unfortunately, development stopped in a state that is broken on Windows


---

# Windows workaround

- [Comment](https://github.com/plotly/Kaleido/issues/150#issuecomment-1293508017) by former plotly employee:

  > We do have this unfortunate situation where some (mostly Windows?) users have
  > hanging calls which no one has gotten to the bottom of just yet, though. I don't
  > know that anyone is actively working on that issue, given the complexity of building
  > the project, but it seems to impact only a small minority of users.

- Feel free to add your experience to [this issue](https://github.com/plotly/Kaleido/issues/134)
- Install an old version of kaleido via pip:

```bash
$ conda activate [your_env]
$ pip install kaleido==0.1.0.post1
```
