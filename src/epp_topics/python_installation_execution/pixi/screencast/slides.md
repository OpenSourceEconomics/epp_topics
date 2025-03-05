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

# Configuration


<div class="grid grid-cols-[40%_60%] gap-5">
<div>

```toml
# pyproject.toml

[tool.pixi.project]
name = "epp"
channels = ["conda-forge"]
platforms = [
  "linux-64",
  "osx-64",
  "osx-arm64",
  "win-64",
]

[tool.pixi.dependencies]
python = "~=3.13"
pandas = ">=2.2"
...

```

</div>
<div>

- Pixi is configured in the `pyproject.toml` file

- The `[tool.pixi.project]` table must specify:

  - The `name` of the project (if not given elsewhere)
  - The `channels` to use for the project
  - The `platforms` to use for the project

- The `[tool.pixi.dependencies]` table specifies the conda dependencies


</div>
</div>

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

---

# Adding dependencies


<div class="grid grid-cols-[60%_40%] gap-5">
<div>

- Via the `pyproject.toml` file

  - Add to the `[tool.pixi.dependencies]` table

  - When calling `pixi run` or `pixi install`, pixi will install the dependencies

- Via the command line

  - `pixi add [package]`

  - `pixi add [package1] [package2]`

</div>
<div>

**Version constraints**

- pandas version 2.2 or higher

  `pandas = ">=2.2"`

- pandas version 2.2.x

  `pandas = "~=2.2"`

- pandas version 2.2.0

  `pandas = "==2.2.0"`


</div>
</div>


---

# The lock file

- Upon installation of dependencies, pixi creates the `pixi.lock` file

- The lock file contains the exact versions of the dependencies that were installed

- The lock file is automatically updated when any dependency is changed

- This ensures reproducibility of the environment

- The lock file **should** be committed to the repository


---

# Environment information

- `pixi list`


---

# Adding PyPi dependencies

1. Via the `pyproject.toml` file

2. Via the command line


---

# Global installation

- pre-commit example


---

# Additional features


- Tasks

- Multiple environments

- ...
