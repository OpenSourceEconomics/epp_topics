"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.git.committing_diffing import SITE_CONTENTS as COMMITTING_DIFFING
from epp_topics.git.motivation import SITE_CONTENTS as MOTIVATION

SITE_CONTENTS = {
    "chapter_title": "Version Control and collaboration with Git and Github",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            MOTIVATION["public"],
            COMMITTING_DIFFING["public"],
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
            MOTIVATION["internal"],
            COMMITTING_DIFFING["internal"],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            MOTIVATION["other"],
            COMMITTING_DIFFING["other"],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            MOTIVATION["built"],
            COMMITTING_DIFFING["built"],
        ),
    ),
}
