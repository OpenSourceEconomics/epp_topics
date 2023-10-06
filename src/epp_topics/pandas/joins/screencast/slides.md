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

### Joining datasets

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- Often when you download data, it comes in several files
- While you might not like it, this is often because the data providers respected
the normal forms!
- In this screencast we show you how to merge or concatenate DataFrames


---

# Concatenating DataFrames vertically


<div class="flex gap-12">
<div>

```python
>>> top
```

<style type="text/css">
#T_ab9b2   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_ab9b2 thead {
  background-color: #3d3d3d;
}
#T_ab9b2 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_ab9b2 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_ab9b2 td {
  padding: 0em;
}
#T_ab9b2 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_ab9b2 caption {
  caption-side: bottom;
}
</style>
<table id="T_ab9b2">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ab9b2_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_ab9b2_level0_col1" class="col_heading level0 col1" >life_exp</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ab9b2_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_ab9b2_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_ab9b2_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_ab9b2_row0_col1" class="data row0 col1" >77.16</td>
    </tr>
    <tr>
      <th id="T_ab9b2_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_ab9b2_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_ab9b2_row1_col1" class="data row1 col1" >78.27</td>
    </tr>
  </tbody>
</table>



```python
>>> bottom
```

<style type="text/css">
#T_849c2   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_849c2 thead {
  background-color: #3d3d3d;
}
#T_849c2 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_849c2 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_849c2 td {
  padding: 0em;
}
#T_849c2 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_849c2 caption {
  caption-side: bottom;
}
</style>
<table id="T_849c2">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_849c2_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_849c2_level0_col1" class="col_heading level0 col1" >life_exp</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_849c2_level0_row0" class="row_heading level0 row0" rowspan="2">Spain</th>
      <th id="T_849c2_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_849c2_row0_col0" class="data row0 col0" >Europe</td>
      <td id="T_849c2_row0_col1" class="data row0 col1" >79.78</td>
    </tr>
    <tr>
      <th id="T_849c2_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_849c2_row1_col0" class="data row1 col0" >Europe</td>
      <td id="T_849c2_row1_col1" class="data row1 col1" >80.94</td>
    </tr>
  </tbody>
</table>



</div>
<div>

```python
>>> pd.concat([top, bottom])
```

<style type="text/css">
#T_65011   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_65011 thead {
  background-color: #3d3d3d;
}
#T_65011 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_65011 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_65011 td {
  padding: 0em;
}
#T_65011 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_65011 caption {
  caption-side: bottom;
}
</style>
<table id="T_65011">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_65011_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_65011_level0_col1" class="col_heading level0 col1" >life_exp</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_65011_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_65011_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_65011_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_65011_row0_col1" class="data row0 col1" >77.16</td>
    </tr>
    <tr>
      <th id="T_65011_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_65011_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_65011_row1_col1" class="data row1 col1" >78.27</td>
    </tr>
    <tr>
      <th id="T_65011_level0_row2" class="row_heading level0 row2" rowspan="2">Spain</th>
      <th id="T_65011_level1_row2" class="row_heading level1 row2" >2002</th>
      <td id="T_65011_row2_col0" class="data row2 col0" >Europe</td>
      <td id="T_65011_row2_col1" class="data row2 col1" >79.78</td>
    </tr>
    <tr>
      <th id="T_65011_level1_row3" class="row_heading level1 row3" >2007</th>
      <td id="T_65011_row3_col0" class="data row3 col0" >Europe</td>
      <td id="T_65011_row3_col1" class="data row3 col1" >80.94</td>
    </tr>
  </tbody>
</table>

<br/>

- concat stacks DataFrames on top of each other
- aligned by columns
- index needs to be compatible
- list can have more than two elements



</div>
</div>


---

# Concatenating DataFrames horizontally

<div class="flex gap-12">
<div>

```python
>>> left
```

