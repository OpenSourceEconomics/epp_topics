"""Definitions of source files for the current chapter."""

from epp_topics.example_chapter.subchapter_1 import SITE_CONTENTS as SUBCHAPTER_1

SITE_CONTENTS = {
    "chapter_title": "Placeholder: Title as displayed in book",
    "public": ("objectives.md",) + SUBCHAPTER_1["public"],
    "internal": (
        "internal_overview.md",
        "objectives.md",
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
    )
    + SUBCHAPTER_1["internal"],
    "other": (
        # "existing figures etc.",
    ),
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
