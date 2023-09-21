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
---

### Effective Programming Practices for Economists

<br>

# Basic Python

### File paths with pathlib

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Topics

- How to get a path to the current directory
- Working with pathlib `Path`s
- Rules for working with file paths


---

# Motivation

- There are many ways to work with file paths in Python
- Some are not portable
- We want to give you one way that is guaranteed to work!

---

# An example

- Consider the following directory structure

```bash
epp_project/
  exercises/
    exercise_1.py
    exercise_2.ipynb

  datasets/
    data.csv
```

- `epp_project`, `exercises` and `datasets` are directories
- `exercise_1.py`, `exercise_2.ipynb` and `data.csv` are files
- Want to load `data.csv` in two different scenarios:
  - from `exercise_1.py`
  - from `exercise_2.ipynb`


---

# How not to do it


```python
# don't do this!
import pandas as pd
path = `"C:\Users\MyName\Documents\epp_projects\datasets\data.csv"`
data = pd.read_csv(path)
```

- This only works on one Computer
- Backslashes (`\`) only work on windows
- Warning: This is what you get when you copy a path from your file explorer

---

# Goal

- Start paths relative to the root folder of the project
- Only make assumptions about directory structure inside the project
- Define the path in a way that is portable across operating systems



---

# Get a path to the project root: In a notebook

<div class="grid grid-cols-2 gap-4">
<div>

The following is in `exercise_2.ipynb`

```python
from pathlib import Path

# get a path to the current directory
this_dir = Path()
print(this_dir)

# make it absolute for readability
this_dir = this_file.resolve()
print(this_file)

# move up to epp_project/
root = this_file.parent
print(root)
```

```txt
---
.
/home/janos/Dropbox/epp_project/exercises
/home/janos/Dropbox/epp_project
```

</div>
<div>

- `Path()` gives a relative path to current directory
- `resolve` makes it absolute for readability
- `.parent` moves up one file/directory
- The output differs on every computer!
- No assumptions made on usernames or folders outside the project

</div>
</div>


---

# Get a path to the project root: In a `.py` file

<div class="grid grid-cols-2 gap-4">
<div>

The following is in `exercise_1.py`

```python
from pathlib import Path

# get a path to the current file
this_file = Path(__file__)
print(this_file)

# move up to epp_project/
root = this_file.parent.parent
print(root)
```
```txt
---

/home/janos/Dropbox/epp_project/exercises
/home/janos/Dropbox/epp_project

```

</div>
<div>

- In a `.py` file `Path()` would lead us to the current directory of the shell from which the file was executed
- The `__file__` variable is a magic variable with the path to the current file
- Have to use `.parent` twice!

</div>
</div>


---

# From the project root to the data file

<div class="grid grid-cols-2 gap-4">
<div>


```python
from pathlib import Path
# redo the .py file version in one line
root = Path(__file__).parent.parent
print(root)

# go to data file
data_path = root / "datasets" / "data.csv"
print(data_path)
print(data_path.exists())
```
```txt
---
/home/janos/Dropbox/epp_project
/home/janos/Dropbox/epp_project/datasets/data.csv
True

```

</div>
<div>

- Once `root` is defined, the rest works the same in notebooks and `.py` files
- Different path snippets are defined using `/`
- Resulting path works on all platforms!


</div>
</div>


---

# Debugging tips




- Use `path.resolve` to get full information about your path
- Use `list(path.iterdir())` to list all files in your current directory
- Build up paths one folder at a time and use `path.exists()` to catch typos


---

# File path rules

  1. Always use pathlib Paths instead of strings
  2. Do not hardcode Paths outside of shared folders
  3. Always concatenate paths with `/`


**Remember**: If you copy paste a path from your windows file explorer, all three rules are violated!
