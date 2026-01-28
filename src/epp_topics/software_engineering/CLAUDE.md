# Software Engineering Guidelines for AI Coding Agents

This document provides guidance for AI coding agents on writing high-quality Python code
based on the software engineering principles taught in this course.

______________________________________________________________________

## Naming Conventions

Good naming is one of the defining differences between good and bad programmers.

### DO

- Use `lowercase_with_underscores` for functions, methods, and local variables
- Use `UPPERCASE_WITH_UNDERSCORES` for global constants
- Use `CamelCase` for classes
- Start function names with a verb in imperative mode: `create_`, `calculate_`,
  `convert_`, `get_`
- Use descriptive names proportional to scope:
  - Short names like `i`, `j`, `df` are acceptable for variables used within a few lines
  - Long, descriptive names for variables used across 20+ lines
- Start private/helper functions with `_underscore`
- Use `lambda_` (with trailing underscore) to avoid Python keywords

### DO NOT

- Use abbreviations, especially ambiguous ones (`constr` could mean constraint or
  constructor)
- Use misspelled words (`rsnbrck` instead of `rosenbrock`, `lambbda` instead of
  `lambda_`)
- Use meaningless distinctions (`Beta` and `beta` for different concepts)
- Append type to variable names (`names_list` instead of just `names`)
- Use built-in keywords as names: `list`, `var`, `dict`, `type`
- Use single letters that cause debugger issues: `n`, `c`, `u`, `s`
- Use hard-to-distinguish letters: `l` (lowercase L) and `I` (uppercase i)
- Start function names with `return_` or `call_`
- Use `and` in function names (split into two functions instead)

### Examples

```python
# Good function names
def process_model_specification(spec): ...


def calculate_portfolio_returns(prices, weights): ...


# Bad function names
def convert_user_provided_model_dictionary_to_model_class_and_set_defaults(
    d,
): ...  # Too long and contains "and"


def call_function(f): ...  # Meaningless, starts with "call"
```

______________________________________________________________________

## Pure Functions

Write pure functions whenever possible. A pure function:

1. Returns identical values for identical arguments
1. Has no side effects (does not modify external state)

### DO

- Pass all required data as function arguments (explicit interfaces)
- Return results instead of modifying inputs
- Push impure operations (file I/O) to the boundaries of your code
- Keep the core logic in pure functions

### DO NOT

- Depend on global variables or external state
- Modify mutable input arguments
- Mix file I/O with data processing logic

### Example: Push Impurities to Boundaries

```python
# Good: Separate I/O from pure logic
def task_clean_data(
    data=SRC / "original_data" / "data.csv",
    produces=BLD / "data.pkl",
):
    df = pd.read_csv(data)  # Impure: file read
    clean = clean_data(df)  # Pure: data processing
    clean.to_pickle(produces)  # Impure: file write


def clean_data(df):
    """Pure function - all logic here."""
    # 99% of your code should be in pure functions like this
    ...
    return cleaned_df
```

### Benefits

- **Testability**: Control everything relevant during testing
- **Parallelization**: No side-effect worries when calling in parallel
- **Reduced mental load**: No hidden state changes to track
- **Compatibility**: Works with functional programming tools and libraries like JAX

______________________________________________________________________

## Style Guides

### Naming Conventions (PEP 8)

- Functions and methods: `lowercase_with_underscores`
- Local variables: `lowercase_with_underscores`
- Global constants: `UPPERCASE_WITH_UNDERSCORES`
- Classes: `CamelCase`
- Private functions: `_leading_underscore`

### Formatting Rules

- Indent with 4 spaces (mandatory in Python)
- Maximum line length of 88 characters
- Two blank lines between function definitions
- One blank line between method definitions
- Whitespace around operators

### DO

- Use automated formatters (ruff, black) and linters
- Set up pre-commit hooks for consistent formatting
- Learn to write roughly compliant code yourself

### DO NOT

- Spend time manually formatting code
- Have discussions about formatting style (automate it instead)
- Assume well-formatted code is automatically good code

______________________________________________________________________

## functools.partial

Use `functools.partial` to create new functions with some arguments pre-filled.

### DO

- Use for plotting functions against one of their arguments
- Use to create functions that only depend on a parameter vector (for optimization,
  differentiation)
- Keep it as a problem solver in your toolkit

### DO NOT

- Overuse partial for every function call
- Create many confusing versions of the same function

### Example

```python
from functools import partial


def objective(params, data, options): ...


# Create a function that only depends on params for optimization
objective_for_optimizer = partial(objective, data=my_data, options=my_options)
result = minimize(objective_for_optimizer, initial_params)
```

______________________________________________________________________

## Error Handling

Good error handling helps users find and fix mistakes quickly.

### DO

