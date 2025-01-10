"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.tools.shell_history import (
    SITE_CONTENTS as shell_history,
)
from epp_topics.tools.unix_navigation import (
    SITE_CONTENTS as unix_navigation,
)
from epp_topics.tools.why_shells_today import (
    SITE_CONTENTS as why_shells_today,
)
from epp_topics.tools.windows_navigation import (
    SITE_CONTENTS as windows_navigation,
)

TOPICS = (
    shell_history,
    why_shells_today,
    unix_navigation,
    windows_navigation,
)

SITE_CONTENTS = {
    "chapter_title": "Miscellaneous Tools",
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
