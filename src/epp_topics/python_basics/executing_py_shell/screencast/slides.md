---
theme: academic
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

# Basic Python

### Executing `.py` files from the shell

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Preparation

- We assume you have installed anaconda and created the course environment
- Open a shell in the root directory of your project
    - On Windows, use the anaconda prompt or the powershell
    - If conda is not recognized in the powershell, check out this [stackoverflow post](https://stackoverflow.com/a/65160772/21900143)
- Activate the environment using `conda activate epp`
- Confirm the activation worked using `conda info`

---

# Example project structure


```bash
epp_project/
  exercises/
    exercise_1.py
    exercise_2.ipynb

  datasets/
    data.csv
```

- Our shell is in the `epp_project` directory
- We want to run `exercise_1.py`
- Command is `python exercises/exercise_1.py`


---

# In action: activate and info

<img src="activate_and_info.png" class="rounded" width="600"/>

---

# In action: execute


<img src="run.png" class="rounded" width="600"/>