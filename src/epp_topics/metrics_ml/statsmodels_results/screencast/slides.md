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

### Working with statsmodels' results objects

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Example

<img src="/scatter-dark.svg" class="rounded" width="600">


---

# Model and Results Objects

<!-- Slide is very full without some negative vertical space. -->
<div style="margin-top:-1em;">

```python
model = smf.ols(
    data=df,
    formula="fraction_using_computer_at_work ~ fraction_with_tertiary_education",
)
model
```
```text
<statsmodels.regression.linear_model.OLS at 0x7fb56c905250>
```
</div>

<!-- Add some spacing after first output for easier distinction between commands. -->
<div style="margin-top:0.75em;">

```python
all_results = model.fit()
all_results
```
```text
<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f84b22e7490>
```

</div>

`RegressionResultsWrapper` contains methods and attributes for all results
- Coefficient estimates
- Predictions / Residuals
- Variance-covariance matrix of estimates
- Many tests

---

# Summarising Regression Results

```python
all_results.summary()
```

<table class="simpletable">
<tr>
  <th>Dep. Variable:</th>    <td>fraction_using_computer_at_work</td> <th>  R-squared:         </th> <td>   0.628</td>
</tr>
<tr>
  <th>Model:</th>                          <td>OLS</td>               <th>  Adj. R-squared:    </th> <td>   0.505</td>
</tr>
<tr>
  <th>Method:</th>                    <td>Least Squares</td>          <th>  F-statistic:       </th> <td>   5.074</td>
</tr>
<tr>
  <th>No. Observations:</th>             <td>     5</td>              <th>Df Residuals:</th>                 <td>     3</td>
</tr>
</table>
<table class="simpletable">
<tr>
                  <td></td>                    <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>
</tr>
<tr>
  <th>Intercept</th>                        <td>    0.4445</td> <td>    0.126</td> <td>    3.541</td> <td> 0.038</td> <td>    0.045</td> <td>    0.844</td>
</tr>
<tr>
  <th>fraction_with_tertiary_education</th> <td>    0.9399</td> <td>    0.417</td> <td>    2.253</td> <td> 0.110</td> <td>   -0.388</td> <td>    2.268</td>
</tr>
</table>


---

# Add Mean Prediction to Data

```python
df["predicted"] = all_results.predict(df)
df
```

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fraction_with_tertiary_education</th>
      <th>&nbsp;&nbsp;fraction_using_computer_at_work</th>
      <th>&nbsp;&nbsp;predicted</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Slovak Republic</th>
      <td style="text-align: right;">0.172</td>
      <td style="text-align: right;">0.534</td>
      <td style="text-align: right;">0.607</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td style="text-align: right;">0.206</td>
      <td style="text-align: right;">0.737</td>
      <td style="text-align: right;">0.638</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td style="text-align: right;">0.314</td>
      <td style="text-align: right;">0.712</td>
      <td style="text-align: right;">0.740</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td style="text-align: right;">0.371</td>
      <td style="text-align: right;">0.754</td>
      <td style="text-align: right;">0.793</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td style="text-align: right;">0.380</td>
      <td style="text-align: right;">0.842</td>
      <td style="text-align: right;">0.802</td>
    </tr>
  </tbody>
</table>

---

# Plot the Regression Line

```python
line_fig = df.plot(x="fraction_with_tertiary_education", y="predicted")
line_fig.show()
```

<img src="/line-dark.svg" class="rounded" width="600">

---

# Add Regression Line to Scatter Plot

```python
fig = df.reset_index().plot.scatter(
    x="fraction_with_tertiary_education",
    y="fraction_using_computer_at_work",
    text="country",
)
# Add the regression line
fig.add_traces(line_fig.data)
# Nicer formatting
fig.update_traces(textposition="top center")
fig.update_xaxes(range=(0.15, 0.4))
fig.show()
```

---

# Data Points and Regression Line

<img src="/scatter-line-dark.svg" class="rounded" width="600">
