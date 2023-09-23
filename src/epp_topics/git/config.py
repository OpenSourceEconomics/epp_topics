"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.git.motivation import SITE_CONTENTS as MOTIVATION
from epp_topics.git.why_git import SITE_CONTENTS as WHY_GIT

TOPICS = [
    MOTIVATION,
    WHY_GIT,
]

SITE_CONTENTS = {
    "chapter_title": "Git and Github",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
        ),
    ),
    "internal": tuple(
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            *[topic["internal"] for topic in TOPICS],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            *[topic["other"] for topic in TOPICS],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            *[topic["built"] for topic in TOPICS],
        ),
    ),
}
