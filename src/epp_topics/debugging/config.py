"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.debugging.avoiding_debugging import SITE_CONTENTS as AVOIDING_DEBGUGGING
from epp_topics.debugging.debugging_intro import SITE_CONTENTS as DEBUGGING_INTRO
from epp_topics.debugging.debugging_psychology import (
    SITE_CONTENTS as DEBUGGING_PSYCHOLOGY,
)
from epp_topics.debugging.debugging_strategies import (
    SITE_CONTENTS as DEBUGGING_STRATEGIES,
)
from epp_topics.debugging.gathering_data import SITE_CONTENTS as GATHERING_DATA
from epp_topics.debugging.pdbp import SITE_CONTENTS as PDBP

TOPICS = [
    DEBUGGING_INTRO,
    AVOIDING_DEBGUGGING,
    DEBUGGING_STRATEGIES,
    DEBUGGING_PSYCHOLOGY,
    GATHERING_DATA,
    PDBP,
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
