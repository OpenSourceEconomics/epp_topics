"""Definitions of source files for the current chapter."""

from epp_topics.git.commiting_diffing import SITE_CONTENTS as COMMITING_DIFFING
from epp_topics.git.motivation import SITE_CONTENTS as MOTIVATION

SITE_CONTENTS = {
    "chapter_title": "Version Control and collaboration with Git and Github",
    "public": ("objectives.md",) + MOTIVATION["public"] + COMMITING_DIFFING["public"],
    "internal": (
        "internal_overview.md",
        "objectives.md",
    )
    + MOTIVATION["internal"]
    + COMMITING_DIFFING["internal"],
    "other": (),
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