- Raise errors as early as possible
- Use descriptive error messages that explain what went wrong and how to fix it
- Use `TypeError` for wrong argument types
- Use `ValueError` for correct types but wrong values
- Create `_fail_if_...` helper functions for each check
- Collect multiple similar errors before raising (when appropriate)
- Define custom exceptions for domain-specific errors

### DO NOT

- Duplicate error handling code
- Run checks repeatedly in nested functions
- Use error handling for things that should be tested instead
- Go too far combining errors across multiple fail functions

### Example: Fail Functions

```python
def convert_lod_to_dol(lod):
    _fail_if_lod_is_not_a_list(lod)
    _fail_if_list_of_wrong_types(lod)
    _fail_if_list_of_dicts_with_different_keys(lod)
    # ... actual implementation


def _fail_if_lod_is_not_a_list(lod):
    if not isinstance(lod, list):
        msg = f"lod must be a list, not {type(lod)}."
        raise TypeError(msg)


def _fail_if_list_of_wrong_types(data):
    invalid_rows = []
    for i, row in enumerate(data):
        if not isinstance(row, dict):
            invalid_rows.append(i)

    if invalid_rows:
        report = "The following rows are not dictionaries:\n"
        for i in invalid_rows:
            report += f"  Row {i} has type {type(data[i])}\n"
        raise TypeError(report)
```

### Custom Exceptions

```python
class NonTabularDataError(Exception):
    """Raised when data has the correct type but is not tabular."""

    pass
```

### Recipe for Good Error Handling

1. Identify inputs that can cause problems (user inputs, unchecked data)
1. List everything that could go wrong, from simple to specific
1. Write one `_fail_if_...` function for each condition
1. Call fail functions at the earliest possible moment
1. Test error messages by calling functions with invalid inputs

______________________________________________________________________

## Testing

### The Idea

- Any project can be decomposed into small steps that can be tested
- Test the steps, not the whole
- Testing interfaces (not implementation) allows improving code without breaking things

### What to Test

- Typical input scenarios
- Corner cases and edge cases
- Expected exceptions
- Any bugs encountered (add to test suite before fixing)

### How to Test

- Write granular tests (one assert per test function)
- Always perform counterchecks (verify test fails when it should)
- Be careful with non-scalar comparisons (use "and" conditions, not "or")

### DO

- Name test files `test_XXX.py` where XXX is the module being tested
- Name test functions `test_YYY_ZZZ` where YYY is the function and ZZZ describes the
  behavior
- Structure tests clearly: define expected, calculate actual, assert equality
- Use `pytest.raises` to test that errors are raised correctly
- Use `@pytest.mark.parametrize` to test multiple inputs with one function

### DO NOT

- Test implementation details (only test interfaces)
- Write tests that pass for the wrong reasons
- Skip counterchecks

### Example: Simple Test

```python
def test_clean_agreement_scale_check_dtype():
    expected = pd.CategoricalDtype(
        categories=[
            "strongly disagree",
            "disagree",
            "neutral",
            "agree",
            "strongly agree",
        ],
        ordered=True,
    )
    actual = _clean_agreement_scale(pd.Series([])).dtype
    assert expected == actual
```

### Example: Testing Exceptions

```python
import pytest


def test_clean_agreement_scale_invalid_data():
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series(["typo"]))
```

### Example: Parametrized Tests

```python
@pytest.mark.parametrize("invalid_input", [-77, "typo"])
def test_clean_agreement_scale_invalid_data(invalid_input):
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series([invalid_input]))
```

______________________________________________________________________

## Data Structures: Choosing Containers

### When to Use Each

| Structure    | Use When                                                              |
| ------------ | --------------------------------------------------------------------- |
| `dict`       | Free/variable fields, fast lookup by key, unknown keys at design time |
| `NamedTuple` | Fixed fields, immutability required, simple data containers           |
| `dataclass`  | Fixed fields, mutability needed, complex options required             |

### The Key Question: Fixed vs. Free Fields

- **Fixed fields**: You know the structure at design time (use NamedTuple/dataclass)
- **Free fields**: Keys are dynamic or unknown at design time (use dict)

### DO

- Use NamedTuple or dataclass when you have a fixed set of attributes
- Prefer immutable structures unless mutability is needed
- Use dictionaries for collections with variable keys

### DO NOT

- Use dictionaries for everything (typos in keys cause runtime errors)
- Forget that dictionaries are highly optimized and often the right choice

### Example: Combining Containers

```python
from typing import NamedTuple


class Student(NamedTuple):
    first_name: str
    last_name: str
    email: str


# Fixed structure for each student, but variable collection of students
students = {
    "janosg": Student(
        first_name="Janos",
        last_name="Gabler",
        email="janos@uni-bonn.de",
    ),
    "timmens": Student(
        first_name="Tim",
        last_name="Mensinger",
        email="tim@uni-bonn.de",
    ),
}
```

### Immutability

> "Where it is not necessary to change, it is necessary not to change." -- Lucius Cary

