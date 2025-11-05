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
title: EPP — Testing code that should raise errors
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Software engineering


### Testing code that should raise errors

<br>


Janoś Gabler and Hans-Martin von Gaudecker



---

# Reminder of the example

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> raw = pd.read_csv("survey.csv")
>>> raw
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Q001</th>
      <th>Q002</th>
      <th>Q003</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strongly disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>1</th>
      <td>strongly agree</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-77</td>
      <td>disagree</td>
      <td>R</td>
    </tr>
    <tr>
      <th>3</th>
      <td>agree</td>
      <td>-77</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-99</td>
      <td>-99</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>6</th>
      <td>neutral</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>7</th>
      <td>disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>8</th>
      <td>strongly agree</td>
      <td>-99</td>
      <td>PYTHON</td>
    </tr>
    <tr>
      <th>9</th>
      <td>agree</td>
      <td>-99</td>
      <td>Ypthon</td>
    </tr>
  </tbody>
</table>

</div>
<div>

<br/>
<br/>


From the metadata you know

- Q001: I am a coding genius
- Q001: I learned a lot
- Q003: What is your favourite language

<br/>

- -77 not readable
- -99 no reply


</div>
</div>

---

# What will happen for invalid data?

<div class="grid grid-cols-2 gap-4">
<div>

```python
def _clean_agreement_scale(sr):
    sr = sr.replace(
        {
            "-77": pd.NA,
            "-99": pd.NA
        }
    )
    categories = [
      "strongly disagree",
      "disagree",
      "neutral",
      "agree",
      "strongly agree"
    ]
    dtype = pd.CategoricalDtype(
      categories=categories,
      ordered=True
    )
    return sr.astype(dtype)
```

</div>
<div>

- What if next year the survey tool changed the representation of missings?
- What if categories were changed?

<br/>
<br/>

- What do you actually expect the function to do?

</div>
</div>


---

# Tests pin down desired behaviour

```python
import pytest


def test_clean_agreement_scale_invalid_data():
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series([-77, "typo"]))
```

<br/>

- Passing two codes that should not work
- We expect a `ValueError` to be raised
- Test will fail if
  - no error is being raised
  - a different error is being raised


---

# Run pytest

<img src="/run_failed.png" class="rounded" width="550"/>

---

# Tests teach you programmes' behaviour

- This is how I learned that `.astype(pd.CategoricalDtype())` sets values that are not
  among the categories to missing!
- Small examples are exactly the right level to learn
- Imagine this would have happened in a large project, where you would have noticed
  only when only 5% of the expected sample size is left in regression tables!
- "Fail early, fail often"


---

# For the record: Solution

```python
def _clean_agreement_scale(sr):
    known_missings = {"-77", "-99"}
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    if invalid_values := set(sr.unique()) - set(categories) - known_missings:
        msg = f"Unexpected values in agreement scale: {invalid_values}"
        raise ValueError(msg)
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.replace({m: pd.NA for m in known_missings}).astype(dtype)
```
---

# Run pytest, again

<img src="/run_fixed.png" class="rounded" width="550"/>
