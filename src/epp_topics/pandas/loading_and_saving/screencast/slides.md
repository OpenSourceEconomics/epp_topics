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

### Loading and saving data

<br>


Janoś Gabler and Hans-Martin von Gaudecker






---

# Example: Loading a csv file

<div class="grid grid-cols-2 gap-12">
<div>


```python
>>> df = pd.read_csv(
...     "gapminder.csv",
...     engine="pyarrow",
... )

>>> df
```

<style type="text/css">
#T_bb5b5   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
}
#T_bb5b5 thead {
  background-color: #D3D3D3;
}
#T_bb5b5 tbody tr:nth-child(even) {
  background-color: #f1f1f1;
}
#T_bb5b5 tbody tr:nth-child(odd) {
  background-color: #fff;
}
#T_bb5b5 td {
  padding: 0em;
}
#T_bb5b5 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_bb5b5 caption {
  caption-side: bottom;
}
</style>
<table id="T_bb5b5">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_bb5b5_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_bb5b5_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_bb5b5_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_bb5b5_level0_col3" class="col_heading level0 col3" >life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_bb5b5_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_bb5b5_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_bb5b5_row0_col1" class="data row0 col1" >Americas</td>
      <td id="T_bb5b5_row0_col2" class="data row0 col2" >2002</td>
      <td id="T_bb5b5_row0_col3" class="data row0 col3" >77.16</td>
    </tr>
    <tr>
      <th id="T_bb5b5_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_bb5b5_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_bb5b5_row1_col1" class="data row1 col1" >Americas</td>
      <td id="T_bb5b5_row1_col2" class="data row1 col2" >2007</td>
      <td id="T_bb5b5_row1_col3" class="data row1 col3" >78.27</td>
    </tr>
    <tr>
      <th id="T_bb5b5_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_bb5b5_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_bb5b5_row2_col1" class="data row2 col1" >Europe</td>
      <td id="T_bb5b5_row2_col2" class="data row2 col2" >2002</td>
      <td id="T_bb5b5_row2_col3" class="data row2 col3" >79.78</td>
    </tr>
    <tr>
      <th id="T_bb5b5_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_bb5b5_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_bb5b5_row3_col1" class="data row3 col1" >Europe</td>
      <td id="T_bb5b5_row3_col2" class="data row3 col2" >2007</td>
      <td id="T_bb5b5_row3_col3" class="data row3 col3" >80.94</td>
    </tr>
  </tbody>
</table>



</div>
<div>

`gapminder.csv` looks like this

```txt
country,continent,year,life_exp
Cuba,Americas,2002,77.158
Cuba,Americas,2007,78.273
Spain,Europe,2002,79.780
Spain,Europe,2007,80.941
```

<br/>

- first argument is path
- `engine="pyarrow"` ensures we are getting modern pandas dtypes
- Many other optional arguments

</div>
</div>



---

# Other read functions

| reader           | extension  | comment                                               |
| -----------------|------------|-------------------------------------------------------|
| `pd.read_csv`    | `.csv`     | Often need to use optional arguments to make it work  |
| `pd.read_pickle` | `.pkl`     | Good for intermediate files; Python specific          |
| `pd.read_stata`  | `.dta`     | Statas proprietary format. Avoid if you can           |
| `pd.read_parquet`| `.parquet` | Very modern and powerful file format                  |
| `pd.read_fwf`    | `.fwf`     | Avoid this whenever you can!                          |

Each read function has a corresponding write function

---

# Example: Write a parquet file

<div class="grid grid-cols-2 gap-4">
<div>

```python
df.to_parquet(
    "gapminder.parquet",
    index=False,
)
```

</div>
<div>

- First argument is a file path
- `index=False` means that the index will be discarded


</div>
</div>


---

# File format recommendations

- Use `.pkl` format for processed datasets that you do not share with others
  - Very fast to read and write
  - Preserves every aspect of your DataFrame (e.g. dtypes)
- Use `.parquet` to save files you want to share with others
  - Can be read by many languages and programs
  - Efficient compression
