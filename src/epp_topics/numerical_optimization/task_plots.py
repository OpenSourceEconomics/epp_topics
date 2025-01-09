from pathlib import Path
from typing import Annotated

import numpy as np
from pytask import Product

from epp_topics.numerical_optimization.simple_optimisers import (
    example_criterion,
    example_gradient,
    minimize_with_history,
    plot_direct_search,
    plot_function,
    plot_history,
    plot_line_search,
    plot_trust_region_algo,
    regression_surrogate,
    taylor_expansion,
)

START_X = np.array([2])


def task_plot_example_function(
    _plots_dep=Path("simple_optimisers.py"),
    function_path: Annotated[Path, Product] = Path()
    / "example_set_up"
    / "screencast"
    / "public"
    / "function.svg",
):
    plot_function().write_image(str(function_path))


def task_plot_grid_search(
    _plots_dep=Path("simple_optimisers.py"),
    history_path: Annotated[Path, Product] = Path()
    / "grid_search"
    / "screencast"
    / "public"
    / "history.svg",
):
    n_points = 100
    grid = np.linspace(0, 20, n_points)
    evaluations = [example_criterion(x) for x in grid]
    argmin_index = np.argmin(evaluations)
    argmin = grid[argmin_index]

    plot_history(grid, argmin).write_image(str(history_path))


path_iterations_db_line_search = [
    Path() / "db_line_search" / "screencast" / "public" / f"iteration_{i}.svg"
    for i in range(8)
]


def task_plots_db_line_search_iterations(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
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
    _plots_dep=Path("simple_optimisers.py"),
    illustration_db_line_search_path: Annotated[Path, Product] = Path()
    / "db_line_search"
    / "screencast"
    / "public"
    / "illustration_db_line_search_real_algo.svg",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="nlopt_lbfgsb",
        jac=example_gradient,
    )
    plot_history(res.history, res.x).write_image(str(illustration_db_line_search_path))


path_iterations_db_trust_region = [
    Path() / "db_trust_region" / "screencast" / "public" / f"iteration_{i}.svg"
    for i in range(6)
]


def task_plots_db_trust_region_iterations(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
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
    _plots_dep=Path("simple_optimisers.py"),
    illustration_db_trust_region_path: Annotated[Path, Product] = Path()
    / "db_trust_region"
    / "screencast"
    / "public"
    / "illustration_db_trust_region_real_algo.svg",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="fides",
        jac=example_gradient,
        hess=None,
    )
    plot_history(res.history, res.x).write_image(str(illustration_db_trust_region_path))


path_iterations_df_trust_region = [
    Path() / "df_trust_region" / "screencast" / "public" / f"iteration_{i}.svg"
    for i in range(6)
]


def task_plots_df_trust_region_iterations(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
    illustration_df_trust_region_path: Annotated[
        Path,
        Product,
    ] = path_iterations_df_trust_region,
):
    radius_list = [2, 3, 4, 2, 3, 1.5]

    for path, radius in zip(
        illustration_df_trust_region_path,
        radius_list,
        strict=True,
    ):
        fig, x = plot_trust_region_algo(x, radius, surrogate_func=regression_surrogate)
        fig.write_image(str(path))


def task_plots_df_trust_region_real_algo(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
    illustration_df_trust_region_path: Annotated[Path, Product] = Path()
    / "df_trust_region"
    / "screencast"
    / "public"
    / "illustration_df_trust_region_real_algo.svg",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="nlopt_cobyla",
    )
    plot_history(res.history, res.x).write_image(str(illustration_df_trust_region_path))


path_iterations_df_direct_search = [
    Path() / "df_direct_search" / "screencast" / "public" / f"iteration_{i}.svg"
    for i in range(5)
]


def task_plots_df_direct_search_iterations(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
    illustration_df_direct_search_path: Annotated[
        Path,
        Product,
    ] = path_iterations_df_direct_search,
):
    deltas = [-1.5, 2, 3, 4, 2]

    for path, delta in zip(illustration_df_direct_search_path, deltas, strict=True):
        fig, x = plot_direct_search(x, x + delta)
        fig.write_image(str(path))


def task_plots_df_direct_search_real_algo(
    x=START_X,
    _plots_dep=Path("simple_optimisers.py"),
    illustration_df_direct_search_path: Annotated[Path, Product] = Path()
    / "df_direct_search"
    / "screencast"
    / "public"
    / "illustration_df_direct_search_real_algo.svg",
):
    res = minimize_with_history(
        example_criterion,
        x,
        method="nlopt_neldermead",
    )
    plot_history(res.history, res.x).write_image(
        str(illustration_df_direct_search_path),
    )
