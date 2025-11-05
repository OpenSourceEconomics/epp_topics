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
title: EPP — Pandas — Functional data cleaning — The How
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Functional data cleaning: The How

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
  raw_survey = pd.read_csv("survey.csv")
  ```


</div>
</div>

---

# Code

```python
def clean_data(raw):
    df = pd.DataFrame(index=raw.index)
    df["coding_genius"] = clean_agreement_scale(raw["Q001"])
    df["learned_a_lot"] = clean_agreement_scale(raw["Q002"])
    df["favorite_language"] = clean_favorite_language(raw["Q003"])
    return df

def clean_agreement_scale(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.astype(dtype)

def clean_favorite_language(sr):
    sr = sr.str.lower().str.strip()
    sr = sr.replace("ypthon", "python")
    return sr.astype(pd.CategoricalDtype())


raw_survey = pd.read_csv("survey.csv")
cleaned_survey = clean_data(raw_survey)
```

---

# Result

<style>
table th {
  text-align: left !important;
}
</style>

<div class="flex gap-8">
<div>

|    | coding_genius     | learned_a_lot   | favorite_language   |
|---:|:------------------|:----------------|:--------------------|
|  0 | strongly disagree | agree           | python              |
|  1 | strongly agree    | strongly agree  | python              |
|  2 | NaN               | disagree        | r                   |
|  3 | agree             | NaN             | python              |
|  4 | NaN               | NaN             | python              |
|  5 | NaN               | strongly agree  | python              |
|  6 | neutral           | strongly agree  | python              |
|  7 | disagree          | agree           | python              |
|  8 | strongly agree    | NaN             | python              |
|  9 | agree             | NaN             | python              |

</div>
<div>


```python
>>> df.dtypes
coding_genius     category
learned_a_lot     category
favorite_language category
dtype: object

>>> df["coding_genius"].cat.categories
[
    'strongly disagree',
    'disagree',
    'neutral',
    'agree',
    'strongly agree'
]

>>> df["favorite_language"].cat.categories
['python', 'r']
```

</div>
</div>


---

# 1. Start with an empty DataFrame


```python
def clean_data(raw):
    df = pd.DataFrame(index=raw.index)
    df["coding_genius"] = clean_agreement_scale(raw["Q001"])
    df["learned_a_lot"] = clean_agreement_scale(raw["Q002"])
    df["favorite_language"] = clean_favorite_language(raw["Q003"])
    return df
```

---

# 2. Touch every variable just once

```python
def clean_data(raw):
    df = pd.DataFrame(index=raw.index)
    df["coding_genius"] = clean_agreement_scale(raw["Q001"])
    df["learned_a_lot"] = clean_agreement_scale(raw["Q002"])
    df["favorite_language"] = clean_favorite_language(raw["Q003"])
    return df
```

---

# 3. Touch with a pure function

```python
def clean_agreement_scale(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.astype(dtype)


def clean_favorite_language(sr):
    sr = sr.str.lower().str.strip()
    sr = sr.replace("ypthon", "python")
    return sr.astype(pd.CategoricalDtype())
```
