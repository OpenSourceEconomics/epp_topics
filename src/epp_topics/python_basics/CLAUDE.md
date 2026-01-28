# Python Basics - Coding Guidelines for AI Agents

This document provides coding best practices for AI agents writing Python code, based on
the "Effective Programming Practices for Economists" course materials.

______________________________________________________________________

## Variables and Scalar Types

### DO

- Use `=` for assignment and `==` for comparison
- Use `int` for whole numbers, `float` for real numbers, `bool` for True/False
- Use `type()` to inspect variable types when debugging
- Remember that Booleans are case-sensitive: `True` and `False` (not `true`/`false`)
- Use `**` for exponentiation (not `^`)

### DON'T

- Don't compare floats for exact equality due to precision issues
  ```python
  # Bad - may fail due to floating point precision
  if 0.1 + 0.2 == 0.3:
      ...

  # Better - use approximate comparison
  import math

  if math.isclose(0.1 + 0.2, 0.3):
      ...
  ```

______________________________________________________________________

## Strings

### DO

- Use f-strings for string formatting (they are readable and powerful)
  ```python
  name = "Alice"
  age = 30
  message = f"{name} is {age} years old"
  ```
- Use single or double quotes consistently; use the other to embed quotes
  ```python
  text = 'embed "double" quotes'
  text = "embed 'single' quotes"
  ```
- Use string methods like `.lower()`, `.upper()`, `.replace()`, `.startswith()`
- Remember that indexing starts at 0 and negative indices count from the end

### DON'T

- Don't assume strings containing numbers behave like numbers
  ```python
  # This concatenates, not adds!
  "123" * 2  # Returns '123123'
  ```

______________________________________________________________________

## Lists, Tuples, and Sets

### DO

- Use **lists** `[]` for mutable, ordered sequences
- Use **tuples** `()` for immutable, ordered sequences (safer, can be dict keys)
- Use **sets** `{}` for unique items and fast membership checking
- Use `len()` to get the number of elements in any collection
- Remember: single-element tuples need a trailing comma: `(1,)`

### DON'T

- Don't use sets when you need to preserve order or allow duplicates
- Don't try to index into sets (they are unordered)
- Don't create empty sets with `{}` (that creates an empty dict)
  ```python
  # Wrong - creates empty dict
  empty = {}

  # Correct - creates empty set
  empty = set()
  ```

### Choosing the Right Container

| Use Case                         | Container     |
| -------------------------------- | ------------- |
| Need to modify elements          | list          |
| Need immutability/hashability    | tuple         |
| Need fast membership checks      | set           |
| Need unique elements             | set           |
| Need to preserve insertion order | list or tuple |

______________________________________________________________________

## Dictionaries

### DO

- Use dictionaries for label-based access (more readable than position-based)
- Use descriptive, meaningful keys
- Access nested dictionaries with chained square brackets: `d[key1][key2]`
- Use `.items()` when you need both keys and values

```python
# Good - descriptive variable name and keys
german_regions = {"North Rhine-Westphalia": 1, "Bavaria": 2}

# Accessing nested dictionaries
students = {
    "Alice": {"age": 25, "grade": "A"},
    "Bob": {"age": 23, "grade": "B"},
}
alice_age = students["Alice"]["age"]
```

### DON'T

- Don't use unhashable types (lists, sets, dicts) as dictionary keys
- Don't use generic variable names like `dictionary` or `dict1`
- Don't forget that modifying a nested dict modifies the original
  ```python
  flat = {"a": 1}
  nested = {"key": flat}
  nested["key"]["a"] = 99  # This also changes flat!
  ```

______________________________________________________________________

## For Loops

### DO

