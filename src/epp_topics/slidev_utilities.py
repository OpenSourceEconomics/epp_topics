"""Utilities for creating slidev compatible snippets.

Most of the code is taken from https://stackoverflow.com/q/49324569/21900143

"""

import pyperclip
from pandas.api.types import is_float_dtype


def get_html(df, scale=0.8):
    """Return html string for a pandas dataframe."""
    assert isinstance(scale, float)
    assert 0.1 <= scale <= 1

    df = df.copy(deep=True)

    for col in df.columns:
        if is_float_dtype(df[col]):
            df[col] = df[col].apply(lambda x: f"{x:.2f}")

    html = df.to_html()
    pyperclip.copy(html)
    return html
