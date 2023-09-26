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

### Executing notebooks in VS Code

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

- The entire directory `epp_project` is opened in VS Code
- We want to run `exercise_2.ipynb` in VS Code


---

# 1. Open the file

<img src="ipynb_file.png" class="rounded" width="600"/>


---

# 2. Command palette (ctrl + shift + p)

<img src="command_select_interpreter.png" class="rounded" width="600"/>


---

# 3. Click on "Select another kernel"

<img src="click_on_other.png" class="rounded" width="600"/>


---

# 4. Click on "Python environments"

<img src="click_on_python_environments.png" class="rounded" width="600"/>

---

# 5. Select the epp environment

<img src="select_epp.png" class="rounded" width="600"/>

---
class: text-xs
---

### Keyboard shortcuts

| Key combination     | Action                           |
| ------------------- | -------------------------------- |
| Ctrl+S              | Save                             |
| ESC                 | Change the cell mode             |
| A                   | Add a cell above                 |
| B                   | Add a cell below                 |
| J or down arrow key | Change a cell to below           |
| K or up arrow key   | Change a cell to above           |
| Ctrl+Enter          | Run the currently selected cell  |
| dd                  | Delete a selected cell           |
| z                   | Undo the last change             |
| M                   | switch the cell type to Markdown |
| Y                   | switch the cell type to code     |
