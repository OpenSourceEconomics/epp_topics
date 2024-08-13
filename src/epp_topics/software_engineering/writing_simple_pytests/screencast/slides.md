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
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Software engineering


### Writing simple (py)tests

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

# First function in clean_data.py

```python
def _clean_agreement_scale(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.astype(dtype)
```

---

# A function in test_clean_data.py


<div class="flex gap-12">
<div>

Function's properties:
- starts with `test_`
- name explains what it does
- defines what we expect
- calls the function to be tested to calculate actual result
- asserts that actual and expected results coincide

</div>
<div>

```python
def test_clean_agreement_scale_check_dtype():
    expected = pd.CategoricalDtype(
        categories=[
            "strongly disagree",
            "disagree",
            "neutral",
            "agree",
            "strongly agree",
        ],
        ordered=True,
    )
    actual = _clean_agreement_scale(pd.Series([])).dtype
    assert expected == actual
```

</div>
</div>


---

# Another function in test_clean_data.py

```python
def test_clean_agreement_scale_known_missings():
    result = _clean_agreement_scale(pd.Series(["-77", "-99"]))
    expected = pd.Series([pd.NA, pd.NA], dtype=result.dtype)
    pd.testing.assert_series_equal(result, expected)
```


---

# Run pytest

<img src="/run_verbose.png" class="rounded" width="550"/>

---

# Basic rules

- Put tests in modules called `test_XXX.py`, with functions `test_YYY_ZZZ`, ...
  - `XXX` is the name of the module to be tested
  - `YYY` is the name of the function to be tested
  - `ZZZ` is a description of the behaviour being tested
- Inside these functions, keep structure clear:
  - Define expected result
  - Calculate actual result
  - Assert that they coincide
- Usually one assert statement per test function
