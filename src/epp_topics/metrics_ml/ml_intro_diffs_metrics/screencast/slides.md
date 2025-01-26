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

### Introduction to Machine Learning

<br/>

Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# The Fundamental difference

<div class="grid grid-cols-2 gap-4">
<div>

**Econometrics**

- Estimate **fundamentally unobservable** parameters and test hypotheses about them

- Cannot test how well it worked

- Focus on justifying assumptions


</div>
<div>

**(Supervised) Machine learning**

- Predict observable things

- Can check how well it works

- Focus on experimentation, evaluation and finding out what works


</div>
</div>

---

# Some implications

- Even though it is tempting, you cannot interpret parameters

- Can be creative in combining simple models into complex ones

- Rapid progress and development of new models

- Programming skills matter more


---

<div class="grid grid-cols-2 gap-12">
<div>

- Very good paper!

- Difference of ML and Econometrics

- Overview of ML methods

- What we can(not) learn with ML

- List of potential applications in econ


</div>
<div>

<img src="/lecture_4/jep.png" class="rounded" width="300" />

</div>
</div>

---

# Terminology

- **feature, attribute**: x-variable, independent variable

- **target**: y-variable, dependent variable

- **model, algorithm**: model

- **training procedure**: estimation method

- **fitting**: running an estimation

- **classification**: regression with discrete dependent variable

- **logistic regression**: binary or multivariate logit

- **instance**: observation

- **classes**: possible values of a discrete dependent variables


---

# Supervised vs unsupervised learning

- **Supervised learning**

  - Training data contains labeled examples of the task to solve

  - Model generalizes this to unseen data

  - Example: Regression, classification

- **Unsupervised learning**

  - Training with label free data

  - Model finds patterns in data

  - Example: Clustering, dimensionality reduction


---

# Overfitting

- Estimating large models on small datasets can lead to overfitting

- Overfitting means:

  - Model can explain the concrete dataset well

  - Model would not work on any other dataset

  - Same reason why we need adjusted $R^2$ in econometrics

  - Need to make sure our model evaluation accounts for overfitting!

---

# Holdout samples

- Split data into training and test dataset

- Fitting and experimentation is only done on training data

- Evaluation is only done on test data

  - Overfitting on training data cannot influence the evaluation

  - Need to avoid leaking any information from test data into model training!

- Typical sizes:

  - 70 to 80 percent for training

  - Rest for validation

---

# The bias variance trade-off

- Econometrics: Model is correctly specified, want consistency and unbiasedness

- ML: Model is a simplification and some amount of bias is ok

- Very simple models, e.g. just an intercept

  - Large bias, Low variance, No overfitting

- Very large models, e.g. including squares, interactions, ...

  - Small bias, High variance, Danger of overfitting

- Most machine learning models have one or more parameters that govern the bias variance trade-off


---

# Example: Penalty in Lasso model

(Unfinished)

- Lasso regression is fitted by minimizing the least squares objective plus a penalty on the parameters

- How much the parameter penalty is weighted

- Typically, model complexity means many non-zero parameters

- Penalty


---

# Different penalties


---

# Two splits are not enough


---

# K-fold cross validation


---

# Systematic hyperparameter tuning
