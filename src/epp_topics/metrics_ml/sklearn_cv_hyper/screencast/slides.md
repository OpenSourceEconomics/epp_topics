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

### Cross-validation and hyperparameter tuning in scikit-learn

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

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

# Example: Penalty in a logit model

- Logistic regression is fitted my minimizing a negative log likelihood function

- Can augment likelihood by a term that penalizes model complexity

- Typically, model complexity means many non-zero parameters

- Penalty is a function of the parameter vector

  $\theta^\ast = \argmin_\theta \ell(\theta; X, y) + \lambda \cdot p(\theta)$


---

# Different penalties

L1: &nbsp;&nbsp; $p(\theta) = \sum_i |\theta_i|$

  - Penalizes all deviations from zero equally

  - Induces sparsity

  - Harder numerical optimization, not compatible with all optimizers

L2: &nbsp;&nbsp; $p(\theta) = \sum_i \theta_i^2$

- Penalizes values close to zero very weakly

- Does not induce sparsity

- Simpler numerical optimization




---

# Two splits are not enough

- Want to set tuning parameters optimally

- Naive approach:

  - Fit models with different parameters on training set

  - Evaluate performance on test set

  - Keep the best

- Problem: Hyperparameters are over-fit to the test set

- Use cross-validation avoids this


---

# K-fold cross validation

- Idea: Split the training data repeatedly into:

  - Data used for actual traning

  - Data used for evaluation

- Repeat k times to get k scores

- Keep model that achieves best average score

- Use actual test set only once in the end to measure model quality



---

# Systematic hyperparameter tuning

- Specify a combination of hyperparameters we want to try

  - Example: Different penalty weightings $\lambda$ in penalized Logit

- Calculate cross validation score for each set of parameters

- Keep model with best performance

- Re-fit best model on entire dataset


---

# Cross-validaton

- Show `cross_val_score`

---

# Hyperparameter tuning

- Show `GridSearchCV` for Lasso penalty
