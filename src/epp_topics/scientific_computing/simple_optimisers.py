import functools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as sm
from scipy.optimize import minimize

sns.set_style("white")

WEIGHTS = [
    9.003014962148157,
    -3.383000146393776,
    -0.6037887934635748,
    1.6984454347036886,
    -0.9447426232680957,
    0.2669069434366247,
    -0.04446368897497234,
    0.00460781796708519,
    -0.0003000790127508276,
    1.1934114174145725e-05,
    -2.6471293419570505e-07,
    2.5090819960943964e-09,
]


def example_criterion(x):
    x = _unpack_x(x)
    exponents = np.arange(len(WEIGHTS))
    return WEIGHTS @ x**exponents


def example_gradient(x):
    x = _unpack_x(x)
    exponents = np.arange(len(WEIGHTS))
    return (WEIGHTS * exponents) @ x ** (exponents - 1).clip(0)


def example_hessian(x):
    x = _unpack_x(x)
    exponents = np.arange(len(WEIGHTS))
    return (WEIGHTS * exponents * (exponents - 1)) @ x ** (exponents - 2).clip(0)


def _unpack_x(x):
    if hasattr(x, "__len__"):
        assert len(x) == 1

    if isinstance(x, pd.DataFrame):
        res = x["value"].to_numpy()[0]
    elif isinstance(x, pd.Series):
        res = x.to_numpy()[0]
    elif isinstance(x, np.ndarray | list | tuple):
        res = x[0]
    else:
        res = float(x)
    return res


def plot_function():
    x_grid = np.linspace(0, 20, 100)
    y_grid = [example_criterion(x) for x in x_grid]
    fig, ax = plt.subplots()
    sns.lineplot(x=x_grid, y=y_grid, ax=ax)
    sns.despine()
    return fig, ax


def plot_history(evaluated_points, argmin):
    """Plot the function and all evaluated points."""
    fig, ax = plot_function()
    sns.rugplot(evaluated_points, ax=ax)
    ax.plot([argmin], [example_criterion(argmin)], marker="*", color="firebrick")
    return fig, ax


def minimize_with_history(fun, x0, method, jac=None, hess=None):
    """Dumbed down scipy minimize that returns full history.

    This is really only meant for illustration in this notebook. In particular,
    the following restrictions apply:

    - Only works for 1 dimensional problems
    - does not support all arguments

    """
    history = []

    def wrapped_fun(x, history=history):
        history.append(_unpack_x(x))
        return fun(x)

    res = minimize(wrapped_fun, x0, method=method, jac=jac, hess=hess)
    res.history = history
    return res


def taylor_expansion(x, x0):
    """Evaluate taylor expansion around x0 at x."""
    x = _unpack_x(x)
    x0 = _unpack_x(x0)
    f = example_criterion(x0)
    f_prime = example_gradient(x0)
    f_double_prime = example_hessian(x0)

    diff = x - x0
    return f + f_prime * diff + f_double_prime * 0.5 * diff**2


def regression_surrogate(x, x0, radius):
    """Evaluate a regression based surrogate model at x.

    x0 and radius define the trust region in which evaluation points are sampled.

    """
    x = _unpack_x(x)
    x0 = _unpack_x(x0)
    deviations = [-radius, 0, radius]

    evaluations = [example_criterion(x0 + deviation) for deviation in deviations]
    df = pd.DataFrame()
    df["x"] = deviations
    df["y"] = evaluations
    params = sm.ols(formula="y ~ x + I(x**2)", data=df).fit().params
    vec = np.array([1, (x - x0), (x - x0) ** 2])
    return params @ vec


def plot_trust_region_algo(x0, radius, surrogate_func):
    fig, ax = plot_function()
    x0 = _unpack_x(x0)
    trust_x_grid = np.linspace(x0 - radius, x0 + radius, 50)
    partialed = functools.partial(surrogate_func, x0=x0, radius=radius)
    trust_y_grid = [partialed(x) for x in trust_x_grid]
    argmin_index = np.argmin(trust_y_grid)
    argmin = trust_x_grid[argmin_index]

    ax.plot([argmin], [partialed(np.array([argmin]))], marker="*", color="firebrick")
    ax.plot(
        [argmin],
        [example_criterion(np.array([argmin]))],
        marker="*",
        color="green",
    )

    sns.lineplot(x=trust_x_grid, y=trust_y_grid, ax=ax)

    new_x = (
        x0
        if example_criterion([argmin]) >= example_criterion(x0)
        else np.array([argmin])
    )

    if surrogate_func == taylor_expansion:
        x_values = [x0]
    else:
        x_values = [x0 - radius, x0, x0 + radius]

    sns.rugplot(x_values, ax=ax)
    return fig, ax, new_x


def plot_direct_search(x0, other):
    fig, ax = plot_function()
    x0 = _unpack_x(x0)
    other = _unpack_x(other)

    x_values = [x0, other]
    evaluations = [example_criterion(x) for x in x_values]

    argmin_index = np.argmin(evaluations)
    argmin = x_values[argmin_index]

    ax.plot([argmin], [example_criterion(argmin)], marker="*", color="firebrick")
    sns.rugplot(x_values, ax=ax)

    return fig, ax, argmin


def plot_line_search(x0):
    fig, ax = plot_function()
    x0 = _unpack_x(x0)

    function_value = example_criterion(x0)
    gradient_value = example_gradient(x0)
    approx_hessian_value = np.clip(example_hessian(x0), 0.1, np.inf)
    base_step = -1 / approx_hessian_value * gradient_value

    gradient_grid = [x0 - 2, x0, x0 + 2]
    gradient_evals = [
        function_value - 2 * gradient_value,
        function_value,
        function_value + 2 * gradient_value,
    ]
    sns.lineplot(x=gradient_grid, y=gradient_evals, ax=ax)

    new_value = np.inf
    x_values = [x0]
    evaluations = [function_value]
    alpha = 1
    while new_value >= function_value:
        new_x = x0 + alpha * base_step
        new_value = example_criterion(new_x)
        x_values.append(new_x)
        evaluations.append(new_value)

    sns.rugplot(x_values, ax=ax)
    ax.plot([new_x], [new_value], marker="*", color="firebrick")
    return fig, ax, new_x
