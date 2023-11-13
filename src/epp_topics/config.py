"""All the general configuration of the project."""

import importlib
from pathlib import Path
from typing import Literal

from pybaum.tree_util import tree_map

# Type aliases
OrigSourceOrSiteSource = Literal["orig_source", "site_source"]

# Add the chapter names here in the order they should appear in the book
CHAPTER_NAMES = [
    "background",
    "tools",
    "git",
    "python_installation_execution",
    "python_basics",
    "pandas",
    "scientific_computing",
    "projects",
    "software_engineering",
    "texts",
    "plotting",
]


SRC = Path(__file__).parent.resolve()
SITE_SOURCE_DIR = SRC.parent.parent / "site_source"
SITE_DIR = SRC.parent.parent.parent / "effective-programming-practices"


def load_sources(chapter_name):
    """Load environment specification using a path to a file as input."""
    path = Path(__file__).parent / chapter_name / "config.py"
    spec = importlib.util.spec_from_file_location(path.name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {
        "chapter_name": chapter_name,
        "site_contents": module.SITE_CONTENTS,
    }


assert len(set(CHAPTER_NAMES)) == len(
    CHAPTER_NAMES,
), "Chapter names must be unique."
_RAW_SOURCES = {c: load_sources(c) for c in CHAPTER_NAMES}


def get_chapter_title(chapter_name: str) -> str:
    """Return a chapter's title as it will appear in the book."""
    return _RAW_SOURCES[chapter_name]["site_contents"]["chapter_title"]


def get_sources_for_chapter(
    chapter_name: str,
    os_o_ss: OrigSourceOrSiteSource,
) -> dict:
    """Get the original sources for a chapter of the site."""
    _r = _RAW_SOURCES[chapter_name]["site_contents"]["pages"]
    out_root = SRC if os_o_ss == "orig_source" else SITE_SOURCE_DIR
    raw = {
        "toc_sources": _r,
        "other": _RAW_SOURCES[chapter_name]["site_contents"].get("other", ()),
        "built": _RAW_SOURCES[chapter_name]["site_contents"].get("built", ())
        if os_o_ss == "site_source"
        else (),
    }
    # Leave empty chapters out completely
    raw = raw if raw["toc_sources"] else {}
    return tree_map(
        func=lambda x: out_root / chapter_name / x,
        tree=raw,
    )
