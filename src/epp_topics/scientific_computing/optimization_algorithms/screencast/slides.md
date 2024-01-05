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

# Scientific Computing

### Choosing optimization algorithms

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Relevant problem properties

- **Smoothness**: Differentiable? Kinks? Discontinuities? Stochastic?
- **Convexity**: Are there local optima?
- **Goal**: Do you need a global solution? How precise?
- **Size**: 2 parameters? 10? 100? 1000? More?
- **Constraints**: Bounds? Linear constraints? Nonlinear constraints?
- **Structure**: Nonlinear least-squares, Log-likelihood function

$\rightarrow$ Properties guide selection but experimentation is important
$\rightarrow$ Always compare multiple algorithms in a criterion plot

---

# Try to make your problem simpler

- Get derivatives using automatic differentiation (JAX, pytorch)
- Make your function faster
- Make your function more stable
- Try to make your function smooth


---

# Choosing local optimizers


```mermaid {theme: 'dark', scale: 0.6}
graph LR
    classDef highlight fill:#FF4500;
    A["Do you have<br/>nonlinear constraints?"] -- yes --> B["differentiable?"]
    B["differentiable?"] -- yes --> C["'ipopt', 'nlopt_slsqp', 'scipy_trust_constr'"]
    B["differentiable?"] -- no --> D["'scipy_cobyla', 'nlopt_cobyla'"]

    A["Do you have<br/>nonlinear constraints?"] -- no --> E["Can you exploit<br/>a least-squares<br/>structure?"]
    E["Can you exploit<br/>a least-squares<br/>structure?"] -- yes --> F["differentiable?"]
    E["Can you exploit<br/>a least-squares<br/>structure?"] -- no --> G["differentiable?"]

    F["differentiable?"] -- yes --> H["'scipy_ls_lm', 'scipy_ls_trf', 'scipy_ls_dogleg'"]
    F["differentiable?"] -- no --> I["'nag_dflos', 'pounders', 'tao_pounders'"]

    G["differentiable?"] -- yes --> J["'scipy_lbfgsb', 'fides'"]
    G["differentiable?"] -- no --> K["'nlopt_bobyqa', 'nlopt_neldermead', 'neldermead_parallel'"]
```



---

# Choosing a global approach


```mermaid {theme: 'dark', scale: 0.6}
graph LR
    classDef highlight fill:#FF4500;
    A["Do you have<br/>3 or less<br/>parameters"] -- yes --> B["scipy_brute"]
    A["Do you have<br/>3 or less<br/>parameters"] -- no --> C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"]
    C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"] -- yes --> D["'nlopt_direct', 'nlopt_isres', 'pygmo_gaco',<br/>'pygmo_de', other pygmo algorithms"]
    C["Is your function<br/>very rugged with<br/>extremely many<br/>local optima?"] -- no --> E["choose a suitable local optimizer and do multistart"]
```

Always refine the result of a global optimizer with a local one
