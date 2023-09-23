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

### Markdown syntax

<br>


Janoś Gabler and Hans-Martin von Gaudecker



---

# Syntax (Headings)

<br/>


<div class="grid grid-cols-2 gap-4">
<div>

<br/>

```
# The largest heading




## The second largest heading



###### The smallest heading
```

</div>
<div>

<br/>

# The Title

<br/>

## The second largest heading

<br/>
<br/>

###### The smallest heading

</div>
</div>

---

# Styling text

<br/>

<div class="grid grid-cols-2 gap-30">
<div>

```

**bold**

*italic*

~~strikethrough~~

***bold and italic***
```


</div>
<div>

**bold**

*italic*

~~strikethrough~~

***bold and italic***


</div>
</div>

---

# Lists

<br/>

<div class="grid grid-cols-2 gap-30">
<div>

```

- This is
- a
- list





1. This is
2. an
3. enumeration
```


</div>
<div>

- This is
- a
- list

<br/>
<br/>

1. This is
2. an
3. enumeration


</div>
</div>


---

# Links and Quotes


<br/>
<br/>

<div class="grid grid-cols-2 gap-30">
<div>

```

[This will be a link](www.google.com)



> This will be a
> multi-line quote
```


</div>
<div>

[This will be a link](www.google.com)

<br/>
<br/>


> This will be a
> multi-line quote


</div>
</div>

---


# Code Snippets

This is the most important one for communication on zulip!!!

<div class="grid grid-cols-2 gap-30">
<div>

<br/>

<pre>
`x = 10`

```python
def f(x):
   return np.ones_like(x)
```
</pre>



</div>
<div>

<br/>

`x = 10`

<br/>
<br/>
<br/>




```python
def f(x):
   return np.ones_like(x)
```


</div>
</div>
