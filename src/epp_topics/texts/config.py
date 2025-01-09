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
from epp_topics.texts.writing_readme_files import (
    SITE_CONTENTS as WRITING_README_FILES,
)

TOPICS = [
    MARKUP_LANGUAGES,
    MARKDOWN_SYNTAX,
    MARKDOWN_APPLICATIONS,
    WRITING_README_FILES,
]

SITE_CONTENTS = {
    "chapter_title": "Texts, Typesetting, and Text Data",
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
