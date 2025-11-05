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
title: EPP — Creating variables
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Creating variables

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Using numpy math functions


<div class="flex gap-12">
<div>

assume that `df` is the gapminder example

```python
>>> import numpy as np
>>> df["log_life_exp"] = np.log(df["life_exp"])
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
      <th>log_life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
      <td>4.35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>4.36</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>4.38</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2007</td>
      <td>80.94</td>
      <td>4.39</td>
    </tr>
  </tbody>
</table>

</div>
<div>

- All functions you'll ever need are implemented:
  - `np.log`
  - `np.exp`
  - `np.sqrt`
  - `np.power`
  - ...
- See [docs](https://numpy.org/doc/stable/reference/routines.math.html) for details
- Index is preserved
- Very fast, vectorized implementations


</div>
</div>

---

# Arithmetic with Series


<div class="flex gap-12">
<div>

```python
>>> df["gdp_billion"] = df["gdp_per_cap"] * df["pop"] / 1e9
>>> df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
      <th>gdp_billion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2002</td>
      <td>6340.65</td>
      <td>11226999</td>
      <td>71.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
      <td>102.16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
      <td>997.21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
      <td>1165.76</td>
    </tr>
  </tbody>
</table>

</div>
<div>

- `*`, `+`, `-`, `/`, ... work as expected
- All calculations are aligned by index
- Not all Series have to come from the same DataFrame or be assigned to a DataFrame


</div>
</div>

---

# Recoding values



<div class="flex gap-12">
<div>

```python
>>> df["country_code"] = df["country"].replace(
...     {"Cuba": "CUB", "Spain": "ESP"}
... )
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
      <th>country_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
      <td>CUB</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
      <td>CUB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
      <td>ESP</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2007</td>
      <td>80.94</td>
      <td>ESP</td>
    </tr>
  </tbody>
</table>

</div>
<div>

<br/>
<br/>

- Can be useful to create new variable or fix typos in string variables
- Not super fast, but faster than any looping approach

</div>
</div>


---

# Vectorized if conditions

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> helper = pd.Series(
...     "rich",
...     index=df.index,
... )

>>> df["income_status"] = helper.where(
    cond=df["gdp_per_cap"] > 10000,
    other="not rich",
)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>year</th>
      <th>gdp_per_cap</th>
      <th>pop</th>
      <th>income_status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>2002</td>
      <td>6340.65</td>
      <td>11226999</td>
      <td>not rich</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>2007</td>
      <td>8948.10</td>
      <td>11416987</td>
      <td>not rich</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>2002</td>
      <td>24835.47</td>
      <td>40152517</td>
      <td>rich</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
      <td>rich</td>
    </tr>
  </tbody>
</table>



</div>
<div>

- `pd.Series.where` takes two Series as arguments:
  1. `cond`: Boolean Series determining **where** values are kept
  2. `other`: Series with **values** to be used where `cond` is `False`
- Can express general if conditions using nested where
- Vectorized and fast


</div>
</div>



---

# When is it okay to loop?

<div class="grid grid-cols-2 gap-12">
<div>

### Over columns: ✅

```python
clean = pd.DataFrame()
for var in varlist:
    clean[var] = clean_variable(df[var])
```

- Such a loop is not just ok, it is often the fastest and most readable option
- Accessing and inserting columns is fast
- Even if `clean_variable` is vectorized, it's runtime will completely dominate any loop overhead
</div>
<div>

###  Over rows: ❌

<br/>
<br/>
<br/>

- Code example intentionally left blank
- Use the vectorized functions from above instead of loops
- List comprehensions, `df.apply`, `map`, etc. are just python loops in disguise and not
faster in this case


</div>
</div>
