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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Data Analysis in Python

### Running regressions using statsmodels

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Example

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fraction_with_tertiary_education</th>
      <th>fraction_using_computer_at_work</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Slovak Republic</th>
      <td style="text-align: right;">0.172</td>
      <td style="text-align: right;">0.534</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td style="text-align: right;">0.206</td>
      <td style="text-align: right;">0.737</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td style="text-align: right;">0.314</td>
      <td style="text-align: right;">0.712</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td style="text-align: right;">0.371</td>
      <td style="text-align: right;">0.754</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td style="text-align: right;">0.380</td>
      <td style="text-align: right;">0.842</td>
    </tr>
  </tbody>
</table>


---

# Example

<img src="scatter-dark.svg" class="rounded" width="600">


---

# Importing conventions

- Plain statsmodels

  ```python
  import statsmodels.api as sm
  ```

- Formula interface

  ```python
  import statsmodels.formula.api as smf
  ```

---

# The formula interface

```python
model = smf.ols(
    data=df,
    formula="fraction_using_computer_at_work ~ fraction_with_tertiary_education",
)
```

- Use a regression model implemented in `statsmodels.formula.api`
- `data` is a dataframe, `formula` is a string
- Separate left-hand side and right-hand by `~`
- Intercept is implicit for OLS
- Right hand-side can contain lots of mathematical expressions
  - `+`, `**`, `*`, `:` for sums, powers, interactions
  - `C()` for categorical variables
  - `np.log()` for logarithms (and any similar functions)

---

# Model objects

```python
[3] model = smf.ols(
        data=df,
        formula="fraction_using_computer_at_work ~ fraction_with_tertiary_education",
    )
    model
```
```text
<statsmodels.regression.linear_model.OLS at 0x7fb56c905250>
```

Almost always, the next step is to call the `.fit()` method on the model object.
