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
title: EPP — Pandas — Inspecting and summarizing data
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


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>pop</th>
      <th>gdp_per_cap</th>
      <th>iso_alpha</th>
      <th>iso_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1952</td>
      <td>28.801</td>
      <td>8425333</td>
      <td>779.445314</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1957</td>
      <td>30.332</td>
      <td>9240934</td>
      <td>820.85303</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1962</td>
      <td>31.997</td>
      <td>10267083</td>
      <td>853.10071</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1967</td>
      <td>34.02</td>
      <td>11537966</td>
      <td>836.197138</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1972</td>
      <td>36.088</td>
      <td>13079460</td>
      <td>739.981106</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1977</td>
      <td>38.438</td>
      <td>14880372</td>
      <td>786.11336</td>
      <td>AFG</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1699</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1987</td>
      <td>62.351</td>
      <td>9216418</td>
      <td>706.157306</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1700</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1992</td>
      <td>60.377</td>
      <td>10704340</td>
      <td>693.420786</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1701</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>1997</td>
      <td>46.809</td>
      <td>11404948</td>
      <td>792.44996</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1702</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2002</td>
      <td>39.989</td>
      <td>11926563</td>
      <td>672.038623</td>
      <td>ZWE</td>
      <td>716</td>
    </tr>
    <tr>
      <th>1703</th>
      <td>Zimbabwe</td>
      <td>Africa</td>
      <td>2007</td>
      <td>43.487</td>
      <td>12311143</td>
      <td>469.709298</td>
      <td>ZWE</td>
      <td>716</td>
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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>life_exp</th>
      <th>pop</th>
      <th>gdp_per_cap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1704.00</td>
      <td>1704.00</td>
      <td>1704.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>59.47</td>
      <td>29601212.32</td>
      <td>7215.33</td>
    </tr>
    <tr>
      <th>std</th>
      <td>12.92</td>
      <td>106157896.74</td>
      <td>9857.45</td>
    </tr>
    <tr>
      <th>min</th>
      <td>23.60</td>
      <td>60011.00</td>
      <td>241.17</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>48.20</td>
      <td>2793664.00</td>
      <td>1202.06</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>60.71</td>
      <td>7023595.50</td>
      <td>3531.85</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>70.85</td>
      <td>19585221.75</td>
      <td>9325.46</td>
    </tr>
    <tr>
      <th>max</th>
      <td>82.60</td>
      <td>1318683096.00</td>
      <td>113523.13</td>
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
<img src="/lineplot.svg" class="rounded" width="400"/>

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
<img src="/scatterplot.svg" class="rounded" width="400"/>

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
