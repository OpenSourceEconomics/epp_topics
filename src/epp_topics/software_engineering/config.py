"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.software_engineering.catching_errors import (
    SITE_CONTENTS as CATCHING_ERRORS,
)
from epp_topics.software_engineering.idea_of_testing import (
    SITE_CONTENTS as IDEA_OF_TESTING,
)
from epp_topics.software_engineering.naming import SITE_CONTENTS as NAMING
from epp_topics.software_engineering.pure_functions import (
    SITE_CONTENTS as PURE_FUNCTIONS,
)
from epp_topics.software_engineering.pytest_error_handling import (
    SITE_CONTENTS as PYTEST_ERROR_HANDLING,
)
from epp_topics.software_engineering.raising_errors import (
    SITE_CONTENTS as RAISING_ERRORS,
)
from epp_topics.software_engineering.reuse_test_code import (
    SITE_CONTENTS as REUSE_TEST_CODE,
)
from epp_topics.software_engineering.style_guides import SITE_CONTENTS as STYLE_GUIDES
from epp_topics.software_engineering.what_and_how_to_test import (
    SITE_CONTENTS as WHAT_AND_HOW_TO_TEST,
)
from epp_topics.software_engineering.what_does_pytest_do import (
    SITE_CONTENTS as WHAT_DOES_PYTEST_DO,
)
from epp_topics.software_engineering.why_error_handling import (
    SITE_CONTENTS as WHY_ERROR_HANDLING,
)
from epp_topics.software_engineering.worked_error_example import (
    SITE_CONTENTS as WORKED_ERROR_EXAMPLE,
)
from epp_topics.software_engineering.writing_simple_pytests import (
    SITE_CONTENTS as WRITING_SIMPLE_PYTESTS,
)

TOPICS = [
    STYLE_GUIDES,
    NAMING,
    PURE_FUNCTIONS,
    IDEA_OF_TESTING,
    WHAT_DOES_PYTEST_DO,
    WRITING_SIMPLE_PYTESTS,
    PYTEST_ERROR_HANDLING,
    WHAT_AND_HOW_TO_TEST,
    REUSE_TEST_CODE,
    WHY_ERROR_HANDLING,
    RAISING_ERRORS,
    WORKED_ERROR_EXAMPLE,
    CATCHING_ERRORS,
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
