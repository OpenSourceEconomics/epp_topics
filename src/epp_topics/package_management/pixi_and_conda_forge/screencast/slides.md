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
1. Pixi
1. Why we recommend conda
1. How to use Pixi


---

# Summary of Last Presentations

- `pip` and `PyPI` are the default package installer and repository for Python

- `pip` can only install Python packages

- A package may rely on non-Python dependencies, in which case

  1. the pre-compiled dependencies are bundled with the Python source in a Python Wheel (e.g., linalg libraries in NumPy)

  1. the user must install the dependencies manually (e.g., CUDA for JAX)

  1. the source code is compiled during installation

➡ non-Python dependencies cannot be shared between packages and their versions are not
guaranteed to be compatible!


---

# Conda Channels

- A channel is a repository of packages (just like PyPI)

- Besides Python, many languages are supported (e.g., R, C++, Fortran, and more)

  ➡ non-Python dependencies can be shared between packages, and a dependency solver can
  ensure version compatibility

- There are many channels:

  - `defaults`: The default channel supported by Anaconda, Inc. (do not use!)

  - `conda-forge`: A community-driven channel with many packages (recommended)

  - `nvidia`: A channel for NVIDIA related packages

  - and many others...



---

# Pixi


- A package, dependency, and environment manager

- Can install packages from any conda channel (and from PyPI)
- A unified way to install packages and manage separate environments
- A modern alternative to the conda package manager (or mamba)

- It goes beyond pip by
  1. Being an environment manager (pip folks require venv or alternatives for this)
  1. Using a robust dependency solver for consistent, conflict-free installations



---

# Differences to pip and PyPI

- Conda can manage non-Python dependencies (e.g., compilers, system libraries)

- Conda channel (e.g., conda-forge) provide pre-compiled binaries

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
