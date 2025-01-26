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

### Introduction to scikit-learn

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Loading datasets from scikit-learn

- Add code to fetch housing data set

- Add note about `sklearn.datasets`

---

# Train-test splits

- The function train_test_split lets you:

  - select the test set size

  - set random_state for reproducibility

---

# Basic scikit-learn steps

- Choose a class of models by importing the appropriate estimator

- Set hyperparameters by instantiating this class

- Arrange data into a features matrix and target vector

- Fit the model to your data by calling the `fit()` method on the model instance

- Apply the model to new data using the `predict()` method

- Evaluate the quality of predictions


---

# Running a Lasso regression in scikit-learn



---

# Computing metrics

- r2 metric

- mean squared error
