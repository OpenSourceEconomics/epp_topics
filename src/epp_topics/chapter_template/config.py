"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.chapter_template.subchapter_1 import SITE_CONTENTS as subchapter_1

TOPICS = (subchapter_1,)


SITE_CONTENTS = {
    "chapter_title": "Python Basics",
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
