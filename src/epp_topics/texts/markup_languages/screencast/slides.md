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

# Texts, typesetting and text data

### Markup languages

<br>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What are markup languages?




<br/>
<br/>

> A markup language is a text-encoding system consisting of a set of symbols inserted in a text document to control its structure, formatting, or the relationship between its parts. (Wikipedia)

<br/>
<br/>


In short: Markup languages let us write pretty documents in plain text files!

---

# Hypertext Markup Language (HTML)

<br/>
<br/>

<div class="grid grid-cols-2 gap-4">
<div>

```html
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```


</div>
<div>

<br/>

## My First Heading

My first paragraph.

</div>
</div>



---

# The workhorse of academia: LaTeX


<br/>
<br/>

<div class="grid grid-cols-2 gap-20">
<div>

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}

\begin{document}

\section*{My First Heading}
My first paragraph.

\end{document}
```


</div>
<div>

<br/>
<br/>

## My First Heading

My first paragraph.

</div>
</div>


---

# It doesn't have to be hard: Markdown


<br/>
<br/>

<div class="grid grid-cols-2 gap-20">
<div>

<br/>
<br/>

```markdown
## My First Heading

My first paragraph.
```


</div>
<div>

<br/>
<br/>

## My First Heading

My first paragraph.

</div>
</div>


---


# Why use markup languages (and not word)?

<br/>

Markup languages can create pretty documents in plain text files

- Better version control
- Powerful editors like vscode
- Easy automation
