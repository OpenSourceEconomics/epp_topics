"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.pandas.columns_and_indices import SITE_CONTENTS as COLUMNS_AND_INDICES
from epp_topics.pandas.creating_variables import SITE_CONTENTS as CREATING_VARIABLES
from epp_topics.pandas.dataframes_and_series import (
    SITE_CONTENTS as DATAFRAMES_AND_SERIES,
)
from epp_topics.pandas.datatypes import SITE_CONTENTS as DATATYPES
from epp_topics.pandas.functional import SITE_CONTENTS as FUNCTIONAL_DATA_MANAGEMENT
from epp_topics.pandas.inspecting_and_summarizing import (
    SITE_CONTENTS as INSPECTING_AND_SUMMARIZING,
)
from epp_topics.pandas.joins import SITE_CONTENTS as JOINS
from epp_topics.pandas.loading_and_saving import SITE_CONTENTS as LOADING_AND_SAVING
from epp_topics.pandas.normal_forms import SITE_CONTENTS as NORMAL_FORMS
from epp_topics.pandas.selection import SITE_CONTENTS as SELECTION
from epp_topics.pandas.what_is_pandas import SITE_CONTENTS as WHAT_IS_PANDAS

TOPICS = [
    WHAT_IS_PANDAS,
    DATAFRAMES_AND_SERIES,
    DATATYPES,
    LOADING_AND_SAVING,
    COLUMNS_AND_INDICES,
    SELECTION,
    INSPECTING_AND_SUMMARIZING,
    CREATING_VARIABLES,
    NORMAL_FORMS,
    JOINS,
    FUNCTIONAL_DATA_MANAGEMENT,
]
SITE_CONTENTS = {
    "chapter_title": "Data management with pandas",
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
