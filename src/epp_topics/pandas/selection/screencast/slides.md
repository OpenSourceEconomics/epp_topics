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

### Selecting rows and columns

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Selecting columns


<div class="grid grid-cols-2 gap-12">
<div>
assume that `df` is the gapminder example

```python
>>> df["country"]
```
```txt
0     Cuba
1     Cuba
2    Spain
3    Spain
Name: country, dtype: string
```
```python
>>> df[["country", "continent"]]
```

<style type="text/css">
#T_e5626   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_e5626 thead {
  background-color: #D3D3D3;
}
#T_e5626 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_e5626 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_e5626 td {
  padding: 0em;
}
#T_e5626 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_e5626 caption {
  caption-side: bottom;
}
</style>
<table id="T_e5626">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_e5626_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_e5626_level0_col1" class="col_heading level0 col1" >continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e5626_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_e5626_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_e5626_row0_col1" class="data row0 col1" >Americas</td>
    </tr>
    <tr>
      <th id="T_e5626_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_e5626_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_e5626_row1_col1" class="data row1 col1" >Americas</td>
    </tr>
    <tr>
      <th id="T_e5626_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_e5626_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_e5626_row2_col1" class="data row2 col1" >Europe</td>
    </tr>
    <tr>
      <th id="T_e5626_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_e5626_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_e5626_row3_col1" class="data row3 col1" >Europe</td>
    </tr>
  </tbody>
</table>



</div>
<div>

<br/>
<br/>


- Column selection is with square brackets
- For multiple columns you need double brackets:
  - Outer: selecting columns
  - Inner: defining a list of variables


</div>
</div>


---

# Selecting individual rows


<div class="grid grid-cols-2 gap-12">
<div>
assume that `df` is the gapminder example

```python
>>> df.loc[1]
```
```txt
country          Cuba
continent    Americas
year             2007
life_exp       78.273
Name: 1, dtype: object
```
```python
>>> df = df.set_index(["country", "year"])
>>> df.loc["Cuba"]
```

<style type="text/css">
#T_81181   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_81181 thead {
  background-color: #D3D3D3;
}
#T_81181 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_81181 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_81181 td {
  padding: 0em;
}
#T_81181 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_81181 caption {
  caption-side: bottom;
}
</style>
<table id="T_81181">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_81181_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_81181_level0_col1" class="col_heading level0 col1" >life_exp</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_81181_level0_row0" class="row_heading level0 row0" >2002</th>
      <td id="T_81181_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_81181_row0_col1" class="data row0 col1" >77.16</td>
    </tr>
    <tr>
      <th id="T_81181_level0_row1" class="row_heading level0 row1" >2007</th>
      <td id="T_81181_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_81181_row1_col1" class="data row1 col1" >78.27</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> df.loc[("Cuba", 2002)]
```
```txt
continent    Americas
life_exp       77.158
Name: (Cuba, 2002), dtype: object
```

<br/>

- Selection of rows needs `.loc[]`
- Selection is label based!
- For a MultiIndex you can specify some or all levels

</div>
</div>

---

# Selecting rows and columns


<div class="grid grid-cols-2 gap-4">
<div>
assume that `df` is the gapminder example

```python
>>> df.loc[1, "country"]
'Cuba'

