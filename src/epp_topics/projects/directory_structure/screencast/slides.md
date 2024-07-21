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
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Reproducible Research


### Directory structure in the templates

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---


# Guiding principles

- Clear separation of inputs and outputs
  - need separate `src` and `bld` folder
- Group files in directories by step of the analysis
  - need `data_management`, `analysis`, `model_specs`, `final` inside `src`
- Separation of long-running analysis tasks from fast visualizations
  - need to separate `analysis` and `final`
