"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)
from epp_topics.python_basics.comprehensions import (
    SITE_CONTENTS as COMPREHENSIONS,
)
from epp_topics.python_basics.dicts import (
    SITE_CONTENTS as DICTS,
)
from epp_topics.python_basics.for_loops import (
    SITE_CONTENTS as FOR_LOOPS,
)
from epp_topics.python_basics.functions_basics import (
    SITE_CONTENTS as FUNCTIONS_BASICS,
)
from epp_topics.python_basics.functions_principles import (
    SITE_CONTENTS as FUNCTIONS_PRINCIPLES,
)
from epp_topics.python_basics.if_conditions import (
    SITE_CONTENTS as IF_CONDITIONS,
)
from epp_topics.python_basics.importing import (
    SITE_CONTENTS as IMPORTING,
)
from epp_topics.python_basics.lists_tuples_sets import (
    SITE_CONTENTS as LISTS_TUPLES_SETS,
)
from epp_topics.python_basics.pathlib import (
    SITE_CONTENTS as PATHLIB,
)
from epp_topics.python_basics.strings import (
    SITE_CONTENTS as STRINGS,
)
from epp_topics.python_basics.tracebacks import (
    SITE_CONTENTS as TRACEBACKS,
)

TOPICS = [
    ASSIGNMENT_AND_SCALAR_TYPES,
    STRINGS,
    LISTS_TUPLES_SETS,
    DICTS,
    FOR_LOOPS,
    IF_CONDITIONS,
    COMPREHENSIONS,
    FUNCTIONS_BASICS,
    FUNCTIONS_PRINCIPLES,
    TRACEBACKS,
    IMPORTING,
    PATHLIB,
]

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
