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
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Miscellaneous Tools

### Navigation in the Unix shell

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Motivation

- Your shell has a present-working-directory (pwd)
- By default, the home directory
- Typically, you want the pwd to be your project folder
  - Can use right click in your file explorer (inefficient)
  - Can use `cd`
- Optionally, you can also create, copy and delete files in the shell

---

# Unix File System

<div class="grid grid-cols-2 gap-45">
<div>

```mermaid {theme: 'dark', scale: 1}
graph LR
    classDef highlight fill:#FF4500;
    A["/"] --- B["etc"]
    A["/"] --- C["usr"]
    C["usr"] --- D["bin"]
    C["usr"] --- E["lib"]
    A["/"] --- F["var"]
    F["var"] --- G["log"]
    A["/"] --- H["home"]
    H["home"] --- I["user_1"]
    I["user_1"] --- J["Documents"]
    I["user_1"] --- K["Downloads"]
    I["user_1"] --- L["mambaforge"]
    class A highlight
    class H highlight
    class I highlight
    class L highlight
```
</div>
<div>

### GUI representation

<center>
<img src="/unix_path_mambaforge.png" width=450>
</center>

### Shell representation

/home/user_1/mambaforge

</div>
</div>


---

# Where to store your projects

- Good idea to store all git repositories somewhere close to home directory
- Example:

```mermaid {theme: 'dark', scale: 1}
graph LR
    A["/home/user_1"] --- B["projects"]
    B["projects"] --- C["master_thesis"]
    B["projects"] --- D["epp"]
    D["epp"] --- E["exercises"]
    D["epp"] --- F["assignments"]
    D["epp"] --- G["final_project"]
```

---

# The z command

- Only type rough names of files to jump to them
- Similar to fuzzy matching in VS Code!
- Gets better the more you use it!
- Installation: https://github.com/rupa/z
