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

<style type="text/css">
#T_3b726   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_3b726 thead {
  background-color: #3d3d3d;
}
#T_3b726 tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_3b726 tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_3b726 td {
  padding: 0em;
}
#T_3b726 th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_3b726 caption {
  caption-side: bottom;
}
</style>
<table id="T_3b726">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_3b726_level0_col0" class="col_heading level0 col0" >country</th>
      <th id="T_3b726_level0_col1" class="col_heading level0 col1" >year</th>
      <th id="T_3b726_level0_col2" class="col_heading level0 col2" >gdp_per_cap</th>
      <th id="T_3b726_level0_col3" class="col_heading level0 col3" >pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3b726_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_3b726_row0_col0" class="data row0 col0" >Cuba</td>
      <td id="T_3b726_row0_col1" class="data row0 col1" >2002</td>
      <td id="T_3b726_row0_col2" class="data row0 col2" >6340.65</td>
      <td id="T_3b726_row0_col3" class="data row0 col3" >11226999</td>
    </tr>
    <tr>
      <th id="T_3b726_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_3b726_row1_col0" class="data row1 col0" >Cuba</td>
      <td id="T_3b726_row1_col1" class="data row1 col1" >2007</td>
      <td id="T_3b726_row1_col2" class="data row1 col2" >8948.10</td>
      <td id="T_3b726_row1_col3" class="data row1 col3" >11416987</td>
    </tr>
    <tr>
      <th id="T_3b726_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_3b726_row2_col0" class="data row2 col0" >Spain</td>
      <td id="T_3b726_row2_col1" class="data row2 col1" >2002</td>
      <td id="T_3b726_row2_col2" class="data row2 col2" >24835.47</td>
      <td id="T_3b726_row2_col3" class="data row2 col3" >40152517</td>
    </tr>
    <tr>
      <th id="T_3b726_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_3b726_row3_col0" class="data row3 col0" >Spain</td>
      <td id="T_3b726_row3_col1" class="data row3 col1" >2007</td>
      <td id="T_3b726_row3_col2" class="data row3 col2" >28821.06</td>
      <td id="T_3b726_row3_col3" class="data row3 col3" >40448191</td>
    </tr>
  </tbody>
</table>

          (long format)

</div>
<div>


<style type="text/css">
#T_85f3a   {
  margin: 0;
  font-family: "Helvetica", "Helvetica", sans-serif;
  border-collapse: collapse;
  border: none;
  font-size: 80%;
  color: #fff;
}
#T_85f3a thead {
  background-color: #3d3d3d;
}
#T_85f3a tbody tr:nth-child(even) {
  background-color: #3d3d3d;
}
#T_85f3a tbody tr:nth-child(odd) {
  background-color: #565656;
}
#T_85f3a td {
  padding: 0em;
}
#T_85f3a th {
  font-weight: bold;
  text-align: left;
  padding: 0em;
}
#T_85f3a caption {
  caption-side: bottom;
}
</style>
<table id="T_85f3a">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_85f3a_level0_col0" class="col_heading level0 col0" >gdp_per_cap_2002</th>
      <th id="T_85f3a_level0_col1" class="col_heading level0 col1" >gdp_per_cap_2007</th>
      <th id="T_85f3a_level0_col2" class="col_heading level0 col2" >pop_2002</th>
      <th id="T_85f3a_level0_col3" class="col_heading level0 col3" >pop_2007</th>
    </tr>
    <tr>
      <th class="index_name level0" >country</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_85f3a_level0_row0" class="row_heading level0 row0" >Cuba</th>
      <td id="T_85f3a_row0_col0" class="data row0 col0" >6340.65</td>
      <td id="T_85f3a_row0_col1" class="data row0 col1" >8948.10</td>
      <td id="T_85f3a_row0_col2" class="data row0 col2" >11226999.00</td>
      <td id="T_85f3a_row0_col3" class="data row0 col3" >11416987.00</td>
    </tr>
    <tr>
      <th id="T_85f3a_level0_row1" class="row_heading level0 row1" >Spain</th>
      <td id="T_85f3a_row1_col0" class="data row1 col0" >24835.47</td>
      <td id="T_85f3a_row1_col1" class="data row1 col1" >28821.06</td>
      <td id="T_85f3a_row1_col2" class="data row1 col2" >40152517.00</td>
      <td id="T_85f3a_row1_col3" class="data row1 col3" >40448191.00</td>
    </tr>
  </tbody>
</table>

<br/>

                      (wide format)


</div>
</div>