<style type="text/css">
#T_50eaf   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_50eaf thead {
  background-color: #3d3d3d;
}
#T_50eaf tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_50eaf tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_50eaf td {
  padding: 0em;
}
#T_50eaf th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_50eaf caption {
  caption-side: bottom;
}
</style>
<table id="T_50eaf">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_50eaf_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_50eaf_level0_col1" class="col_heading level0 col1" >life_exp</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_50eaf_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_50eaf_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_50eaf_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_50eaf_row0_col1" class="data row0 col1" >77.16</td>
    </tr>
    <tr>
      <th id="T_50eaf_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_50eaf_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_50eaf_row1_col1" class="data row1 col1" >78.27</td>
    </tr>
    <tr>
      <th id="T_50eaf_level0_row2" class="row_heading level0 row2" rowspan="2">Spain</th>
      <th id="T_50eaf_level1_row2" class="row_heading level1 row2" >2002</th>
      <td id="T_50eaf_row2_col0" class="data row2 col0" >Europe</td>
      <td id="T_50eaf_row2_col1" class="data row2 col1" >79.78</td>
    </tr>
    <tr>
      <th id="T_50eaf_level1_row3" class="row_heading level1 row3" >2007</th>
      <td id="T_50eaf_row3_col0" class="data row3 col0" >Europe</td>
      <td id="T_50eaf_row3_col1" class="data row3 col1" >80.94</td>
    </tr>
  </tbody>
</table>

```python
>>> right
```

<style type="text/css">
#T_a05f6   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_a05f6 thead {
  background-color: #3d3d3d;
}
#T_a05f6 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_a05f6 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_a05f6 td {
  padding: 0em;
}
#T_a05f6 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_a05f6 caption {
  caption-side: bottom;
}
</style>
<table id="T_a05f6">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a05f6_level0_col0" class="col_heading level0 col0" >gdp_per_cap</th>
      <th id="T_a05f6_level0_col1" class="col_heading level0 col1" >pop</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a05f6_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_a05f6_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_a05f6_row0_col0" class="data row0 col0" >6340.65</td>
      <td id="T_a05f6_row0_col1" class="data row0 col1" >11226999</td>
    </tr>
    <tr>
      <th id="T_a05f6_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_a05f6_row1_col0" class="data row1 col0" >8948.10</td>
      <td id="T_a05f6_row1_col1" class="data row1 col1" >11416987</td>
    </tr>
    <tr>
      <th id="T_a05f6_level0_row2" class="row_heading level0 row2" rowspan="2">Spain</th>
      <th id="T_a05f6_level1_row2" class="row_heading level1 row2" >2002</th>
      <td id="T_a05f6_row2_col0" class="data row2 col0" >24835.47</td>
      <td id="T_a05f6_row2_col1" class="data row2 col1" >40152517</td>
    </tr>
    <tr>
      <th id="T_a05f6_level1_row3" class="row_heading level1 row3" >2007</th>
      <td id="T_a05f6_row3_col0" class="data row3 col0" >28821.06</td>
      <td id="T_a05f6_row3_col1" class="data row3 col1" >40448191</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> pd.concat([left, right], axis="columns")
