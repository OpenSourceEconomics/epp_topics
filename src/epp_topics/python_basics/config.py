"""Definitions of source files for the current chapter."""

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
    "public": ("objectives.md",) + ASSIGNMENT_AND_SCALAR_TYPES["public"],
    "internal": (
        "internal_overview.md",
        "objectives.md",
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
    )
    + ASSIGNMENT_AND_SCALAR_TYPES["internal"],
    "other": (
        # "existing figures etc.",
    ),
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
