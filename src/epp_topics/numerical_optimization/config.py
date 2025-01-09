"""Definitions of source files for the current chapter."""

import itertools

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
from epp_topics.scientific_computing.optimagic_overview import (
    SITE_CONTENTS as OPTIMAGIC_OVERVIEW,
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
    SITE_CONTENTS as OPTIMIZATION_MECHANICS,
)
from epp_topics.scientific_computing.set_up_function_grid_search import (
    SITE_CONTENTS as SET_UP_FUNCTION_GRID_SEARCH,
)

TOPICS = [
    SET_UP_FUNCTION_GRID_SEARCH,
    OPTIMIZATION_INTRO,
    OPTIMIZATION_MECHANICS,
    OPTIMAGIC_OVERVIEW,
    OPTIMIZATION_ALGORITHMS,
    DB_LINE_SEARCH,
    DB_TRUST_REGION,
    DF_DIRECT_SEARCH,
    DF_TRUST_REGION,
    OPTIMIZATION_HISTORIES,
]


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
