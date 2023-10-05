"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.software_engineering.styleguides import SITE_CONTENTS as STYLEGUIDES

TOPICS = [
    STYLEGUIDES,
]


SITE_CONTENTS = {
    "chapter_title": "Software Engineering",
    "pages": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["pages"] for topic in TOPICS],
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
