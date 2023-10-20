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
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Executing ".py"-files from VS Code

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Preparation

We assume you have:
- Installed anaconda and created the course environment
- Installed VS Code with all relevant Python extensions
- Opened the root directory of your project in VS Code

---

# Example project structure


```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["epp_project"] --- B["exercises"]
    B["exercises"] --- C["exercise_1.ipynb"]
    B["exercises"] --- D["exercise_2.py"]
    A["epp_project"] --- E["datasets"]
    E["datasets"] --- F["data.csv"]
```

<br/>

- We want to run `exercise_1.py` in VS Code


---

# 1. Open the file

<img src="py_file.png" class="rounded" width="600"/>


---

# 2. Command palette (ctrl + shift + p)

<img src="command_select_interpreter.png" class="rounded" width="600"/>


---

# 3. Select the epp environment

<img src="selecting_epp_env.png" class="rounded" width="600"/>


---

# 4. Run the file

<img src="click_run.png" class="rounded" width="600"/>
