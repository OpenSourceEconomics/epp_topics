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

| reader            | extension | comment                                              |
| ----------------- | --------- | ---------------------------------------------------- |
| `pd.read_csv`     | `.csv`    | Often need to use optional arguments to make it work |
| `pd.read_pickle`  | `.pkl`    | Good for intermediate files; Python specific.        |
| `pd.read_feather` | `.arrow`  | Very modern and powerful file format.                |
| `pd.read_stata`   | `.dta`    | Stata's proprietary format. Avoid if you can.        |
| `pd.read_fwf`     | `.fwf`    | Avoid this whenever you can!                         |

Each read function has a corresponding write function

---

# Example: Write an Apache Arrow file

<div class="grid grid-cols-2 gap-4">
<div>

```python
df.to_feather(path="gapminder.arrow")
```

</div>
<div>

- First argument is a file path
- More keyword arguments would allow for specifying compression level, format version
- Methods for other file formats tend to require more options

</div>
</div>

---

# File format recommendations

- Use `.pkl` format for processed datasets that you do not share with others
  - Very fast to read and write
  - Preserves every aspect of your DataFrame (e.g. dtypes)
- Use `.arrow` to save files you want to share with others
  - Can be read by many languages and programs
  - Efficient compression
- Use `.dta` iff sharing with Stata users
