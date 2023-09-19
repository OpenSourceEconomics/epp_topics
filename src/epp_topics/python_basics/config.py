"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)
from epp_topics.python_basics.dicts import (
    SITE_CONTENTS as DICTS,
)
from epp_topics.python_basics.lists_tuples_sets import (
    SITE_CONTENTS as LISTS_TUPLES_SETS,
)
from epp_topics.python_basics.strings import (
    SITE_CONTENTS as STRINGS,
)

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            ASSIGNMENT_AND_SCALAR_TYPES["public"],
            STRINGS["public"],
            LISTS_TUPLES_SETS["public"],
            DICTS["public"],
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
            STRINGS["internal"],
            LISTS_TUPLES_SETS["internal"],
            DICTS["internal"],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            ASSIGNMENT_AND_SCALAR_TYPES["other"],
            STRINGS["other"],
            LISTS_TUPLES_SETS["other"],
            DICTS["other"],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            ASSIGNMENT_AND_SCALAR_TYPES["built"],
            STRINGS["built"],
            LISTS_TUPLES_SETS["built"],
            DICTS["built"],
        ),
    ),
}