```

<style type="text/css">
#T_fe317   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_fe317 thead {
  background-color: #3d3d3d;
}
#T_fe317 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_fe317 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_fe317 td {
  padding: 0em;
}
#T_fe317 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_fe317 caption {
  caption-side: bottom;
}
</style>
<table id="T_fe317">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_fe317_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_fe317_level0_col1" class="col_heading level0 col1" >life_exp</th>
      <th id="T_fe317_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
      <th id="T_fe317_level0_col3" class="col_heading level0 col3" >pop</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="index_name level1" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_fe317_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_fe317_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_fe317_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_fe317_row0_col1" class="data row0 col1" >77.16</td>
      <td id="T_fe317_row0_col2" class="data row0 col2" >6340.65</td>
      <td id="T_fe317_row0_col3" class="data row0 col3" >11226999</td>
    </tr>
    <tr>
      <th id="T_fe317_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_fe317_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_fe317_row1_col1" class="data row1 col1" >78.27</td>
      <td id="T_fe317_row1_col2" class="data row1 col2" >8948.10</td>
      <td id="T_fe317_row1_col3" class="data row1 col3" >11416987</td>
    </tr>
    <tr>
      <th id="T_fe317_level0_row2" class="row_heading level0 row2" rowspan="2">Spain</th>
      <th id="T_fe317_level1_row2" class="row_heading level1 row2" >2002</th>
      <td id="T_fe317_row2_col0" class="data row2 col0" >Europe</td>
      <td id="T_fe317_row2_col1" class="data row2 col1" >79.78</td>
      <td id="T_fe317_row2_col2" class="data row2 col2" >24835.47</td>
      <td id="T_fe317_row2_col3" class="data row2 col3" >40152517</td>
    </tr>
    <tr>
      <th id="T_fe317_level1_row3" class="row_heading level1 row3" >2007</th>
      <td id="T_fe317_row3_col0" class="data row3 col0" >Europe</td>
      <td id="T_fe317_row3_col1" class="data row3 col1" >80.94</td>
      <td id="T_fe317_row3_col2" class="data row3 col2" >28821.06</td>
      <td id="T_fe317_row3_col3" class="data row3 col3" >40448191</td>
    </tr>
  </tbody>
</table>

<br/>
<br/>

- with `axis="columns"`, DataFrames are stacked horizontally
- Used to be `axis=1`

</div>
</div>

---

# 1:1 merges


<div class="flex gap-12">
<div>

```python
>>> left
```

<style type="text/css">
#T_13a7a   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_13a7a thead {
  background-color: #3d3d3d;
}
#T_13a7a tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_13a7a tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_13a7a td {
  padding: 0em;
}
#T_13a7a th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_13a7a caption {
  caption-side: bottom;
}
</style>
<table id="T_13a7a">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_13a7a_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_13a7a_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_13a7a_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_13a7a_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_13a7a_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_13a7a_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_13a7a_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_13a7a_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_13a7a_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_13a7a_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_13a7a_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_13a7a_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_13a7a_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_13a7a_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_13a7a_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_13a7a_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_13a7a_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_13a7a_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_13a7a_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
  </tbody>
</table>


```python
>>> right
```

<style type="text/css">
#T_c3897   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_c3897 thead {
  background-color: #3d3d3d;
}
#T_c3897 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_c3897 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_c3897 td {
  padding: 0em;
}
#T_c3897 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_c3897 caption {
  caption-side: bottom;
}
</style>
<table id="T_c3897">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c3897_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_c3897_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_c3897_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
      <th id="T_c3897_level0_col3" class="col_heading level0 col3" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c3897_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_c3897_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_c3897_row0_col1" class="data row0 col1" >2007</td>
      <td id="T_c3897_row0_col2" class="data row0 col2" >8948.10</td>
      <td id="T_c3897_row0_col3" class="data row0 col3" >11416987</td>
    </tr>
    <tr>
      <th id="T_c3897_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_c3897_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_c3897_row1_col1" class="data row1 col1" >2002</td>
      <td id="T_c3897_row1_col2" class="data row1 col2" >24835.47</td>
      <td id="T_c3897_row1_col3" class="data row1 col3" >40152517</td>
    </tr>
    <tr>
      <th id="T_c3897_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_c3897_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_c3897_row2_col1" class="data row2 col1" >2007</td>
      <td id="T_c3897_row2_col2" class="data row2 col2" >28821.06</td>
      <td id="T_c3897_row2_col3" class="data row2 col3" >40448191</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> pd.merge(left, right, on=["country", "year"])
```

