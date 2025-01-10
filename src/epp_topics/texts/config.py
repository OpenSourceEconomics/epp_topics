"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.texts.markdown_applications import (
    SITE_CONTENTS as markdown_applications,
)
from epp_topics.texts.markdown_syntax import (
    SITE_CONTENTS as markdown_syntax,
)
from epp_topics.texts.markup_languages import (
    SITE_CONTENTS as markup_languages,
)
from epp_topics.texts.writing_readme_files import (
    SITE_CONTENTS as writing_readme_files,
)

TOPICS = (
    markup_languages,
    markdown_syntax,
    markdown_applications,
    writing_readme_files,
)

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
