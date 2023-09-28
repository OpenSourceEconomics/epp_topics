"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.tools.shell_history import (
    SITE_CONTENTS as SHELL_HISTORY,
)
from epp_topics.tools.unix_navigation import (
    SITE_CONTENTS as UNIX_NAVIGATION,
)
from epp_topics.tools.why_shells_today import (
    SITE_CONTENTS as WHY_SHELLS_TODAY,
)
from epp_topics.tools.windows_navigation import (
    SITE_CONTENTS as WINDOWS_NAVIGATION,
)

TOPICS = [
    SHELL_HISTORY,
    WHY_SHELLS_TODAY,
    UNIX_NAVIGATION,
    WINDOWS_NAVIGATION,
]

SITE_CONTENTS = {
    "chapter_title": "Miscellaneous Tools",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
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
