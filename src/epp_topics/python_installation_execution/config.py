"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.python_installation_execution.environments import (
    SITE_CONTENTS as environments,
)
from epp_topics.python_installation_execution.executing_notebook_browser import (
    SITE_CONTENTS as executing_notebook_browser,
)
from epp_topics.python_installation_execution.executing_notebook_vscode import (
    SITE_CONTENTS as executing_notebook_vscode,
)
from epp_topics.python_installation_execution.executing_py_shell import (
    SITE_CONTENTS as executing_py_shell,
)
from epp_topics.python_installation_execution.executing_py_vscode import (
    SITE_CONTENTS as executing_py_vscode,
)
from epp_topics.python_installation_execution.executing_pytask import (
    SITE_CONTENTS as executing_pytask,
)
from epp_topics.python_installation_execution.executing_pytest import (
    SITE_CONTENTS as executing_pytest,
)
from epp_topics.python_installation_execution.installation_linux import (
    SITE_CONTENTS as installation_linux,
)
from epp_topics.python_installation_execution.installation_mac import (
    SITE_CONTENTS as installation_mac,
)
from epp_topics.python_installation_execution.installation_windows import (
    SITE_CONTENTS as installation_windows,
)
from epp_topics.python_installation_execution.installation_wsl import (
    SITE_CONTENTS as installation_wsl,
)

TOPICS = (
    installation_linux,
    installation_mac,
    installation_windows,
    installation_wsl,
    executing_notebook_browser,
    executing_notebook_vscode,
    executing_py_shell,
    executing_py_vscode,
    executing_pytask,
    executing_pytest,
    environments,
)

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
