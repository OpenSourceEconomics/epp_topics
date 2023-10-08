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
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Reproducible Research


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

<style type="text/css">
#T_1750e   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_1750e thead {
  background-color: #3d3d3d;
}
#T_1750e tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_1750e tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_1750e td {
  padding: 0em;
}
#T_1750e th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_1750e caption {
  caption-side: bottom;
}
</style>
<table id="T_1750e">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_1750e_level0_col0" class="col_heading level0 col0" >Q001</th>
      <th id="T_1750e_level0_col1" class="col_heading level0 col1" >Q002</th>
      <th id="T_1750e_level0_col2" class="col_heading level0 col2" >Q003</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_1750e_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_1750e_row0_col0" class="data row0 col0" >strongly disagree</td>
      <td id="T_1750e_row0_col1" class="data row0 col1" >agree</td>
      <td id="T_1750e_row0_col2" class="data row0 col2" >python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_1750e_row1_col0" class="data row1 col0" >strongly agree</td>
      <td id="T_1750e_row1_col1" class="data row1 col1" >strongly agree</td>
      <td id="T_1750e_row1_col2" class="data row1 col2" >Python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_1750e_row2_col0" class="data row2 col0" >-77</td>
      <td id="T_1750e_row2_col1" class="data row2 col1" >disagree</td>
      <td id="T_1750e_row2_col2" class="data row2 col2" >R</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_1750e_row3_col0" class="data row3 col0" >agree</td>
      <td id="T_1750e_row3_col1" class="data row3 col1" >-77</td>
      <td id="T_1750e_row3_col2" class="data row3 col2" >Python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_1750e_row4_col0" class="data row4 col0" >-99</td>
      <td id="T_1750e_row4_col1" class="data row4 col1" >-99</td>
      <td id="T_1750e_row4_col2" class="data row4 col2" >Python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_1750e_row5_col0" class="data row5 col0" >nan</td>
      <td id="T_1750e_row5_col1" class="data row5 col1" >strongly agree</td>
      <td id="T_1750e_row5_col2" class="data row5 col2" >Python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_1750e_row6_col0" class="data row6 col0" >neutral</td>
      <td id="T_1750e_row6_col1" class="data row6 col1" >strongly agree</td>
      <td id="T_1750e_row6_col2" class="data row6 col2" > Python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_1750e_row7_col0" class="data row7 col0" >disagree</td>
      <td id="T_1750e_row7_col1" class="data row7 col1" >agree</td>
      <td id="T_1750e_row7_col2" class="data row7 col2" >python</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_1750e_row8_col0" class="data row8 col0" >strongly disagree</td>
      <td id="T_1750e_row8_col1" class="data row8 col1" >-99</td>
      <td id="T_1750e_row8_col2" class="data row8 col2" >PYTHON</td>
    </tr>
    <tr>
      <th id="T_1750e_level0_row9" class="row_heading level0 row9" >9</th>
      <td id="T_1750e_row9_col0" class="data row9 col0" >-77</td>
      <td id="T_1750e_row9_col1" class="data row9 col1" >-99</td>
      <td id="T_1750e_row9_col2" class="data row9 col2" >Ypthon</td>
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

<img src="run_verbose.png" class="rounded" width="550"/>

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