<style type="text/css">
#T_a9953   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_a9953 thead {
  background-color: #3d3d3d;
}
#T_a9953 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_a9953 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_a9953 td {
  padding: 0em;
}
#T_a9953 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_a9953 caption {
  caption-side: bottom;
}
</style>
<table id="T_a9953">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a9953_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_a9953_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_a9953_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_a9953_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_a9953_level0_col4" class="col_heading level0 col4" >gdp_per_cap</th>
      <th id="T_a9953_level0_col5" class="col_heading level0 col5" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a9953_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_a9953_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_a9953_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_a9953_row0_col2" class="data row0 col2" >2007</td>
      <td id="T_a9953_row0_col3" class="data row0 col3" >78.27</td>
      <td id="T_a9953_row0_col4" class="data row0 col4" >8948.10</td>
      <td id="T_a9953_row0_col5" class="data row0 col5" >11416987</td>
    </tr>
    <tr>
      <th id="T_a9953_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_a9953_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_a9953_row1_col1" class="data row1 col1" >Europe</td>
      <td id="T_a9953_row1_col2" class="data row1 col2" >2002</td>
      <td id="T_a9953_row1_col3" class="data row1 col3" >79.78</td>
      <td id="T_a9953_row1_col4" class="data row1 col4" >24835.47</td>
      <td id="T_a9953_row1_col5" class="data row1 col5" >40152517</td>
    </tr>
  </tbody>
</table>

<br/>

- merge does not align on index but on one or several merge keys
- by default, it does an inner join
- Important: using concat would have been catastrophic in this case!


</div>
</div>


---

<div class="flex gap-12">
<div>

```python
>>> pd.merge(left, right, on=["country", "year"], how="inner")
```

<style type="text/css">
#T_a9953   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_a9953 thead {
  background-color: #3d3d3d;
}
#T_a9953 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_a9953 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_a9953 td {
  padding: 0em;
}
#T_a9953 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_a9953 caption {
  caption-side: bottom;
}
</style>
<table id="T_a9953">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a9953_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_a9953_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_a9953_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_a9953_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_a9953_level0_col4" class="col_heading level0 col4" >gdp_per_cap</th>
      <th id="T_a9953_level0_col5" class="col_heading level0 col5" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a9953_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_a9953_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_a9953_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_a9953_row0_col2" class="data row0 col2" >2007</td>
      <td id="T_a9953_row0_col3" class="data row0 col3" >78.27</td>
      <td id="T_a9953_row0_col4" class="data row0 col4" >8948.10</td>
      <td id="T_a9953_row0_col5" class="data row0 col5" >11416987</td>
    </tr>
    <tr>
      <th id="T_a9953_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_a9953_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_a9953_row1_col1" class="data row1 col1" >Europe</td>
      <td id="T_a9953_row1_col2" class="data row1 col2" >2002</td>
      <td id="T_a9953_row1_col3" class="data row1 col3" >79.78</td>
      <td id="T_a9953_row1_col4" class="data row1 col4" >24835.47</td>
      <td id="T_a9953_row1_col5" class="data row1 col5" >40152517</td>
    </tr>
  </tbody>
</table>

```python
>>> pd.merge(left, right, on=["country", "year"], how="left")
```


