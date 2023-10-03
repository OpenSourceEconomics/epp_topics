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

# Background

### A Brief History of Operating Systems

<br/>

Janoś Gabler and Hans-Martin von Gaudecker


---

# Two broad lines


<div class="grid grid-cols-2 gap-4">
<div>

1. Unix-based/inspired (Linux, MacOS X)
<br/>

1. Windows



</div>
<div>

<center>
<img src="vt100.jpg" width=350>
</center>

<br/>
<br/>

</div>
</div>

---

# Unix

<div class="grid grid-cols-2 gap-4">
<div>

- Developed at Bell labs starting 1969 ([some history](https://arstechnica.com/gadgets/2019/08/unix-at-50-it-starts-with-a-mainframe-a-gator-and-three-dedicated-researchers))
- Quickly evolved to become the main OS for servers.
- Became a commercial product in the early 1980s.
- Early OSS spin-offs: Berkeley Software Distribution (BSD) and GNU's Not
  Unix (GNU).

</div>
<div>

<center>
<img src="bell-labs.jpg" width=350>
</center>

</div>
</div>

---

# Linux

<div class="grid grid-cols-2 gap-4">
<div>

- In 1991, Linus Torvalds wrote a new kernel inspired by the Unix
  kernel from scratch.
- Many flavours of Linux today: Debian, Ubuntu, Red Hat, Mint,
  Android, ...

</div>
<div>

<center>
<img src="linus.jpg" width=350>
</center>

</div>
</div>


---

# MacOS X

<div class="grid grid-cols-2 gap-4">
<div>

- After parting ways with Apple in the 1980s, Steve Jobs founded a
  company called NeXT.
- Developed the OS NeXTstep, which was based partly on the BSD.
- NeXT was bought by Apple in 1996
- Eventually brought back Jobs as CEO.
- MacOS X, iOS, ... all based on NeXTstep and thus BSD, Unix.

</div>
<div>

<center>
<img src="stevejobs-next.jpg" width=300>
</center>

</div>
</div>


---

# POSIX

- Stands for Portable Operating System Interface
- Aims to establish a standard for Unix derivatives.


---


# Windows

<div class="grid grid-cols-2 gap-4">
<div>

- Complex history of corporate collaborations between Microsoft / IBM.
- Big break between MS-DOS / Windows 9x and Windows NT, XP, subsequent
  versions.

</div>
<div>

<center>
<img src="windows-1-desktop.jpg" width=350>
</center>

</div>
</div>


---

# Signs of convergence

- Most of Microsoft's cloud services seem to be running Linux
- Since version 10, Windows includes the [Windows Subsystem for Linux
  (WSL)](https://docs.microsoft.com/en-us/windows/wsl)
