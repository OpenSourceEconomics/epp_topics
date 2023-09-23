"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.texts.markup_languages import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)

TOPICS = [
    ASSIGNMENT_AND_SCALAR_TYPES,
]

SITE_CONTENTS = {
    "chapter_title": "Texts, typesetting and text data",
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
