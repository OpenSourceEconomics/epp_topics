"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.projects.what_does_pytask_do import SITE_CONTENTS as WHAT_DOES_PYTASK_DO

TOPICS = [
    WHAT_DOES_PYTASK_DO,
]
SITE_CONTENTS = {
    "chapter_title": "Reproducible Research",
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
