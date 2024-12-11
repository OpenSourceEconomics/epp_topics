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

# Conda, Anaconda, and conda-forge

<br/>


---

# Contents

1. What is conda?
1. The Anaconda distribution
1. The conda-forge channel
1. Differences to pip and PyPI
1. Why this matters for managing environments


---

# What is conda?

- A package, dependency, and environment manager  

- Works for Python and other languages  
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
