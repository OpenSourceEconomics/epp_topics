"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as assignment_and_scalar_types,
)
from epp_topics.python_basics.comprehensions import (
    SITE_CONTENTS as comprehensions,
)
from epp_topics.python_basics.dicts import (
    SITE_CONTENTS as dicts,
)
from epp_topics.python_basics.for_loops import (
    SITE_CONTENTS as for_loops,
)
from epp_topics.python_basics.functions_basics import (
    SITE_CONTENTS as functions_basics,
)
from epp_topics.python_basics.functions_principles import (
    SITE_CONTENTS as functions_principles,
)
from epp_topics.python_basics.if_conditions import (
    SITE_CONTENTS as if_conditions,
)
from epp_topics.python_basics.importing import (
    SITE_CONTENTS as importing,
)
from epp_topics.python_basics.lists_tuples_sets import (
    SITE_CONTENTS as lists_tuples_sets,
)
from epp_topics.python_basics.pathlib import (
    SITE_CONTENTS as pathlib,
)
from epp_topics.python_basics.strings import (
    SITE_CONTENTS as strings,
)
from epp_topics.python_basics.tracebacks import (
    SITE_CONTENTS as tracebacks,
)

TOPICS = (
    assignment_and_scalar_types,
    strings,
    lists_tuples_sets,
    dicts,
    for_loops,
    if_conditions,
    comprehensions,
    functions_basics,
    functions_principles,
    tracebacks,
    importing,
    pathlib,
)

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
