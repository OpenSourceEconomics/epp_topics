import functools

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import statsmodels.formula.api as sm
from optimagic import minimize

# For recording, use plotly_dark+presentation, else just presentation
template_name = "plotly_dark+presentation"

pio.templates.default = template_name
pio.templates[pio.templates.default].layout["height"] = 600
pio.templates[pio.templates.default].layout["width"] = 800
pio.templates[template_name].layout.autosize = False

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
    fig = px.line(x=x_grid, y=y_grid)
    # remove axis names
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")
    return fig


def plot_history(evaluated_points, argmin):
    _fix_if_argmin_is_in_evaluated_points(evaluated_points, argmin)

    argmin = _check_argmin(argmin)

    x_grid = np.linspace(0, 20, 100)
    y_grid = [example_criterion(x) for x in x_grid]
    fig = px.line(x=x_grid, y=y_grid)
    # remove axis names
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")

    fig.add_scatter(
        x=evaluated_points,
        y=[example_criterion(x) for x in evaluated_points],
        mode="markers",
        marker={"size": 3, "color": "orange"},
        name="All evaluations",
    )

    fig.add_scatter(
        x=[argmin],
        y=[example_criterion(argmin)],
        mode="markers",
        marker={"size": 12, "color": "yellow"},
        name="Best evaluation",
        marker_symbol="star",
    )

    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )

    return fig


def _check_argmin(argmin):
    if isinstance(argmin, np.ndarray):
        if len(argmin) == 1:
            argmin = argmin[0]
        else:
            raise ValueError("argmin should be a float or a np.ndarray of length 1")
    return argmin


def _fix_if_argmin_is_in_evaluated_points(evaluated_points, argmin):
    if argmin in evaluated_points:
        evaluated_points = evaluated_points[:-1]


def minimize_with_history(fun, x0, method, jac=None, hess=None):
    """Dumbed down optimagic.minimize that returns full history.

    This is really only meant for illustration in this notebook. In particular,
    the following restrictions apply:

    - Only works for 1 dimensional problems
    - does not support all arguments

    """
    history = []

    def wrapped_fun(x, history=history):
        history.append(_unpack_x(x))
        return fun(x)

    res = minimize(wrapped_fun, x0, algorithm=method, jac=jac, hess=hess)
    res.history = history
    return res


def taylor_expansion(x, x0, radius):
    """Evaluate taylor expansion around x0 at x."""
    x = _unpack_x(x)
    x0 = _unpack_x(x0)
    f = example_criterion(x0)
    f_prime = example_gradient(x0)
    f_double_prime = example_hessian(x0)

    if radius <= 0:
        raise ValueError("radius should be positive")

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
    fig = plot_function()
    x0 = _unpack_x(x0)
    trust_x_grid = np.linspace(x0 - radius, x0 + radius, 50)
    partialed = functools.partial(surrogate_func, x0=x0, radius=radius)
    trust_y_grid = [partialed(x) for x in trust_x_grid]
    argmin_index = np.argmin(trust_y_grid)
    argmin = trust_x_grid[argmin_index]

    fig.add_scatter(
        x=trust_x_grid,
        y=trust_y_grid,
        mode="lines",
        name="Surrogate model",
        line={"color": "darkorange", "width": 2},
    )

    new_x = (
        x0
        if example_criterion([argmin]) >= example_criterion(x0)
        else np.array([argmin])
    )

    if surrogate_func == taylor_expansion:
        x_values = [x0]

        fig.add_scatter(
            x=[argmin],
            y=[partialed(np.array([argmin]))],
            mode="markers",
            marker={"size": 12, "color": "yellow"},
            name="Approximate next evaluation",
            marker_symbol="star",
        )
        fig.add_scatter(
            x=[argmin],
            y=[example_criterion(np.array([argmin]))],
            mode="markers",
            marker={"size": 12, "color": "green"},
            name="True next evaluation",
            marker_symbol="star",
        )
    else:
        x_values = [x0 - radius, x0, x0 + radius]
        # remove x in x_values if it is equal to argmin
        x_values = [x for x in x_values if x != argmin]

        fig.add_scatter(
            x=[argmin],
            y=[partialed(np.array([argmin]))],
            mode="markers",
            marker={"size": 12, "color": "yellow"},
            name="Next evaluation",
            marker_symbol="star",
        )

    fig.add_scatter(
        x=x_values,
        y=[example_criterion(x) for x in x_values],
        mode="markers",
        marker={"size": 3, "color": "orange"},
        name="Initial evaluation",
    )

    # put legend above in a line
    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )

    return fig, new_x


def plot_direct_search(x0, other):
    fig = plot_function()
    x0 = _unpack_x(x0)
    other = _unpack_x(other)

    x_values = [x0, other]
    evaluations = [example_criterion(x) for x in x_values]

    argmin_index = np.argmin(evaluations)
    argmin = x_values[argmin_index]

    x_values = x_values[:argmin_index] + x_values[argmin_index + 1 :]

    fig.add_scatter(
        x=x_values,
        y=[example_criterion(x) for x in x_values],
        mode="markers",
        marker={"size": 3, "color": "orange"},
        name="Initial evaluation",
    )

    fig.add_scatter(
        x=[argmin],
        y=[example_criterion(argmin)],
        mode="markers",
        marker={"size": 12, "color": "yellow"},
        name="Next evaluation",
        marker_symbol="star",
    )

    # put legend above in a line
    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )

    return fig, argmin


def plot_line_search(x0):
    fig = plot_function()
    x0 = _unpack_x(x0)

    function_value = example_criterion(x0)
    gradient_value = example_gradient(x0)
    approx_hessian_value = np.clip(example_hessian(x0), 0.1, np.inf)
    base_step = -1 / approx_hessian_value * gradient_value

    fig.add_scatter(
        x=[x0],
        y=[function_value],
        mode="markers",
        marker={"size": 10, "color": "orange"},
        name="Initial point",
    )

    gradient_grid = [x0 - 2, x0, x0 + 2]
    gradient_evals = [
        function_value - 2 * gradient_value,
        function_value,
        function_value + 2 * gradient_value,
    ]

    fig.add_scatter(
        x=gradient_grid,
        y=gradient_evals,
        mode="lines",
        name="Gradient",
        line={"color": "orange", "width": 2},
    )

    new_value = np.inf
    x_values = [x0]
    evaluations = [function_value]
    alpha = 1
    while new_value >= function_value:
        new_x = x0 + alpha * base_step
        new_value = example_criterion(new_x)
        x_values.append(new_x)
        evaluations.append(new_value)

    # mark the point of the next step with a star
    fig.add_scatter(
        x=[new_x],
        y=[new_value],
        mode="markers",
        marker={"size": 12, "color": "yellow"},
        name="Next initial point",
        marker_symbol="star",
    )

    # put legend above in a line
    fig.update_layout(
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )

    return fig, new_x
