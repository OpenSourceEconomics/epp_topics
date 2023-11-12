"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.plotting.goals_workflow import SITE_CONTENTS as GOALS_WORKFLOW
from epp_topics.plotting.plotly_practice import SITE_CONTENTS as PLOTLY_PRACTICE
from epp_topics.plotting.what_to_plot import SITE_CONTENTS as WHAT_TO_PLOT
from epp_topics.plotting.why_plotly_prerequisites import (
    SITE_CONTENTS as WHY_PLOTLY_PREREQUISITES,
)

TOPICS = [GOALS_WORKFLOW, WHAT_TO_PLOT, WHY_PLOTLY_PREREQUISITES, PLOTLY_PRACTICE]


SITE_CONTENTS = {
    "chapter_title": "Plotting",
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
