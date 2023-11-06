"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.scientific_computing.creating_arrays import (
    SITE_CONTENTS as CREATING_ARRAYS,
)
from epp_topics.scientific_computing.indexing import SITE_CONTENTS as INDEXING
from epp_topics.scientific_computing.math_functions import (
    SITE_CONTENTS as MATH_FUNCTIONS,
)
from epp_topics.scientific_computing.randomness import SITE_CONTENTS as RANDOMNESS
from epp_topics.scientific_computing.vectorization_and_broadcasting import (
    SITE_CONTENTS as VECTORIZATION_AND_BROADCASTING,
)
from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as WHAT_IS_NUMPY
from epp_topics.scientific_computing.what_is_scipy import SITE_CONTENTS as WHAT_IS_SCIPY

TOPICS = [
    WHAT_IS_NUMPY,
    CREATING_ARRAYS,
    INDEXING,
    MATH_FUNCTIONS,
    RANDOMNESS,
    VECTORIZATION_AND_BROADCASTING,
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
