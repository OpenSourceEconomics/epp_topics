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

# Data management with pandas

### Creating variables

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Using numpy math functions


<div class="flex gap-12">
<div>

assume that `df` is the gapminder example

```python
>>> import numpy as np
>>> df["log_life_exp"] = np.log(df["life_exp"])
>>> df
```

<style type="text/css">
#T_06533   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_06533 thead {
  background-color: #3d3d3d;
}
#T_06533 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_06533 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_06533 td {
  padding: 0em;
}
#T_06533 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_06533 caption {
  caption-side: bottom;
}
</style>
<table id="T_06533">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_06533_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_06533_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_06533_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_06533_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_06533_level0_col4" class="col_heading level0 col4" >log_life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_06533_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_06533_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_06533_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_06533_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_06533_row0_col3" class="data row0 col3" >77.16</td>
      <td id="T_06533_row0_col4" class="data row0 col4" >4.35</td>
    </tr>
    <tr>
      <th id="T_06533_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_06533_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_06533_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_06533_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_06533_row1_col3" class="data row1 col3" >78.27</td>
      <td id="T_06533_row1_col4" class="data row1 col4" >4.36</td>
    </tr>
    <tr>
      <th id="T_06533_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_06533_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_06533_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_06533_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_06533_row2_col3" class="data row2 col3" >79.78</td>
      <td id="T_06533_row2_col4" class="data row2 col4" >4.38</td>
    </tr>
    <tr>
      <th id="T_06533_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_06533_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_06533_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_06533_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_06533_row3_col3" class="data row3 col3" >80.94</td>
      <td id="T_06533_row3_col4" class="data row3 col4" >4.39</td>
    </tr>
  </tbody>
</table>



</div>
<div>

- All functions you'll ever need are implemented:
  - `np.log`
  - `np.exp`
  - `np.sqrt`
  - `np.power`
  - ...
- See [docs](https://numpy.org/doc/stable/reference/routines.math.html) for details
- Index is preserved
- Very fast, vectorized implementations


</div>
</div>

---

# Arithmetic with Series


<div class="flex gap-12">
<div>

```python
>>> df["gdp_billion"] = df["gdp_per_cap"] * df["pop"] / 1e9
>>> df
```

<style type="text/css">
#T_7413b   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_7413b thead {
  background-color: #3d3d3d;
}
#T_7413b tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_7413b tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_7413b td {
  padding: 0em;
}
#T_7413b th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_7413b caption {
  caption-side: bottom;
}
</style>
<table id="T_7413b">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7413b_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_7413b_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_7413b_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
      <th id="T_7413b_level0_col3" class="col_heading level0 col3" >pop</th>
      <th id="T_7413b_level0_col4" class="col_heading level0 col4" >gdp_billion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7413b_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_7413b_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_7413b_row0_col1" class="data row0 col1" >2002</td>
      <td id="T_7413b_row0_col2" class="data row0 col2" >6340.65</td>
      <td id="T_7413b_row0_col3" class="data row0 col3" >11226999</td>
      <td id="T_7413b_row0_col4" class="data row0 col4" >71.19</td>
    </tr>
    <tr>
      <th id="T_7413b_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_7413b_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_7413b_row1_col1" class="data row1 col1" >2007</td>
      <td id="T_7413b_row1_col2" class="data row1 col2" >8948.10</td>
      <td id="T_7413b_row1_col3" class="data row1 col3" >11416987</td>
      <td id="T_7413b_row1_col4" class="data row1 col4" >102.16</td>
    </tr>
    <tr>
      <th id="T_7413b_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_7413b_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_7413b_row2_col1" class="data row2 col1" >2002</td>
      <td id="T_7413b_row2_col2" class="data row2 col2" >24835.47</td>
      <td id="T_7413b_row2_col3" class="data row2 col3" >40152517</td>
      <td id="T_7413b_row2_col4" class="data row2 col4" >997.21</td>
    </tr>
    <tr>
      <th id="T_7413b_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_7413b_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_7413b_row3_col1" class="data row3 col1" >2007</td>
      <td id="T_7413b_row3_col2" class="data row3 col2" >28821.06</td>
      <td id="T_7413b_row3_col3" class="data row3 col3" >40448191</td>
      <td id="T_7413b_row3_col4" class="data row3 col4" >1165.76</td>
    </tr>
  </tbody>
</table>



</div>
<div>

- `*`, `+`, `-`, `/`, ... work as expected
- All calculations are aligned by index
- Not all Series have to come from the same DataFrame or be assigned to a DataFrame


</div>
</div>

---

# Recoding values



<div class="flex gap-12">
<div>

```python
>>> df["country_code"] = df["country"].replace(
...     {"Cuba": "CUB", "Spain": "ESP"}
... )
>>> df
```

