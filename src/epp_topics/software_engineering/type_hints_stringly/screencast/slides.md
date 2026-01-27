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
title: From Stringly-Typed to Strongly-Typed
defaults:
  layout: default
---

# From Stringly-Typed to Strongly-Typed

### A Case Study in API Evolution

<br/>

Effective Programming Practices for Economists

---

# What is "Stringly-Typed"?

<br/>

> Using strings to represent structured data that should have its own types

<br/>

```python
# Stringly-typed
config = {
    "algorithm": "scipy_lbfgsb",
    "stopping.max_iterations": 1000,
    "convergence.tolerance": 1e-6,
}

# What algorithms exist? What options are valid?
# No autocomplete, no error checking, no documentation
```

---

# The Problem with Strings

<br/>

### 1. Typos are silent errors

```python
minimize(algorithm="scipy_lbfgsp")  # Typo! Discovered at runtime
```

<br/>

### 2. No IDE autocomplete

```python
minimize(algorithm="")  # What are my options?
```

<br/>

### 3. No documentation

```python
# Is it "maxiter" or "max_iter" or "max_iterations"?
```

---

# Case Study: optimagic

<br/>

### optimagic is an optimization library that unified interfaces to many algorithms

<br/>

In 2024, they migrated from stringly-typed to strongly-typed APIs.

<br/>

Let's examine what changed and why.

---

# Algorithm Selection: Before

<br/>

```python
import optimagic as om

# Select algorithm by string
result = om.minimize(
    fun=objective,
    params=initial_params,
    algorithm="scipy_lbfgsb",  # String - typos possible
)

# What algorithms are available?
# What if I typo "scipy_lbfgsp"?
# Runtime error, possibly cryptic
```

---

# Algorithm Selection: After

<br/>

```python
import optimagic as om

# Select algorithm by object
result = om.minimize(
    fun=objective,
    params=initial_params,
    algorithm=om.algorithms.scipy_lbfgsb,  # Object - IDE helps
)

# Benefits:
# - Autocomplete shows all available algorithms
# - Typos caught immediately by IDE
# - Can inspect algorithm properties
```

---

# Bounds: Before

<br/>

```python
# Four separate arguments - easy to confuse
result = om.minimize(
    fun=objective,
    params=params,
    lower_bounds=params - 1,
    upper_bounds=params + 1,
    soft_lower_bounds=params - 2,
    soft_upper_bounds=params + 2,
)

# Which is lower vs upper?
# What if I swap them?
```

---

# Bounds: After

<br/>

```python
# Single typed object - clear structure
bounds = om.Bounds(
    lower=params - 1,
    upper=params + 1,
    soft_lower=params - 2,
    soft_upper=params + 2,
)

result = om.minimize(
    fun=objective,
    params=params,
    bounds=bounds,  # Single argument
)

# Named fields prevent confusion
```

---

# The Bounds Dataclass

<br/>

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Bounds:
    lower: PyTree | None = None
    upper: PyTree | None = None
    soft_lower: PyTree | None = None
    soft_upper: PyTree | None = None
```

<br/>

### Benefits:

- Clear field names
- IDE autocomplete
- Immutable (frozen)
- Sensible defaults

---

# Constraints: Before

<br/>

```python
# Dictionaries with magic keys
constraints = [
    {"type": "fixed", "selector": lambda x: x[0]},
    {"type": "increasing", "selector": lambda x: x[1:4]},
]

# Which keys are required?
# What are valid values for "type"?
# Discovered at runtime...
```

---

# Constraints: After

<br/>

```python
# Typed constraint objects
constraints = [
    om.FixedConstraint(selector=lambda x: x[0]),
    om.IncreasingConstraint(selector=lambda x: x[1:4]),
]

# Each constraint type is its own class
# IDE shows required and optional parameters
# Invalid combinations caught by type checker
```

---

# The Constraint Hierarchy

<br/>

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Constraint(ABC):
    """Base class for all constraints."""
    @abstractmethod
    def _to_dict(self) -> dict[str, Any]:
        pass

@dataclass(frozen=True)
class FixedConstraint(Constraint):
    selector: Callable[[PyTree], PyTree]

@dataclass(frozen=True)
class IncreasingConstraint(Constraint):
    selector: Callable[[PyTree], PyTree]
```

