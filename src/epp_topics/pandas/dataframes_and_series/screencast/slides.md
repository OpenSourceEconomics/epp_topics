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
title: EPP — Pandas — DataFrames and Series
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### DataFrames and Series

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is a DataFrame

<div class="flex gap-8">
<div>

```python
>>> df = pd.read_csv(path, engine="pyarrow")
>>> df
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
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
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
  1. Matrix/Array with labels
  1. Dictionary of columns
- Can inspect index and column names

</div>
</div>

---

# What is a Series?

<br/>

<div class="flex gap-8">
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

- Each column of a DataFrame is a Series
- Mental model: Vector with an index
- All entries in a Series have the same dtype

</div>
</div>

---

# Creating DataFrames and Series

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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>1</td>
      <td>bla</td>
    </tr>
    <tr>
      <th>d</th>
      <td>3</td>
      <td>blubb</td>
    </tr>
  </tbody>
</table>



<br/>


```python
>>> pd.Series(
...     [3.0, 4.5], index=["x", "y"],
... )
```
```txt
x    3.0
y    4.5
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
>>> sr = pd.Series(
...   [2.71, 3.14],
...   index=["d", "c"],
... )
>>> df["new_col"] = sr
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>new_col</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>1</td>
      <td>bla</td>
      <td>3.14</td>
    </tr>
    <tr>
      <th>d</th>
      <td>3</td>
      <td>blubb</td>
      <td>2.71</td>
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
