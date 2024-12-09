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
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Package Management

### Pip and PyPI

<br/>


---

# Contents

1. Package installer for Python (pip)

1. The Python Package Index (PyPI)

1. Non-pure (binary) packages

1. Some consequences

---

# Package installer for Python (pip)

<div v-click>

- The de-facto default installer outside of scientific Python

</div>

<div v-click>

- Has all standard commands to install, uninstall, and manage packages

</div>

<div v-click>

- Can install from:
  - Local directories (we have seen that)
  - Version control systems (e.g., GitHub, GitLab, etc.)
  - URLs (e.g., from a website)
  - ***PyPI (The official Python Package Index)***
  - Private package indexes

</div>


---

# The Python Package Index (PyPI)

- Central hub for Python packages:

  Example: https://pypi.org/project/optimagic/

- Contains

  - Package metadata
  - Package source code (Source Distribution)
  - Wheels (Built distributions)

- Contains only Python packages!

---

# Example

---

# Non-pure (binary) packages

- Before: pure Python package (e.g., optimagic)

<div v-click>

- What about packages that rely on code from other languages (e.g., C, C++)?
	- This code needs to be compiled before execution
  - Examples: NumPy, SciPy, pandas, JAX, PyTorch, etc.

</div>

<div v-click>

- Usually: Pre-compile these parts for most relevant platforms (add to Wheels file)

</div>

<div v-click>

- `pip install numpy`:
  - Installs NumPy's plain Python source code as well as the pre-compiled parts, and all
    of NumPy's dependencies (and their dependencies...)
  - If no pre-compiled parts are available (e.g., you use a non-standard platform),
    `pip` will download the complete source code and tries to compile the relevant code
    (this, however, requires build tools to be available ---for example, a C++ compiler)

</div>


---

# Example

---

# Some Consequences

<div v-click>

- Libraries that rely on compiled code need to add pre-compiled binaries to their
  packages

</div>

<div v-click>

- There is no way to share pre-compiled binaries across packages

  - No problem if that code is written specifically for your package

  - Annoying if you rely on another package that is written in another language

</div>

<div v-click>

- Sometimes programs require additional libraries to be installed on the system because
  it would be too complicated to include them in the package wheel
  
  Example: cuda tools for PyTorch, JAX, etc.

</div>

<div v-click>

- ***Next week we will see how conda and conda-forge solve this problem! (+pixi)***

</div>


---

# Additional References

- [Python Packages (Beuzen & Timbers, 2023)](https://py-pkgs.org/welcome)