---

# Function Types: Before

<br/>

```python
def objective(params):
    # What should this return?
    # A scalar? A dict? An array?
    return ???

# optimagic had to guess from return value
```

---

# Function Types: After

<br/>

```python
import optimagic as om

@om.mark.least_squares
def residuals(params):
    """Now optimagic knows this returns residuals."""
    return params - target

@om.mark.likelihood
def log_likelihood(params):
    """Now optimagic knows this returns log-likelihoods."""
    return -0.5 * (params - target) ** 2
```

<br/>

### Decorators make intent explicit

---

# The Mark Decorators

<br/>

```python
from enum import Enum

class AggregationLevel(Enum):
    SCALAR = "scalar"
    LEAST_SQUARES = "least_squares"
    LIKELIHOOD = "likelihood"

def least_squares(func):
    """Mark function as returning residuals."""
    func._aggregation_level = AggregationLevel.LEAST_SQUARES
    return func
```

<br/>

### Type information attached to functions at runtime

---

# Options: Before

<br/>

```python
# Nested string keys
options = {
    "stopping.max_iterations": 1000,
    "convergence.relative_criterion_tolerance": 1e-6,
    "initial_radius": 0.1,
}

# Typos silently ignored!
# "convergance.tolerance" → no error, just doesn't work
```

---

# Options: After

<br/>

```python
@dataclass(frozen=True)
class StoppingOptions:
    max_iterations: int = 1000
    max_evaluations: int | None = None

@dataclass(frozen=True)
class ConvergenceOptions:
    relative_criterion_tolerance: float = 1e-8
    absolute_criterion_tolerance: float = 1e-14

# Typos caught by type checker
# IDE shows all available options
```

---


# Using Enums for Options

<br/>

```python
from enum import Enum

class SamplingMethod(Enum):
    SOBOL = "sobol"
    RANDOM = "random"
    HALTON = "halton"
    LATIN_HYPERCUBE = "latin_hypercube"

@dataclass(frozen=True)
class MultistartOptions:
    sampling_method: SamplingMethod = SamplingMethod.RANDOM
    n_samples: int = 100

# IDE shows all valid sampling methods
# Typos impossible
```

---

# Using Literal for String Options

<br/>

```python
from typing import Literal

@dataclass(frozen=True)
class MultistartOptions:
    # Still accepts strings, but constrained
    sampling_method: Literal["sobol", "random", "halton"] = "random"

    # Or mix Literal with callable for flexibility
    batch_evaluator: Literal["joblib", "threading"] | Callable = "joblib"
```

---

# Design Principle: Generous Input, Strict Output

<br/>

```python
def minimize(
    fun: Callable,
    params: Any,
    algorithm: str | Algorithm,  # Accept both
    bounds: dict | Bounds | None = None,  # Accept both
) -> OptimizeResult:  # Return typed result
    ...
```

<br/>

### Accept flexible inputs, return typed outputs

- Users can migrate gradually
- New code gets full type benefits

---

# Lessons Learned

<br/>

### 1. Start with the API you want

Design typed APIs from the start when possible

<br/>

### 2. Use dataclasses for configuration

Replace dicts with frozen dataclasses

<br/>

### 3. Use enums or Literal for fixed options

Eliminate typos for known values

<br/>

### 4. Provide migration path

Support both old and new APIs during transition

---

# Applying to Your Code

<br/>

### Signs you need stronger typing:

- Configuration dicts with string keys
- Functions that accept string arguments for "mode" or "type"
- Separate arguments that should be grouped
- Runtime errors from typos in strings

<br/>

### Steps to migrate:

1. Create dataclasses for configuration
2. Replace string options with Enum or Literal
3. Group related arguments into typed objects
4. Add deprecation warnings for old API

---

# Summary

<br/>

### Stringly-typed problems:

- Typos become runtime errors
- No IDE support
- No documentation

<br/>

### Strongly-typed solutions:

- Dataclasses for structured config
- Enums/Literal for fixed options
- Classes for related concepts
- Decorators for function metadata

<br/>

### Key insight:

Types are documentation that the computer can check.
