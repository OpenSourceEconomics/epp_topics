"""All the general configuration of the project."""

import importlib
from pathlib import Path
from typing import Literal, NamedTuple

from pybaum.tree_util import tree_just_flatten, tree_map

# Type aliases
OrigSourceOrBookSource = Literal["orig_source", "book_source"]
StudentsOrTeachers = Literal["students", "teachers"]
StudentMaterialTypes = Literal["prep", "class", "post", "exam_prep"]
StudentMaterialTypesStrings = dict[StudentMaterialTypes, list[str]]


class StudentMaterialInts(NamedTuple):
    prep: int
    in_class: int
    post: int
    exam_prep: int


class StudentMaterialStrings(NamedTuple):
    prep: tuple[str]
    in_class: tuple[str]
    post: tuple[str]
    exam_prep: tuple[str] = ()


# Specify the most recent materials (see CHAPTER_NAMES below) to include in the book
MOST_RECENT_MATERIALS = StudentMaterialInts(
    prep=0,
    in_class=1,
    post=2,
    exam_prep=3,
)


# Add the chapter names here in the order they should appear in the book
CHAPTER_NAMES = {
    0: "example_chapter",
    # 1: "einfuehrung",
    # 2: "kinderzuschlag",
    # 10: "daten",
}


SRC = Path(__file__).parent.resolve()
BOOK_SOURCE_DIR = SRC.parent.parent / "book_source"
BOOK_DIR = {
    "students": SRC.parent.parent / "book_students",
    "teachers": SRC.parent.parent / "book_teachers",
}
JUPYTERHUB_REPO_DIR = SRC.parent.parent.parent / "fsp"

TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()


def load_sources(chapter_number, chapter_name):
    """Load environment specification using a path to a file as input."""
    path = Path(__file__).parent / chapter_name / "config.py"
    spec = importlib.util.spec_from_file_location(path.name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return {
        "chapter_number": chapter_number,
        "chapter_name": chapter_name,
        "book_contents": module.BOOK_CONTENTS,
    }


assert len(set(CHAPTER_NAMES.values())) == len(
    CHAPTER_NAMES,
), "Chapter names must be unique."
_RAW_SOURCES = {c: load_sources(n, c) for n, c in CHAPTER_NAMES.items()}


def filter_student_lectures(n: int) -> bool:
    """Filter entire lectures."""
    return max(tree_just_flatten(MOST_RECENT_MATERIALS)) >= n


def filter_student_contents(
    n: int,
    contents: StudentMaterialStrings,
) -> list[str]:
    """Filter the contents of a lecture (preparation, in-class, post, old exams)."""
    return {
        typ: names
        for typ, names in contents._asdict().items()
        if n <= getattr(MOST_RECENT_MATERIALS, typ)
    }


def get_chapter_title(chapter_name: str) -> str:
    """Return a chapter's title as it will appear in the book."""
    return _RAW_SOURCES[chapter_name]["book_contents"]["chapter_title"]


def get_sources_for_chapter(
    chapter_name: str,
    s_o_t: StudentsOrTeachers,
    os_o_bs: OrigSourceOrBookSource,
) -> dict:
    """Get the original sources for a chapter of the student or teacher book."""
    n = _RAW_SOURCES[chapter_name]["chapter_number"]
    _r = _RAW_SOURCES[chapter_name]["book_contents"][s_o_t]
    out_dir = SRC if os_o_bs == "orig_source" else BOOK_SOURCE_DIR / s_o_t
    raw = {
        "toc_sources": filter_student_contents(n=n, contents=_r)
        if s_o_t == "students"
        else _r,
        "other": _RAW_SOURCES[chapter_name]["book_contents"].get("other", ()),
        "built": _RAW_SOURCES[chapter_name]["book_contents"].get("built", ())
        if os_o_bs == "book_source"
        else (),
    }
    # Leave empty chapters out completely
    raw = raw if raw["toc_sources"] else {}
    return tree_map(
        func=lambda x: out_dir / chapter_name / x,
        tree=raw,
    )
