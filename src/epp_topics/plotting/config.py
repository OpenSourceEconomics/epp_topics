"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.plotting.background import SITE_CONTENTS as BACKGROUND
from epp_topics.plotting.practical import SITE_CONTENTS as PRACTICAL

TOPICS = [
    BACKGROUND,
    PRACTICAL,
]


SITE_CONTENTS = {
    "chapter_title": "Plotting",
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
