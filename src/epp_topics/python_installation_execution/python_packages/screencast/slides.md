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
title: EPP — Python Installation — Python Packages
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Package Management

### Python Packages

<br/>


---

# Contents


1. How do I create a Python package?
1. How do I install and run my package?
1. What does the `__pycache__` folder do?
1. What does the `-e` in `pip install -e ...` do?
1. When can I do
   ```python
   from package import Variable
   ```
   instead of
   ```python
   from package.module import Variable
   ```
1. Why do we sometimes write
   ```python
   if __name__ == "__main__":
      ...
   ```


---

# How to create a Python package?

<div class="grid grid-cols-2 gap-15">

<div>
<b>Directory structure</b>

```console
package/
├── src/
│   └── package/
│       ├── __init__.py
│       ├── module1.py
│       └── subpackage/
│           ├── __init__.py
│           └── module2.py
└── pyproject.toml
```
</div>

<div v-click>
<b>Meta Information</b>

```toml
# pyproject.toml
[project]
dependencies = ["numpy>=2"]
name = "package"
requires-python = ">= 3.11"
version = "0.1.0"

[[project.authors]]
name = "Tim Mensinger"
email = "mensingertim@gmail.com"

[build-system]
build-backend = "hatchling.build"
requires = ["hatchling"]
```
</div>

</div>

---

# Example

---

# How do we install and run our package?

<div class="grid grid-cols-2 gap-15">

<div>
<b>Install</b>

```console
$ pip install /path/to/package
```

<br>

- Copies the package content's and the package metadata to the `"site-packages"`
  directory of the current environment

</div>

<div v-click>
<b>Run</b>

```python
from package.module1 import Variable1
from package.subpackage.module2 import Variable2
...
```
</div>

</div>

---

# Example


---

# What does the pycache folder do?

> "To speed up loading modules, Python caches the compiled version of each module in the
   `__pycache__` directory under the name module.version.pyc, where the version encodes
   the format of the compiled file; it generally contains the Python version number."

<br>

> "A program doesn’t run any faster when it is read from a .pyc file than when it is read
  from a .py file; the only thing that’s faster about .pyc files is the speed with which
  they are loaded."

[---Python docs: 6.1.3. “Compiled” Python files](https://docs.python.org/3/tutorial/modules.html#compiled-python-files)


---

- There is no single Python "compiler"

  - Default, [**CPython**](https://github.com/python/cpython): Fast compilation to
    bytecode, which is then executed by "virtual machines" (aka interpreters)

- Other "compilers" exist and come with different trade-offs:
  - [**Jython**](https://www.jython.org/): Translates Python code into Java bytecode,
    allowing it to run on the Java Virtual Machine and interact with Java code

  - [**PyPy**](https://pypy.org/): A Python interpreter and just-in-time compiler that
    can be faster than CPython for some workloads

  - [**Cython**](https://cython.org/): A static compiler that translates Python code
    into C code

  - [**Numba**](https://numba.pydata.org/): A just-in-time compiler that translates
    Python code into machine code using the [LLVM](https://llvm.org/) compiler
    infrastructure

  - [**XLA**](https://openxla.org/xla): A domain-specific compiler for linear algebra
    that can be used with machine learning frameworks like JAX or PyTorch

  - ...


---

# Editable installs

<div class="grid grid-cols-2 gap-15">

<div>

Want to update `Variable1` to

```python
Variable1 = "The first variable (updated)"
```

➡ Example

<div v-click>
<b>Command</b>

```console
$ pip install --help
...
-e, --editable <path/url>
  Install a project in editable mode (i.e.
  setuptools "develop mode") from a local project
  path or a VCS url.
...
```
</div>
</div>

<div v-click>
<b>Internally</b>

- **Regular install**

  `pip` copies [the package contents]() to `"site-packages"`

  This is also what happens when installing from GitHub, PyPI, etc.

- **Editable install** (with `--editable`)

  `pip` copies [the path to the package]() to `"site-packages"`

</div>

</div>


---

# Importing from packages

<div class="grid grid-cols-2 gap-15">


<div>
<b>Before</b>

```python
from package.module1 import Variable1
from package.subpackage.module2 import Variable2
...
```
</div>

<div v-click>
<b>We want</b>
```python
from package import Variable1
from package import Variable2
...
```
</div>

</div>


---

# Example



---

# If name equals main

<div class="grid grid-cols-2 gap-15">


<div>

```python
# module1.py
Variable1 = "The first variable"

print("This is module1.py")

```
</div>

<div v-click>

```python
# module1.py
Variable1 = "The first variable"

if __name__ == "__main__":
  print("This is module1.py")
```
</div>

</div>


---

# Additional References

- [Python Packages (Beuzen & Timbers, 2023)](https://py-pkgs.org/welcome)
