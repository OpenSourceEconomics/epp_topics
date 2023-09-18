"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.chapter_template.subchapter_1 import SITE_CONTENTS as SUBCHAPTER_1

SITE_CONTENTS = {
    "chapter_title": "Placeholder: Title as displayed in book",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            SUBCHAPTER_1["public"],
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
            SUBCHAPTER_1["internal"],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            SUBCHAPTER_1["other"],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            SUBCHAPTER_1["built"],
        ),
    ),
}
