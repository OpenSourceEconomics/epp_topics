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
title: Effective Programming Practices for Economists
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Running Python code via pytask

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Preparation

- We assume you have installed anaconda and created the course environment
- Open a shell in the root directory of your project
    - On Windows, use the anaconda prompt or the powershell
    - If conda is not recognized in the powershell, check out this
      [stackoverflow post](https://stackoverflow.com/a/65160772/21900143)
- Activate the environment using `conda activate epp`
- Confirm the activation worked using `conda info`


---

# 0: Activate and Info

<img src="activate_and_info.png" class="rounded" width="600"/>

---

# How does pytask execute code?

- Executing .py files: Run the entire file
- Executing notebooks: Run individual cells
- Pytask: Run individual functions in multiple .py files

Very useful for automating research pipelines

---

# Example Project Structure


```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["example"] --- B["task_hello.py"]
    A["example"] --- C["task_world.py"]
```

<br/>

- Our shell is in the `example` directory
- We want to run all functions that start with `task_` in both `.py` files
- Command is `pytask`


---

# 1: Execute

<img src="run_1.png" class="rounded" width="600"/>


---

# 1: Execute again

<img src="run_2.png" class="rounded" width="600"/>
