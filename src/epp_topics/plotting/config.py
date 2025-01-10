"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.plotting.goals_workflow import SITE_CONTENTS as goals_workflow
from epp_topics.plotting.graph_objects import SITE_CONTENTS as graph_objects
from epp_topics.plotting.quick_plots import SITE_CONTENTS as quick_plots
from epp_topics.plotting.tweak_px import SITE_CONTENTS as tweak_px
from epp_topics.plotting.what_to_plot import SITE_CONTENTS as what_to_plot
from epp_topics.plotting.why_plotly_prerequisites import (
    SITE_CONTENTS as why_plotly_prerequisites,
)

TOPICS = (
    goals_workflow,
    what_to_plot,
    why_plotly_prerequisites,
    quick_plots,
    tweak_px,
    graph_objects,
)

SITE_CONTENTS = {
    "chapter_title": "Plotting",
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
