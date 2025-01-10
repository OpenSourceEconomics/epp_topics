"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.numerical_optimization.db_line_search import (
    SITE_CONTENTS as db_line_search,
)
from epp_topics.numerical_optimization.db_trust_region import (
    SITE_CONTENTS as db_trust_region,
)
from epp_topics.numerical_optimization.df_direct_search import (
    SITE_CONTENTS as df_direct_search,
)
from epp_topics.numerical_optimization.df_trust_region import (
    SITE_CONTENTS as df_trust_region,
)
from epp_topics.numerical_optimization.example_set_up import (
    SITE_CONTENTS as example_set_up,
)
from epp_topics.numerical_optimization.grid_search import (
    SITE_CONTENTS as grid_search,
)
from epp_topics.numerical_optimization.introduction import (
    SITE_CONTENTS as introduction,
)
from epp_topics.numerical_optimization.optimagic_overview import (
    SITE_CONTENTS as optimagic_overview,
)
from epp_topics.numerical_optimization.optimization_algorithms import (
    SITE_CONTENTS as optimization_algorithms,
)
from epp_topics.numerical_optimization.optimization_histories import (
    SITE_CONTENTS as optimization_histories,
)
from epp_topics.numerical_optimization.optimization_mechanics import (
    SITE_CONTENTS as optimization_mechanics,
)

TOPICS = (
    introduction,
    optimagic_overview,
    optimization_mechanics,
    optimization_algorithms,
    optimization_histories,
    example_set_up,
    grid_search,
    db_line_search,
    db_trust_region,
    df_direct_search,
    df_trust_region,
)


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