<style type="text/css">
#T_d7261   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_d7261 thead {
  background-color: #3d3d3d;
}
#T_d7261 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_d7261 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_d7261 td {
  padding: 0em;
}
#T_d7261 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_d7261 caption {
  caption-side: bottom;
}
</style>
<table id="T_d7261">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_d7261_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_d7261_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_d7261_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_d7261_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_d7261_level0_col4" class="col_heading level0 col4" >gdp_per_cap</th>
      <th id="T_d7261_level0_col5" class="col_heading level0 col5" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d7261_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d7261_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_d7261_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_d7261_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_d7261_row0_col3" class="data row0 col3" >77.16</td>
      <td id="T_d7261_row0_col4" class="data row0 col4" >nan</td>
      <td id="T_d7261_row0_col5" class="data row0 col5" >nan</td>
    </tr>
    <tr>
      <th id="T_d7261_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_d7261_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_d7261_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_d7261_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_d7261_row1_col3" class="data row1 col3" >78.27</td>
      <td id="T_d7261_row1_col4" class="data row1 col4" >8948.10</td>
      <td id="T_d7261_row1_col5" class="data row1 col5" >11416987.00</td>
    </tr>
    <tr>
      <th id="T_d7261_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_d7261_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_d7261_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_d7261_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_d7261_row2_col3" class="data row2 col3" >79.78</td>
      <td id="T_d7261_row2_col4" class="data row2 col4" >24835.47</td>
      <td id="T_d7261_row2_col5" class="data row2 col5" >40152517.00</td>
    </tr>
  </tbody>
</table>


```python
>>> pd.merge(left, right, on=["country", "year"], how="outer")
```

<style type="text/css">
#T_63e94   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_63e94 thead {
  background-color: #3d3d3d;
}
#T_63e94 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_63e94 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_63e94 td {
  padding: 0em;
}
#T_63e94 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_63e94 caption {
  caption-side: bottom;
}
</style>
<table id="T_63e94">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_63e94_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_63e94_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_63e94_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_63e94_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_63e94_level0_col4" class="col_heading level0 col4" >gdp_per_cap</th>
      <th id="T_63e94_level0_col5" class="col_heading level0 col5" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_63e94_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_63e94_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_63e94_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_63e94_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_63e94_row0_col3" class="data row0 col3" >77.16</td>
      <td id="T_63e94_row0_col4" class="data row0 col4" >nan</td>
      <td id="T_63e94_row0_col5" class="data row0 col5" >nan</td>
    </tr>
    <tr>
      <th id="T_63e94_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_63e94_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_63e94_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_63e94_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_63e94_row1_col3" class="data row1 col3" >78.27</td>
      <td id="T_63e94_row1_col4" class="data row1 col4" >8948.10</td>
      <td id="T_63e94_row1_col5" class="data row1 col5" >11416987.00</td>
    </tr>
    <tr>
      <th id="T_63e94_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_63e94_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_63e94_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_63e94_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_63e94_row2_col3" class="data row2 col3" >79.78</td>
      <td id="T_63e94_row2_col4" class="data row2 col4" >24835.47</td>
      <td id="T_63e94_row2_col5" class="data row2 col5" >40152517.00</td>
    </tr>
    <tr>
      <th id="T_63e94_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_63e94_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_63e94_row3_col1" class="data row3 col1" >nan</td>
      <td id="T_63e94_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_63e94_row3_col3" class="data row3 col3" >nan</td>
      <td id="T_63e94_row3_col4" class="data row3 col4" >28821.06</td>
      <td id="T_63e94_row3_col5" class="data row3 col5" >40448191.00</td>
    </tr>
  </tbody>
</table>



</div>
<div>

<br/>
<br/>
<br/>

- The `how` argument determines which rows are kept
- The default `"inner"` is not always a good choice

</div>
</div>


---

