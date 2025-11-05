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
title: EPP — Executing ".py"-files from VS Code
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Basic Python

### Executing ".py"-files from VS Code

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# Preparation

We assume you have:

- Installed pixi

- Installed VS Code with all relevant Python extensions

- Opened the root directory of your project in VS Code, which contains a
  `pyproject.toml` file

---

# Example project structure


```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["example"] --- B["pyproject.toml"]
    A --- C["script.py"]
```

<br/>

- We want to run `script.py` in VS Code


---

# 1. Open the file

<img src="/0-py_file.png" class="rounded" width="600"/>


---

# 2. Command palette (ctrl + shift + p)

Create a new terminal

<img src="/1-create_new_terminal.png" class="rounded" width="600"/>

---

# 3. Type `pixi run python script.py`

<img src="/2-type_pixi_run_python_script_py.png" class="rounded" width="600"/>

---

# 4. .pixi folder with Python exists now

<img src="/3-executed_pixi_run_python_script_py-annotated.png" class="rounded" width="600"/>

---

# 5. Hard way I: Select Interpreter

Again via command palette (ctrl + shift + p)

<img src="/4-python_select_interpreter.png" class="rounded" width="600"/>

---

# 6. Hard way II: Pick "Enter ... path"

<img src="/5-enter_interpreter_path.png" class="rounded" width="600"/>

---

# 6. Hard way III: Pick "Find..."

<img src="/6-browse.png" class="rounded" width="600"/>

---

# 7. Hard way IV: Pick the right one

Located in `.pixi/envs/default/bin/python[version]`

<img src="/7-pick-the-right-one.png" class="rounded" width="600"/>

---

# 8. Easier: Close and reopen VS Code

<img src="/8-easier-close-reopen-vscode.png" class="rounded" width="600"/>

---

# 9. Finally: Run the file

<img src="/9-clicked-run-annotated.png" class="rounded" width="600"/>


---

# Important

Whenever you come back to the project, you start directly with the last step
