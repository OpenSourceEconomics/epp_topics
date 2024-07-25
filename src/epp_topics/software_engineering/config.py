"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.software_engineering.deciding_containers import (
    SITE_CONTENTS as DECIDING_CONTAINERS,
)
from epp_topics.software_engineering.defining_containers import (
    SITE_CONTENTS as DEFINING_CONTAINERS,
)
from epp_topics.software_engineering.error_handling_intro import (
    SITE_CONTENTS as ERROR_HANDLING_INTRO,
)
from epp_topics.software_engineering.idea_of_testing import (
    SITE_CONTENTS as IDEA_OF_TESTING,
)
from epp_topics.software_engineering.naming import SITE_CONTENTS as NAMING
from epp_topics.software_engineering.partial import SITE_CONTENTS as PARTIAL
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
from epp_topics.software_engineering.which_errors_to_handle import (
    SITE_CONTENTS as WHICH_ERRORS_TO_HANDLE,
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
    ERROR_HANDLING_INTRO,
    WHICH_ERRORS_TO_HANDLE,
    RAISING_ERRORS,
    WORKED_ERROR_EXAMPLE,
    DEFINING_CONTAINERS,
    DECIDING_CONTAINERS,
    PARTIAL,
]


SITE_CONTENTS = {
    "chapter_title": "Software Engineering",
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
