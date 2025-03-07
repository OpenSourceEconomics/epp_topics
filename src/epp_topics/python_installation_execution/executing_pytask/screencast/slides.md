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
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Running Python code via pytask

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Preparation

We assume you have:

- Installed pixi

- Navigated to the root directory of your project in a shell

- Opened the root directory of your project in VS Code, which contains a
  `pyproject.toml` file that includes pytask

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
- Command is `pixi run pytask`


---

# 1: Execute

<img src="/run_1.png" class="rounded" width="600"/>


---

# 1: Execute again

<img src="/run_2.png" class="rounded" width="600"/>
