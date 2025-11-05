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
title: EPP — Selecting rows and columns
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

# Overview

- Selecting columns
- Selecting individual rows
- Selecting rows and columns
- Selecting rows using Boolean Series
- Selecting rows with queries

---

# Selecting columns


<div class="grid grid-cols-2 gap-12">
<div>

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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>Europe</td>
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


<div class="flex gap-12">
<div>

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
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2002</th>
      <td>Americas</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Americas</td>
      <td>78.27</td>
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

```python
>>> df.loc[1, "country"]
'Cuba'

>>> df.loc[[1, 3], ["country", "year"]]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
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

# Selecting rows using Boolean Series

<div class="grid grid-cols-2 gap-4">
<div>

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
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
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

```python
>>> df.query("year >= 2005")
```

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
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
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


<br/>


```python
>>> df.query("year >= 2005 & continent == 'Europe'")
```

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

- `.query` selects rows based on strings with conditions
- Can use index names just as column names
- Use single quotes (`'`) for string value inside the query
- More readable than selection via Boolean Series

</div>
</div>
