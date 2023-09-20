"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.background.file_systems import SITE_CONTENTS as FILE_SYSTEMS
# from epp_topics.background.floats import SITE_CONTENTS as FLOATS
from epp_topics.background.graphs import SITE_CONTENTS as GRAPHS
from epp_topics.background.os_history import SITE_CONTENTS as OS_HISTORY

SITE_CONTENTS = {
    "chapter_title": "Some Background",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            OS_HISTORY["public"],
            GRAPHS["public"],
            FILE_SYSTEMS["public"],
            # FLOATS["public"],
        ),
    ),
    "internal": tuple(
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            OS_HISTORY["internal"],
            GRAPHS["internal"],
            FILE_SYSTEMS["internal"],
            # FLOATS["internal"],
        ),
    ),
    "other": tuple(
        itertools.chain(
            OS_HISTORY["other"],
            GRAPHS["other"],
            FILE_SYSTEMS["other"],
            # FLOATS["other"],
        ),
    ),
    "built": tuple(
        itertools.chain(
            OS_HISTORY["built"],
            GRAPHS["built"],
            FILE_SYSTEMS["built"],
            # FLOATS["built"],
        ),
    ),
}
