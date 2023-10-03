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

# Reproducible Research


### What does pytask do?

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# A tiny example project



<div class="flex gap-12">
<div>

```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A["example"] --- B["gapminder.arrow"]
    A["example"] --- C["task_clean_data.py"]
    A["example"] --- D["task_plot_life_expectancy.py"]
```


</div>
<div>

- `example/task_clean_data.py`
  - Contains the function `task_clean_data`
  - If called, the function reads in `example/gapminder.arrow` and produces
    `example/bld/data.pkl`
- `example/task_plot_life_expectancy.py`
  - Contains the function `task_plot_life_expectancy`
  - If called, the function reads in `example/bld/data.pkl` and produces
    `example/bld/life_expectancy.svg`


</div>
</div>

---

# Step 1: collection

<div class="grid grid-cols-2 gap-12">
<div>

<br/>

- Go through all folders in working directory
- Collect all files with name `task_XXX.py`
- Go through those files and collect all functions that start with `task_`
- Task functions and their (default) inputs will be used to construct the workflow

</div>
<div>

<img src="collect.png" class="rounded" width="350"/>


</div>
</div>


---

# Step 2: Dependency graph (DAG)


<div class="grid grid-cols-2 gap-4">
<div>

- Inspect function signatures to build a dependency graph
- `produces` describes function output
- Other arguments are function dependencies
- DAG structure enables to determine an order of execution that respects dependency
structure (topological sort)

</div>
<div>

<img src="collect_nodes.png" class="rounded" width="350"/>


</div>
</div>


---

# Can you see the DAG?

<div class="grid grid-cols-2 gap-30">
<div>

<img src="collect_nodes.png" class="rounded" width="350"/>

</div>
<div>


```mermaid {theme: 'dark', scale: 0.7}
graph TD
    classDef highlight fill:#FF4500;
    X["example/gapminder.arrow"] ---> A["task_clean_data.py::task_clean_data"]
    A["task_clean_data.py::task_clean_data"] ---> B["example/bld/data.pkl"]
    B["example/bld/data.pkl"] ---> C["task_plot_life_expectancy.py::task_plot_life_expectancy"]
    C["task_plot_life_expectancy.py::task_plot_life_expectancy"] ---> D["example/bld/life_expectancy.svg"]

```

</div>
</div>

---

# Step 3: Track changes and execute

- Pytask knows which files should need to be generated
- Also keeps track on when code or products have changed
- Functions are only run if:
    - They have changed
    - A dependency has changed
- Huge time savings in large empirical projects!


---

# Run the first time

<img src="run_1.png" class="rounded" width="700"/>

---

# Delete plot and run again

<img src="run_2_after_deleting_plot.png" class="rounded" width="700"/>

---

# Delete cleaned data and run again

<img src="run_3_after_deleting_data.png" class="rounded" width="700"/>
