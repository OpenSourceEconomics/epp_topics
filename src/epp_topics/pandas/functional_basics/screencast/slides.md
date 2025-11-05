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
title: EPP — Pandas — Functional data cleaning — Basics
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Functional data cleaning: Basics

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

- All variables are strings after running

  ```python
  raw = pd.read_csv("survey.csv")
  ```


</div>
</div>

---

<div class="grid grid-cols-2 gap-4">
<div>

# Example

```python
>>> def clean(survey_df):
...     out = pd.DataFrame(index=survey_df.index)
...     out["coding_genius"] = convert_to_ordered_cat(survey_df["Q001"])
...     out["learned_a_lot"] = convert_to_ordered_cat(survey_df["Q002"])
...     out["favorite_language"] = _clean_favorite_language(survey_df["Q003"])
...     return out

>>> df = clean(raw)
```
</div>
<div>

# Rules

- Start with an empty DataFrame for the clean data

- One pure function (could be identity) per variable (df column).

- Each function returns a new Series

- Avoid state at all costs. I.e., touch every variable just once.

</div>
</div>
