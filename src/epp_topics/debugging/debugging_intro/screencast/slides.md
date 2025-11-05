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
title: EPP — Introduction to debugging
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Debugging

### Introduction to debugging

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# What is debugging

- Debugging means fixing code that does not do what it should
- Two main situations
    - Your code does not run
    - Your code runs but you know the results are wrong
- Debugging is a skill that can be learned

---

# Why debugging is is important


- According to studies, programmers spend between 25 and 50 % of their time debugging
- There are huge differences in debugging efficiency of different programmers!
- We need to spend some effort to:
  - Avoid debugging
  - Be better at debugging

---

# The two modes (Eisenstadt, 1993)

- **Inspeculation**, a hypbrid of:
  - "inspection" (code inspection),
  - "simulation" (hand-simulation),
  - and "speculation".
  - No experimentation, but "thinking about" the code.
- **Data gathering**
  - What we usually think of when talking about debugging
  - What a debugger can make drastically more efficient
- Striking parallel to the scientific method
