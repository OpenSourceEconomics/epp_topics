---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: Effective Programming Practices for Economists
defaults:
  layout: center
themeConfig:
  paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br>

# Basic Python

### Importing, Modules, Namespaces

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Contents

- What are libraries?
- Different ways to import libraries or parts of libraries
- Namespaces
- Modules
- Typical errors when importing


---

# Third party libraries

- Python is a general purpose programming language
- The base language you have seen so far is extended by labraries
  - Standard library (e.g. pathlib, functools)
  - Third party libraries (e.g. numpy, pandas, scipy)
- Libraries need to be imported to use them
- Third party libraries need to be installed


---

# The example

- We will use the numpy library as example
- Numpy is a library that provides efficient data structures and functions for working with matrices and higher dimensional arrays
- You can watch the numpy screencast for details but otherwise just ignore the numpy specific details for now


---

# Different ways to import

<div class="grid grid-cols-2 gap-4">
<div>

Import one function / object
```python
from numpy import array
```
Import an entire library
```python
import numpy
```
Import entire library and rename it
```python
import numpy as np
```
Import everything from a library
```python
from numpy import *
```

</div>
<div>

- Use single import if you need one thing
- Use library import if you need many functions
- Use shorthand if there is a convention, e.g. numpy (np), pandas (pd), seaborn (sns)
- Never ever use `import *`

</div>
</div>

---

# Namespaces or why not use `import *`


<div class="grid grid-cols-2 gap-4">
<div>

```python
# bad option
>>> from math import log
>>> log(2.718281828459045)
1.0

# better option
>>> import math
>>> math.log(2.718281828459045)
1.0
```

</div>
<div>

- Multiple libraries could implement `log`
  - math library: The natural logarithm
  - web development library: Write a log file
- Importing an entire library makes it very explicit from which namespace you use a function
- Namespaces are one of the reasons why Python can succeed in so many different areas!

</div>
</div>



---

# Modules

- So far we imported from packages or the standad library
- You can import from any module (a module is a `.py` file)
- In larger projects you will split code across multiple modules and import from them


---

# ModuleNotFoundError

```python
>>> from numpai import array
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[32], line 1
----> 1 from nampai import array

ModuleNotFoundError: No module named 'nampai'
```

- Meaning: The library you asked for is not found
- Do you have a typo in the library name?
- Is the library installed in your environment?
- **Is the correct environment activated?**


---

# ImportError

```python
from numpy import arrrrray
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
Cell In[33], line 1
----> 1 from numpy import arrrrray

ImportError: cannot import name 'arrrrray' from 'numpy' (/home/janos/miniconda3/
envs/dl_intro/lib/python3.11/site-packages/numpy/__init__.py)
```

- Something went wrong during import
- Do you have typos in what you want to import?
- Is the correct version of the library installed?
