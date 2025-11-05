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
title: EPP — Functional data management — Fundamental rules
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Data management with pandas

### Functional data management: Fundamental rules

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---


<div class="grid grid-cols-2 gap-4">
<div>

# Example

```python
>>> def clean(df):
...     out = pd.DataFrame()
...     out["a"] = convert_to_ordered_cat(df["Q001"])
...     out["b"] = convert_to_ordered_cat(df["Q002"])
...     out["c"] = _clean_c(df["Q003"], out["b"])
...     return out
```
</div>
<div>

# Rules

- Start with an empty DataFrame for the clean data

- Touch every variable just once

</div>
</div>
