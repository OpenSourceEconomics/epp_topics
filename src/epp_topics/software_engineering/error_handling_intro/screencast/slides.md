---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: EPP — Software Engineering — Introduction to error handling
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Software engineering

### Introduction to error handling

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- You have seen what good tracebacks and error messages give you:
  - Where did something go wrong?
  - What exactly went wrong?
  - Sometimes: How can you fix it
- You might also have seen some error messages that were not helpful at all

<br/>

Goal: Learn how to add great error handling to your code


---

# Example

<div class="flex gap-4">
<div>

```python
def create_markdown_table(data):
    """Create a markdown table from a list of
    dictionaries or a dictionary of lists.

    """
    if isinstance(data, dict):
        lod = convert_dol_to_lod(data)
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
