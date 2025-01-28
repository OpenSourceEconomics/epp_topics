"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.metrics_ml.ml_intro_diffs_metrics import (
    SITE_CONTENTS as ml_intro_diffs_metrics,
)
from epp_topics.metrics_ml.overview import SITE_CONTENTS as overview
from epp_topics.metrics_ml.sklearn_cv_hyper import SITE_CONTENTS as sklearn_cv_hyper
from epp_topics.metrics_ml.sklearn_intro import SITE_CONTENTS as sklearn_intro
from epp_topics.metrics_ml.statsmodels_intro import SITE_CONTENTS as statsmodels_intro
from epp_topics.metrics_ml.statsmodels_results import (
    SITE_CONTENTS as statsmodels_results,
)

TOPICS = (
    overview,
    statsmodels_intro,
    statsmodels_results,
    ml_intro_diffs_metrics,
    sklearn_intro,
    sklearn_cv_hyper,
)


SITE_CONTENTS = {
    "chapter_title": "Data Analysis in Python",
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
