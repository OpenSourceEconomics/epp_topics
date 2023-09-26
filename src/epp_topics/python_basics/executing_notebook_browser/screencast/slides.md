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

<br/>

# Basic Python

### Executing notebooks in a browser

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---


# Preparation

- We assume you have installed anaconda and created the course environment
- Open a shell in the root directory of your project
    - On Windows, use the anaconda prompt or the powershell
    - If conda is not recognized in the powershell, check out this [stackoverflow
      post](https://stackoverflow.com/a/65160772/21900143)
- Activate the environment using `conda activate epp`
- Confirm the activation worked using `conda info`
---

# 0. Activate and Info

<img src="activate_and_info.png" class="rounded" width="600"/>

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

- Our shell is in the `epp_project` directory
- We want to run `exercise_2.ipynb` in the browser
- Command is `jupyter notebook`


---

# 1. Start Notebook

<img src="blocked_terminal.png" class="rounded" width="600"/>


---

# 2. Landing Page

<img src="starting_page.png" class="rounded" width="600"/>


---

# 3. Click on Folder

<img src="folder.png" class="rounded" width="600"/>


---

# 4. Work in the Notebook

<img src="notebook.png" class="rounded" width="600"/>
