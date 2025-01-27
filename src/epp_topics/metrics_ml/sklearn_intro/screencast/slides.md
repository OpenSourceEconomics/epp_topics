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

- Toy datasets are found using `sklearn.datasets.load_*`

  ```python
  from sklearn.datasets import load_diabetes
  diabets = load_diabetes()
  ```

- Real world datasets can be downloaded using `sklearn.datasets.fetch_*`

  ```python
  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  ```

- Some datasets can be generated using `sklearn.datasets.make_*`

  ```python
  from sklearn.datasets import make_regression
  X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
  ```

---

# Example: California Housing

```python
>>> from sklearn.datasets import fetch_california_housing
>>> housing = fetch_california_housing()
>>> housing.keys()
dict_keys(['data', 'target', 'frame', 'target_names', 'feature_names', 'DESCR'])
```

```python
>>> housing["data"].shape
(20640, 8)
```

```python
>>> housing["feature_names"]
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
```

```python
>>> housing["target"].shape
(20640,)
```

```python
>>> housing["target_names"]
['MedHouseVal']
```
Re-define our target as 1 if the median house value is above the median, 0 otherwise:
```python
import numpy as np
target = (housing["target"] > np.median(housing["target"])).astype(int)
```

---

# Train-test splits

<div class="grid grid-cols-[52%_48%] gap-4">
<div>


```python
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(
...   housing["data"],
...   target,
...   random_state=1234,
...   test_size=0.3,
... )
>>> X_train.shape
(14448, 8)
```
```python
>>> y_train.shape
(14448,)
```
```python
>>> X_test.shape
(6192, 8)
```
```python
>>> y_test.shape
(6192,)
```
</div>
<div>

- The function `train_test_split` lets you:

  - select the test set size

  - set `random_state` for reproducibility

</div>
</div>

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


---

# Standard errors vs statsmodels
