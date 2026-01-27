"""Create exercise and solution notebooks for the current subchapter."""

from pathlib import Path

from pybaum import tree_map

from .config import SITE_CONTENTS as _SITE_CONTENTS


def add_this_dir(filename):
    """Add the current directory's name to the filename."""
    return f"{Path(__file__).parent.name}/{filename}"


SITE_CONTENTS = tree_map(
    add_this_dir,
    _SITE_CONTENTS,
)
