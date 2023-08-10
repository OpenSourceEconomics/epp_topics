"""Definitions of source files for the current chapter."""

from epp_topics.config import StudentMaterialStrings

BOOK_CONTENTS = {
    "chapter_title": "Placeholder: Title as displayed in book",
    "students": StudentMaterialStrings(
        prep=(
            "objectives.md",
            "preparation.md",
            # "All .md or .ipynb files",
            # "for preparation phase",
        ),
        in_class=(
            "in_class_exercise.ipynb",
            # "All .md or .ipynb files",
            # "for in-class",
        ),
        post=(
            # "All .md or .ipynb files",
            # "for post-class phase",
        ),
    ),
    "teachers": (
        "contents.md",
        "objectives.md",
        "preparation.md",
        "in_class_exercise.ipynb",
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
    ),
    "other": (
        # "existing figures etc.",
    ),
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