- Immutable objects prevent many bugs
- Prefer NamedTuple (immutable) over dataclass (mutable by default)
- Use `@dataclass(frozen=True)` if you need dataclass features but want immutability

______________________________________________________________________

## Type Hints

Type hints make Python code safer, more maintainable, and self-documenting. They enable
IDE autocomplete, catch bugs before runtime, and serve as always up-to-date
documentation.

### DO

- Add type hints to all function parameters and return types
- Use built-in types directly: `list[int]`, `dict[str, float]`, `tuple[int, str]`
- Use `| None` for optional values: `str | None`
- Use `|` for union types: `int | str`
- Use `Path` from pathlib for file paths
- Use `pd.DataFrame` for pandas DataFrames
- Use the Python 3.12+ generic syntax: `def first[T](items: list[T]) -> T:`
- Run a type checker (ty, pyright) regularly to catch errors

### DO NOT

- Use old typing module imports (`Optional`, `Union`, `List`, `Dict`) - use modern
  syntax
- Leave function signatures untyped
- Use `Any` except as a last resort for untyped external code
- Use `list` without specifying element type (use `list[int]` not just `list`)

### Basic Syntax

```python
from pathlib import Path
import pandas as pd


def load_data(path: Path) -> pd.DataFrame:
    """Load data from a CSV file."""
    return pd.read_csv(path)


def calculate_mean(values: list[float]) -> float:
    """Calculate the arithmetic mean."""
    return sum(values) / len(values)


def find_user(user_id: int) -> str | None:
    """Return username or None if not found."""
    return users.get(user_id)
```

### Type Aliases

```python
# Use the type statement for readable aliases
type UserId = int
type Coordinates = tuple[float, float]
type Matrix = list[list[float]]


def get_location(user_id: UserId) -> Coordinates: ...
```

### Generic Functions and Classes

```python
# Generic function - preserves input type
def first[T](items: list[T]) -> T:
    return items[0]


# Generic class
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

### Dataclasses with Types

```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ModelConfig:
    """Immutable configuration for a model."""

    n_periods: int
    discount_factor: float = 0.95
    grid_points: int = 100


@dataclass
class SimulationResult:
    """Mutable result container."""

    values: list[float] = field(default_factory=list)
    converged: bool = False
```

### Callable Types

```python
from collections.abc import Callable


def apply_operation(
    a: int,
    b: int,
    op: Callable[[int, int], float],
) -> float:
    return op(a, b)
```

### Literal and NewType for Precision

```python
from typing import Literal, NewType


# Literal constrains to specific values
def set_mode(mode: Literal["read", "write", "append"]) -> None: ...


# NewType creates distinct types from the same base
UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def process_order(
    user_id: UserId, order_id: OrderId
) -> None: ...  # Type checker catches if you swap these
```

### Protocol for Duck Typing

```python
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None: ...


def render(item: Drawable) -> None:
    item.draw()


# Any class with draw() method works - no inheritance needed
class Circle:
    def draw(self) -> None:
        print("Drawing circle")


render(Circle())  # OK
```

### NumPy Array Types

```python
import numpy as np
from numpy.typing import NDArray


def simulate(
    n_simulations: int,
    seed: int | None = None,
) -> NDArray[np.float64]:
    rng = np.random.default_rng(seed)
    return rng.random(n_simulations)
```

### Running Type Checkers

```bash
# ty (from Astral, recommended)
pixi run ty check src/

# pyright
pixi run pyright src/

# Strict mode for more checks
pixi run ty check --strict src/
```

______________________________________________________________________

## Quick Reference: Common Patterns

### Function Structure (with Type Hints)

```python
from pathlib import Path
import pandas as pd


def calculate_statistics(
    data: pd.DataFrame,
    columns: list[str],
) -> dict[str, float]:
    """Calculate summary statistics for specified columns.

    Args:
        data: Input DataFrame with numeric columns.
        columns: Column names to analyze.

    Returns:
        Dictionary mapping column names to their means.

    Raises:
        ValueError: When columns are not found in data.

    """
    _fail_if_columns_missing(data, columns)

    result = {col: float(data[col].mean()) for col in columns}

    return result
```

### Test Structure

```python
def test_function_name_behavior_being_tested() -> None:
    # Arrange: Set up expected result
    expected = ...

    # Act: Call the function
    actual = function_under_test(input_data)

    # Assert: Verify result
    assert actual == expected
```

### Error Handling Pattern

```python
def _fail_if_condition_not_met(param: SomeType) -> None:
    if not some_condition(param):
        msg = f"Clear description of what went wrong: {param}"
        raise AppropriateError(msg)
```

### Typed Dataclass Pattern

```python
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Config:
    """Immutable project configuration."""

    src_dir: Path
    bld_dir: Path
    n_simulations: int = 1000
    seed: int = 42


@dataclass
class Result:
    """Mutable result container."""

    values: list[float] = field(default_factory=list)
    success: bool = False
```
