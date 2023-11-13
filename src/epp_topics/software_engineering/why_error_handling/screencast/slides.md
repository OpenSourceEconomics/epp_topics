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
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### Why and where to raise errors

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- You have seen what good tracebacks and error messages give you:
  - Where did something go wrong?
  - What exactly went wrong?
  - Sometimes: How can you fix it
- You might also have got some error messages that were not helpful at all

<br/>

In this section, you will learn how to add great error handling to your code


---

# Example

<div class="flex gap-4">
<div>

```python
def create_markdown_table(data):
    """Create a markdown table from a list
    of dictionaries or dictionary of lists.

    """
    if isinstance(data, dict):
        lod = convert_dol_to_lod(data):
    else:
        lod = data

    keys = list(lod[0])

    lines = [
        _create_header(keys),
        _create_separator(len(keys)),
    ]

    for row in lod:
        lines.append(_create_data_row(row))

    return "\n".join(lines)
```

</div>
<div>

```python
def _create_header(keys):
    header = "|"
    for key in keys:
        header += f" {key} |"
    return header


def _create_separator(n_cols):
    separator = "|"
    for _ in range(n_cols):
        separator += " ------ |"
    return separator


def _create_data_row(row_dict):
    row_string = "|"
    for key in row_dict:
        row_string += f" {row_dict[key]} |"
    return row_string
```


</div>
</div>


---

# Which errors to handle?

- If your function is correct the only source of errors is `data`
- To make sure your function is correct, testing is better than error
handling
- So what could go wrong with `data`?
  - `data` is neither a list nor a dict
  - `data` is a dict but contains values that are not lists
  - `data` is a dict of list but the list have unequal length
  - `data` is a list, but contains entries that are not dicts
  - `data` is a list of dicts but the dicts have different keys

---

# Goals

- Raise errors as early as possible
- Absolutely avoid duplicated code for error handling
- Try to avoid running checks repeatedly


---

# Where to handle errors in the example

- in `create_markdown_table`
  - `data` is neither a list nor a dict
- in `convert_dol_to_lod`:
  - `data` is a dict but contains values that are not lists
  - `data` is a dict of list but the list have unequal length
- in a function that also gets called in `convert_lod_to_dol`
  - `data` is a list, but contains entries that are not dicts
  - `data` is a list of dicts but the dicts have different keys
