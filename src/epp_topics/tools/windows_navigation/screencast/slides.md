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
title: EPP — Tools — Navigation in the Windows shell
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Miscellaneous Tools

### Navigation in the Windows shell

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

# Windows File System

<div class="grid grid-cols-2 gap-45">
<div>

```mermaid {theme: 'dark', scale: 0.8}
graph LR
    classDef highlight fill:#FF4500;
    A[C:]
    A --> B["Program Files"]
    B --> C["Microsoft"]
    B --> D["Adobe"]
    A --> E["Users"]
    E --> F["user_1"]
    F --> H["Documents"]
    F --> I["Downloads"]
    F --> P["mambaforge"]
    A --> M["Windows"]
    M --> N["System32"]
    A --> O["ProgramData"]
    X["I:"] --> Z["Second Drive"]
    class A highlight
    class E highlight
    class F highlight
    class P highlight
```
<br/>
<br/>
</div>
<div>


### GUI representation

<center>
<img src="/windows_path_mambaforge.png" width=250>
</center>


### Shell representation

C:\Users\user_1\mambaforge

</div>
</div>


---

# Where to store your projects

- Good idea to store all git repositories somewhere close to home directory
- Example:

```mermaid {theme: 'dark', scale: 1}
graph LR
    A["C:\Users\user_1"] --- B["projects"]
    B["projects"] --- C["master_thesis"]
    B["projects"] --- D["epp"]
    D["epp"] --- E["exercises"]
    D["epp"] --- F["assignments"]
    D["epp"] --- G["final_project"]
```
