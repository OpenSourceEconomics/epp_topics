"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.background.file_systems import SITE_CONTENTS as FILE_SYSTEMS
from epp_topics.background.graphs import SITE_CONTENTS as GRAPHS
from epp_topics.background.os_history import SITE_CONTENTS as OS_HISTORY

SITE_CONTENTS = {
    "chapter_title": "Some Background",
    "pages": tuple(
        itertools.chain(
            ("content_objectives.md",),
            OS_HISTORY["pages"],
            GRAPHS["pages"],
            FILE_SYSTEMS["pages"],
        ),
    ),
    "other": tuple(
        itertools.chain(
            OS_HISTORY["other"],
            GRAPHS["other"],
            FILE_SYSTEMS["other"],
        ),
    ),
    "built": tuple(
        itertools.chain(
            OS_HISTORY["built"],
            GRAPHS["built"],
            FILE_SYSTEMS["built"],
        ),
    ),
}
