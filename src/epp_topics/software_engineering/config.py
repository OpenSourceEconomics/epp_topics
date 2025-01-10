"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.software_engineering.deciding_containers import (
    SITE_CONTENTS as deciding_containers,
)
from epp_topics.software_engineering.defining_containers import (
    SITE_CONTENTS as defining_containers,
)
from epp_topics.software_engineering.error_handling_intro import (
    SITE_CONTENTS as error_handling_intro,
)
from epp_topics.software_engineering.idea_of_testing import (
    SITE_CONTENTS as idea_of_testing,
)
from epp_topics.software_engineering.naming import SITE_CONTENTS as naming
from epp_topics.software_engineering.partial import SITE_CONTENTS as partial
from epp_topics.software_engineering.pure_functions import (
    SITE_CONTENTS as pure_functions,
)
from epp_topics.software_engineering.pytest_error_handling import (
    SITE_CONTENTS as pytest_error_handling,
)
from epp_topics.software_engineering.raising_errors import (
    SITE_CONTENTS as raising_errors,
)
from epp_topics.software_engineering.reuse_test_code import (
    SITE_CONTENTS as reuse_test_code,
)
from epp_topics.software_engineering.style_guides import SITE_CONTENTS as style_guides
from epp_topics.software_engineering.what_and_how_to_test import (
    SITE_CONTENTS as what_and_how_to_test,
)
from epp_topics.software_engineering.what_does_pytest_do import (
    SITE_CONTENTS as what_does_pytest_do,
)
from epp_topics.software_engineering.which_errors_to_handle import (
    SITE_CONTENTS as which_errors_to_handle,
)
from epp_topics.software_engineering.worked_error_example import (
    SITE_CONTENTS as worked_error_example,
)
from epp_topics.software_engineering.writing_simple_pytests import (
    SITE_CONTENTS as writing_simple_pytests,
)

TOPICS = (
    style_guides,
    naming,
    pure_functions,
    idea_of_testing,
    what_does_pytest_do,
    writing_simple_pytests,
    pytest_error_handling,
    what_and_how_to_test,
    reuse_test_code,
    error_handling_intro,
    which_errors_to_handle,
    raising_errors,
    worked_error_example,
    defining_containers,
    deciding_containers,
    partial,
)

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
