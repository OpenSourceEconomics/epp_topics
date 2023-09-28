"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_basics.assignment_and_scalar_types import (
    SITE_CONTENTS as ASSIGNMENT_AND_SCALAR_TYPES,
)
from epp_topics.python_basics.dicts import (
    SITE_CONTENTS as DICTS,
)
from epp_topics.python_basics.executing_notebook_browser import (
    SITE_CONTENTS as EXECUTING_NOTEBOOK_BROWSER,
)
from epp_topics.python_basics.executing_notebook_vscode import (
    SITE_CONTENTS as EXECUTING_NOTEBOOK_VSCODE,
)
from epp_topics.python_basics.executing_py_shell import (
    SITE_CONTENTS as EXECUTING_PY_SHELL,
)
from epp_topics.python_basics.executing_py_vscode import (
    SITE_CONTENTS as EXECUTING_PY_VSCODE,
)
from epp_topics.python_basics.executing_pytask_pytest_pdb import (
    SITE_CONTENTS as EXECUTING_PYTASK_PYTEST_PDB,
)
from epp_topics.python_basics.for_loops import (
    SITE_CONTENTS as FOR_LOOPS,
)
from epp_topics.python_basics.functions_basics import (
    SITE_CONTENTS as FUNCTIONS_BASICS,
)
from epp_topics.python_basics.functions_principles import (
    SITE_CONTENTS as FUNCTIONS_PRINCIPLES,
)
from epp_topics.python_basics.if_conditions import (
    SITE_CONTENTS as IF_CONDITIONS,
)
from epp_topics.python_basics.importing import (
    SITE_CONTENTS as IMPORTING,
)
from epp_topics.python_basics.lists_tuples_sets import (
    SITE_CONTENTS as LISTS_TUPLES_SETS,
)
from epp_topics.python_basics.pathlib import (
    SITE_CONTENTS as PATHLIB,
)
from epp_topics.python_basics.strings import (
    SITE_CONTENTS as STRINGS,
)
from epp_topics.python_basics.tracebacks import (
    SITE_CONTENTS as TRACEBACKS,
)

TOPICS = [
    ASSIGNMENT_AND_SCALAR_TYPES,
    STRINGS,
    LISTS_TUPLES_SETS,
    DICTS,
    FOR_LOOPS,
    IF_CONDITIONS,
    FUNCTIONS_BASICS,
    FUNCTIONS_PRINCIPLES,
    TRACEBACKS,
    IMPORTING,
    PATHLIB,
    EXECUTING_NOTEBOOK_BROWSER,
    EXECUTING_NOTEBOOK_VSCODE,
    EXECUTING_PY_SHELL,
    EXECUTING_PY_VSCODE,
    EXECUTING_PYTASK_PYTEST_PDB,
]

SITE_CONTENTS = {
    "chapter_title": "Python Basics",
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
