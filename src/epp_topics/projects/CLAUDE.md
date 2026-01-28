# CLAUDE.md - Project Structure Guidelines for AI Agents

This document provides guidance for AI coding agents on structuring reproducible Python
research projects based on the Effective Programming Practices for Economists (EPP)
course materials.

## Overview

This chapter covers reproducible research practices using **pytask** (a build system for
executing research workflows) and the **econ-project-templates** (a recommended
directory structure implementing best practices).

______________________________________________________________________

## Reproducibility Principles

### DO

- Include all source data, starting from the original format you obtained it
- Include all source code needed to produce results
- Document all programs/packages needed to run the code
- Use environment files to automate package installation
- Pin package versions when the project reaches milestones (e.g., submission)
- Keep raw data and source code under version control
- Create published results from the main branch with no uncommitted changes
- Use git tags/releases to mark submissions and revisions
- Put all generated files in a separate folder (e.g., `bld/`) that can be safely deleted
- Provide a README documenting directory structure, package installation, and how to run
  code
- Strive for readable source code with appropriate docstrings and comments

### DO NOT

- Put generated/output files under version control (they become outdated, explode repo
  size, and do not help reproducibility)
- Rely on notebooks that need manual execution
- Use manual clicking, copy-pasting, or commenting out code
- Require running multiple files in a specific order manually
- Store intermediate outputs as a substitute for reproducibility

______________________________________________________________________

## Directory Structure

### DO

- Maintain clear separation of inputs (`src/`) and outputs (`bld/`)
- Group files by analysis step inside `src/`:
  - `original_data/` - raw source data
  - `data_management/` - data cleaning and preparation
  - `analysis/` - regressions, estimations, computations
  - `model_specs/` - model configuration files
  - `final/` - visualizations and final outputs
- Separate long-running analysis tasks from fast visualization tasks
- Put code that runs regressions in `analysis/`
- Put code that visualizes estimation results in `final/`

### DO NOT

- Mix source files and generated outputs in the same directory
- Put visualization code in the same file as estimation code
- Trigger expensive re-computations when only changing plot aesthetics

### Example Structure

```
my_project/
├── src/
│   └── my_project/
│       ├── config.py
│       ├── original_data/
│       ├── data_management/
│       │   └── task_clean_data.py
│       ├── analysis/
│       │   └── task_run_model.py
│       ├── model_specs/
│       └── final/
│           └── task_plot_results.py
├── bld/
│   └── python/
│       ├── data/
│       ├── models/
│       └── figures/
├── tests/
├── paper/
└── environment.yml
```

______________________________________________________________________

## Path Handling

### DO

- Start paths relative to the project root folder
- Only make assumptions about directory structure inside the project
- Use `pathlib.Path` for all file paths (portable across operating systems)
- Define common paths (SRC, BLD, etc.) in a central `config.py` file
- Import paths from config.py in all task files

### DO NOT

- Use hardcoded absolute paths
- Use string paths instead of `pathlib.Path` objects
- Duplicate path definitions across files
- Make assumptions about paths outside the project directory

### Example config.py

```python
from pathlib import Path

SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld").resolve()
TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()
PAPER_DIR = SRC.joinpath("..", "..", "paper").resolve()
```

### Example Usage in Task Files

```python
from my_project.config import SRC, BLD


def task_clean_data(
    raw_data=SRC / "original_data" / "data.csv",
    produces=BLD / "data" / "clean_data.pkl",
): ...
```

______________________________________________________________________

## Writing Pytask Tasks

### File and Function Naming

### DO

- Name task files as `task_*.py` (e.g., `task_clean_data.py`)
- Name task functions as `task_*` (e.g., `task_clean_data`)
- Use `pathlib.Path` objects as default arguments for all file dependencies and products
- Use the reserved keyword `produces` for output files
- Use any other argument names for input dependencies

### DO NOT

- Use function names that do not start with `task_`
- Use file names that do not start with `task_`
- Use string paths instead of `pathlib.Path` objects
- Omit default values for task arguments (they are needed to build the dependency graph)

