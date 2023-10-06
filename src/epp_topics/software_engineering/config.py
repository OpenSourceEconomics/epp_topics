"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.software_engineering.idea_of_testing import (
    SITE_CONTENTS as IDEA_OF_TESTING,
)
from epp_topics.software_engineering.naming import SITE_CONTENTS as NAMING
from epp_topics.software_engineering.pure_functions import (
    SITE_CONTENTS as PURE_FUNCTIONS,
)
from epp_topics.software_engineering.styleguides import SITE_CONTENTS as STYLEGUIDES
from epp_topics.software_engineering.what_does_pytest_do import (
    SITE_CONTENTS as WHAT_DOES_PYTEST_DO,
)

TOPICS = [
    STYLEGUIDES,
    NAMING,
    PURE_FUNCTIONS,
    IDEA_OF_TESTING,
    WHAT_DOES_PYTEST_DO,
]


SITE_CONTENTS = {
    "chapter_title": "Software Engineering",
    "pages": tuple(
        itertools.chain(
            ("content_objectives.md",),
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
