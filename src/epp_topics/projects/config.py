"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.projects.directory_structure import SITE_CONTENTS as DIRECTORY_STRUCTURE
from epp_topics.projects.paths import SITE_CONTENTS as PATHS
from epp_topics.projects.pytask_docs import SITE_CONTENTS as PYTASK_DOCS
from epp_topics.projects.reproducibility import SITE_CONTENTS as REPRODUCIBILITY
from epp_topics.projects.setup import SITE_CONTENTS as SETUP
from epp_topics.projects.what_are_templates import SITE_CONTENTS as WHAT_ARE_TEMPLATES
from epp_topics.projects.what_does_pytask_do import SITE_CONTENTS as WHAT_DOES_PYTASK_DO
from epp_topics.projects.writing_pytasks_multiple_outputs import (
    SITE_CONTENTS as WRITING_PYTASKS_MULTIPLE_OUTPUTS,
)
from epp_topics.projects.writing_simple_pytasks import (
    SITE_CONTENTS as WRITING_SIMPLE_PYTASKS,
)

TOPICS = [
    REPRODUCIBILITY,
    WHAT_DOES_PYTASK_DO,
    WRITING_SIMPLE_PYTASKS,
    WRITING_PYTASKS_MULTIPLE_OUTPUTS,
    PYTASK_DOCS,
    WHAT_ARE_TEMPLATES,
    SETUP,
    DIRECTORY_STRUCTURE,
    PATHS,
]

SITE_CONTENTS = {
    "chapter_title": "Reproducible Research",
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
