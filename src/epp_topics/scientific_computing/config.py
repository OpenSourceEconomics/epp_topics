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
from epp_topics.scientific_computing.estimagic_features import (
    SITE_CONTENTS as ESTIMAGIC_FEATURES,
)
from epp_topics.scientific_computing.indexing import SITE_CONTENTS as INDEXING
from epp_topics.scientific_computing.jax_intro import (
    SITE_CONTENTS as JAX_INTRO,
)
from epp_topics.scientific_computing.optimization_algorithms import (
    SITE_CONTENTS as OPTIMIZATION_ALGORITHMS,
)
from epp_topics.scientific_computing.optimization_histories import (
    SITE_CONTENTS as OPTIMIZATION_HISTORIES,
)
from epp_topics.scientific_computing.optimization_intro import (
    SITE_CONTENTS as OPTIMIZATION_INTRO,
)
from epp_topics.scientific_computing.optimization_mechanics import (
    SITE_CONTENTS as OPTIMIZATION_PROBLEMS,
)
from epp_topics.scientific_computing.randomness import SITE_CONTENTS as RANDOMNESS
from epp_topics.scientific_computing.speedup_arrays import (
    SITE_CONTENTS as SPEEDUP_ARRAYS,
)
from epp_topics.scientific_computing.speedup_intro import (
    SITE_CONTENTS as SPEEDUP_INTRO,
)
from epp_topics.scientific_computing.speedup_line_profile import (
    SITE_CONTENTS as SPEEDUP_LINE_PROFILE,
)
from epp_topics.scientific_computing.speedup_measuring_time import (
    SITE_CONTENTS as SPEEDUP_MEASURING_TIME,
)
from epp_topics.scientific_computing.speedup_numba import (
    SITE_CONTENTS as SPEEDUP_NUMBA,
)
from epp_topics.scientific_computing.speedup_numpy import (
    SITE_CONTENTS as SPEEDUP_NUMPY,
)
from epp_topics.scientific_computing.speedup_snakeviz import (
    SITE_CONTENTS as SPEEDUP_SNAKEVIZ,
)
from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as WHAT_IS_NUMPY

TOPICS = [
    WHAT_IS_NUMPY,
    CREATING_ARRAYS,
    INDEXING,
    CALCULATIONS_ON_ARRAYS,
    CALCULATIONS_BETWEEN_ARRAYS,
    RANDOMNESS,
    BROADCASTING,
    OPTIMIZATION_INTRO,
    ESTIMAGIC_FEATURES,
    OPTIMIZATION_PROBLEMS,
    OPTIMIZATION_HISTORIES,
    OPTIMIZATION_ALGORITHMS,
    SPEEDUP_INTRO,
    SPEEDUP_MEASURING_TIME,
    SPEEDUP_SNAKEVIZ,
    SPEEDUP_LINE_PROFILE,
    SPEEDUP_ARRAYS,
    SPEEDUP_NUMPY,
    SPEEDUP_NUMBA,
    JAX_INTRO,
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
