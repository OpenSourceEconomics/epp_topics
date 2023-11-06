"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as WHAT_IS_NUMPY

TOPICS = [
    WHAT_IS_NUMPY,
]


SITE_CONTENTS = {
    "chapter_title": "Scientific Computing",
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
