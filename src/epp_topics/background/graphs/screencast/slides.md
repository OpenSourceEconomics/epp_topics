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
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Background

### A Primer on Graphs

<br/>

Janoś Gabler and Hans-Martin von Gaudecker


---

# Graph definition

A graph $G$ is a pair $(N, E)$ of sets, where $N$ are nodes and $E$ are edges:

$$G = (N, E)$$

Edges are
- sets of two nodes (undirected graphs)
- pairs of nodes (directed graphs)


---

# Chain (undirected)

<div class="grid grid-cols-2 gap-45">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, x_2, x_3\} \\[2ex]
E = & \big\{ \\
    & \quad \{x_0, x_1\}, \\
    & \quad \{x_1, x_2\}, \\
    & \quad \{x_2, x_3\} \\
    & \big\}
\end{align*}
$$


</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_0 --- x_1
    x_1 --- x_2
    x_2 --- x_3
```

</div>
</div>


---

# Chain (undirected)

<div class="grid grid-cols-2 gap-45">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, x_2, x_3\} \\[2ex]
E = & \big\{ \\
    & \quad \{x_1, x_0\}, \\
    & \quad \{x_1, x_2\}, \\
    & \quad \{x_2, x_3\} \\
    & \big\}
\end{align*}
$$


</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_0 --- x_1
    x_1 --- x_2
    x_2 --- x_3
```

</div>
</div>


---

# Chain (directed)

<div class="grid grid-cols-2 gap-45">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, x_2, x_3\} \\[2ex]
E = & \big\{ \\
    & \quad (x_0, x_1), \\
    & \quad (x_1, x_2), \\
    & \quad (x_2, x_3) \\
    & \big\}
\end{align*}
$$

</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_0 --> x_1
    x_1 --> x_2
    x_2 --> x_3
```

</div>
</div>


---

# Tree (undirected)

<div class="grid grid-cols-2 gap-20">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, \ldots, x_8\} \\[2ex]
E = & \big\{ \\
    & \quad \{x_0, x_1\}, \{x_1, x_2\},  \{x_2, x_3\}, \\
    & \quad \{x_2, x_4\}, \{x_1, x_5\}, \{x_5, x_6\}, \\
    & \quad \{x_5, x_7\}, \{x_5, x_8\} \\
    & \big\}
\end{align*}
$$

</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_4((x<sub>4</sub>))
    x_5((x<sub>5</sub>))
    x_6((x<sub>6</sub>))
    x_7((x<sub>7</sub>))
    x_8((x<sub>8</sub>))
    x_0 --- x_1
    x_1 --- x_2
    x_2 --- x_3
    x_2 --- x_4
    x_1 --- x_5
    x_5 --- x_6
    x_5 --- x_7
    x_5 --- x_8
```

</div>
</div>


---

# Tree (directed, "arborescence")

<div class="grid grid-cols-2 gap-20">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, \ldots, x_8\} \\[2ex]
E = & \big\{ \\
    & \quad (x_0, x_1), (x_1, x_2),  (x_2, x_3), \\
    & \quad (x_2, x_4), (x_1, x_5), (x_5, x_6), \\
    & \quad (x_5, x_7), (x_5, x_8) \\
    & \big\}
\end{align*}
$$

</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_4((x<sub>4</sub>))
    x_5((x<sub>5</sub>))
    x_6((x<sub>6</sub>))
    x_7((x<sub>7</sub>))
    x_8((x<sub>8</sub>))
    x_0 --> x_1
    x_1 --> x_2
    x_2 --> x_3
    x_2 --> x_4
    x_1 --> x_5
    x_5 --> x_6
    x_5 --> x_7
    x_5 --> x_8
```

</div>
</div>


---

# Directed Acyclic Graph (DAG)

<div class="grid grid-cols-2 gap-20">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, \ldots, x_8\} \\[2ex]
E = & \big\{ \\
    & \quad (x_0, x_1), (x_1, x_2),  (x_2, x_3), \\
    & \quad (x_2, x_4), (x_1, x_5), (x_5, x_6), \\
    & \quad (x_5, x_7), (x_5, x_8), (x_4, x_6) \\
    & \big\}
\end{align*}
$$

</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_4((x<sub>4</sub>))
    x_5((x<sub>5</sub>))
    x_6((x<sub>6</sub>))
    x_7((x<sub>7</sub>))
    x_8((x<sub>8</sub>))
    x_0 --> x_1
    x_1 --> x_2
    x_2 --> x_3
    x_2 --> x_4
    x_1 --> x_5
    x_5 --> x_6
    x_5 --> x_7
    x_5 --> x_8
    x_4 --> x_6
```

</div>
</div>


---

# Directed ~~Acyclic~~ Graph

<div class="grid grid-cols-2 gap-20">
<div>

$$
\begin{align*}
N = & \{x_0, x_1, \ldots, x_8\} \\[2ex]
E = & \big\{ \\
    & \quad (x_0, x_1), (x_1, x_2),  (x_2, x_3), \\
    & \quad (x_2, x_4), (x_1, x_5), (x_5, x_6), \\
    & \quad (x_5, x_7), (x_5, x_8), (x_4, x_6), \\
    & \quad (x_5, x_0) \\
    & \big\}
\end{align*}
$$

</div>
<div>

```mermaid {theme: 'dark', scale: 1}
graph BT
    x_0((x<sub>0</sub>))
    x_1((x<sub>1</sub>))
    x_2((x<sub>2</sub>))
    x_3((x<sub>3</sub>))
    x_4((x<sub>4</sub>))
    x_5((x<sub>5</sub>))
    x_6((x<sub>6</sub>))
    x_7((x<sub>7</sub>))
    x_8((x<sub>8</sub>))
    x_0 --> x_1
    x_1 --> x_2
    x_2 --> x_3
    x_2 --> x_4
    x_1 --> x_5
    x_5 --> x_6
    x_5 --> x_7
    x_5 --> x_8
    x_4 --> x_6
    x_5 --> x_0
```

</div>
</div>


---

# Graph Use Cases

- The file system
- Git
- Reproducible research
- Causal theory
- Behavioural economics
- ...
