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
title: EPP — Optimization — Choosing optimization algorithms
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Numerical Optimization

### Choosing optimization algorithms

<br/>

Janoś Gabler and Hans-Martin von Gaudecker

---

# [Steps for choosing an algorithm](https://optimagic.readthedocs.io/en/latest/how_to/how_to_algorithm_selection.html#the-three-steps-for-selecting-algorithms)

<br/>

1. Theory (intro here)

1. Experimentation (histories video)

1. Refine until convergence

---

# Relevant problem properties

- **Smoothness**: Differentiable? Kinks? Discontinuities? Stochastic?

- **Convexity**: Are there local optima?

- **Goal**: If not convex, do you need a global solution? How precise does a solution
  need to be?

- **Size**: 2 parameters? 10? 100? 1,000? Millions? Billions?

- **Constraints**: Bounds? Linear constraints? Nonlinear constraints?

- **Structure**: Nonlinear least-squares, Log-likelihood function

$\rightarrow$ Properties guide selection but experimentation is important

$\rightarrow$ Always compare multiple algorithms in a criterion plot

---

# Try to make your problem simpler

- Get derivatives using automatic differentiation (JAX, pytorch)

- Make your function faster

- Make your function more stable

- Make your function smooth

---

# Choosing local optimizers

Next slide has a practical guide, see [optimagic
docs](https://optimagic.readthedocs.io/en/latest/how_to/how_to_algorithm_selection.html#how-to-select-a-local-optimizer)
for more details.

---

```mermaid {theme: 'dark', scale: 0.6}
graph LR
    classDef highlight fill:#FF4500;
    A["Do you have<br/>nonlinear<br/>constraints?"] -- yes --> B["differentiable?"]
    B["Is your objective function differentiable?"] -- yes --> C["ipopt<br/>nlopt_slsqp<br/>scipy_trust_constr"]
    B["differentiable?"] -- no --> D["scipy_cobyla<br/>nlopt_cobyla"]

    A["Do you have<br/>nonlinear constraints?"] -- no --> E["Can you exploit<br/>a least-squares<br/>structure?"]
    E["Can you exploit<br/>a least-squares<br/>structure?"] -- yes --> F["differentiable?"]
    E["Can you exploit<br/>a least-squares<br/>structure?"] -- no --> G["differentiable?"]

    F["differentiable?"] -- yes --> H["scipy_ls_lm<br/>scipy_ls_trf<br/>scipy_ls_dogbox"]
    F["differentiable?"] -- no --> I["tranquilo<br/>nag_dflos<br/>pounders"]

    G["differentiable?"] -- yes --> J["scipy_lbfgsb<br/>nlopt_lbfgsb<br/>fides"]
    G["differentiable?"] -- no --> K["nlopt_bobyqa<br/>nlopt_neldermead<br/>neldermead_parallel"]
```

---

# Choosing a global approach

```mermaid {theme: 'dark', scale: 0.6}
graph LR
    classDef highlight fill:#FF4500;
    A["Do you have<br/>3 or less<br/>parameters"] -- yes --> B["scipy_brute"]
    A["Do you have<br/>3 or less<br/>parameters"] -- no --> C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"]
    C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"] -- yes --> D["nlopt_direct<br/>nlopt_isres<br/>pygmo_gaco<br/>pygmo_de<br/>other pygmo algorithms"]
    C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"] -- no --> E["choose a suitable local optimizer and do multistart"]
```

Always refine the result of a global optimizer with a local one
