"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.numerical_optimization.db_line_search import (
    SITE_CONTENTS as DB_LINE_SEARCH,
)
from epp_topics.numerical_optimization.db_trust_region import (
    SITE_CONTENTS as DB_TRUST_REGION,
)
from epp_topics.numerical_optimization.df_direct_search import (
    SITE_CONTENTS as DF_DIRECT_SEARCH,
)
from epp_topics.numerical_optimization.df_trust_region import (
    SITE_CONTENTS as DF_TRUST_REGION,
)
from epp_topics.numerical_optimization.example_set_up import (
    SITE_CONTENTS as EXAMPLE_SET_UP,
)
from epp_topics.numerical_optimization.grid_search import (
    SITE_CONTENTS as GRID_SEARCH,
)
from epp_topics.numerical_optimization.optimagic_overview import (
    SITE_CONTENTS as OPTIMAGIC_OVERVIEW,
)
from epp_topics.numerical_optimization.optimization_algorithms import (
    SITE_CONTENTS as OPTIMIZATION_ALGORITHMS,
)
from epp_topics.numerical_optimization.optimization_histories import (
    SITE_CONTENTS as OPTIMIZATION_HISTORIES,
)
from epp_topics.numerical_optimization.optimization_intro import (
    SITE_CONTENTS as OPTIMIZATION_INTRO,
)
from epp_topics.numerical_optimization.optimization_mechanics import (
    SITE_CONTENTS as OPTIMIZATION_MECHANICS,
)

TOPICS = [
    OPTIMIZATION_INTRO,
    OPTIMIZATION_MECHANICS,
    OPTIMAGIC_OVERVIEW,
    OPTIMIZATION_ALGORITHMS,
    OPTIMIZATION_HISTORIES,
    EXAMPLE_SET_UP,
    GRID_SEARCH,
    DB_LINE_SEARCH,
    DB_TRUST_REGION,
    DF_DIRECT_SEARCH,
    DF_TRUST_REGION,
]


SITE_CONTENTS = {
    "chapter_title": "Numerical Optimization",
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
