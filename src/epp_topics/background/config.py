"""Definitions of source files for the current chapter."""

from epp_topics.background.os_history import SITE_CONTENTS as OS_HISTORY

SITE_CONTENTS = {
    "chapter_title": "Placeholder: Title as displayed in book",
    "public": ("objectives.md",) + OS_HISTORY["public"],
    "internal": (
        "internal_overview.md",
        "objectives.md",
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
    )
    + OS_HISTORY["internal"],
    "other": OS_HISTORY["other"],
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
