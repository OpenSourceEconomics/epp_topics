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

### Setting and renaming columns and indices

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Why the Index is important

<div class="grid grid-cols-2 gap-4">
<div>

The dataframe from before

<style type="text/css">
#T_70f15   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_70f15 thead {
  background-color: #D3D3D3;
}
#T_70f15 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_70f15 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_70f15 td {
  padding: 0em;
}
#T_70f15 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_70f15 caption {
  caption-side: bottom;
}
</style>
<table id="T_70f15">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_70f15_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_70f15_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_70f15_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_70f15_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_70f15_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_70f15_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_70f15_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_70f15_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_70f15_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_70f15_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_70f15_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_70f15_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_70f15_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_70f15_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_70f15_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_70f15_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_70f15_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_70f15_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_70f15_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
    <tr>
      <th id="T_70f15_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_70f15_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_70f15_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_70f15_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_70f15_row3_col3" class="data row3 col3" >80.94</td>
    </tr>
  </tbody>
</table>

Same dataset, different Index

<style type="text/css">
#T_9729f   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_9729f thead {
  background-color: #D3D3D3;
}
#T_9729f tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_9729f tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_9729f td {
  padding: 0em;
}
#T_9729f th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_9729f caption {
  caption-side: bottom;
}
</style>
<table id="T_9729f">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9729f_level0_col0" class="col_heading level0 col0" >continent</th>
      <th id="T_9729f_level0_col1" class="col_heading level0 col1" >life_exp</th>
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
      <th id="T_9729f_level0_row0" class="row_heading level0 row0" rowspan="2">Cuba</th>
      <th id="T_9729f_level1_row0" class="row_heading level1 row0" >2002</th>
      <td id="T_9729f_row0_col0" class="data row0 col0" >Americas</td>
      <td id="T_9729f_row0_col1" class="data row0 col1" >77.16</td>
    </tr>
    <tr>
      <th id="T_9729f_level1_row1" class="row_heading level1 row1" >2007</th>
      <td id="T_9729f_row1_col0" class="data row1 col0" >Americas</td>
      <td id="T_9729f_row1_col1" class="data row1 col1" >78.27</td>
    </tr>
    <tr>
      <th id="T_9729f_level0_row2" class="row_heading level0 row2" rowspan="2">Spain</th>
      <th id="T_9729f_level1_row2" class="row_heading level1 row2" >2002</th>
      <td id="T_9729f_row2_col0" class="data row2 col0" >Europe</td>
      <td id="T_9729f_row2_col1" class="data row2 col1" >79.78</td>
    </tr>
    <tr>
      <th id="T_9729f_level1_row3" class="row_heading level1 row3" >2007</th>
      <td id="T_9729f_row3_col0" class="data row3 col0" >Europe</td>
      <td id="T_9729f_row3_col1" class="data row3 col1" >80.94</td>
    </tr>
  </tbody>
</table>



</div>
<div>

<br/>
<br/>

- We have seen that pandas aligns new columns in a DataFrame by index
- Many other operations are aligned by index
- Using a meaningful index makes this even safer
- Index should be unique and not contain floats


</div>
</div>

---

# Setting and resetting the index


<div class="grid grid-cols-2 gap-4">
<div>

assume `df` is our gapminder example

```python
>>> df.index
RangeIndex(start=0, stop=4, step=1)

>>> df = df.set_index(["country", "year"])
>>> df.index
```
```txt
MultiIndex([( 'Cuba', 2002),
            ( 'Cuba', 2007),
            ('Spain', 2002),
            ('Spain', 2007)],
           names=['country', 'year'])
```
```python
>>> df = df.reset_index()
>>> df.index
RangeIndex(start=0, stop=4, step=1)
```


</div>
<div>

<br/>
<br/>

- `set_index` and `reset_index` are inverse functions
- `set_index` can take any column or list of columns
- Optional argument `drop=True` or `drop=False` determines what happens with the old index in `set_index`

</div>
</div>

---

# Renaming columns

<div class="flex gap-8">
<div>

assume `df` is our gapminder example

```python
>>> df.columns
```
```txt
Index(['country', 'continent', 'year',
 'life_exp'], dtype='string')
```

```python
>>> new_names = {
...     "life_exp": "life expectancy",
...     "country": "country name",
...     "continent": "continent name",
... }

>>> df = df.rename(columns=new_names)
>>> df.columns
```
```txt
Index(['country name', 'continent name',
 'year', 'life expectancy'], dtype='string')
```


</div>
<div>

<br/>
<br/>


- Dict can contain only the subset of variables that is actually renamed
- Renaming the index works the same way but is rarely needed
- Instead of a dict, you can provide a function that converts the old name to the new name!


</div>
</div>
