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
title: EPP — What does pytest do?
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Software engineering


### What does pytest do?

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Example

consider this hypothetical survey about a programming course

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

# Two functions in clean_data.py

```python
def _clean_agreement_scale(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.astype(dtype)


def _clean_favorite_language(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    sr = sr.str.lower().str.strip()
    sr = sr.replace("ypthon", "python")
    return sr.astype(pd.CategoricalDtype())
```

---

# New module: test_clean_data.py

- 4 assertions whether actual results match our expectation
- Will look at syntax in subsequent screencast


---

# Step 1: Collection

<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

<br/>

- Go through all folders in working directory
- Collect all files with name `test_XXX.py`
- Go through those files and collect all functions that start with `test_`
- All these test functions will be executed (fine-grained control possible)

</div>
<div class="col-span-3">

<img src="/collect_only.png" class="rounded" width="500"/>


</div>
</div>


---

# Step 2: Execute the tests

<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

- All test functions are executed
- A report is printed to the screen

</div>
<div class="col-span-3">

<img src="/run.png" class="rounded" width="500"/>

</div>
</div>


---

# Step 2: Execute the tests

<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

- `pytest -v` gives more detailed progress reports
- Can be very helpful for long-running tests

</div>
<div class="col-span-3">

<img src="/run_verbose.png" class="rounded" width="500"/>

</div>
</div>

---

# Step 3: Inspect failures

<img src="/run_failed.png" class="rounded" width="600"/>

---

# Step 3: Inspect failures with pdb

<img src="/run_pdb.png" class="rounded" width="600"/>
