# CLAUDE.md - Background Chapter

This file provides guidance for AI coding agents working on projects related to the
background concepts covered in this chapter. The content is derived from course
materials on operating systems, file systems, floating point numbers, and graph theory.

______________________________________________________________________

## Operating Systems

### Key Knowledge

- There are two broad lines of operating systems: Unix-based/inspired (Linux, MacOS) and
  Windows.
- Linux and MacOS share Unix heritage, which means they have similar behaviors for many
  programming tasks.
- Windows has a completely separate history from Unix (originating from MS-DOS).
- Code that works on one operating system may not work on another due to fundamental
  differences.
- There are signs of convergence: Windows Subsystem for Linux (WSL) allows running Linux
  on Windows.

### DO

- Write cross-platform code whenever possible.
- Test code on multiple operating systems if the project targets different platforms.
- Use platform-agnostic libraries (e.g., `pathlib` in Python) for file operations.
- Consider using WSL when developing on Windows for Unix-like behavior.

### DON'T

- Assume code working on Windows will automatically work on MacOS/Linux or vice versa.
- Hardcode platform-specific assumptions without proper conditionals.
- Ignore platform differences when writing installation or setup instructions.

______________________________________________________________________

## File Systems

### Key Knowledge

- Unix-based systems (Linux, MacOS) use forward slashes `/` as directory separators.
- Windows uses backslashes `\` as directory separators.
- Unix root directory is `/`; Windows uses drive letters like `C:\`.
- Unix has a single directory tree; Windows has separate trees for each drive.
- MacOS uses `/Users/username/` while Linux uses `/home/username/`.
- **Critical**: Unix-based file systems are case-sensitive (`Documents` and `documents`
  are different), while Windows is case-insensitive.
- Modern Windows can accept forward slashes in paths, but Unix cannot use backslashes.

### DO

- Use forward slashes `/` for cross-platform compatibility (works on all systems).
- Use absolute paths when clarity is needed.
- Use platform-agnostic path handling libraries:
  - Python: `pathlib.Path` or `os.path`
  - Other languages: equivalent cross-platform path utilities
- Be consistent with file naming conventions to avoid case-sensitivity issues.
- Know where files are stored for reproducibility purposes.

### DON'T

- Use backslashes `\` in paths intended for cross-platform use.
- Mix case variations of the same filename (e.g., `Data.csv` and `data.csv`).
- Assume cloud sync services handle case conflicts gracefully.
- Rely on "recent documents" or search functionality for reproducible workflows.
- Hardcode paths like `C:\Users\...` or `/home/...` without abstraction.

### Path Examples

```python
# GOOD: Cross-platform path handling
from pathlib import Path

data_path = Path("data") / "input" / "file.csv"

# BAD: Hardcoded Windows path
data_path = "C:\\Users\\user\\data\\file.csv"

# BAD: Hardcoded Unix path
data_path = "/home/user/data/file.csv"

# ACCEPTABLE: Forward slashes work everywhere
data_path = "data/input/file.csv"
```

______________________________________________________________________

## Floating Point Numbers

### Key Knowledge

- Floating point numbers cannot represent all real numbers exactly.
- Many decimal fractions (like 0.1) have no exact binary representation.
- Floating point arithmetic can produce unexpected results due to rounding errors.
- The IEEE 754 standard defines how floating point numbers are stored and computed.
- Accumulated rounding errors can cause significant issues in numerical computations.

### DO

- Use appropriate tolerance when comparing floating point numbers.
- Use dedicated libraries for precise decimal arithmetic when needed (e.g., Python's
  `decimal` module).
- Be aware of potential precision loss in financial or scientific calculations.
- Use `math.isclose()` or `numpy.isclose()` for float comparisons in Python.
- Consider the order of operations to minimize accumulated errors.

### DON'T

- Compare floating point numbers with exact equality (`==`).
- Assume `0.1 + 0.2 == 0.3` will evaluate to `True`.
- Use floating point for currency calculations without understanding the implications.
- Ignore potential precision issues in iterative numerical algorithms.

### Examples

```python
# BAD: Direct equality comparison
if result == 0.3:
    print("Equal")

# GOOD: Use tolerance-based comparison
import math

if math.isclose(result, 0.3, rel_tol=1e-9):
    print("Close enough")

# GOOD: NumPy equivalent
import numpy as np

if np.isclose(result, 0.3):
    print("Close enough")

# For financial calculations, consider:
from decimal import Decimal

price = Decimal("19.99")
```

______________________________________________________________________

## Graph Theory Basics

### Key Knowledge

- A graph G is a pair (N, E) where N is a set of nodes and E is a set of edges.
- **Undirected graphs**: Edges are sets of two nodes (order does not matter).
- **Directed graphs**: Edges are ordered pairs of nodes (direction matters).
- **Chain**: Nodes connected in sequence.
- **Tree**: A connected graph with no cycles; only one path between any two nodes.
- **Arborescence**: A directed tree where each node has exactly one parent (except
  root).
- **Directed Acyclic Graph (DAG)**: A directed graph with no cycles; cannot return to a
  node by following edges.

### Applications in Programming

- **File systems** are trees (directories and files form a hierarchy).
- **Git** uses DAGs to track commits and branches.
- **Reproducible research** pipelines are DAGs (tasks depend on other tasks).
- **Build systems** use DAGs to determine compilation order.

### DO

- Understand that file systems are tree structures rooted at `/` (Unix) or drive letters
  (Windows).
- Use DAG-based workflow tools (like `pytask`, `make`, `dvc`) for reproducible research.
- Recognize that Git history forms a DAG, which explains merge behavior.
- Use graph visualization to understand complex dependencies.

### DON'T

- Create circular dependencies in build systems or research workflows.
- Confuse directed and undirected relationships when modeling problems.
- Assume all graph structures allow cycles when they may require acyclicity.

### Graph Type Quick Reference

| Type          | Directed      | Cycles Allowed | Key Property             |
| ------------- | ------------- | -------------- | ------------------------ |
| Chain         | Can be either | No             | Linear sequence          |
| Tree          | Undirected    | No             | One path between nodes   |
| Arborescence  | Yes           | No             | Each node has one parent |
| DAG           | Yes           | No             | No directed cycles       |
| General Graph | Either        | Yes            | Most flexible            |

______________________________________________________________________

## General Best Practices for AI Agents

### Cross-Platform Development

1. Always prefer platform-agnostic solutions.
1. Use `pathlib` or equivalent for file path handling.
1. Test on multiple platforms when feasible.
1. Document platform-specific requirements clearly.

### Numerical Computing

1. Never use `==` for floating point comparison.
1. Choose appropriate precision for the problem domain.
1. Be explicit about tolerance levels in comparisons.

### Project Structure

1. Understand that projects are typically organized as directory trees.
1. Use relative paths within projects for portability.
1. Structure workflows as DAGs to ensure reproducibility.

### Code Portability Checklist

- [ ] Paths use forward slashes or pathlib
- [ ] No hardcoded absolute paths
- [ ] File names are consistently cased
- [ ] Floating point comparisons use tolerances
- [ ] Dependencies form a DAG (no circular imports/dependencies)
