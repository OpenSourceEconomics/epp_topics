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
title: EPP — Pandas — What is (modern) pandas?
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### What is (modern) pandas?

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is pandas?

- Industry standard DataFrame library in Python
- Covers all you need for data management
  - Loading datasets in many formats
  - Cleaning data
  - Generating variables
  - Reshaping datasets
- Compatible with all plotting and statistics libraries

---

# What is a DataFrame?

<br/>

<div class="grid grid-cols-2 gap-12">
<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2007</td>
      <td>80.94</td>
    </tr>
  </tbody>
</table>

</div>

<div>

- Tabular data format
- Variables are columns
- Observations are rows
- Can be manipulated in Python


</div>
</div>


---

# What is **modern** pandas?

- Pandas was created in 2008 and has some baggage
- With version 3.0 many things will improve
- Those features can already be enabled now:
  - More speed and less memory usage through better dtypes
  - Less confusion through copy-on-write
  - Better handling of missing values
  - Removal of the `inplace` argument


---

# How to use modern pandas

- Install version 2.1 or higher of pandas
- Install version 13.0 or higher of pyarrow
- Set some options after import

```python
import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
```

- When loading datasets, use `engine="pyarrow"` if available
