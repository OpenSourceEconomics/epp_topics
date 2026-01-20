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
title: Collections and Generics
defaults:
  layout: default
---

# Collections and Generics

### Typing Lists, Dicts, and Custom Containers

<br/>

Effective Programming Practices for Economists

---

# Built-in Collection Types

<br/>

```python
# Python 3.9+ syntax (lowercase)
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95, "Bob": 87}
coordinates: tuple[float, float] = (1.0, 2.0)
unique_ids: set[int] = {1, 2, 3}
```

<br/>

### Pattern: `container[element_type]`

- `list[T]` - list of T
- `dict[K, V]` - dict with keys K and values V
- `tuple[T1, T2]` - tuple with specific types
- `set[T]` - set of T

---

# Lists

<br/>

```python
# List of integers
numbers: list[int] = [1, 2, 3, 4, 5]

# List of strings
names: list[str] = ["Alice", "Bob", "Carol"]

# Nested list (matrix)
matrix: list[list[float]] = [
    [1.0, 2.0],
    [3.0, 4.0],
]

# Empty list with type annotation
results: list[float] = []
```

---

# Dictionaries

<br/>

```python
# String keys, integer values
word_counts: dict[str, int] = {"hello": 5, "world": 3}

# Integer keys, list values
user_scores: dict[int, list[float]] = {
    1: [95.0, 87.5],
    2: [78.0, 82.0],
}

# Nested dictionaries
config: dict[str, dict[str, str]] = {
    "database": {"host": "localhost", "port": "5432"},
    "cache": {"host": "redis", "port": "6379"},
}
```

---

# Tuples: Fixed vs Variable Length

<br/>

### Fixed-length tuple (specific types per position):

```python
# Exactly two elements: (name, age)
person: tuple[str, int] = ("Alice", 30)

# Exactly three elements
rgb: tuple[int, int, int] = (255, 128, 0)
```

<br/>

### Variable-length tuple (homogeneous):

```python
# Any number of integers
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
```

---

# Sets and Frozensets

<br/>

```python
# Mutable set
active_users: set[int] = {1, 2, 3}

# Immutable frozenset
valid_statuses: frozenset[str] = frozenset({"active", "pending", "closed"})
```

<br/>

### When to use which:

- `set` - when you need to add/remove elements
- `frozenset` - when you need a hashable set (dict keys, set of sets)

---

# Abstract Collection Types

<br/>

```python
from collections.abc import Sequence, Mapping, Iterable

def process_items(items: Sequence[int]) -> int:
    """Accept list, tuple, or any sequence."""
    return sum(items)

def lookup(data: Mapping[str, int], key: str) -> int:
    """Accept dict or any mapping."""
    return data[key]

def count_items(items: Iterable[str]) -> int:
    """Accept any iterable (list, set, generator, etc.)."""
    return sum(1 for _ in items)
```

---

# When to Use Abstract Types

<br/>

### Use concrete types (`list`, `dict`) when:

- You need specific methods (e.g., `list.append`)
- You're returning a value (be specific)

<br/>

### Use abstract types (`Sequence`, `Mapping`) when:

- You only read from the collection
- You want to accept multiple input types
- You're writing library code

<br/>

```python
# Good: Accept any sequence, return specific list
def double_values(values: Sequence[int]) -> list[int]:
    return [v * 2 for v in values]
```

---

# Generics with TypeVar

<br/>

```python
from typing import TypeVar

T = TypeVar("T")

def first_element(items: list[T]) -> T:
    """Return first element, preserving the type."""
    return items[0]

# Usage:
first_element([1, 2, 3])       # Returns int
first_element(["a", "b"])      # Returns str
```

<br/>

### TypeVar creates a placeholder type

The same `T` means "same type throughout"

---

# Constrained TypeVars

<br/>

```python
from typing import TypeVar

# T can only be int or float
Number = TypeVar("Number", int, float)

def add_numbers(a: Number, b: Number) -> Number:
    return a + b

add_numbers(1, 2)       # OK: both int
add_numbers(1.0, 2.0)   # OK: both float
add_numbers(1, 2.0)     # Error: mixing types!
```

---

# Bounded TypeVars

<br/>

```python
from typing import TypeVar

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

# T must be Animal or a subclass
AnimalType = TypeVar("AnimalType", bound=Animal)

def make_speak(animal: AnimalType) -> str:
    return animal.speak()
```

---

# Generic Classes

<br/>

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Usage:
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
value: int = int_stack.pop()  # Type is preserved
```

---

# Python 3.12 Syntax

<br/>

```python
# New in Python 3.12: simpler generic syntax

# Old way
from typing import TypeVar, Generic
T = TypeVar("T")
class Stack(Generic[T]): ...

# New way (Python 3.12+)
class Stack[T]:
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...

# Also for functions
def first[T](items: list[T]) -> T:
    return items[0]
```

---

# Callable Types

<br/>

```python
from collections.abc import Callable

# Function that takes two ints and returns a float
Operation = Callable[[int, int], float]

def apply_operation(
    a: int,
    b: int,
    op: Callable[[int, int], float],
) -> float:
    return op(a, b)

def divide(x: int, y: int) -> float:
    return x / y

result = apply_operation(10, 3, divide)
```

---

# Callable with TypeVar

<br/>

```python
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")

def apply_twice(
    func: Callable[[T], R],
    value: T,
) -> tuple[R, R]:
    """Apply function twice, return both results."""
    return func(value), func(value)

def square(x: int) -> int:
    return x * x

result: tuple[int, int] = apply_twice(square, 5)
```

---

# Common Patterns

<br/>

### Optional list parameter:

```python
def process(items: list[int] | None = None) -> list[int]:
    if items is None:
        items = []
    return [x * 2 for x in items]
```

<br/>

### Dict with default:

```python
def get_config(
    overrides: dict[str, str] | None = None,
) -> dict[str, str]:
    config = {"host": "localhost", "port": "8080"}
    if overrides:
        config.update(overrides)
    return config
```

---

# Type Narrowing

<br/>

```python
def process(value: int | str | None) -> str:
    if value is None:
        return "empty"
    if isinstance(value, int):
        # Here, type checker knows value is int
        return str(value * 2)
    # Here, type checker knows value is str
    return value.upper()
```

<br/>

### Type checkers understand:

- `if x is None` / `if x is not None`
- `isinstance(x, Type)`
- `assert isinstance(x, Type)`

---

# Summary

<br/>

### Collections:

- `list[T]`, `dict[K, V]`, `tuple[T1, T2]`, `set[T]`
- Use `Sequence`, `Mapping`, `Iterable` for flexible inputs

<br/>

### Generics:

- `TypeVar` for type-preserving functions
- `Generic[T]` for type-preserving classes
- Python 3.12: `class Foo[T]:` syntax

<br/>

### Next: Dataclasses and Typed Structures
