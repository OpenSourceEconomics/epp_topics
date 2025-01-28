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

### Cross-validation and hyperparameters in scikit-learn

<br/>

Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# The bias-variance trade-off

- Econometrics: Model is correctly specified, want consistency and unbiasedness

- Very simple models, e.g. just an intercept and a couple of regressors

  - Large bias, low variance, no overfitting

- Very large models, e.g. including squares, interactions, ...

  - Small bias, high variance, danger of overfitting

- ML: Model is a simplification and some amount of bias is ok

- Most ML models have one or more parameters that govern the bias variance trade-off

---

# Example: Penalty in a logit model

- Logistic regression is fit by minimizing a negative log likelihood function

- Can augment likelihood by a term that penalizes model complexity

- Typically, model complexity means many non-zero parameters

- Penalty is a function of the parameter vector

  $\theta^\ast = \argmin_\theta \ell(\theta; X, y) + \lambda \cdot p(\theta)$

---

# Different penalties

- L1: &nbsp;&nbsp; $p(\theta) = \sum_i |\theta_i|$

  - Penalizes all deviations from zero equally

  - Induces sparsity

  - Harder numerical optimization, not compatible with all optimizers

- L2: &nbsp;&nbsp; $p(\theta) = \sum_i \theta_i^2$

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

- Use cross-validation to avoid this

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

<div class="grid grid-cols-[52%_48%] gap-4">

<div>

```python
>>> from sklearn.model_selection import cross_val_score
>>> scores = cross_val_score(
...   LogisticRegression(max_iter=3000),
...   X_train,
...   y_train,
...   cv=5
... )
>>> scores
array([
  0.84844291,
  0.84532872,
  0.85709343,
  0.84492904,
  0.86396677
])
```

```python
>>> scores.mean()
0.8519521727205328
```

</div>
<div>

- Import and create instance as normal, do not call `fit()`

- L2 penalty is default

- Provide data to `cross_val_score`

- `cv` argument specifies number of folds

- `cross_val_score` will call `fit()` repeatedly

</div>
</div>

---

# Systematic hyperparameter tuning

- Specify a combination of hyperparameters we want to try

- Calculate cross validation score for each set of parameters

- Keep model with best performance

- Re-fit best model on entire dataset

- Implement in `GridSearchCV`

---

# Grid Search

<div class="grid grid-cols-[50%_50%] gap-3">
<div>

```python
>>> from sklearn.model_selection import GridSearchCV
>>> param_grid = {
...   "penalty": ["l2", "l1"],
...   "C": [0.1, 1, 10],
... }
>>> grid = GridSearchCV(
...   LogisticRegression(solver="liblinear"),
...   param_grid,
...   cv=5,
... )
>>> grid.fit(X_train, y_train)
```

```python
>>> grid.best_params_
{'C': 10, 'penalty': 'l1'}
```

```python
>>> grid.best_estimator_.score(
...   X_test,
...   y_test
... )
0.8430232558139535
```

</div>
<div>

- `param_grid` keys are names of arguments of `LogisticRegression`

- `param_grid` values are lists of possible values for the arguments

- Setting up the grid does not fit models yet

- `grid.fit()` takes some time and often produces warnings

</div>
</div>
