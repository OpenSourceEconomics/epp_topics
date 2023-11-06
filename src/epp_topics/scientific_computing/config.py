"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.scientific_computing.broadcasting import (
    SITE_CONTENTS as BROADCASTING,
)
from epp_topics.scientific_computing.calculations_between_arrays import (
    SITE_CONTENTS as CALCULATIONS_BETWEEN_ARRAYS,
)
from epp_topics.scientific_computing.calculations_on_arrays import (
    SITE_CONTENTS as CALCULATIONS_ON_ARRAYS,
)
from epp_topics.scientific_computing.creating_arrays import (
    SITE_CONTENTS as CREATING_ARRAYS,
)
from epp_topics.scientific_computing.indexing import SITE_CONTENTS as INDEXING
from epp_topics.scientific_computing.randomness import SITE_CONTENTS as RANDOMNESS
from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as WHAT_IS_NUMPY
from epp_topics.scientific_computing.what_is_scipy import SITE_CONTENTS as WHAT_IS_SCIPY

TOPICS = [
    WHAT_IS_NUMPY,
    CREATING_ARRAYS,
    INDEXING,
    CALCULATIONS_ON_ARRAYS,
    CALCULATIONS_BETWEEN_ARRAYS,
    RANDOMNESS,
    BROADCASTING,
    WHAT_IS_SCIPY,
]


SITE_CONTENTS = {
    "chapter_title": "Scientific Computing",
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
