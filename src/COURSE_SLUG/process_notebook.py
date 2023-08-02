"""Utility functions for processing Jupyter notebooks."""

from copy import deepcopy
from typing import Literal

import nbformat


def process_notebook(
    nb_raw: nbformat.notebooknode.NotebookNode,
    ex_o_sol: Literal["exercise", "solution"] = "exercise",
    solution_title_suffix: str = " (solution)",
):
    """Process an internal notebook into an exercise or solution notebook.

    Internal notebooks contain exercises and solutions. Solution cells are marked with
    '## solution' if they are code cells and with '!! solution' if they are markdown
    cells.

    Args:
        nb_raw: The path to the internal notebook.
        ex_o_sol: If 'exercise', all solution cells are replaced by empty cells.
            If 'solution', the content of all cells is kept but the comments that mark
            them as solution are removed.
        solution_title_suffix: The suffix for the solution title.

    Returns:
        nbformat.notebooknode.NotebookNode: The processed notebook.
    """
    assert ex_o_sol in ("exercise", "solution")

    out = deepcopy(nb_raw)
    out.cells = [_process_cell(c, ex_o_sol=ex_o_sol) for c in out.cells]

    if ex_o_sol == "solution":
        out.cells[0] = _adjust_title(out.cells[0], suffix=solution_title_suffix)

    return out


def _adjust_title(cell, suffix):
    if cell["cell_type"] != "markdown" or suffix in (None, "", False):
        return cell

    out = deepcopy(cell)

    title, *body = out["source"].split("\n", maxsplit=1)

    new_title = title + suffix

    out["source"] = "\n".join([new_title, *body])
    return out


def _process_cell(cell, ex_o_sol):
    if not _is_solution(cell):
        return cell

    out = deepcopy(cell)
    if ex_o_sol == "exercise":
        out["source"] = ""
    elif ex_o_sol == "solution":
        marker, content = out["source"].split("\n", maxsplit=1)
        out["source"] = content
    else:
        raise ValueError("target must be 'exercise' or 'solution'.")

    return out


def _is_solution(cell):
    source = cell.source.lower().replace(" ", "")
    if cell["cell_type"] == "markdown":
        out = source.startswith(("!!solution", "!solution"))
    elif cell["cell_type"] == "code":
        out = source.startswith(("##solution", "#solution"))
    else:
        out = False
    return out
