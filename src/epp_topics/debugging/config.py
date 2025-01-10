"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.debugging.avoiding_debugging import SITE_CONTENTS as avoiding_debgugging
from epp_topics.debugging.debugging_intro import SITE_CONTENTS as debugging_intro
from epp_topics.debugging.debugging_psychology import (
    SITE_CONTENTS as debugging_psychology,
)
from epp_topics.debugging.debugging_strategies import (
    SITE_CONTENTS as debugging_strategies,
)
from epp_topics.debugging.gathering_data import SITE_CONTENTS as gathering_data
from epp_topics.debugging.pdbp import SITE_CONTENTS as pdbp

TOPICS = (
    debugging_intro,
    debugging_strategies,
    avoiding_debgugging,
    debugging_psychology,
    gathering_data,
    pdbp,
)


SITE_CONTENTS = {
    "chapter_title": "Debugging",
    "pages": tuple(
        itertools.chain(
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
