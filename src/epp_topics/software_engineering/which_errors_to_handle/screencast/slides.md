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

### Which errors to handle

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

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
