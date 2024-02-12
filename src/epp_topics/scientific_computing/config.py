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
from epp_topics.scientific_computing.db_line_search import (
    SITE_CONTENTS as DB_LINE_SEARCH,
)
from epp_topics.scientific_computing.db_trust_region import (
    SITE_CONTENTS as DB_TRUST_REGION,
)
from epp_topics.scientific_computing.df_direct_search import (
    SITE_CONTENTS as DF_DIRECT_SEARCH,
)
from epp_topics.scientific_computing.df_trust_region import (
    SITE_CONTENTS as DF_TRUST_REGION,
)
from epp_topics.scientific_computing.indexing import SITE_CONTENTS as INDEXING
from epp_topics.scientific_computing.randomness import SITE_CONTENTS as RANDOMNESS
from epp_topics.scientific_computing.set_up_function_grid_search import (
    SITE_CONTENTS as SET_UP_FUNCTION_GRID_SEARCH,
)
from epp_topics.scientific_computing.what_is_numpy import SITE_CONTENTS as WHAT_IS_NUMPY

TOPICS = [
    DB_LINE_SEARCH,
    DB_TRUST_REGION,
    DF_DIRECT_SEARCH,
    DF_TRUST_REGION,
    SET_UP_FUNCTION_GRID_SEARCH,
    WHAT_IS_NUMPY,
    CREATING_ARRAYS,
    INDEXING,
    CALCULATIONS_ON_ARRAYS,
    CALCULATIONS_BETWEEN_ARRAYS,
    RANDOMNESS,
    BROADCASTING,
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
