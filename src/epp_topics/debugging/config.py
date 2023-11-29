"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.debugging.debugging_intro import SITE_CONTENTS as DEBUGGING_INTRO

TOPICS = [
    DEBUGGING_INTRO,
]


SITE_CONTENTS = {
    "chapter_title": "Debugging",
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
