"""Definitions of source files for the current chapter."""

import itertools

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
from epp_topics.python_installation_execution.installation_pixi_intro import (
    SITE_CONTENTS as installation_pixi_intro,
)
from epp_topics.python_installation_execution.pip_and_pypi import (
    SITE_CONTENTS as pip_and_pypi,
)
from epp_topics.python_installation_execution.pixi_and_conda_forge import (
    SITE_CONTENTS as pixi_and_conda_forge,
)
from epp_topics.python_installation_execution.pixi_changing_environments import (
    SITE_CONTENTS as pixi_changing_environments,
)
from epp_topics.python_installation_execution.python_packages import (
    SITE_CONTENTS as python_packages,
)

TOPICS = (
    installation_pixi_intro,
    executing_py_shell,
    executing_py_vscode,
    executing_notebook_vscode,
    executing_pytask,
    executing_pytest,
    pixi_changing_environments,
    python_packages,
    pip_and_pypi,
    pixi_and_conda_forge,
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
