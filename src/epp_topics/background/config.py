"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.background.file_systems import SITE_CONTENTS as file_systems
from epp_topics.background.graphs import SITE_CONTENTS as graphs
from epp_topics.background.os_history import SITE_CONTENTS as os_history

TOPICS = (
    os_history,
    graphs,
    file_systems,
)

SITE_CONTENTS = {
    "chapter_title": "Some Background",
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
