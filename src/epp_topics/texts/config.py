"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.texts.markdown_applications import (
    SITE_CONTENTS as MARKDOWN_APPLICATIONS,
)
from epp_topics.texts.markdown_syntax import (
    SITE_CONTENTS as MARKDOWN_SYNTAX,
)
from epp_topics.texts.markup_languages import (
    SITE_CONTENTS as MARKUP_LANGUAGES,
)

TOPICS = [
    MARKUP_LANGUAGES,
    MARKDOWN_SYNTAX,
    MARKDOWN_APPLICATIONS,
]

SITE_CONTENTS = {
    "chapter_title": "Texts, Typesetting, and Text Data",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
        ),
    ),
    "internal": tuple(
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            *[topic["internal"] for topic in TOPICS],
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
