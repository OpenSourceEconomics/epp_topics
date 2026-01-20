---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Type Hints in Python
drawings:
  persist: false
transition: fade
title: Type Hints Introduction
defaults:
  layout: default
---

# Why Type Hints?

### Making Python Code Safer and More Maintainable

<br/>

Effective Programming Practices for Economists

---

# Python is Dynamically Typed

<br/>

```python
def add(a, b):
    return a + b

add(1, 2)        # Returns 3
add("hello", " world")  # Returns "hello world"
add([1, 2], [3, 4])     # Returns [1, 2, 3, 4]
```

<br/>

### Flexibility is great, but...

- What types does `add` actually expect?
- Will it work with my data?
- What does it return?

---

# The Problem with Dynamic Typing

<br/>

```python
def calculate_portfolio_return(prices, weights):
    # What are prices and weights?
    # Lists? NumPy arrays? DataFrames? Dicts?
    return sum(p * w for p, w in zip(prices, weights))
```

<br/>

### Questions your IDE can't answer:

- Does `prices` need to be the same length as `weights`?
- Can I pass a pandas Series?
- What if I accidentally swap the arguments?

---

# Type Hints to the Rescue

<br/>

```python
def calculate_portfolio_return(
    prices: list[float],
    weights: list[float],
) -> float:
    return sum(p * w for p, w in zip(prices, weights))
```

<br/>

### Now we know:

- Both arguments are lists of floats
- The function returns a float
- IDE can warn us about mistakes

---

# Three Benefits of Type Hints

<br/>

### 1. Documentation

Types are always up-to-date documentation (unlike comments)

<br/>

### 2. IDE Support

Autocomplete, refactoring, and error detection

<br/>

### 3. Bug Prevention

Type checkers catch errors before runtime

---

# Type Hints are Optional

<br/>

```python
# Python doesn't enforce types at runtime!

def greet(name: str) -> str:
    return f"Hello, {name}"

greet(42)  # Runs without error!
# Returns "Hello, 42"
```

<br/>

### Type hints are for:

- **Developers** reading the code
- **IDEs** providing assistance
- **Type checkers** (mypy, pyright) finding bugs

---

# Type Checkers: mypy and pyright

<br/>

```bash
# Install mypy
pixi add mypy

# Check your code
pixi run mypy my_module.py
```

<br/>

```python
# my_module.py
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(42)  # mypy error: Argument 1 has incompatible type "int"
```

---

# IDE Integration

<br/>

Modern IDEs (VS Code, PyCharm) use type hints for:

- **Autocomplete** - knows what methods are available
- **Error highlighting** - red squiggles for type mismatches
- **Refactoring** - safely rename across codebase
- **Documentation** - hover to see types

<br/>

### VS Code with Pylance

- Real-time type checking
- Inferred types shown on hover
- "Go to definition" works better

---

# Writing Python Like It's Rust

<br/>

> "Parse, don't validate" - Make illegal states unrepresentable

<br/>

### The Rust philosophy applied to Python:

1. Use types to encode **what** something is
2. Make invalid inputs **impossible** to construct
3. Let the type system catch errors **before runtime**

<br/>

Source: [Writing Python Like It's Rust](https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html)

---

# Real-World Impact: optimagic

<br/>

### Before (stringly-typed):

```python
minimize(fun=f, params=x, algorithm="scipy_lbfgsb")
# Typo? No error until runtime!
```

<br/>

### After (strongly-typed):

```python
minimize(fun=f, params=x, algorithm=om.algorithms.scipy_lbfgsb)
# IDE autocomplete, typos caught immediately
```

<br/>

The library migrated its entire API for better developer experience.

---

# When to Use Type Hints

<br/>

### Always use them for:

- Function signatures (arguments and return types)
- Class attributes
- Public APIs

<br/>

### Optional for:

- Local variables (often inferred)
- Quick scripts and notebooks
- Prototype code

<br/>

### Rule of thumb:

If someone else will read it, add types.

---

# Summary

<br/>

### Type hints make Python code:

1. **Self-documenting** - Types explain intent
2. **Safer** - Catch bugs before runtime
3. **More maintainable** - Refactor with confidence

<br/>

### Next: Basic Type Hint Syntax

Learn how to annotate functions, variables, and more.
