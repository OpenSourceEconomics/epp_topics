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

### Inspecting and summarizing data

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- So far we have looked at tiny DataFrames
- Real datasets don't fit on a screen
- Need quick ways to:
  - Look at subsets
  - Calculate summary statistics
  - Plot distributions

---

# Example



<style type="text/css">
#T_6f488   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_6f488 thead {
  background-color: #3d3d3d;
}
#T_6f488 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_6f488 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_6f488 td {
  padding: 0em;
}
#T_6f488 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_6f488 caption {
  caption-side: bottom;
}
</style>
<table id="T_6f488">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_6f488_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_6f488_level0_col1" class="col_heading level0 col1" >continent</th>
      <th id="T_6f488_level0_col2" class="col_heading level0 col2" >year</th>
      <th id="T_6f488_level0_col3" class="col_heading level0 col3" >life_exp</th>
      <th id="T_6f488_level0_col4" class="col_heading level0 col4" >pop</th>
      <th id="T_6f488_level0_col5" class="col_heading level0 col5" >gdp_per_cap</th>
      <th id="T_6f488_level0_col6" class="col_heading level0 col6" >iso_alpha</th>
      <th id="T_6f488_level0_col7" class="col_heading level0 col7" >iso_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6f488_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_6f488_row0_col0" class="data row0 col0" >Afghanistan</td>
      <td id="T_6f488_row0_col1" class="data row0 col1" >Asia</td>
      <td id="T_6f488_row0_col2" class="data row0 col2" >1952</td>
      <td id="T_6f488_row0_col3" class="data row0 col3" >28.801000</td>
      <td id="T_6f488_row0_col4" class="data row0 col4" >8425333</td>
      <td id="T_6f488_row0_col5" class="data row0 col5" >779.445314</td>
      <td id="T_6f488_row0_col6" class="data row0 col6" >AFG</td>
      <td id="T_6f488_row0_col7" class="data row0 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_6f488_row1_col0" class="data row1 col0" >Afghanistan</td>
      <td id="T_6f488_row1_col1" class="data row1 col1" >Asia</td>
      <td id="T_6f488_row1_col2" class="data row1 col2" >1957</td>
      <td id="T_6f488_row1_col3" class="data row1 col3" >30.332000</td>
      <td id="T_6f488_row1_col4" class="data row1 col4" >9240934</td>
      <td id="T_6f488_row1_col5" class="data row1 col5" >820.853030</td>
      <td id="T_6f488_row1_col6" class="data row1 col6" >AFG</td>
      <td id="T_6f488_row1_col7" class="data row1 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_6f488_row2_col0" class="data row2 col0" >Afghanistan</td>
      <td id="T_6f488_row2_col1" class="data row2 col1" >Asia</td>
      <td id="T_6f488_row2_col2" class="data row2 col2" >1962</td>
      <td id="T_6f488_row2_col3" class="data row2 col3" >31.997000</td>
      <td id="T_6f488_row2_col4" class="data row2 col4" >10267083</td>
      <td id="T_6f488_row2_col5" class="data row2 col5" >853.100710</td>
      <td id="T_6f488_row2_col6" class="data row2 col6" >AFG</td>
      <td id="T_6f488_row2_col7" class="data row2 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_6f488_row3_col0" class="data row3 col0" >Afghanistan</td>
      <td id="T_6f488_row3_col1" class="data row3 col1" >Asia</td>
      <td id="T_6f488_row3_col2" class="data row3 col2" >1967</td>
      <td id="T_6f488_row3_col3" class="data row3 col3" >34.020000</td>
      <td id="T_6f488_row3_col4" class="data row3 col4" >11537966</td>
      <td id="T_6f488_row3_col5" class="data row3 col5" >836.197138</td>
      <td id="T_6f488_row3_col6" class="data row3 col6" >AFG</td>
      <td id="T_6f488_row3_col7" class="data row3 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_6f488_row4_col0" class="data row4 col0" >Afghanistan</td>
      <td id="T_6f488_row4_col1" class="data row4 col1" >Asia</td>
      <td id="T_6f488_row4_col2" class="data row4 col2" >1972</td>
      <td id="T_6f488_row4_col3" class="data row4 col3" >36.088000</td>
      <td id="T_6f488_row4_col4" class="data row4 col4" >13079460</td>
      <td id="T_6f488_row4_col5" class="data row4 col5" >739.981106</td>
      <td id="T_6f488_row4_col6" class="data row4 col6" >AFG</td>
      <td id="T_6f488_row4_col7" class="data row4 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_6f488_row5_col0" class="data row5 col0" >Afghanistan</td>
      <td id="T_6f488_row5_col1" class="data row5 col1" >Asia</td>
      <td id="T_6f488_row5_col2" class="data row5 col2" >1977</td>
      <td id="T_6f488_row5_col3" class="data row5 col3" >38.438000</td>
      <td id="T_6f488_row5_col4" class="data row5 col4" >14880372</td>
      <td id="T_6f488_row5_col5" class="data row5 col5" >786.113360</td>
      <td id="T_6f488_row5_col6" class="data row5 col6" >AFG</td>
      <td id="T_6f488_row5_col7" class="data row5 col7" >4</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row6" class="row_heading level0 row6" >...</th>
      <td id="T_6f488_row6_col0" class="data row6 col0" >...</td>
      <td id="T_6f488_row6_col1" class="data row6 col1" >...</td>
      <td id="T_6f488_row6_col2" class="data row6 col2" >...</td>
      <td id="T_6f488_row6_col3" class="data row6 col3" >...</td>
      <td id="T_6f488_row6_col4" class="data row6 col4" >...</td>
      <td id="T_6f488_row6_col5" class="data row6 col5" >...</td>
      <td id="T_6f488_row6_col6" class="data row6 col6" >...</td>
      <td id="T_6f488_row6_col7" class="data row6 col7" >...</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row7" class="row_heading level0 row7" >1699</th>
      <td id="T_6f488_row7_col0" class="data row7 col0" >Zimbabwe</td>
      <td id="T_6f488_row7_col1" class="data row7 col1" >Africa</td>
      <td id="T_6f488_row7_col2" class="data row7 col2" >1987</td>
      <td id="T_6f488_row7_col3" class="data row7 col3" >62.351000</td>
      <td id="T_6f488_row7_col4" class="data row7 col4" >9216418</td>
      <td id="T_6f488_row7_col5" class="data row7 col5" >706.157306</td>
      <td id="T_6f488_row7_col6" class="data row7 col6" >ZWE</td>
      <td id="T_6f488_row7_col7" class="data row7 col7" >716</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row8" class="row_heading level0 row8" >1700</th>
      <td id="T_6f488_row8_col0" class="data row8 col0" >Zimbabwe</td>
      <td id="T_6f488_row8_col1" class="data row8 col1" >Africa</td>
      <td id="T_6f488_row8_col2" class="data row8 col2" >1992</td>
      <td id="T_6f488_row8_col3" class="data row8 col3" >60.377000</td>
      <td id="T_6f488_row8_col4" class="data row8 col4" >10704340</td>
      <td id="T_6f488_row8_col5" class="data row8 col5" >693.420786</td>
      <td id="T_6f488_row8_col6" class="data row8 col6" >ZWE</td>
      <td id="T_6f488_row8_col7" class="data row8 col7" >716</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row9" class="row_heading level0 row9" >1701</th>
      <td id="T_6f488_row9_col0" class="data row9 col0" >Zimbabwe</td>
      <td id="T_6f488_row9_col1" class="data row9 col1" >Africa</td>
      <td id="T_6f488_row9_col2" class="data row9 col2" >1997</td>
      <td id="T_6f488_row9_col3" class="data row9 col3" >46.809000</td>
      <td id="T_6f488_row9_col4" class="data row9 col4" >11404948</td>
      <td id="T_6f488_row9_col5" class="data row9 col5" >792.449960</td>
      <td id="T_6f488_row9_col6" class="data row9 col6" >ZWE</td>
      <td id="T_6f488_row9_col7" class="data row9 col7" >716</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row10" class="row_heading level0 row10" >1702</th>
      <td id="T_6f488_row10_col0" class="data row10 col0" >Zimbabwe</td>
      <td id="T_6f488_row10_col1" class="data row10 col1" >Africa</td>
      <td id="T_6f488_row10_col2" class="data row10 col2" >2002</td>
      <td id="T_6f488_row10_col3" class="data row10 col3" >39.989000</td>
      <td id="T_6f488_row10_col4" class="data row10 col4" >11926563</td>
      <td id="T_6f488_row10_col5" class="data row10 col5" >672.038623</td>
      <td id="T_6f488_row10_col6" class="data row10 col6" >ZWE</td>
      <td id="T_6f488_row10_col7" class="data row10 col7" >716</td>
    </tr>
    <tr>
      <th id="T_6f488_level0_row11" class="row_heading level0 row11" >1703</th>
      <td id="T_6f488_row11_col0" class="data row11 col0" >Zimbabwe</td>
      <td id="T_6f488_row11_col1" class="data row11 col1" >Africa</td>
      <td id="T_6f488_row11_col2" class="data row11 col2" >2007</td>
      <td id="T_6f488_row11_col3" class="data row11 col3" >43.487000</td>
      <td id="T_6f488_row11_col4" class="data row11 col4" >12311143</td>
      <td id="T_6f488_row11_col5" class="data row11 col5" >469.709298</td>
      <td id="T_6f488_row11_col6" class="data row11 col6" >ZWE</td>
      <td id="T_6f488_row11_col7" class="data row11 col7" >716</td>
    </tr>
  </tbody>
