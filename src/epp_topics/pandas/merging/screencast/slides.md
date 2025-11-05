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
title: EPP — Merging datasets
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Merging datasets

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- Often when you download data, it comes in several files
- While you might not like it, this is often because the data providers respected
  the normal forms!
- Or it comes from very different sources
- In this screencast we show you how to merge or concatenate DataFrames


---

# Concatenating DataFrames vertically


<div class="flex gap-12">
<div>

```python
>>> top
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
    </tr>
    <tr>
      <th>country</th>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Cuba</th>
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


```python
>>> bottom
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
    </tr>
    <tr>
      <th>country</th>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Spain</th>
      <th>2002</th>
      <td>Europe</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Europe</td>
      <td>80.94</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> pd.concat([top, bottom])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
    </tr>
    <tr>
      <th>country</th>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Cuba</th>
      <th>2002</th>
      <td>Americas</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Americas</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Spain</th>
      <th>2002</th>
      <td>Europe</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Europe</td>
      <td>80.94</td>
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
  </tbody>
</table>


```python
>>> right
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> pd.concat([left, right], axis="columns")
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
    <tr>
      <th>country</th>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Cuba</th>
      <th>2002</th>
      <td>Americas</td>
      <td>77.16</td>
      <td>6340.65</td>
      <td>11226999</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Americas</td>
      <td>78.27</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Spain</th>
      <th>2002</th>
      <td>Europe</td>
      <td>79.78</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Europe</td>
      <td>80.94</td>
      <td>28821.06</td>
      <td>40448191</td>
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

# Careful with non-meaningful indices


<div class="flex gap-12">
<div>

```python
>>> left
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
  </tbody>
</table>


```python
>>> right
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
    </tr>
  </tbody>
</table>

</div>
<div>

```python
>>> pd.concat([left, right], axis="columns")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
    </tr>
  </tbody>
</table>



<br/>


</div>
</div>


---

# 1:1 merges


<div class="flex gap-12">
<div>

```python
>>> left
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2002</td>
      <td>6340.65</td>
      <td>11226999</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
  </tbody>
</table>

```python
>>> right
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
    </tr>
  </tbody>
</table>


</div>
<div>

```python
>>> pd.merge(left, right, on=["country", "year"])
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
  </tbody>
</table>

<br/>

- merge does not align on index by default
- can change using arguments `left_index=True` and `right_index=True`
- can also use `merge` method on DataFrame (becomes "left" frame)
- by default, it does an inner join


</div>
</div>


---

<div class="flex gap-12">
<div>

```python
>>> pd.merge(left, right, on=["country", "year"], how="inner")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>8948.10</td>
      <td>11416987</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>24835.47</td>
      <td>40152517</td>
    </tr>
  </tbody>
</table>

```python
>>> pd.merge(left, right, on=["country", "year"], how="left")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>8948.10</td>
      <td>11416987.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>24835.47</td>
      <td>40152517.00</td>
    </tr>
  </tbody>
</table>


```python
>>> pd.merge(left, right, on=["country", "year"], how="outer")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>8948.10</td>
      <td>11416987.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>24835.47</td>
      <td>40152517.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>NaN</td>
      <td>2007</td>
      <td>nan</td>
      <td>28821.06</td>
      <td>40448191.00</td>
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

# m:1 merges

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> left
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2002</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2002</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
      <td>80.94</td>
    </tr>
  </tbody>
</table>

```python
>>> right
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Havana</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>Madrid</td>
    </tr>
  </tbody>
</table>



</div>
<div>

```python
>>> pd.merge(left, right, on="country")
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>life_exp</th>
      <th>capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2002</td>
      <td>77.16</td>
      <td>Havana</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>78.27</td>
      <td>Havana</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2002</td>
      <td>79.78</td>
      <td>Madrid</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
      <td>80.94</td>
      <td>Madrid</td>
    </tr>
  </tbody>
</table>

<br/>

- The type of merge is determined by the data, not by calling a different function
- m:1 means that many entries in `left` are matched to one entry in `right`

</div>
</div>


---

# Other merges

- There are also "1:m" and "m:m" merges
- Check the pandas [tutorial](https://pandas.pydata.org/docs/user_guide/merging.html)
for details


---

# Concat vs. merge

- Use `concat` if it is safe to do
  - Index / columns are compatible
  - Only 1:1 merging
- Use `merge`
  - if you do anything outside of 1:1 merging
  - if you need more control


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
