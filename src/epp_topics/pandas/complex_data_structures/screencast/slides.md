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

### Dealing with complex data structures

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- Real-world data often has complex structure
- Understanding how to organize data is crucial
- Proper data organization can save weeks of work
- These principles come from database research


---

# 1. Values have no internal structure

- a.k.a. the **first normal form**
- I.e., no need for parsing values before using them
- E.g. store first names and last names separately
- Not too often a problem in economic data
  - X-digit industrial or educational classifiers
  - Store each digit level you need in a separate variable

---

# 2. No redundant information in tables

- a.k.a. the **second normal form**
- In a panel structure: Store time-constant characteristics in a
  separate table
- Violations make things much harder and error-prone:
  - Changes to data
  - Consistency checks
  - Selecting observations


---

# 3. No structure in variable names

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
