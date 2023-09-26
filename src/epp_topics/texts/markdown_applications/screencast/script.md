# Script: Markdown applications

There is only a title slide. Just do a live demo:

## Zulip demo: Write the following message

````markdown
In the task where we should use Python to calculate the output value of a Cobb-Douglas
production function (assignment 1, exercise 2) the following line:

```python
cobb_douglas(labor, capital, alpha)
```

gives me a type error:

```pytb
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'float'
```

I don't understand the error because I'm just passing in numbers.

Here is a minimal example to reproduce the error:

```python
labor = (2.5,)
capital = 4.5
alpha = 0.33


def cobb_douglas(labor, capital, alpha):
    return labor**alpha * capital ** (1 - alpha)


cobb_douglas(labor, capital, alpha)
```

I attach the entire traceback as `txt` file ...

````

## GitHub demo

- Open [epp_topics github](https://github.com/OpenSourceEconomics/epp_topics) and create
  an issue in Markdown. The issue content could be something:

```markdown
We should add the following screencasts on the shell soon:

- A short history of computer interfaces
- Shell navigation on linux and mac
- Shell navigation on windows

@janosg, can you come up with a first draft?
```
