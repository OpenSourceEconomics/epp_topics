"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.tools.shell_history import (
    SITE_CONTENTS as SHELL_HISTORY,
)

TOPICS = [
    SHELL_HISTORY,
]

SITE_CONTENTS = {
    "chapter_title": "Tools and installation",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
        ),
    ),
    "internal": tuple(
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            *[topic["internal"] for topic in TOPICS],
        ),
    ),
    "other": tuple(
        itertools.chain(
            *[topic["other"] for topic in TOPICS],
        ),
    ),
    "built": tuple(
        itertools.chain(
            *[topic["built"] for topic in TOPICS],
        ),
    ),
}
