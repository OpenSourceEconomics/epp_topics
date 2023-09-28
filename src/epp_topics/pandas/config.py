"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.pandas.columns_and_indices import SITE_CONTENTS as COLUMNS_AND_INDICES
from epp_topics.pandas.creating_variables import SITE_CONTENTS as CREATING_VARIABLES
from epp_topics.pandas.datatypes import SITE_CONTENTS as DATATYPES
from epp_topics.pandas.functional import SITE_CONTENTS as FUNCTIONAL_DATA_MANAGEMENT
from epp_topics.pandas.groupby import SITE_CONTENTS as GROUPBY
from epp_topics.pandas.inspecting_and_summarizing import (
    SITE_CONTENTS as INSPECTING_AND_SUMMARIZING,
)
from epp_topics.pandas.joins import SITE_CONTENTS as JOINS
from epp_topics.pandas.loading_and_saving import SITE_CONTENTS as LOADING_AND_SAVING
from epp_topics.pandas.missings import SITE_CONTENTS as MISSINGS
from epp_topics.pandas.normal_forms import SITE_CONTENTS as NORMAL_FORMS
from epp_topics.pandas.selection import SITE_CONTENTS as SELECTION
from epp_topics.pandas.series_and_dataframes import (
    SITE_CONTENTS as SERIES_AND_DATAFRAMES,
)
from epp_topics.pandas.what_is_pandas import SITE_CONTENTS as WHAT_IS_PANDAS

TOPICS = [
    WHAT_IS_PANDAS,
    SERIES_AND_DATAFRAMES,
    DATATYPES,
    LOADING_AND_SAVING,
    CREATING_VARIABLES,
    INSPECTING_AND_SUMMARIZING,
    MISSINGS,
    COLUMNS_AND_INDICES,
    SELECTION,
    NORMAL_FORMS,
    JOINS,
    GROUPBY,
    FUNCTIONAL_DATA_MANAGEMENT,
]
SITE_CONTENTS = {
    "chapter_title": "Data management with pandas",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
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
