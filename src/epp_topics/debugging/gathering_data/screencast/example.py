from functools import partial

import numpy as np
import pandas as pd

pd.options.plotting.backend = "plotly"


def plot_cobb_douglas(x2, gamma1, gamma2, a, lb, ub):
    """Plot the Cobb-Douglas production function for a given x2."""
    func = partial(cobb_douglas, x2=x2, gamma1=gamma1, gamma2=gamma2, a=a)
    data = _create_plotting_data(func, lb, ub)
    return data.plot()


def cobb_douglas(x1, x2, gamma1, gamma2, a):
    """Calculate the output of a Cobb-Douglas production function."""
    return (a * x1**gamma1 * x2**gamma2,)


def _create_plotting_data(func, lb, ub):
    """Create the data for plotting the Cobb-Douglas production function."""
    x1_grid = np.linspace(lb, ub, 100)
    evaluations = [func(x1) for x1 in x1_grid]
    return pd.Series(evaluations, index=x1_grid)


if __name__ == "__main__":
    fig = plot_cobb_douglas(x2=1, gamma1=0.5, gamma2=0.5, a=1, lb=0, ub=10)
    fig.write_image("cobb_douglas.png")