# 1:m merges

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> left
```

<style type="text/css">
#T_2b141   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_2b141 thead {
  background-color: #3d3d3d;
}
#T_2b141 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_2b141 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_2b141 td {
  padding: 0em;
}
#T_2b141 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_2b141 caption {
  caption-side: bottom;
}
</style>
<table id="T_2b141">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_2b141_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_2b141_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_2b141_level0_col2" class="col_heading level0 col2" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2b141_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_2b141_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_2b141_row0_col1" class="data row0 col1" >2002</td>
      <td id="T_2b141_row0_col2" class="data row0 col2" >77.16</td>
    </tr>
    <tr>
      <th id="T_2b141_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_2b141_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_2b141_row1_col1" class="data row1 col1" >2007</td>
      <td id="T_2b141_row1_col2" class="data row1 col2" >78.27</td>
    </tr>
    <tr>
      <th id="T_2b141_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_2b141_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_2b141_row2_col1" class="data row2 col1" >2002</td>
      <td id="T_2b141_row2_col2" class="data row2 col2" >79.78</td>
    </tr>
    <tr>
      <th id="T_2b141_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_2b141_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_2b141_row3_col1" class="data row3 col1" >2007</td>
      <td id="T_2b141_row3_col2" class="data row3 col2" >80.94</td>
    </tr>
  </tbody>
</table>

```python
>>> right
```

<style type="text/css">
#T_88577   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_88577 thead {
  background-color: #3d3d3d;
}
#T_88577 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_88577 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_88577 td {
  padding: 0em;
}
#T_88577 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_88577 caption {
  caption-side: bottom;
}
</style>
<table id="T_88577">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_88577_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_88577_level0_col1" class="col_heading level0 col1" >capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_88577_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_88577_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_88577_row0_col1" class="data row0 col1" >Havana</td>
    </tr>
    <tr>
      <th id="T_88577_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_88577_row1_col0" class="data row1 col0" >Spain</td>
      <td id="T_88577_row1_col1" class="data row1 col1" >Madrid</td>
    </tr>
  </tbody>
</table>



</div>
<div>

```python
>>> pd.merge(left, right, on="country")
```

<style type="text/css">
#T_96b28   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_96b28 thead {
  background-color: #3d3d3d;
}
#T_96b28 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_96b28 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_96b28 td {
  padding: 0em;
}
#T_96b28 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_96b28 caption {
  caption-side: bottom;
}
</style>
<table id="T_96b28">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_96b28_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_96b28_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_96b28_level0_col2" class="col_heading level0 col2" >life_exp</th>
      <th id="T_96b28_level0_col3" class="col_heading level0 col3" >capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_96b28_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_96b28_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_96b28_row0_col1" class="data row0 col1" >2002</td>
      <td id="T_96b28_row0_col2" class="data row0 col2" >77.16</td>
      <td id="T_96b28_row0_col3" class="data row0 col3" >Havana</td>
    </tr>
    <tr>
      <th id="T_96b28_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_96b28_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_96b28_row1_col1" class="data row1 col1" >2007</td>
      <td id="T_96b28_row1_col2" class="data row1 col2" >78.27</td>
      <td id="T_96b28_row1_col3" class="data row1 col3" >Havana</td>
    </tr>
    <tr>
      <th id="T_96b28_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_96b28_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_96b28_row2_col1" class="data row2 col1" >2002</td>
      <td id="T_96b28_row2_col2" class="data row2 col2" >79.78</td>
      <td id="T_96b28_row2_col3" class="data row2 col3" >Madrid</td>
    </tr>
    <tr>
      <th id="T_96b28_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_96b28_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_96b28_row3_col1" class="data row3 col1" >2007</td>
      <td id="T_96b28_row3_col2" class="data row3 col2" >80.94</td>
      <td id="T_96b28_row3_col3" class="data row3 col3" >Madrid</td>
    </tr>
  </tbody>
</table>

<br/>

- The type of merge is determined by the data, not by calling a different function
- 1:m means that one entry in `right` is matched to many items in `left`


</div>
</div>


---

# Other merges

- There are also "m:1" and "m:m" merges
- Check the pandas [tutorial](https://pandas.pydata.org/docs/user_guide/merging.html)
for details


---

# Concat vs. merge

- Use `concat` if you can
  - 1:1 joins
  - Index and columns are set properly
- Use `merge` if you need more control


---

# Check your data before and after

- Many people are afraid of merging
- This is because merges often go wrong
- Reason: badly prepared data
  - Want to do a 1:1 merge but merge key contains duplicates
  - Merge keys are not properly cleaned
  - ...
- Check your data before merging to avoid problems
- Check that you get the expected number of observations after merging
