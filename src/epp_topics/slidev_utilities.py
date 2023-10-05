"""Utilities for creating slidev compatible snippets.

Most of the code is taken from https://stackoverflow.com/q/49324569/21900143

"""

import pyperclip
from pandas.api.types import is_float_dtype


def get_html(df, scale=0.8):
    """Return html string for a pandas dataframe."""
    assert isinstance(scale, float)
    assert 0.1 <= scale <= 1  # noqa: PLR2004
    font_percent = f"{int(scale * 100)}%"

    df = df.copy(deep=True)

    for col in df.columns:
        if is_float_dtype(df[col]):
            df[col] = df[col].apply(lambda x: f"{x:.2f}")

    styles = [
        # table properties
        {
            "selector": " ",
            "props": [
                ("margin", "0"),
                ("font-family", '"Helvetica", "Helvetica", sans-serif'),
                ("border-collapse", "collapse"),
                ("border", "none"),
                ("font-size", font_percent),
                ("color", "#fff"),
            ],
        },
        # header color - optional
        {"selector": "thead", "props": [("background-color", "#3d3d3d")]},
        # background shading
        {
            "selector": "tbody tr:nth-child(even)",
            "props": [("background-color", "#3d3d3d")],
        },
        {
            "selector": "tbody tr:nth-child(odd)",
            "props": [("background-color", "#565656")],
        },
        # cell spacing
        {"selector": "td", "props": [("padding", "0em")]},
        # header cell properties
        {
            "selector": "th",
            "props": [
                ("font-weight", "bold"),
                ("text-align", "left"),
                ("padding", "0em"),
            ],
        },
        # caption placement
        {"selector": "caption", "props": [("caption-side", "bottom")]},
    ]
    html = df.style.set_table_styles(styles)

    pyperclip.copy(html.to_html())

    return html
