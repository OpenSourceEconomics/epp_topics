"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.projects.directory_structure import SITE_CONTENTS as directory_structure
from epp_topics.projects.paths import SITE_CONTENTS as paths
from epp_topics.projects.pytask_docs import SITE_CONTENTS as pytask_docs
from epp_topics.projects.reproducibility import SITE_CONTENTS as reproducibility
from epp_topics.projects.reusing_pytask_functions import (
    SITE_CONTENTS as reusing_pytask_functions,
)
from epp_topics.projects.setup import SITE_CONTENTS as setup
from epp_topics.projects.what_are_templates import SITE_CONTENTS as what_are_templates
from epp_topics.projects.what_does_pytask_do import SITE_CONTENTS as what_does_pytask_do
from epp_topics.projects.writing_pytasks_multiple_outputs import (
    SITE_CONTENTS as writing_pytasks_multiple_outputs,
)
from epp_topics.projects.writing_simple_pytasks import (
    SITE_CONTENTS as writing_simple_pytasks,
)

TOPICS = (
    reproducibility,
    what_does_pytask_do,
    writing_simple_pytasks,
    writing_pytasks_multiple_outputs,
    reusing_pytask_functions,
    pytask_docs,
    what_are_templates,
    setup,
    directory_structure,
    paths,
)

SITE_CONTENTS = {
    "chapter_title": "Reproducible Research",
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
