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

# Non-pure (binary) packages

- Before: pure Python package (e.g., optimagic)

<div v-click>

- What about packages that rely on code from other languages (e.g., C, C++)?

	- For compiled languages the code requires compilation before execution
  - Examples: NumPy, SciPy, pandas, JAX, PyTorch, etc.

</div>

<div v-click>

- Usually: Pre-compile these parts for most relevant platforms

  - Combine pre-compiled parts with plain Python source in a _"wheel"_

  - Example: `pip install numpy`

</div>



---

# Running `pip install numpy`

_(Ignoring dependencies for now.)_

- If wheels are available for your platform, `pip` downloads the wheel and install
  it.
  - Plain Python source code and pre-compiled parts installed
  - Example: [
numpy-2.2.0-cp313-cp313-musllinux_1_2_x86_64.whl](https://files.pythonhosted.org/packages/5a/3d/d20d24ee313992f0b7e7b9d9eef642d9b545d39d5b91c4a2cc8c98776328/numpy-2.2.0-cp313-cp313-musllinux_1_2_x86_64.whl)

- If no wheels are available for your platform, `pip` downloads the source and tries
  to compile the relevant code
  - Requires build tools to be available (e.g., a C++ compiler)
  - Example: [
numpy-2.2.0.tar.gz](https://files.pythonhosted.org/packages/47/1b/1d565e0f6e156e1522ab564176b8b29d71e13d8caf003a08768df3d5cec5/numpy-2.2.0.tar.gz)

---

# Some Consequences

<div v-click>

- Libraries that rely on compiled code need to add pre-compiled binaries to their
  packages

</div>

<div v-click>

- There is no way to share pre-compiled binaries across packages

  - No problem if that code is written specifically for your package

  - Problematic if not (memory, versions)

</div>

<div v-click>

- Sometimes programs require additional libraries to be installed on the system because
  it would be too complicated to include them in the package wheel

  Example: CUDA toolkit for JAX, PyTorch, etc.

</div>

<div v-click>

- ***[Next session: How do conda and conda-forge solve this problem!]()***

</div>


---

# Additional References

- [Python Packages (Beuzen & Timbers, 2023)](https://py-pkgs.org/welcome)
