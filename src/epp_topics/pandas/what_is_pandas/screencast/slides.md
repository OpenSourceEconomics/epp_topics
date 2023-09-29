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

# Data management with pandas

### What is (modern) pandas

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is pandas

- Industry standard DataFrame library in Python
- Covers all you need for data management
  - Loading datasets in many formats
  - Cleaning data
  - Generating variables
  - Reshaping datasets
- Compatible with all plotting and statistics libraries

---

# What is a DataFrame

<br/>

<div class="grid grid-cols-2 gap-12">
<div>

<br/>

- Tabular data format
- Variables are columns
- Observations are rows
- Can be manipulated in Python


</div>
<div>

<style type="text/css">
#T_0534c   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_0534c thead {
  background-color: #3d3d3d;
}
#T_0534c tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_0534c tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_0534c td {
  padding: 0em;
}
#T_0534c th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_0534c caption {
  caption-side: bottom;
}
</style>
<table id="T_0534c">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_0534c_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_0534c_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_0534c_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_0534c_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0534c_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_0534c_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_0534c_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_0534c_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_0534c_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_0534c_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_0534c_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_0534c_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_0534c_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_0534c_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_0534c_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_0534c_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_0534c_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_0534c_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_0534c_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
    <tr>
      <th id="T_0534c_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_0534c_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_0534c_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_0534c_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_0534c_row3_col3" class="data row3 col3" >80.94</td>
    </tr>
  </tbody>
</table>



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

- Use the engine keyword when loading datasets