>>> df.loc[[1, 3], ["country", "year"]]
```

<style type="text/css">
#T_697dc   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_697dc thead {
  background-color: #D3D3D3;
}
#T_697dc tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_697dc tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_697dc td {
  padding: 0em;
}
#T_697dc th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_697dc caption {
  caption-side: bottom;
}
</style>
<table id="T_697dc">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_697dc_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_697dc_level0_col1" class="col_heading level0 col1" >year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_697dc_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_697dc_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_697dc_row0_col1" class="data row0 col1" >2007</td>
    </tr>
    <tr>
      <th id="T_697dc_level0_row1" class="row_heading level0 row1" >3</th>
      <td id="T_697dc_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_697dc_row1_col1" class="data row1 col1" >2007</td>
    </tr>
  </tbody>
</table>



</div>
<div>

<br/>

- Use `.loc[rows, columns]` to select rows and columns
- Can use everything you have seen before

</div>
</div>

---

# Selecting rows based on boolean Series

<div class="grid grid-cols-2 gap-4">
<div>
assume that `df` is the gapminder example

```python
df["year"] >= 2005
```
```txt
0    False
1     True
2    False
3     True
Name: year, dtype: bool
```
```python
>>> df[df["year"] >= 2005]
```

<style type="text/css">
#T_f3dd2   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_f3dd2 thead {
  background-color: #D3D3D3;
}
#T_f3dd2 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_f3dd2 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_f3dd2 td {
  padding: 0em;
}
#T_f3dd2 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_f3dd2 caption {
  caption-side: bottom;
}
</style>
<table id="T_f3dd2">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_f3dd2_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_f3dd2_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_f3dd2_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_f3dd2_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f3dd2_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_f3dd2_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_f3dd2_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_f3dd2_row0_col2" class="data row0 col2" >2007</td>
      <td id="T_f3dd2_row0_col3" class="data row0 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_f3dd2_level0_row1" class="row_heading level0 row1" >3</th>
      <td id="T_f3dd2_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_f3dd2_row1_col1" class="data row1 col1" >Europe</td>
      <td id="T_f3dd2_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_f3dd2_row1_col3" class="data row1 col3" >80.94</td>
    </tr>
  </tbody>
</table>


</div>
<div>

<br/>
<br/>

- Comparisons of Series produce Boolean Series!
- Complex conditions with `|` and `&`
- Boolean Series can be used for selecting rows
- Works also inside `.loc`


</div>
</div>

---

# Selecting rows with queries

<div class="flex gap-12">
<div>
assume that `df` is the gapminder example

```python
>>>df.query("year >= 2005")
```

<style type="text/css">
#T_b43ab   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_b43ab thead {
  background-color: #D3D3D3;
}
#T_b43ab tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_b43ab tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_b43ab td {
  padding: 0em;
}
#T_b43ab th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_b43ab caption {
  caption-side: bottom;
}
</style>
<table id="T_b43ab">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_b43ab_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_b43ab_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_b43ab_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_b43ab_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_b43ab_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_b43ab_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_b43ab_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_b43ab_row0_col2" class="data row0 col2" >2007</td>
      <td id="T_b43ab_row0_col3" class="data row0 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_b43ab_level0_row1" class="row_heading level0 row1" >3</th>
      <td id="T_b43ab_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_b43ab_row1_col1" class="data row1 col1" >Europe</td>
      <td id="T_b43ab_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_b43ab_row1_col3" class="data row1 col3" >80.94</td>
    </tr>
  </tbody>
</table>

<br/>


```python
>>> df.query("year >= 2005 & continent == 'Europe'")
```

<style type="text/css">
#T_6b8dc   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_6b8dc thead {
  background-color: #D3D3D3;
}
#T_6b8dc tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_6b8dc tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_6b8dc td {
  padding: 0em;
}
#T_6b8dc th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_6b8dc caption {
  caption-side: bottom;
}
</style>
<table id="T_6b8dc">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6b8dc_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_6b8dc_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_6b8dc_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_6b8dc_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6b8dc_level0_row0" class="row_heading level0 row0" >3</th>
      <td id="T_6b8dc_row0_col0" class="data row0 col0" >Spain</td>
      <td id="T_6b8dc_row0_col1" class="data row0 col1" >Europe</td>
      <td id="T_6b8dc_row0_col2" class="data row0 col2" >2007</td>
      <td id="T_6b8dc_row0_col3" class="data row0 col3" >80.94</td>
    </tr>
  </tbody>
</table>


</div>
<div>

- `.query` selects rows based on strings with conditions
- Use single quotes (`'`) for string value inside the query
- More readable than selection via boolean Series

</div>
</div>
