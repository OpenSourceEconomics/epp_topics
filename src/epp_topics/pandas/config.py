"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.pandas.columns_and_indices import SITE_CONTENTS as columns_and_indices
from epp_topics.pandas.creating_variables import SITE_CONTENTS as creating_variables
from epp_topics.pandas.dataframes_and_series import (
    SITE_CONTENTS as dataframes_and_series,
)
from epp_topics.pandas.datatypes import SITE_CONTENTS as datatypes
from epp_topics.pandas.functional import SITE_CONTENTS as functional_data_management
from epp_topics.pandas.functional_fundamentals import (
    SITE_CONTENTS as functional_fundamentals,
)
from epp_topics.pandas.inspecting_and_summarizing import (
    SITE_CONTENTS as inspecting_and_summarizing,
)
from epp_topics.pandas.loading_and_saving import SITE_CONTENTS as loading_and_saving
from epp_topics.pandas.merging import SITE_CONTENTS as merging
from epp_topics.pandas.rules import SITE_CONTENTS as rules
from epp_topics.pandas.selection import SITE_CONTENTS as selection
from epp_topics.pandas.what_is_pandas import SITE_CONTENTS as what_is_pandas

TOPICS = (
    what_is_pandas,
    dataframes_and_series,
    datatypes,
    loading_and_saving,
    columns_and_indices,
    selection,
    inspecting_and_summarizing,
    creating_variables,
    rules,
    merging,
    functional_fundamentals,
    functional_data_management,
)

SITE_CONTENTS = {
    "chapter_title": "Data management with pandas",
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