</table>

---

## Summarize an entire DataFrame

<div class="flex gap-12">
<div>

assume that `df` is the full gapminder data

```python
>>> relevant = ["life_exp", "pop", "gdp_per_cap"]
>>> df[relevant].describe()
```

<style type="text/css">
#T_7c219   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_7c219 thead {
  background-color: #3d3d3d;
}
#T_7c219 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_7c219 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_7c219 td {
  padding: 0em;
}
#T_7c219 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_7c219 caption {
  caption-side: bottom;
}
</style>
<table id="T_7c219">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7c219_level0_col0" class="col_heading level0 col0" >life_exp</th>
      <th id="T_7c219_level0_col1" class="col_heading level0 col1" >pop</th>
      <th id="T_7c219_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7c219_level0_row0" class="row_heading level0 row0" >count</th>
      <td id="T_7c219_row0_col0" class="data row0 col0" >1704.00</td>
      <td id="T_7c219_row0_col1" class="data row0 col1" >1704.00</td>
      <td id="T_7c219_row0_col2" class="data row0 col2" >1704.00</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row1" class="row_heading level0 row1" >mean</th>
      <td id="T_7c219_row1_col0" class="data row1 col0" >59.47</td>
      <td id="T_7c219_row1_col1" class="data row1 col1" >29601212.32</td>
      <td id="T_7c219_row1_col2" class="data row1 col2" >7215.33</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row2" class="row_heading level0 row2" >std</th>
      <td id="T_7c219_row2_col0" class="data row2 col0" >12.92</td>
      <td id="T_7c219_row2_col1" class="data row2 col1" >106157896.74</td>
      <td id="T_7c219_row2_col2" class="data row2 col2" >9857.45</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row3" class="row_heading level0 row3" >min</th>
      <td id="T_7c219_row3_col0" class="data row3 col0" >23.60</td>
      <td id="T_7c219_row3_col1" class="data row3 col1" >60011.00</td>
      <td id="T_7c219_row3_col2" class="data row3 col2" >241.17</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row4" class="row_heading level0 row4" >25%</th>
      <td id="T_7c219_row4_col0" class="data row4 col0" >48.20</td>
      <td id="T_7c219_row4_col1" class="data row4 col1" >2793664.00</td>
      <td id="T_7c219_row4_col2" class="data row4 col2" >1202.06</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row5" class="row_heading level0 row5" >50%</th>
      <td id="T_7c219_row5_col0" class="data row5 col0" >60.71</td>
      <td id="T_7c219_row5_col1" class="data row5 col1" >7023595.50</td>
      <td id="T_7c219_row5_col2" class="data row5 col2" >3531.85</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row6" class="row_heading level0 row6" >75%</th>
      <td id="T_7c219_row6_col0" class="data row6 col0" >70.85</td>
      <td id="T_7c219_row6_col1" class="data row6 col1" >19585221.75</td>
      <td id="T_7c219_row6_col2" class="data row6 col2" >9325.46</td>
    </tr>
    <tr>
      <th id="T_7c219_level0_row7" class="row_heading level0 row7" >max</th>
      <td id="T_7c219_row7_col0" class="data row7 col0" >82.60</td>
      <td id="T_7c219_row7_col1" class="data row7 col1" >1318683096.00</td>
      <td id="T_7c219_row7_col2" class="data row7 col2" >113523.13</td>
    </tr>
  </tbody>
