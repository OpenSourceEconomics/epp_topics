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

### Rules for data management

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- So far we have shown you the mechanics of using pandas
- Now we talk about general best practices
  - Can save weeks of work in large projects
  - Grounded in database research


---

# 1. Never ever change source data

- **Source data**: Original dataset as downloaded or collected
- Commit the source data to git and never change it
- All modified datasets should be stored under different names
- Modified datasets should not be under version control!


---

# 2. Separate data mgm't and analysis

- **Data management**: Converting source data to formats your analysis programs need
- Separate data management code from analysis code
- Never modify the content of a variable outside the data management code!


---

# 3. Values have no internal structure

- a.k.a. the **first normal form**
- I.e., no need for parsing values before using them
- E.g. store first names and last names separately
- Not too often a problem in economic data
  - X-digit industrial or educational classifiers
  - Store each digit level you need in a separate variable

---

# 4. No redundant information in tables

- a.k.a. the **second normal form**
- In a panel structure: Store time-constant characteristics in a
  separate table
- Violations make things much harder and error-prone:
  - Changes to data
  - Consistency checks
  - Selecting observations


---

# 5. No structure in variable names

- a.k.a. use long format if you can
- There should not be different variables with similar content referring to different
  time periods etc.
- If you need wide format for regressions, still do your data management in long format


<br/>

<div class="flex gap-4">
<div>

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
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>2007</td>
      <td>28821.06</td>
      <td>40448191</td>
    </tr>
  </tbody>
</table>

          (long format)

</div>
<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gdp_per_cap_2002</th>
      <th>gdp_per_cap_2007</th>
      <th>pop_2002</th>
      <th>pop_2007</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cuba</th>
      <td>6340.65</td>
      <td>8948.10</td>
      <td>11226999.00</td>
      <td>11416987.00</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>24835.47</td>
      <td>28821.06</td>
      <td>40152517.00</td>
      <td>40448191.00</td>
    </tr>
  </tbody>
</table>

<br/>

                      (wide format)


</div>
</div>
