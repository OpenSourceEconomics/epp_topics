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

### Series and DataFrames

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is a DataFrame

<div class="grid grid-cols-2 gap-12">
<div>

```python
>>> df = pd.read_csv(path)
>>> df
```

<style type="text/css">
#T_d622d   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_d622d thead {
  background-color: #D3D3D3;
}
#T_d622d tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_d622d tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_d622d td {
  padding: 0em;
}
#T_d622d th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_d622d caption {
  caption-side: bottom;
}
</style>
<table id="T_d622d">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_d622d_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_d622d_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_d622d_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_d622d_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d622d_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_d622d_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_d622d_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_d622d_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_d622d_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_d622d_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_d622d_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_d622d_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_d622d_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_d622d_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_d622d_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_d622d_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_d622d_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_d622d_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_d622d_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
    <tr>
      <th id="T_d622d_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_d622d_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_d622d_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_d622d_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_d622d_row3_col3" class="data row3 col3" >80.94</td>
    </tr>
  </tbody>
</table>



```python
>>> df.columns
```
```txt
Index(['country', 'continent', 'year', 'life_exp'],
dtype='string')
```
```python
>>> df.index
```
```txt
RangeIndex(start=0, stop=4, step=1)
```

</div>
<div>

<br/>
<br/>
<br/>

- Tabular dataset, typically loaded from a file
- Two mental models:
  - Matrix/Array with labels
  - Dictionary of columns
- Can inspect index and column names

</div>
</div>

---

# What is a Series

<br/>

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> sr = df["country"]
>>> type(sr)
pandas.core.series.Series

>>> sr
```
```txt
0     Cuba
1     Cuba
2    Spain
3    Spain
Name: country, dtype: string
```

</div>
<div>

<br/>
<br/>

- Each columnn of a DataFrame is a Series
- Mental model: Vector with an index
- All entries in a Series have the same dtype

</div>
</div>

---

# Creating Series and DataFrames

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> df = pd.DataFrame(
...     data=[[1, "bla"], [3, "blubb"]],
...     columns=["a", "b"],
...     index=["c", "d"]
... )
>>> df
```


<style type="text/css">
#T_214be   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_214be thead {
  background-color: #D3D3D3;
}
#T_214be tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_214be tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_214be td {
  padding: 0em;
}
#T_214be th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_214be caption {
  caption-side: bottom;
}
</style>
<table id="T_214be">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_214be_level0_col0" class="col_heading level0 col0" >a</th>
      <th id="T_214be_level0_col1" class="col_heading level0 col1" >b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_214be_level0_row0" class="row_heading level0 row0" >c</th>
      <td id="T_214be_row0_col0" class="data row0 col0" >0</td>
      <td id="T_214be_row0_col1" class="data row0 col1" >bla</td>
    </tr>
    <tr>
      <th id="T_214be_level0_row1" class="row_heading level0 row1" >d</th>
      <td id="T_214be_row1_col0" class="data row1 col0" >1</td>
      <td id="T_214be_row1_col1" class="data row1 col1" >blubb</td>
    </tr>
  </tbody>
</table>


<br/>


```python
>>> sr = pd.Series([2.71, 3.14], index=["b", "a"])
>>> sr
```
```txt
b    2.71
a    3.14
dtype: float64
```

</div>
<div>

<br/>
<br/>
<br/>

- Data for a DataFrame can be nested lists or similar things
- Columns and index can be ints, strings and tuples
- **Powerful strategy**: Whenever you learn pandas or debug problems, create tiny
DataFrames and Series to gain better understanding

</div>
</div>



---

# Assignment is index aligned!

<div class="grid grid-cols-2 gap-4">
<div>

We continue using df from before

<br/>


```python
>>> sr = pd.Series([2.71, 3.14], index=["b", "a"])
>>> df["new_col"] = sr
```

<style type="text/css">
#T_d0474   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_d0474 thead {
  background-color: #D3D3D3;
}
#T_d0474 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_d0474 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_d0474 td {
  padding: 0em;
}
#T_d0474 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_d0474 caption {
  caption-side: bottom;
}
</style>
<table id="T_d0474">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_d0474_level0_col0" class="col_heading level0 col0" >a</th>
      <th id="T_d0474_level0_col1" class="col_heading level0 col1" >b</th>
      <th id="T_d0474_level0_col2" class="col_heading level0 col2" >new_col</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d0474_level0_row0" class="row_heading level0 row0" >c</th>
      <td id="T_d0474_row0_col0" class="data row0 col0" >0</td>
      <td id="T_d0474_row0_col1" class="data row0 col1" >bla</td>
      <td id="T_d0474_row0_col2" class="data row0 col2" >3.14</td>
    </tr>
    <tr>
      <th id="T_d0474_level0_row1" class="row_heading level0 row1" >d</th>
      <td id="T_d0474_row1_col0" class="data row1 col0" >1</td>
      <td id="T_d0474_row1_col1" class="data row1 col1" >blubb</td>
      <td id="T_d0474_row1_col2" class="data row1 col2" >2.71</td>
    </tr>
  </tbody>
</table>


</div>
<div>

<br/>
<br/>
<br/>

- New columns can be assigned with square brackets
- Index is automatically aligned!
  - Makes many things safer!
  - Can make pandas slow

</div>
</div>
