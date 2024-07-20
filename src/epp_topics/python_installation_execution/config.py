"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_installation_execution.environments import (
    SITE_CONTENTS as ENVIRONMENTS,
)
from epp_topics.python_installation_execution.executing_notebook_browser import (
    SITE_CONTENTS as EXECUTING_NOTEBOOK_BROWSER,
)
from epp_topics.python_installation_execution.executing_notebook_vscode import (
    SITE_CONTENTS as EXECUTING_NOTEBOOK_VSCODE,
)
from epp_topics.python_installation_execution.executing_py_shell import (
    SITE_CONTENTS as EXECUTING_PY_SHELL,
)
from epp_topics.python_installation_execution.executing_py_vscode import (
    SITE_CONTENTS as EXECUTING_PY_VSCODE,
)
from epp_topics.python_installation_execution.executing_pytask import (
    SITE_CONTENTS as EXECUTING_PYTASK,
)
from epp_topics.python_installation_execution.executing_pytest import (
    SITE_CONTENTS as EXECUTING_PYTEST,
)
from epp_topics.python_installation_execution.installation_linux import (
    SITE_CONTENTS as INSTALLATION_LINUX,
)
from epp_topics.python_installation_execution.installation_mac import (
    SITE_CONTENTS as INSTALLATION_MAC,
)
from epp_topics.python_installation_execution.installation_windows import (
    SITE_CONTENTS as INSTALLATION_WINDOWS,
)
from epp_topics.python_installation_execution.installation_wsl import (
    SITE_CONTENTS as INSTALLATION_WSL,
)

TOPICS = [
    INSTALLATION_LINUX,
    INSTALLATION_MAC,
    INSTALLATION_WINDOWS,
    INSTALLATION_WSL,
    EXECUTING_NOTEBOOK_BROWSER,
    EXECUTING_NOTEBOOK_VSCODE,
    EXECUTING_PY_SHELL,
    EXECUTING_PY_VSCODE,
    EXECUTING_PYTASK,
    EXECUTING_PYTEST,
    ENVIRONMENTS,
]

SITE_CONTENTS = {
    "chapter_title": "Python: Installation and Execution",
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
