---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
selectable: true
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

# Pixi, conda, and conda-forge

<br/>


---

# Overview

1. Summary of last talk
   <br>*(only for jour fixe not epp)*
1. Conda channels
1. What is Pixi?
1. Differences to pip and PyPI / Example
1. How to use Pixi?


---

# Summary of last talk

- `pip` and `PyPI` are the default package installer and repository for Python

<div v-click>

- `pip` can only install Python packages

</div>

<div v-click>

- A package may rely on non-Python dependencies, in which case

  1. the pre-compiled dependencies are bundled with the Python source in a Python Wheel (e.g., linalg libraries in NumPy)

  1. the user must install the dependencies manually (e.g., CUDA for JAX)

  1. (the source code is compiled during installation)

</div>

<div v-click>

➡ Non-Python dependencies cannot be shared between packages (memory issues)

</div>

<div v-click>

➡ Their versions are not guaranteed to be compatible (conflicts)

</div>

<div v-click>

➡ Cannot assure reproducibility (environment depends on the user's system)

</div>


---

# Conda Channels


- A channel is a repository of packages (just like PyPI)

<div v-click>

- Besides Python, many languages are supported (e.g., R, C++, Fortran, and more)

</div>

  <div v-click>

  ➡ Non-Python dependencies can be shared between packages

  </div>

  <div v-click>

  ➡ Dependency solver can ensure version compatibility

  </div>

  <div v-click>

  ➡ Environment does not need to rely on the user's system

  </div>

<div v-click>

- There are many channels:

  - `defaults`: The default channel supported by Anaconda, Inc. (do not use!)

  - `conda-forge`: A community-driven channel with many packages (recommended)

  - `nvidia`: A channel for NVIDIA related packages

  - and many others...

</div>


---

# Pixi


- A package, dependency, and environment manager for _conda packages_

<div v-click>

- A modern alternative to the conda package manager (or mamba)

</div>

<div v-click>

- Can install packages from any conda channel (and from PyPI)

</div>

<div v-click>

- A unified way to install packages and manage separate environments

</div>

<div v-click>

- It goes beyond pip by

  1. Being an environment manager (pip folks require venv or alternatives for this)
  1. Using a robust dependency solver for consistent, conflict-free installations

     _Note: conda vs. mamba vs. pixi_

</div>


---

# Differences to pip and PyPI


- Conda channels can contain non-Python libraries, PyPI does not

- Pixi (or conda/mamba) can install from conda channels and PyPI

<div v-click>

**Implications:**

- Fewer dependency conflicts
- Better reproducibility (environment is not system-dependent)
- Easier installation (e.g., CUDA toolkit can be installed via pixi)

</div>


---

# Example

Let's look at the packages in the environment when we

1. `pip install numpy`

1. `pixi add numpy`

   _(or `conda/mamba install numpy`)_


---

# How to use Pixi?

1. [Transitioning from conda to pixi](https://pixi.sh/dev/switching_from/conda/)

1. [Config file](https://pixi.sh/dev/advanced/pyproject_toml/)

1. Pixi's lock file

1. [Basic Usage](https://pixi.sh/dev/basic_usage/)

1. A "realistic" example

---

# Transitioning from conda to pixi

```console
$ pixi init --import environment.yml
```

---

# Config file

- Do not use pixi's custom `pixi.toml` config

- Instead, use the `pyproject.toml` file

However, from the docs:

> "We don't advise to use the pyproject.toml file for anything else than python
> projects, the pixi.toml is better suited for other types of projects."


---

# Pixi's lock file

- Why? From the docs:
  > - To save a working installation state, without copying the entire environment's data.
  > - To ensure the project configuration is aligned with the installed environment.
  > - To give the user a file that contains all the information about the environment.

- The lockfile is updated when you install/remove packages or change the config file

- `pixi --version` must be greater or equal to the lock file version (backward comp.)

- Running commands using the lock file:

  ```console
  $ pixi run --frozen python script.py
  ```


---

# Basic Usage (running scripts)

- Start from scratch

  ```console
  $ pixi init --format pyproject
  ```

- Install a package

  ```console
  $ pixi add numpy
  ```

- Create scripts

  ```python
  # script.py
  import numpy as np
  print(f"NumPy version: {np.__version__}")
  ```

- Run the script

  ```console
  $ pixi run python script.py
  ```


---

# Basic Usage (pixi shell)

- Start a shell (in the correct directory)

  ```console
  $ pixi shell
  ```

- Run the script

  ```console
  $ python script.py
  ```

- Exit the shell

  ```console
  $ exit
  ```

- **Discussion**: When to use this?

  - With `pixi run ...` you can never forget to activate the correct environment
  - With `pixi shell` you can easily change directories and run scripts from the wrong
    environment


---

# Basic Usage (tasks)

- Create a task

  ```toml
  # pyproject.toml
  [tool.pixi.tasks]
  task-name = "python script.py"
  ```

- Run the task

  ```console
  $ pixi run task-name
  ```

---

# Basic Usage (global installations)

- Some executables / packages should be available globally on your system

- Install, for example `vim`, globally

  ```console
  $ pixi global install vim
  ```

- Verify installation location

  ```console
  $ which vim
  ```

- Uninstall

  ```console
  $ pixi global uninstall vim
  ```


---

# A "realistic" example

- We want to create a single environment:

  - Using Python 3.13

  - Which supports an editable install of the project
  - That runs on Windows, MacOS (intel and arm), and Linux
  - With pandas, plotly, kaleido


---

# Step 1

- Create a new environment

  ```console
  $ pixi init --format pyproject
  ```

- Add Python 3.13

  ```console
  $ pixi add python=3.13
  ```

---

# Step 2

- Specify operating systems

  ```toml
  # pyproject.toml
  [tool.pixi.project]
  platforms = ["win-64", "osx-64", "osx-arm64", "linux-64"]
  ```

---

# Step 3

- Add conda-forge packages

  ```console
  $ pixi add pandas plotly python-kaleido
  ```

- Install Chrome

  ```console
  pixi run plotly_get_chrome
  ```

---

# Step 4 (verify)

- Create a plotting script

  ```python
  # plot.py
  import pandas as pd

  data = pd.DataFrame({
      "x": [1, 2, 3, 4],
      "y": [10, 15, 13, 17]
  })

  fig = data.plot.scatter(x="x", y="y", backend="plotly")
  fig.write_image("scatter.png")
  ```

- Run the script

  ```console
  $ pixi run python /path/to/plot.py
  ```

---

# Next time

- Multi-channel installations

- Installing ML libraries with GPU support

- Multi-environments

- Advanced tasks

- GitHub Actions

- Best practices

<br/>

**Send me questions and complicated use-cases!**


<!--

# Installing JAX with CUDA support

- We want to install JAX and CUDA such that we can compute on the GPU

- When working with an NVIDIA GPU, we need to install the CUDA toolkit

- For modern Macs with M-chips, we need the experimental [Metal plug-in](https://developer.apple.com/metal/jax/)

  _(We will not do this today)_

-->
