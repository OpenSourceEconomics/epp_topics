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

# Pixi, conda, and conda-forge

<br/>


---

# Contents

1. Summary of last presentations
   <br>*(only for jour fixe not epp)*
1. Conda channels
1. Pixi and Conda
1. Why we recommend conda
1. How to use Pixi


---

# Summary of Last Presentations

- `pip` and `PyPI` are the default package installer and repository for Python

- `pip` can only install Python packages

- A package may rely on non-Python dependencies, in which case

  - the pre-compiled dependencies are bundled with the Python source in a Python Wheel (e.g., linalg libraries in NumPy)

  - the user must install the dependencies manually (e.g., CUDA for JAX)

  - the source code is compiled during installation

➡ non-Python dependencies cannot be shared between packages and their versions are not
guaranteed to be compatible!


---

# Conda Channels

- A channel is a repository of packages (just like PyPI)

- Besides Python many languages can be supported (e.g., R, C++, Fortran, and more)

- There are many channels:

  - `defaults`: The default channel supported by Anaconda, Inc. (do not use!)

  - `conda-forge`: A community-driven channel with many packages (recommended)

  - `bioconda`: A channel for bioinformatics packages


---

# Pixi and Conda


- A package, dependency, and environment manager

- Can install all packages
- A unified way to install packages and manage separate environments


---

# The Anaconda Distribution

- A curated collection of packages maintained by Anaconda, Inc.

- Distributed with conda, Python, and many scientific libraries
- Often used in data science to quickly get a working setup


---

# The conda-forge Channel

- A community-driven collection of recipes for building packages

- Maintains a wide variety of packages and up-to-date versions
- Compatible with Anaconda and other conda installations


---

# Differences to pip and PyPI

- Conda can manage non-Python dependencies (e.g., compilers, system libraries)

- Conda-forge provides pre-compiled binaries for multiple platforms

- pip relies solely on Python wheels or source code from PyPI


---

# Example

Let's look at the packages in the environment when we

1. `pip install numpy`

1. `conda install numpy`


---

# Why This Matters

- Easier environment management: Reproducibility, isolation, and fewer conflicts

- Pre-compiled binaries: Faster, more reliable installations
- Community contributions: Quick updates and broader package availability


---

# Additional References

- [Conda Documentation](https://docs.conda.io/en/latest/)
- [Anaconda Documentation](https://docs.anaconda.com/)
- [conda-forge Docs](https://conda-forge.org/)
- [Python Packages (Beuzen & Timbers, 2023)](https://py-pkgs.org/welcome)
