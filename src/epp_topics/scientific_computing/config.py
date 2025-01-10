"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.scientific_computing.broadcasting import (
    SITE_CONTENTS as broadcasting,
)
from epp_topics.scientific_computing.calculations_between_arrays import (
    SITE_CONTENTS as calculations_between_arrays,
)
from epp_topics.scientific_computing.calculations_on_arrays import (
    SITE_CONTENTS as calculations_on_arrays,
)
from epp_topics.scientific_computing.creating_arrays import (
    SITE_CONTENTS as creating_arrays,
)
from epp_topics.scientific_computing.indexing import SITE_CONTENTS as indexing
from epp_topics.scientific_computing.randomness import SITE_CONTENTS as randomness
from epp_topics.scientific_computing.speedup_intro import (
    SITE_CONTENTS as speedup_intro,
)
from epp_topics.scientific_computing.speedup_line_profile import (
    SITE_CONTENTS as speedup_line_profile,
)
from epp_topics.scientific_computing.speedup_measuring_time import (
    SITE_CONTENTS as speedup_measuring_time,
)
from epp_topics.scientific_computing.speedup_numba import (
    SITE_CONTENTS as speedup_numba,
)
from epp_topics.scientific_computing.speedup_numpy import (
    SITE_CONTENTS as speedup_numpy,
)
from epp_topics.scientific_computing.speedup_snakeviz import (
    SITE_CONTENTS as speedup_snakeviz,
)
from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as what_is_numpy

TOPICS = (
    what_is_numpy,
    creating_arrays,
    indexing,
    calculations_on_arrays,
    calculations_between_arrays,
    randomness,
    broadcasting,
    speedup_intro,
    speedup_measuring_time,
    speedup_snakeviz,
    speedup_line_profile,
    speedup_numpy,
    speedup_numba,
)


SITE_CONTENTS = {
    "chapter_title": "Scientific Computing",
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
