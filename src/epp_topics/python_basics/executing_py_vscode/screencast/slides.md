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
themeConfig:
  paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br>

# Basic Python

### Executing `.py` files from vscode

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Preparation

- We assume you have:
  - Installed anaconda and created the course environment
  - Installed vscode with all relevant Python extensions
- Open the root directory of your project in vscode

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
- We want to run `exercise_1.py` in vscode


---

# In action: Open file

<img src="py_file.png" class="rounded" width="600"/>



---

# In action: Command palette (ctrl + shift + p)

<img src="command_select_interpreter.png" class="rounded" width="600"/>




---

# In action: Select the epp environment

<img src="selecting_epp_env.png" class="rounded" width="600"/>


---

# In action: Run the file

<img src="click_run.png" class="rounded" width="600"/>
