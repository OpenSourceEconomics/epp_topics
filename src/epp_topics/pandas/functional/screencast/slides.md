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
title: EPP — Functional data management
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Functional data management

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- So far we have shown you the mechanics of using pandas
- Now we talk about general best practices
  - Can save weeks of work in large projects
  - Grounded in database research and software engineering


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

# How to implement these principles?

- Use a **functional approach** to data management
- Structure your code with pure functions
- Each function does one thing and does it well
- Let's see an example!

---

# Example

consider this hypothetical survey about a programming course

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> raw = pd.read_csv("survey.csv")
>>> raw
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Q001</th>
      <th>Q002</th>
      <th>Q003</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strongly disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>1</th>
      <td>strongly agree</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-77</td>
      <td>disagree</td>
      <td>R</td>
    </tr>
    <tr>
      <th>3</th>
      <td>agree</td>
      <td>-77</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-99</td>
      <td>-99</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>6</th>
      <td>neutral</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>7</th>
      <td>disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>8</th>
      <td>strongly agree</td>
      <td>-99</td>
      <td>PYTHON</td>
    </tr>
    <tr>
      <th>9</th>
      <td>agree</td>
      <td>-99</td>
      <td>Ypthon</td>
    </tr>
  </tbody>
</table>


</div>
<div>

<br/>
<br/>


From the metadata you know

- Q001: I am a coding genius
- Q001: I learned a lot
- Q003: What is your favourite language

<br/>

- -77 not readable
- -99 no reply


</div>
</div>
