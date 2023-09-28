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

### Datatypes

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# The need for different datatypes

<div class="grid grid-cols-2 gap-12">
<div>

Consider the gapminder data

<style type="text/css">
#T_ae7c1   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_ae7c1 thead {
  background-color: #D3D3D3;
}
#T_ae7c1 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_ae7c1 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_ae7c1 td {
  padding: 0em;
}
#T_ae7c1 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_ae7c1 caption {
  caption-side: bottom;
}
</style>
<table id="T_ae7c1">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ae7c1_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_ae7c1_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_ae7c1_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_ae7c1_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ae7c1_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_ae7c1_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_ae7c1_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_ae7c1_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_ae7c1_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_ae7c1_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_ae7c1_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_ae7c1_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_ae7c1_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_ae7c1_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_ae7c1_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_ae7c1_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_ae7c1_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_ae7c1_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_ae7c1_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
    <tr>
      <th id="T_ae7c1_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_ae7c1_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_ae7c1_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_ae7c1_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_ae7c1_row3_col3" class="data row3 col3" >80.94</td>
    </tr>
  </tbody>
</table>

```python
>>> df.dtypes
```
```txt
country      string[pyarrow_numpy]
continent    string[pyarrow_numpy]
year                         int64
life_exp                   float64
dtype: object
```

</div>
<div>

<br/>
<br/>

- Each column has a dtype
- Enables efficient storage and fast computation
- Dtypes are not always set optimally after loading data


</div>
</div>

---

# Benefits of good type representation

- Fast calculations in a low level language
- Access to operations that are only relevant for some types
- Memory efficiency

---

# Converting to efficient dtypes

<div class="flex">
<div>

```python
>>> better_dtypes = {
...     "country": pd.CategoricalDtype(),
...     "continent": pd.CategoricalDtype(),
...     "year": pd.UInt16Dtype(),
...     "life_exp": pd.Float64Dtype(),
... }

>>> df = df.astype(better_dtypes)
>>> df.dtypes
```
```txt
country      category
continent    category
year           UInt16
life_exp      Float64
dtype: object
```

</div>
<div>

<br/>
<br/>

- Depending on how you load your data, the dtypes are not set optimally
- If so, you can create a dictionary that maps columns to the dtypes you want

</div>
</div>

---

# String vs. Categorical

- `pd.CategoricalDtype()` is for data that takes values in a fixed and relatively
small set of categories
    - Internally stored as small integers
    - Very fast relabeling or resorting of categories
- `pd.StringDtype()` is for actual text data
    - Internally stored as `pyarrow` array
    - Fast string functions similar to methods of Python strings


---



# Overview of numeric dtypes

| Type                | Properties                                             |
|---------------------|--------------------------------------------------------|
| `pd.Int8Dtype()` 	  | Byte (-128 to 127)                                     |
| `pd.Int16Dtype()` 	| Integer (-32768 to 32767)                              |
| `pd.Int32Dtype()` 	| Integer (-2147483648 to 2147483647)                    |
| `pd.Int64Dtype()` 	| Integer (-9223372036854775808 to 9223372036854775807)  |
| `pd.UInt8Dtype()` 	| Unsigned integer (0 to 255)                            |
| `pd.UInt16Dtype()` 	| Unsigned integer (0 to 65535)                          |
| `pd.UInt32Dtype()` 	| Unsigned integer (0 to 4294967295)                     |
| `pd.uint64Dtype()` 	| Unsigned integer (0 to 18446744073709551615)           |
| `pd.float64Dtype()` |	Double precision float                                 |

---

# Working with strings


<div class="flex">
<div>

```python
>>> sr = pd.Series(["Guido", "Tim", "Raymond"])

>>> sr.str.lower()
```
```txt
0      guido
1        tim
2    raymond
dtype: string
```
```python
>>> sr.str.replace("i", "iii")
```
```txt
0    Guiiido
1      Tiiim
2    Raymond
dtype: string
```

</div>
<div>

- The `.str` accessor provides access to the string methods
- Vectorized and fast implementations!
- Other examples:
  - `sr.str.len`
  - `sr.str.contains`
  - ...

- See [this tutorial](https://pandas.pydata.org/docs/user_guide/text.html) for more
string methods

</div>
</div>


---

# Working with categoricals


<div class="flex">
<div>

```python
>>> cat_type = pd.CategoricalDtype(
...     categories=["low", "middle", "high"],
...     ordered=True,
... )

>>> sr = pd.Series(
...     ["low", "high", "high"],
...     dtype=cat_type,
... )

>>> sr
0     low
1    high
2    high
dtype: category
Categories (3, string): [low < middle < high]
```

</div>
<div>

<br/>

- Categories are defined independent of data
  - Protection against invalid categories
  - Good for visualization!
- `sr.cat` accessor provides access to methods
- See [this tutorial](https://pandas.pydata.org/docs/user_guide/categorical.html)
for more methods


</div>
</div>
