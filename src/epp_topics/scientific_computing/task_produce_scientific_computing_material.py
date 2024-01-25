from pathlib import Path
from typing import Annotated

import numpy as np
from pytask import Product

from epp_topics.config import SITE_SOURCE_DIR
from epp_topics.scientific_computing.simple_optimisers import (
    example_criterion,
    example_gradient,
    example_hessian,
    minimize_with_history,
    plot_direct_search,
    plot_function,
    plot_history,
    plot_line_search,
    plot_trust_region_algo,
    regression_surrogate,
    taylor_expansion,
)

PLOTS_FOLDER = SITE_SOURCE_DIR / "scientific_computing" / "plots"
START_X = np.array([2])


def task_plots_set_up_grid_search(
    function_plot_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "set_up_grid_search"
    / "function_plot.png",
    history_grid_search_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "set_up_grid_search"
    / "history_grid_search.png",
):
    plot_function().write_image(str(function_plot_path))

    n_points = 100
    grid = np.linspace(0, 20, n_points)
    evaluations = [example_criterion(x) for x in grid]
    argmin_index = np.argmin(evaluations)
    argmin = grid[argmin_index]

    plot_history(grid, argmin).write_image(str(history_grid_search_path))


path_iterations_db_line_search = [
    PLOTS_FOLDER / "db_line_search" / f"iteration_{i}.png" for i in range(8)
]


def task_plots_db_line_search_iterations(
    x=START_X,
    illustration_db_line_search_path: Annotated[
        Path,
        Product,
    ] = path_iterations_db_line_search,
):
    for path in illustration_db_line_search_path:
        fig, x = plot_line_search(x)
        fig.write_image(str(path))


def task_plots_db_line_search_real_algo(
    x=START_X,
    illustration_db_line_search_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "db_line_search"
    / "illustration_db_line_search_real_algo.png",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="L-BFGS-B",
        jac=example_gradient,
    )
    plot_history(res.history, res.x).write_image(str(illustration_db_line_search_path))


path_iterations_db_trust_region = [
    PLOTS_FOLDER / "db_trust_region" / f"iteration_{i}.png" for i in range(6)
]


def task_plots_db_trust_region_iterations(
    x=START_X,
    illustration_db_trust_region_path: Annotated[
        Path,
        Product,
    ] = path_iterations_db_trust_region,
):
    radius_list = [2, 3, 4, 2, 3, 3]

    for path, radius in zip(
        illustration_db_trust_region_path,
        radius_list,
        strict=True,
    ):
        fig, x = plot_trust_region_algo(x, radius, surrogate_func=taylor_expansion)
        fig.write_image(str(path))


def task_plots_db_trust_region_real_algo(
    x=START_X,
    illustration_db_trust_region_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "db_trust_region"
    / "illustration_db_trust_region_real_algo.png",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="trust-ncg",
        jac=example_gradient,
        hess=example_hessian,
    )
    plot_history(res.history, res.x).write_image(str(illustration_db_trust_region_path))


path_iterations_df_trust_region = [
    PLOTS_FOLDER / "df_trust_region" / f"iteration_{i}.png" for i in range(6)
]


def task_plots_df_trust_region_iterations(
    x=START_X,
    illustration_df_trust_region_path: Annotated[
        Path,
        Product,
    ] = path_iterations_df_trust_region,
):
    radius_list = [2, 3, 4, 2, 3, 3]

    for path, radius in zip(
        illustration_df_trust_region_path,
        radius_list,
        strict=True,
    ):
        fig, x = plot_trust_region_algo(x, radius, surrogate_func=regression_surrogate)
        fig.write_image(str(path))


def task_plots_df_trust_region_real_algo(
    x=START_X,
    illustration_df_trust_region_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "df_trust_region"
    / "illustration_df_trust_region_real_algo.png",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="Cobyla",
    )
    plot_history(res.history, res.x).write_image(str(illustration_df_trust_region_path))


path_iterations_df_direct_search = [
    PLOTS_FOLDER / "df_direct_search" / f"iteration_{i}.png" for i in range(5)
]


def task_plots_df_direct_search_iterations(
    x=START_X,
    illustration_df_direct_search_path: Annotated[
        Path,
        Product,
    ] = path_iterations_df_direct_search,
):
    deltas = [-2, 2, 3, 4, 2]

    for path, delta in zip(illustration_df_direct_search_path, deltas, strict=True):
        fig, x = plot_direct_search(x, x + delta)
        fig.write_image(str(path))


def task_plots_df_direct_search_real_algo(
    x=START_X,
    illustration_df_direct_search_path: Annotated[Path, Product] = PLOTS_FOLDER
    / "df_direct_search"
    / "illustration_df_direct_search_real_algo.png",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="Nelder-Mead",
    )
    plot_history(res.history, res.x).write_image(
        str(illustration_df_direct_search_path),
    )