</table>


</div>
<div>

<br/>
<br/>
<br/>

- `.describe` can summarize entire DataFrames
- Result is again a DataFrame
- Often good idea to select a subset of columns

</div>
</div>


---

# Calculate specific statistics

<div class="grid grid-cols-2 gap-4">
<div>
assume that `df` is the full gapminder data

```python
>>> df["life_exp"].mean()
59.474439366197174

>>> df.groupby("year").mean()
```
```txt
year
1952    49.057620
1957    51.507401
1962    53.609249
...
```



</div>
<div>

- Standard summary statistics are implemented and named as expected:
  - `std`
  - `min` and `max`
  - `median` and `quantile`
- Vectorized and really fast implementations


</div>
</div>


---

# Quick plotting: Series

<div class="flex gap-12">
<div>

```python
>>> pd.options.plotting.backend = "plotly"
>>> df.groupby("year")["life_exp"].mean().plot()
```
<img src="lineplot.png" class="rounded" width="400"/>

</div>
<div>

- Any Series has a `.plot` method
- Any Series has a `.hist` method
- Summary statistics based on groupby return Series which can again be plotted

</div>
</div>

---

# Quick plotting: DataFrames

<div class="flex gap-12">
<div>

```python
>>> pd.options.plotting.backend = "plotly"
>>> df.plot.scatter(x="year", y="life_exp",
                    color="country")
```
<img src="scatterplot.png" class="rounded" width="400"/>

</div>
<div>

- Any DataFrame has a `.plot` method
- Defaults to line plot, can access `.scatter` and many more
- Notebook gives you interactive plots

</div>
</div>

---

# Statistics for categorical data

```python
>>> df["country"].unique()[:2]
```
```txt
<ArrowStringArrayNumpySemantics>
['Afghanistan', 'Albania']
Length: 2, dtype: string
```
```python
>>> df["country"].value_counts().sort_index()[:2]
```
```txt
country
Afghanistan    12
Albania        12
Name: count, dtype: int64
```
