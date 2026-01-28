# CLAUDE.md - Python Installation and Execution Guidelines

This document provides guidance for AI coding agents working with Python environments
and code execution in this project. The recommendations are based on best practices from
the Effective Programming Practices for Economists course.

## Package Management with Pixi

Pixi is the recommended package and environment manager for this project. It manages
conda packages and provides isolated, reproducible environments for each project.

### DO

- Use `pixi run <command>` to execute any command that requires the project environment
  - `pixi run python script.py` instead of `python script.py`
  - `pixi run pytest` instead of `pytest`
  - `pixi run pytask` instead of `pytask`
- Use `pixi add <package>` to add new conda-forge dependencies
- Use `pixi add --pypi <package>` for packages only available on PyPI
- Use `pyproject.toml` for pixi configuration (not `pixi.toml`)
- Commit the `pixi.lock` file to version control for reproducibility
- Use `pixi run --frozen python script.py` when you want to use the exact locked
  versions
- Use `pixi list` to see all packages in the current environment
- Specify platform compatibility in `pyproject.toml`:
  ```toml
  [tool.pixi.project]
  platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]
  ```

### DO NOT

- Do not use `pip install` directly - use `pixi add` or `pixi add --pypi` instead
- Do not use `conda install` - use `pixi add` instead
- Do not use the `defaults` conda channel - use `conda-forge` instead
- Do not forget to prefix commands with `pixi run`
- Do not manually edit `pixi.lock` - it is automatically managed
- Do not use `pixi shell` for running scripts (prefer `pixi run` to avoid forgetting to
  activate the correct environment)

### Version Constraints

When specifying package versions in `pyproject.toml`:

- Version 2.2 or higher: `package = ">=2.2"`
- Version 2.2.x (compatible releases): `package = "~=2.2"`
- Exact version 2.2.0: `package = "==2.2.0"`
- Most recent compatible version: `package = "*"`

______________________________________________________________________

## Python Package Structure

### DO

- Use the `src` layout for Python packages:
  ```
  project/
  ├── src/
  │   └── package/
  │       ├── __init__.py
  │       └── module.py
  └── pyproject.toml
  ```
- Include `__init__.py` files in all package directories
- Use `pip install -e .` (editable install) during development so changes are reflected
  immediately
- Use `if __name__ == "__main__":` guard for code that should only run when the file is
  executed directly
- Export commonly used objects in `__init__.py` for convenient imports

### DO NOT

- Do not commit `__pycache__` directories to version control
- Do not forget the `__init__.py` files in package directories
- Do not use regular `pip install .` during development (changes require reinstallation)

______________________________________________________________________

## Pip and PyPI

### DO

- Understand that pip can install from: local directories, GitHub/GitLab, URLs, and PyPI
- Prefer conda-forge packages over PyPI when available (better dependency resolution)
- Use pip only through pixi: `pixi add --pypi <package>`

### DO NOT

- Do not run `pip install` outside of a pixi environment
- Do not expect pip to handle non-Python dependencies (like CUDA) - use pixi/conda-forge
  instead
- Do not assume all platforms have pre-built wheels - some packages may require
  compilation

______________________________________________________________________

## Executing Python Code

### From the Shell

```bash
# Correct way
pixi run python script.py

# Also correct (with relative paths)
pixi run python ../script.py
```

### In VS Code

1. Open the project root directory (containing `pyproject.toml`) in VS Code
1. Run any `pixi run` command once to create the `.pixi` environment
1. Select the Python interpreter from `.pixi/envs/default/bin/python`
1. Use the run button or `pixi run python script.py` in the terminal

### DO

- Always run pixi commands from a directory containing (or with a parent containing)
  `pyproject.toml`
- Ensure VS Code has the correct Python interpreter selected (from the `.pixi`
  environment)
- Use absolute or correct relative paths when running scripts

### DO NOT

- Do not run `python script.py` without `pixi run` prefix
- Do not assume the system Python is the correct one

______________________________________________________________________

## Executing Jupyter Notebooks

### Prerequisites

- The `ipykernel` package must be in `pyproject.toml` dependencies
- VS Code must have Python extensions installed

### DO

- Select the kernel from the pixi environment (Python Environments -> default)
- Use `Shift+Enter` to run cells and move to the next cell
- Use `Ctrl+Enter` to run a cell and stay in it

### DO NOT

- Do not use a system Python kernel - always use the pixi environment kernel
- Do not forget to install `ipykernel` in the project dependencies

______________________________________________________________________

## Executing Tests with pytest

pytest runs individual test functions across multiple files.

### DO

- Run tests with `pixi run pytest`
- Name test files with `test_` prefix (e.g., `test_module.py`)
- Name test functions with `test_` prefix (e.g., `def test_function():`)
- Include `pytest` in your `pyproject.toml` dependencies

### DO NOT

- Do not run `pytest` without `pixi run`
- Do not forget the `test_` prefix for test files and functions

______________________________________________________________________

## Executing Tasks with pytask

pytask runs individual task functions for reproducible research pipelines.

### DO

- Run tasks with `pixi run pytask`
- Name task files with `task_` prefix (e.g., `task_analysis.py`)
- Name task functions with `task_` prefix (e.g., `def task_clean_data():`)
- Include `pytask` in your `pyproject.toml` dependencies
- Let pytask skip tasks that are already up-to-date (it tracks dependencies)

### DO NOT

- Do not run `pytask` without `pixi run`
- Do not forget the `task_` prefix for task files and functions

______________________________________________________________________

## Environment Configuration Summary

A typical `pyproject.toml` for pixi:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"

[build-system]
build-backend = "hatchling.build"
requires = ["hatchling"]

[tool.pixi.project]
name = "my-project"
channels = ["conda-forge"]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]

[tool.pixi.dependencies]
python = ">=3.13"
numpy = ">=2.2"
pandas = "*"
pytest = "*"
ipykernel = "*"

[tool.pixi.pypi-dependencies]
# For packages only on PyPI
some-pypi-package = "*"

[tool.pixi.tasks]
test = "pytest"
```

______________________________________________________________________

## Quick Reference Commands

| Task                    | Command                              |
| ----------------------- | ------------------------------------ |
| Add conda package       | `pixi add <package>`                 |
| Add PyPI package        | `pixi add --pypi <package>`          |
| Run Python script       | `pixi run python script.py`          |
| Run tests               | `pixi run pytest`                    |
| Run tasks               | `pixi run pytask`                    |
| List installed packages | `pixi list`                          |
| Initialize new project  | `pixi init --format pyproject`       |
| Import from conda env   | `pixi init --import environment.yml` |

______________________________________________________________________

## Why Pixi over pip/conda?

1. **Better dependency resolution**: Uses a robust solver for conflict-free
   installations
1. **Non-Python dependencies**: Can install system libraries (e.g., CUDA toolkit)
1. **Reproducibility**: Lock file ensures exact environment reproduction
1. **No activation needed**: `pixi run` automatically uses the correct environment
1. **Cross-platform**: Single configuration works across Windows, macOS, and Linux
