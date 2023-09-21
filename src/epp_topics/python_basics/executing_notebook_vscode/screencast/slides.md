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

### Executing notebooks in vscode

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
- We want to run `exercise_2.ipynb` in vscode


---

# In action: Open file

<img src="ipynb_file.png" class="rounded" width="600"/>



---

# In action: Command palette (ctrl + shift + p)

<img src="command_select_interpreter.png" class="rounded" width="600"/>


---

# In action: Click on select another kernel

<img src="click_on_other.png" class="rounded" width="600"/>


---

# In action: Click on python environments

<img src="click_on_python_environments.png" class="rounded" width="600"/>

---

# In action: Select the epp environment

<img src="select_epp.png" class="rounded" width="600"/>

---

# Keyboard shortcuts


```txt
Ctrl+S               Save
ESC                  Change the cell mode
A                    Add a cell above
B                    Add a cell below
J or down arrow key  Change a cell to below
K or up arrow key    Change a cell to above
Ctrl+Enter           Run the currently selected cell
dd                   Delete a selected cell
z                    Undo the last change
M                    switch the cell type to Markdown
Y                    switch the cell type to code
```
