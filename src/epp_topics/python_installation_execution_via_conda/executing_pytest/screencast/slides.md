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
title: EPP — Python Installation (conda) — Running Python code via pytest
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Running Python code via pytest

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

<img src="/activate_and_info.png" class="rounded" width="600"/>

---

# How does pytest execute code?

- Executing .py files: Run the entire file
- Executing notebooks: Run individual cells
- Pytest: Run individual functions in multiple .py files

Very useful for automating test execution across an entire project

---

# Example Project Structure


```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["example"] --- B["cobb_douglas.py"]
    A["example"] --- C["test_cobb_douglas.py"]
```

<br/>

- Our shell is in the `example` directory
- We want to run all functions that start with `test_` in `test_cobb_douglas.py`
- Could be spread across multiple test files, across different subdirectories
- Command is `pytest`


---

# 1: Execute

<img src="/run.png" class="rounded" width="600"/>
