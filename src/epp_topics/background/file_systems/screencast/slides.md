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
themeConfig:
  paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br>

# Background

### File Systems

<br>

Janoś Gabler and Hans-Martin von Gaudecker


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
```
</div>
<div>

</div>
</div>


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

<div v-click>

### GUI representation

<center>
<img src="unix_path_mambaforge.png" width=450>
</center>

</div>

<div v-click>

### Shell representation

/home/user_1/mambaforge

</div>
</div>
</div>


---

# Windows File System

<div class="grid grid-cols-2 gap-45">
<div>

```mermaid {theme: 'dark', scale: 0.8}
graph LR
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
```
<br>
<br>
</div>
<div>

</div>
</div>


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
<br>
<br>
</div>
<div>

<div v-click>

### GUI representation

<center>
<img src="windows_path_mambaforge.png" width=250>
</center>

</div>

<div v-click>

### Shell representation

C:\Users\user_1\mambaforge

</div>
</div>
</div>
