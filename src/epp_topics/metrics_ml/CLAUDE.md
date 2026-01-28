# Machine Learning and Econometrics Guidelines for AI Agents

This document provides guidance for AI coding agents working with machine learning and
econometrics code in Python, based on the course materials in this chapter.

## Table of Contents

1. [Fundamental Differences: ML vs Econometrics](#fundamental-differences-ml-vs-econometrics)
1. [Terminology Mapping](#terminology-mapping)
1. [Statsmodels Usage](#statsmodels-usage)
1. [Scikit-learn Usage](#scikit-learn-usage)
1. [Model Evaluation](#model-evaluation)
1. [Cross-Validation and Hyperparameter Tuning](#cross-validation-and-hyperparameter-tuning)

______________________________________________________________________

## Fundamental Differences: ML vs Econometrics

Understanding when to use each approach is critical for writing correct code.

### Econometrics

- Goal: Estimate **fundamentally unobservable** parameters and test hypotheses
- Cannot directly test how well estimation worked
- Focus on justifying assumptions (identification, exogeneity, etc.)
- Parameters have causal/structural interpretations

### Machine Learning (Supervised)

- Goal: Predict observable outcomes
- Can directly measure prediction quality on held-out data
- Focus on experimentation, evaluation, and finding what works
- Parameters generally should NOT be interpreted causally

### DO

- Use econometrics (statsmodels) when the goal is causal inference or hypothesis testing
- Use machine learning (scikit-learn) when the goal is prediction
- Always clarify the goal before choosing an approach

### DON'T

- Do NOT interpret ML model parameters as causal effects
- Do NOT use ML predictions as evidence of causal relationships
- Do NOT skip holdout samples when the goal is prediction

______________________________________________________________________

## Terminology Mapping

When translating between econometrics and ML contexts:

| Machine Learning    | Econometrics                                     |
| :------------------ | :----------------------------------------------- |
| feature, attribute  | x-variable, independent variable                 |
| target              | y-variable, dependent variable                   |
| model, algorithm    | model                                            |
| training procedure  | estimation method                                |
| fitting             | running an estimation                            |
| classification      | regression with discrete dependent variable      |
| logistic regression | binary or multivariate logit                     |
| instance            | observation                                      |
| classes             | possible values of a discrete dependent variable |

______________________________________________________________________

## Statsmodels Usage

Statsmodels is the primary library for econometric analysis in Python.

### Import Conventions

```python
# Plain statsmodels API
import statsmodels.api as sm

# Formula interface (recommended for most use cases)
import statsmodels.formula.api as smf
```

### Running Regressions with the Formula Interface

```python
import statsmodels.formula.api as smf

# Create model object
model = smf.ols(
    formula="y_variable ~ x_variable1 + x_variable2",
    data=df,
)

# Fit the model to get results
results = model.fit()

# Or with robust standard errors
results = model.fit(cov_type="HC1")
```

### Formula Syntax

The formula interface uses patsy syntax:

- `~` separates left-hand side (dependent) from right-hand side (independent variables)
- `+` adds variables
- `*` includes main effects and interaction
- `:` includes only the interaction
- `**` for polynomial terms
- `C(variable)` for categorical variables
- `np.log(variable)` for transformations

### DO

- Use the formula interface (`smf`) for readable, maintainable code
- Always call `.fit()` on the model object to get results
- Use `cov_type` parameter for robust standard errors when appropriate
- Access results via the results object (e.g., `results.params`, `results.summary()`)

### DON'T

- Do NOT forget that the intercept is implicit in OLS (included by default)
- Do NOT confuse the model object with the results object

### Working with Results Objects

```python
# Get summary table
results.summary()

# Access coefficients
results.params

# Generate predictions
df["predicted"] = results.predict(df)

# Access other attributes
results.rsquared
results.pvalues
results.conf_int()
```

______________________________________________________________________

## Scikit-learn Usage

Scikit-learn is the primary library for machine learning in Python.

### Basic Workflow Steps

1. Arrange data into features matrix (X) and target vector (y)
1. Split into training and test sets
1. Choose and import an estimator class
1. Instantiate with hyperparameters
1. Fit the model using `.fit()`
1. Generate predictions using `.predict()`
1. Evaluate predictions

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,  # 30% for testing
    random_state=1234,  # For reproducibility
)
```

### Example: Classification with Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

# Instantiate with hyperparameters
model = LogisticRegression(
    fit_intercept=True,
    penalty=None,  # or "l1", "l2"
)

# Fit on training data
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
accuracy = model.score(X_test, y_test)
```

### DO

- Always split data into training and test sets BEFORE fitting
- Set `random_state` for reproducibility
- Fit on training data only
- Evaluate on test data only
- Use 70-80% of data for training, rest for testing

### DON'T

- Do NOT evaluate on the same data used for training (leads to overfitting)
- Do NOT leak test set information into training
- Do NOT skip setting `random_state` when reproducibility matters

______________________________________________________________________

## Model Evaluation

### Classification Metrics

#### Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
```

- Measures share of correctly predicted data points
- Simple but can be misleading with imbalanced data

#### Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_test, y_pred, normalize="true")
```

- Rows are true labels, columns are predictions
- Diagonal shows correctly classified shares per class

#### Precision, Recall, and F1 Score

```python
from sklearn.metrics import precision_score, recall_score, f1_score

# Per-class scores
precision = precision_score(y_test, y_pred, average=None)
recall = recall_score(y_test, y_pred, average=None)
f1 = f1_score(y_test, y_pred, average=None)

# Aggregated scores for imbalanced data
precision_macro = precision_score(y_test, y_pred, average="macro")
f1_weighted = f1_score(y_test, y_pred, average="weighted")
```

- **Precision**: True positives / Predicted positives (use when false positives are
  costly)
- **Recall**: True positives / Actual positives (use when false negatives are costly)
- **F1**: Harmonic mean of precision and recall (balanced metric)

#### Classification Report

```python
from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    y_pred,
    target_names=["Class 0", "Class 1"],
)
print(report)
```

### DO

- Use `classification_report` for a comprehensive view of model performance
- Use `average="macro"` or `average="weighted"` for imbalanced data
- Check per-class metrics, not just overall accuracy
- Use confusion matrix to understand error patterns

### DON'T

- Do NOT rely solely on accuracy with imbalanced data
- Do NOT use default `average` settings without understanding class distribution
- Do NOT ignore minority class performance

______________________________________________________________________

## Cross-Validation and Hyperparameter Tuning

### The Bias-Variance Trade-off

- Simple models: Large bias, low variance, no overfitting
- Complex models: Small bias, high variance, danger of overfitting
- Hyperparameters control this trade-off

### Why Two Splits Are Not Enough

If you tune hyperparameters on the test set, you overfit to the test set. Use
cross-validation on training data instead.

### K-Fold Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

scores = cross_val_score(
    LogisticRegression(max_iter=3000),
    X_train,
    y_train,
    cv=5,  # 5-fold cross-validation
)

mean_score = scores.mean()
```

### Grid Search for Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Define parameter grid
param_grid = {
    "penalty": ["l1", "l2"],
    "C": [0.1, 1, 10],
}

# Set up grid search
grid = GridSearchCV(
    LogisticRegression(solver="liblinear", max_iter=3000),
    param_grid,
    cv=5,
)

# Fit (this trains many models)
grid.fit(X_train, y_train)

# Access best parameters and model
best_params = grid.best_params_
best_model = grid.best_estimator_

# Final evaluation on test set
test_score = best_model.score(X_test, y_test)
```

### Regularization Penalties

- **L1 (Lasso)**: Induces sparsity (some coefficients become exactly zero)
- **L2 (Ridge)**: Shrinks coefficients toward zero but does not induce sparsity

### DO

- Use cross-validation for hyperparameter tuning
- Reserve the test set for final evaluation only
- Use `GridSearchCV` for systematic hyperparameter search
- Set `max_iter` high enough to ensure convergence
- Use appropriate solver for your penalty type (e.g., `solver="liblinear"` for L1)

### DON'T

- Do NOT tune hyperparameters directly on the test set
- Do NOT use the test set multiple times during model development
- Do NOT ignore convergence warnings
- Do NOT forget to refit the best model on all training data after CV

______________________________________________________________________

## Quick Reference: Common Patterns

### Statsmodels OLS Regression

```python
import statsmodels.formula.api as smf

model = smf.ols(formula="y ~ x1 + x2 + C(categorical_var)", data=df)
results = model.fit()
print(results.summary())
predictions = results.predict(new_data)
```

### Scikit-learn Classification Pipeline

```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Grid search with cross-validation
param_grid = {"C": [0.1, 1, 10], "penalty": ["l1", "l2"]}
grid = GridSearchCV(
    LogisticRegression(solver="liblinear", max_iter=3000),
    param_grid,
    cv=5,
)
grid.fit(X_train, y_train)

# Evaluate
y_pred = grid.best_estimator_.predict(X_test)
print(classification_report(y_test, y_pred))
```