### Task Function Structure

### DO

- Keep task functions focused on three steps:
  1. Read input data
  1. Execute the task (preferably by calling a separate function)
  1. Write output
- Separate the actual computation logic into helper functions (prefixed with `_`)
- Make helper functions testable by keeping I/O separate from computation

### Example Simple Task

```python
from pathlib import Path
import pandas as pd

BLD = Path(__file__).parent / "bld"


def task_clean_data(raw_file=Path("gapminder.arrow"), produces=BLD / "data.pkl"):
    raw = pd.read_feather(raw_file)
    clean = _clean_data(raw)
    clean.to_pickle(produces)


def _clean_data(raw):
    df = raw.rename(
        columns={
            "lifeExp": "life_exp",
            "gdpPercap": "gdp_per_cap",
        },
    )
    return df.query("continent == 'Asia'")
```

______________________________________________________________________

## Tasks with Multiple Dependencies or Products

### DO

- Use a single `pathlib.Path` for single dependencies/products
- Use a dictionary or list of `pathlib.Path` objects for multiple dependencies/products
- Nest containers as needed, as long as atomic elements are `pathlib.Path` objects
- Use multiple keyword arguments for multiple dependencies

### Example Multiple Products

```python
BLD = Path(__file__).parent / "bld"

products = {
    "Asia": BLD / "life_expectancy_asia.svg",
    "Europe": BLD / "life_expectancy_europe.svg",
}


def task_plot_life_expectancy(
    data_file=BLD / "data.pkl",
    produces=products,
):
    df = pd.read_pickle(data_file)
    for region, fig_file in produces.items():
        fig = _plot_life_expectancy(df[df["continent"] == region])
        fig.write_image(fig_file)
```

______________________________________________________________________

## Reusing Task Functions (Looping Over Tasks)

### When to Loop Over Tasks vs Products

### DO Loop Over Tasks When

- Tasks are long-running (enables parallel execution)
- You need more granular caching (only re-run failed/changed tasks)
- Working with different model specifications
- Tasks are independent and can run in parallel

### DO Loop Over Products When

- Creating the same style of graphs from the same dataset
- Tasks are fast and simple
- You want to keep fewer task definitions

### Example Looping Over Tasks

```python
from pytask import task

BLD = Path(__file__).parent / "bld"

for region in ("Asia", "Europe"):

    @task(id=region)
    def task_plot_life_expectancy(
        data_file=BLD / "data.pkl",
        produces=BLD / f"life_expectancy_{region.lower()}.svg",
        region=region,
    ):
        df = pd.read_pickle(data_file)
        fig = _plot_life_expectancy(df[df["continent"] == region])
        fig.write_image(produces)
```

### DO

- Define the task function within a for loop
- Use the `@task(id=...)` decorator to set unique task IDs
- Set path arguments based on the loop variable
- Pass the loop variable as an argument if needed inside the function

### DO NOT

- Use `pytask.loop` (does not exist)
- Expect loop variables to be captured correctly without passing them as arguments

______________________________________________________________________

## Pytask Commands Reference

### DO Use These Commands

- `pytask` - Run all tasks that need updating
- `pytask collect` - List all collected tasks without running them
- `pytask collect --nodes` - Show tasks with their dependencies and products
- Use parallel execution for faster runtime on independent tasks

______________________________________________________________________

## Summary Checklist for AI Agents

When structuring a Python research project:

1. Create `src/` and `bld/` directories to separate source and output
1. Organize `src/` into `original_data/`, `data_management/`, `analysis/`,
   `model_specs/`, `final/`
1. Create a `config.py` with SRC, BLD path definitions using `pathlib`
1. Name task files as `task_*.py` and task functions as `task_*`
1. Use `pathlib.Path` default arguments for all file dependencies
1. Use `produces` keyword for output files
1. Keep task functions simple: read, compute (via helper), write
1. Use dictionaries for multiple products/dependencies
1. Loop over tasks (not products) for long-running or parallelizable work
1. Never commit generated files to version control
1. Document the project structure and setup in README
