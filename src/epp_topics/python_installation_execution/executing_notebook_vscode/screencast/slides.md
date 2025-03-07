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

### Executing notebooks in VS Code

<br/>

Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Preparation

We assume you have:

- Installed pixi

- Installed VS Code with all relevant Python extensions

- Opened the root directory of your project in VS Code, which contains a
  `pyproject.toml` file installing the `ipykernel` package

- Ran some pixi command and picked the correct Python interpreter in VS Code (see
  previous slide deck)

---

# Example project structure

```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["example"] --- B["pyproject.toml"]
    A --- C["script.py"]
    A --- D["notebook.ipynb"]
```

<br/>

- The entire directory `example` is opened in VS Code
- We want to run `notebook.ipynb` in VS Code

---

# 1. Prerequisites: ipykernel

<img src="/0-pyproject-toml-annotated.png" class="rounded" width=600/>

---

# 2. Prerequisites: Python env picked

<img src="/1-setting-annotated.png" class="rounded" width=600/>

---

# 3. Select kernel

<img src="/2-select-kernel-annotated.png" class="rounded" width=600/>

---

# 4. Select Python environment

<img src="/3-select-kernel-python-env.png" class="rounded" width=600/>

---

# 5. Select Python environment "default"

<img src="/4-select-kernel-default-env.png" class="rounded" width=600/>

---

# 6. Run cell via shift + enter

<img src="/5-executed-cell-via-shift-enter.png" class="rounded" width=600/>

---

# Important

Whenever you come back to the project, you start directly with the last step


---
class: text-sm
---

### Keyboard shortcuts

| Key combination     | Action                                                    |
| ------------------- | --------------------------------------------------------- |
| Ctrl+S              | Save                                                      |
| ESC                 | Change the cell mode                                      |
| A                   | Add a cell above                                          |
| B                   | Add a cell below                                          |
| J or down arrow key | Change a cell to below                                    |
| K or up arrow key   | Change a cell to above                                    |
| Ctrl+Enter          | Run the currently selected cell and stay in that cell     |
| Shift+Enter         | Run the currently selected cell and move to the next cell |
| dd                  | Delete a selected cell                                    |
| z                   | Undo the last change                                      |
| M                   | switch the cell type to Markdown                          |
| Y                   | switch the cell type to code                              |
