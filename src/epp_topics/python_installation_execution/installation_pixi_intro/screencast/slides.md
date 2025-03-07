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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Python Installation and Execution

### Introduction to Pixi

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# What is pixi?

- When using programs like Stata or Matlab you often only have a single version of the
  program installed

  → Problematic when different projects require different versions of the program

- We want an independent environment for each project

  → Pixi allows you to create and manage per-project environments


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

- The environment is automatically installed when `pixi run` is called

- Any command that relies on the environment **must be** prefixed with `pixi run`:

  - `python script.py` → `pixi run python script.py`

  - `pytest` → `pixi run pytest`

  - ...

</div>
</div>
