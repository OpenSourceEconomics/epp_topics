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
title: EPP — Python Installation — Installation and introduction to Pixi
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Python Installation and Execution

### Installation and introduction to Pixi

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# What is pixi?

- When using programs like Stata or Matlab you typically have single version of the
  program installed

  → Problematic when different projects require different versions of the program

  → Worse when depending on custom extensions / libraries

- We want an independent environment for each project

  → Pixi allows you to create and manage per-project environments


---

# Installation

- In your terminal of choice, execute a tiny shell script found here:

  https://pixi.sh/latest/#installation

- Re-start your terminal

- If you have any issues, reach out on the course Zulip!


---

# Using pixi

<div class="grid grid-cols-[40%_60%] gap-5">
<div>

<br>

```console
$ cd path/to/project
$ ls
script.py
pyproject.toml
```

<br>


```py
# script.py

print("Hello, world!")
```

<br>


```console
$ pixi run python script.py
Hello, world!
```

</div>
<div>

- There is no need to install or activate the pixi environment manually!

- The environment is automatically installed/updated when `pixi run` is called

- Any command that relies on the environment **must be** prefixed with `pixi run`:

  - `python script.py` → `pixi run python script.py`

  - `pytest` → `pixi run pytest`

  - ...

</div>
</div>
