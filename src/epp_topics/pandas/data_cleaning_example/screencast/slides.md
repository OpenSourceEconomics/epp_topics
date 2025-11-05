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
title: EPP — Pandas — Data cleaning example
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Data cleaning example

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Survey of course participants

<style>
table th {
  text-align: left !important;
}
</style>

<div class="grid grid-cols-2 gap-8">
<div>

|    | Q001              | Q002           | Q003   |
|---:|:------------------|:---------------|:-------|
|  0 | strongly disagree | agree          | python |
|  1 | strongly agree    | strongly agree | Python |
|  2 | -77               | disagree       | R      |
|  3 | agree             | -77            | Python |
|  4 | -99               | -99            | Python |
|  5 | nan               | strongly agree | Python |
|  6 | neutral           | strongly agree | Python |
|  7 | disagree          | agree          | python |
|  8 | strongly agree    | -99            | PYTHON |
|  9 | agree             | -99            | Ypthon |

</div>
<div>

- Q001: I am a coding genius
- Q002: I learned a lot
- Q003: What is your favourite language?

<br/>

- -77 not readable
- -99 no reply

<br/>

```python
>>> df = pd.read_csv("survey.csv")
>>> df.dtypes
Q001    str
Q002    str
Q003    str
dtype: object
```

</div>
</div>