<style type="text/css">
#T_c4e60   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_c4e60 thead {
  background-color: #3d3d3d;
}
#T_c4e60 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_c4e60 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_c4e60 td {
  padding: 0em;
}
#T_c4e60 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_c4e60 caption {
  caption-side: bottom;
}
</style>
<table id="T_c4e60">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c4e60_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_c4e60_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_c4e60_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_c4e60_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_c4e60_level0_col4" class="col_heading level0 col4" >country_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c4e60_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_c4e60_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_c4e60_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_c4e60_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_c4e60_row0_col3" class="data row0 col3" >77.16</td>
      <td id="T_c4e60_row0_col4" class="data row0 col4" >CUB</td>
    </tr>
    <tr>
      <th id="T_c4e60_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_c4e60_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_c4e60_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_c4e60_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_c4e60_row1_col3" class="data row1 col3" >78.27</td>
      <td id="T_c4e60_row1_col4" class="data row1 col4" >CUB</td>
    </tr>
    <tr>
      <th id="T_c4e60_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_c4e60_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_c4e60_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_c4e60_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_c4e60_row2_col3" class="data row2 col3" >79.78</td>
      <td id="T_c4e60_row2_col4" class="data row2 col4" >ESP</td>
    </tr>
    <tr>
      <th id="T_c4e60_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_c4e60_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_c4e60_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_c4e60_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_c4e60_row3_col3" class="data row3 col3" >80.94</td>
      <td id="T_c4e60_row3_col4" class="data row3 col4" >ESP</td>
    </tr>
  </tbody>
</table>


</div>
<div>

<br/>
<br/>

- Can be useful to create new variable or fix typos in string variables
- Not super fast, but faster than any looping approach

</div>
</div>


---

# Vectorized if conditions

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> helper = pd.Series(
...     "rich",
...     index=df.index,
... )

>>> df["income_status"] = helper.where(
    cond=gapm_more["gdp_per_cap"] > 10000,
    other="not rich",
)
```

<style type="text/css">
#T_d7a4a   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_d7a4a thead {
  background-color: #3d3d3d;
}
#T_d7a4a tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_d7a4a tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_d7a4a td {
  padding: 0em;
}
#T_d7a4a th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_d7a4a caption {
  caption-side: bottom;
}
</style>
<table id="T_d7a4a">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_d7a4a_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_d7a4a_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_d7a4a_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
      <th id="T_d7a4a_level0_col3" class="col_heading level0 col3" >income_status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d7a4a_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d7a4a_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_d7a4a_row0_col1" class="data row0 col1" >2002</td>
      <td id="T_d7a4a_row0_col2" class="data row0 col2" >6340.65</td>
      <td id="T_d7a4a_row0_col3" class="data row0 col3" >not rich</td>
    </tr>
    <tr>
      <th id="T_d7a4a_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_d7a4a_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_d7a4a_row1_col1" class="data row1 col1" >2007</td>
      <td id="T_d7a4a_row1_col2" class="data row1 col2" >8948.10</td>
      <td id="T_d7a4a_row1_col3" class="data row1 col3" >not rich</td>
    </tr>
    <tr>
      <th id="T_d7a4a_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_d7a4a_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_d7a4a_row2_col1" class="data row2 col1" >2002</td>
      <td id="T_d7a4a_row2_col2" class="data row2 col2" >24835.47</td>
      <td id="T_d7a4a_row2_col3" class="data row2 col3" >rich</td>
    </tr>
    <tr>
      <th id="T_d7a4a_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_d7a4a_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_d7a4a_row3_col1" class="data row3 col1" >2007</td>
      <td id="T_d7a4a_row3_col2" class="data row3 col2" >28821.06</td>
      <td id="T_d7a4a_row3_col3" class="data row3 col3" >rich</td>
    </tr>
  </tbody>
</table>



</div>
<div>

- `pd.Series.where` takes two Series as arguments:
  1. `cond`: Boolean Series determining **where** values are kept
  2. `other`: Series with **values** to be used where `cond` is `False`
- Can express general if conditions using nested where
- Vectorized and fast


</div>
</div>



---

# When is it okay to loop?

<div class="grid grid-cols-2 gap-12">
<div>

### Over columns: ✅

```python
clean = pd.DataFrame()
for var in varlist:
    clean[var] = clean_variable(df[var])
```

- Such a loop is not just ok, it is often the fastest and most readable option
- Accessing and inserting columns is fast
- Even if `clean_variable` is vectorized, it's runtime will completely dominate any loop overhead
</div>
<div>

###  Over rows: ❌

<br/>
<br/>
<br/>

- Code example intentionally left blank
- Use the vectorized functions from above instead of loops
- List comprehensions, `df.apply`, `map`, etc. are just python loops in disguise and not
faster in this case


</div>
</div>
