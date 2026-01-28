# Numerical Optimization - Guidelines for AI Coding Agents

This document provides guidelines for AI coding agents implementing numerical
optimization code based on the recommendations from the Effective Programming Practices
for Economists course.

## Table of Contents

1. [Core Concepts](#core-concepts)
1. [Using optimagic](#using-optimagic)
1. [Algorithm Selection](#algorithm-selection)
1. [Function Setup Best Practices](#function-setup-best-practices)
1. [Debugging and Diagnostics](#debugging-and-diagnostics)
1. [Algorithm-Specific Guidance](#algorithm-specific-guidance)

______________________________________________________________________

## Core Concepts

### Terminology

- **Criterion function** (or objective function): The function being minimized or
  maximized
- **Parameters** (or params, variables): The vector of numbers to optimize over
- **Bounds** (or box constraints): Lower and upper bounds for parameters
- **Constraints**: Conditions that must be satisfied at the optimum
- **Solution**: Usually refers to the argmin/argmax, not just the min/max value

### Key Insight

Choosing the right optimizer can make the difference between:

- Minutes vs. weeks of computation time
- Reliable solutions vs. painful manual intervention

______________________________________________________________________

## Using optimagic

optimagic provides a unified interface to optimization algorithms from many libraries.
Always use optimagic for numerical optimization in this codebase.

### Basic Usage

```python
import numpy as np
import optimagic as om


def sphere(x):
    return (x**2).sum()


start_params = np.ones(5)

res = om.minimize(
    fun=sphere,
    params=start_params,
    algorithm="scipy_lbfgsb",
)
```

### DO's

- **DO** use `om.minimize()` for minimization and `om.maximize()` for maximization
- **DO** explicitly specify the algorithm - there is no default optimizer because no
  single algorithm works well for all problems
- **DO** use structured parameter formats (dicts, nested structures) for complex
  problems
- **DO** inspect the result object attributes: `res.params`, `res.criterion`,
  `res.n_criterion_evaluations`, `res.success`, `res.message`
- **DO** use `np.inf` and `-np.inf` for unbounded parameters when needed

### DON'Ts

- **DON'T** rely on a default optimizer - always specify one explicitly
- **DON'T** assume the optimization succeeded without checking `res.success`
- **DON'T** use flat vectors for parameters in complex models - use structured formats

### Structured Parameters Example

```python
params = {"a": 0, "b": 1, "c": pd.Series([2, 3, 4])}


def dict_sphere(x):
    return x["a"] ** 2 + x["b"] ** 2 + (x["c"] ** 2).sum()


res = om.minimize(
    fun=dict_sphere,
    params=params,
    algorithm="scipy_neldermead",
)
```

### Specifying Bounds

```python
res = om.minimize(
    fun=dict_sphere,
    params=params,
    algorithm="scipy_neldermead",
    lower_bounds={"b": 0.5},  # Only specify bounds for parameters that need them
    upper_bounds={"a": 10.0},
)
```

______________________________________________________________________

## Algorithm Selection

### Three-Step Process

1. **Theory**: Use problem properties to select candidate algorithms
1. **Experimentation**: Compare algorithms using criterion plots
1. **Refine**: Iterate until convergence is achieved

### Relevant Problem Properties

| Property    | Questions to Ask                                                          |
| ----------- | ------------------------------------------------------------------------- |
| Smoothness  | Is it differentiable? Are there kinks? Discontinuities? Is it stochastic? |
| Convexity   | Are there local optima?                                                   |
| Goal        | Do you need a global solution? How precise?                               |
| Size        | How many parameters? (2? 10? 100? 1000+?)                                 |
| Constraints | Bounds only? Linear constraints? Nonlinear constraints?                   |
| Structure   | Is it a least-squares problem? Log-likelihood?                            |

### Local Optimizer Selection Guide

#### With Nonlinear Constraints

| Differentiable? | Recommended Algorithms                       |
| --------------- | -------------------------------------------- |
| Yes             | `ipopt`, `nlopt_slsqp`, `scipy_trust_constr` |
| No              | `scipy_cobyla`, `nlopt_cobyla`               |

#### Without Nonlinear Constraints - Least-Squares Structure

| Differentiable? | Recommended Algorithms                           |
| --------------- | ------------------------------------------------ |
| Yes             | `scipy_ls_lm`, `scipy_ls_trf`, `scipy_ls_dogbox` |
| No              | `tranquilo`, `nag_dflos`, `pounders`             |

#### Without Nonlinear Constraints - General Problems

| Differentiable? | Recommended Algorithms                                    |
| --------------- | --------------------------------------------------------- |
| Yes             | `scipy_lbfgsb`, `nlopt_lbfgsb`, `fides`                   |
| No              | `nlopt_bobyqa`, `nlopt_neldermead`, `neldermead_parallel` |

### Global Optimizer Selection Guide

| Condition                                   | Recommended Approach                                    |
| ------------------------------------------- | ------------------------------------------------------- |
| 3 or fewer parameters                       | `scipy_brute` (grid search)                             |
| Many parameters, smooth function            | Multistart with a local optimizer                       |
| Very rugged function with many local optima | `nlopt_direct`, `nlopt_isres`, `pygmo_gaco`, `pygmo_de` |

### DO's for Algorithm Selection

- **DO** always compare multiple algorithms using criterion plots
- **DO** refine the result of a global optimizer with a local optimizer
- **DO** use multistart optimization for non-convex problems when feasible
- **DO** consider `fides` - it is often underrated and performs well

### DON'Ts for Algorithm Selection

- **DON'T** assume one algorithm works for all problems
- **DON'T** use grid search with more than 3 parameters (curse of dimensionality)
- **DON'T** expect global optimizers to be precise - always refine locally
- **DON'T** use Nelder-Mead by default - it is widely used but rarely optimal

______________________________________________________________________

## Function Setup Best Practices

### Making Your Problem Simpler

1. **Get derivatives using automatic differentiation** (JAX, PyTorch)

   - Can provide 5-50x speedups
   - Game changer if applicable to your problem

1. **Make your function faster**

   - Profile and optimize bottlenecks
   - Consider vectorization

1. **Make your function more stable**

   - Example: Evaluate log densities instead of densities in likelihood functions

1. **Make your function smooth**

   - Example: Use kernel smoothing in method of simulated moments

### DO's for Criterion Functions

- **DO** start with relatively narrow bounds around parameters and iteratively relax
  them
- **DO** ensure all parameters have finite bounds for global optimization
- **DO** spend time finding good starting values - this is crucial
- **DO** return scalar values from your criterion function

### DON'Ts for Criterion Functions

- **DON'T** underestimate the time needed to define a good criterion function
- **DON'T** ignore numerical stability issues
- **DON'T** use bounds that are too wide initially

______________________________________________________________________

## Debugging and Diagnostics

### Criterion Plots

Always visualize optimization histories to compare algorithm performance.

```python
# Single optimization
om.criterion_plot(res)

# With monotone option (shows current best value)
om.criterion_plot(res, monotone=True)

# Limit x-axis
om.criterion_plot(res, max_evaluations=300)

# Compare multiple optimizations
results = {}
for algo in ["scipy_neldermead", "nlopt_neldermead", "fides"]:
    results[algo] = om.minimize(sphere, np.arange(10), algorithm=algo)

om.criterion_plot(results, max_evaluations=200)
```

### DO's for Debugging

- **DO** always run at least two optimizers and compare them in a criterion plot
- **DO** use `monotone=True` when there are extreme values in the history
- **DO** check which optimizer found the lowest/highest value
- **DO** check which optimizer converged fastest
- **DO** use dictionaries as input to `criterion_plot` for automatic legends

### DON'Ts for Debugging

- **DON'T** assume an optimization succeeded without visual inspection
- **DON'T** assume you found the global optimum just because an optimizer converged
- **DON'T** ignore the optimization history

### What You Can Learn from Criterion Plots

- Which optimizer was faster
- Which optimizer found the better solution
- Whether optimization is still making progress
- Whether you might be stuck in a local optimum

### What You Cannot Learn from Criterion Plots

- Whether you found the global optimum
- Whether you picked the perfect optimizer

______________________________________________________________________

## Algorithm-Specific Guidance

### Grid Search

**Use when**: 1-3 parameters, need guaranteed coverage

**Properties**:

- Needs finite bounds on all parameters
- Desired precision determines number of grid points
- Cannot get stuck in local minima

**Warning - Curse of Dimensionality**:

- With p parameters and n grid points per dimension: n^p evaluations needed
- Example: 5 parameters, 100 grid points = 10^10 evaluations = ~115 days at 1ms/eval

### Derivative-Based Line Search (e.g., L-BFGS-B)

**Use when**: Function is differentiable, no nonlinear constraints

**How it works**:

1. Use first derivative to get step direction
1. Use (approximated) second derivative to guess step length
1. Line search to refine step length
1. Accept and repeat

**Properties**:

- No tuning parameters needed (big advantage)
- Can get stuck in local minima
- Standard gradient descent may be better for very high-dimensional problems (Hessian
  becomes too large)

### Derivative-Based Trust Region (e.g., fides)

**Use when**: Function is differentiable, want robust convergence

**How it works**:

1. Build quadratic Taylor approximation within trust region
1. Minimize the approximation
1. Compare expected vs actual improvement
1. Adjust trust region radius accordingly

**Properties**:

- Smaller trust regions give better approximations
- Can reject bad steps (more robust than line search)
- Can get stuck in local minima

### Derivative-Free Direct Search (e.g., Nelder-Mead)

**Use when**: Function is not differentiable, relatively few parameters

**How it works**:

1. Explore parameter space systematically in a pattern
1. Accept best values
1. Adjust step sizes based on success/failure

**Properties**:

- Only uses ordering information (which value is smallest), not magnitudes
- Slow but robust to small amounts of noise
- Does NOT help with large amounts of noise
- Nelder-Mead is very widely used but very seldomly the best choice

### Derivative-Free Trust Region (e.g., BOBYQA, COBYLA)

**Use when**: No derivatives available, want trust region robustness

**How it works**:

- Similar to derivative-based trust region
- Uses surrogate model (interpolation or regression) instead of Taylor approximation

**Properties**:

- Interpolation: Exact fit at evaluation points
- Regression: Better for noisy functions (uses more evaluation points)
- Better fit within trust region than derivative-based methods
- Use when you only have numerical derivatives (faster than finite differences)

______________________________________________________________________

## Quick Reference

### Minimum Code Template

```python
import numpy as np
import optimagic as om


def criterion(params):
    # Your objective function here
    return scalar_value


start_params = ...  # Your initial guess
bounds = ...  # Optional: {"param_name": (lower, upper)}

res = om.minimize(
    fun=criterion,
    params=start_params,
    algorithm="scipy_lbfgsb",  # Choose based on problem properties
    lower_bounds=lower_bounds,  # Optional
    upper_bounds=upper_bounds,  # Optional
)

# Always check results
print(f"Success: {res.success}")
print(f"Message: {res.message}")
print(f"Criterion value: {res.criterion}")
print(f"Parameters: {res.params}")

# Visualize history
om.criterion_plot(res)
```

### Algorithm Quick Selection

| Situation                  | First Choice                    |
| -------------------------- | ------------------------------- |
| Smooth, no constraints     | `scipy_lbfgsb`                  |
| Smooth, with constraints   | `ipopt`                         |
| Least-squares, smooth      | `scipy_ls_lm`                   |
| Not smooth, few params     | `nlopt_bobyqa`                  |
| Global search, few params  | `scipy_brute`                   |
| Global search, many params | Multistart with local optimizer |