- Use for loops to avoid code repetition (DRY: Don't Repeat Yourself)
- Choose descriptive names for loop variables
- Use `.items()` to loop over dictionary key-value pairs
- Indent loop body by 4 spaces

```python
# Good - descriptive loop variable
names = ["Alice", "Bob", "Carol"]
for name in names:
    print(name.lower())

# Good - looping over dict items
scores = {"Alice": 95, "Bob": 87}
for name, score in scores.items():
    print(f"{name}: {score}")
```

### Common Loop Patterns

**Mapping loop** - transform each element:

```python
squares = []
for i in [1, 2, 3, 4, 5]:
    squares.append(i**2)
```

**Reduction loop** - aggregate to single value:

```python
numbers = [1, 2, 3]
total = 0
for n in numbers:
    total += n
```

**Filtering loop** - select elements meeting a condition:

```python
names = ["Guy", "Ray", "Tim"]
names_with_i = []
for name in names:
    if "i" in name:
        names_with_i.append(name)
```

### DON'T

- Don't avoid loops just because "loops are slow" - premature optimization is bad
- Don't use loops when a simple built-in function exists (`sum()`, `len()`, etc.)

______________________________________________________________________

## If Conditions

### DO

- Use `if`, `elif`, and `else` for control flow
- End condition lines with `:`
- Indent the body by 4 spaces
- Use `and`, `or`, `not` for complex conditions

```python
if value < 0:
    result = "negative"
elif value > 0:
    result = "positive"
else:
    result = "zero"
```

### DON'T

- Don't use `=` (assignment) when you mean `==` (comparison)
  ```text
  # WRONG - SyntaxError
  if x = 5:
      ...
  ```
  ```python
  # Correct
  if x == 5:
      ...
  ```
- Don't rely on implicit boolean conversion if it hurts readability

### Truthy/Falsy Values

- `0`, `[]`, `{}`, `""`, `()`, `set()`, `None` are falsy
- Non-zero numbers, non-empty containers are truthy

______________________________________________________________________

## Comprehensions

### DO

- Use list/dict comprehensions when they fit on one line
- Use comprehensions for simple mapping and filtering

```python
# Good - fits on one line, easy to read
squares = [x**2 for x in range(10)]

# Good - filtering comprehension
evens = [x for x in range(10) if x % 2 == 0]

# Good - dict comprehension
name_to_lower = {name: name.lower() for name in names}
```

### DON'T

- Don't use comprehensions for complex logic that requires multiple lines
- Don't expect comprehensions to solve performance problems (only ~few % faster)
- Don't sacrifice readability for brevity

```python
# Bad - too complex for a comprehension
result = [process(x) for x in data if condition1(x) and condition2(x) and condition3(x)]

# Better - use a loop for complex logic
result = []
for x in data:
    if condition1(x) and condition2(x) and condition3(x):
        result.append(process(x))
```

______________________________________________________________________

## Functions

### DO

- Name functions with `lowercase_with_underscores`
- Use keyword arguments for functions with more than one argument
- Set sensible default values for optional parameters
- Pass all variables the function needs as arguments
- Return values explicitly with `return`

```python
def utility_crra(consumption, gamma=1.5):
    """Calculate CRRA utility."""
    return consumption ** (1 - gamma) / (1 - gamma)


# Good - using keyword arguments
result = utility_crra(consumption=1.0, gamma=2.0)
```

### DON'T

- Don't rely on global variables inside functions

  ```python
  # Bad - uses global variable
  global_msg = "Hello {}!"


  def greet(name):
      print(global_msg.format(name))  # Dangerous!


  # Good - pass as argument
  def greet(name, msg="Hello {}!"):
      print(msg.format(name))
  ```

- Don't modify mutable arguments in place

  ```python
  # Bad - modifies the original list
  def append_4(some_list):
      some_list.append(4)
      return some_list


  # Good - create a copy first
  def append_4(some_list):
      result = some_list.copy()
      result.append(4)
      return result
  ```

### Why Functions Matter

- Reuse code and avoid duplication
- Structure code and reduce cognitive load
- Make code testable (pytest requires functions)
- Enable reproducibility
- Foundation for functional and object-oriented programming

______________________________________________________________________

## Importing

### DO

- Import specific items when you only need a few things
- Import entire libraries with conventional aliases
- Keep imports at the top of the file

```python
# Good - specific import
from pathlib import Path

# Good - conventional alias
import numpy as np
import pandas as pd

# Good - full library import
import math
```

### DON'T

- **Never** use `from library import *` (pollutes namespace)
  ```python
  # NEVER do this
  from numpy import *
  ```
- Don't forget which namespace a function belongs to

### Common Import Errors

- `ModuleNotFoundError`: Library not installed or typo in name
- `ImportError`: Typo in the specific function/class being imported

______________________________________________________________________

## File Paths with pathlib

### DO

- **Always** use `pathlib.Path` objects instead of strings
- Concatenate paths with `/` operator
- Start paths relative to the project root
- Use `.resolve()` for debugging to see full paths
- Use `.exists()` to verify paths

```python
from pathlib import Path

# In a .py file
root = Path(__file__).parent.parent
data_path = root / "datasets" / "data.csv"

# In a notebook
root = Path(".").resolve().parent
data_path = root / "datasets" / "data.csv"

# Debugging
print(data_path.resolve())
print(data_path.exists())
```

### DON'T

- **Never** hardcode absolute paths from your file explorer
  ```python
  # WRONG - not portable
  path = "C:\\Users\\MyName\\project\\data.csv"

  # WRONG - backslashes
  path = "datasets\data.csv"
  ```
- Don't use backslashes `\` in paths (Windows-only)
- Don't assume paths outside the project structure

### Three Rules for File Paths

1. Always use `pathlib.Path` objects instead of strings
1. Do not hardcode any parts of a path outside of the project's directory
1. Always concatenate paths with `/`

______________________________________________________________________

## Tracebacks and Error Handling

### DO

- Read tracebacks from bottom to top
- Look for three key pieces of information:
  1. What type of exception occurred
  1. Where it occurred (file and line number)
  1. What exactly happened (error message)
- Create minimal reproducible examples when asking for help

### Common Exception Types

| Exception     | Cause                             |
| ------------- | --------------------------------- |
| `ValueError`  | Invalid value passed to function  |
| `KeyError`    | Missing dictionary key or typo    |
| `TypeError`   | Wrong type (e.g., unhashable key) |
| `ImportError` | Typo in import or missing module  |
| `NameError`   | Variable not defined              |

### DON'T

- Don't ignore tracebacks
- Don't just say "it doesn't work" when asking for help
- Don't send screenshots of code (send formatted text instead)

______________________________________________________________________

## General Best Practices

### Code Style

- Use 4 spaces for indentation (not tabs)
- Use descriptive variable and function names
- Avoid generic names like `data`, `temp`, `x` (except in small scopes)

### DRY Principle

**Don't Repeat Yourself** - If you write similar code multiple times:

1. Extract it into a function
1. Use a loop
1. Use comprehensions for simple cases

### Readability Over Brevity

- Choose clear code over clever code
- Add comments for non-obvious logic
- Use meaningful names that explain intent
