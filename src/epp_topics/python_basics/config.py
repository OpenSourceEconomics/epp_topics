"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            ASSIGNMENT_AND_SCALAR_TYPES["public"],
        ),
    ),
    "internal": tuple(
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            ASSIGNMENT_AND_SCALAR_TYPES["internal"],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            ASSIGNMENT_AND_SCALAR_TYPES["other"],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            ASSIGNMENT_AND_SCALAR_TYPES["built"],
        ),
    ),
}