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

### Practical approach

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Why we use plotly in class

- Interactive plots work out of the box
- Supports all relevant output formats:
    - Interactive dashboards
    - HTML
    - static image formats
- Also available in R and Julia


---

# Windows Issues

- On some windows computers, the static export gets stuck
- A workaround is to install and old version of kaleido

```txt
pip install kaleido==0.1.0.post1
```
- You need to do this after activating your environment!
