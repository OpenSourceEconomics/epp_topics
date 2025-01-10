"""Definitions of source files for the current chapter."""

import itertools

from epp_topics.git.branches import SITE_CONTENTS as branches
from epp_topics.git.cloning_repos import SITE_CONTENTS as cloning_repos
from epp_topics.git.collaboration import SITE_CONTENTS as collaboration
from epp_topics.git.committing import SITE_CONTENTS as committing
from epp_topics.git.creating_repos import SITE_CONTENTS as creating_repos
from epp_topics.git.github import SITE_CONTENTS as github
from epp_topics.git.how_git_works import SITE_CONTENTS as how_git_works
from epp_topics.git.installing_git import SITE_CONTENTS as installing_git
from epp_topics.git.introduction import SITE_CONTENTS as introduction
from epp_topics.git.merging_and_conflicts import SITE_CONTENTS as merging_and_conflicts
from epp_topics.git.pre_commits import SITE_CONTENTS as pre_commits
from epp_topics.git.staging import SITE_CONTENTS as staging
from epp_topics.git.undoing_things import SITE_CONTENTS as undoing_things
from epp_topics.git.why_git import SITE_CONTENTS as why_git

TOPICS = (
    introduction,
    why_git,
    installing_git,
    how_git_works,
    creating_repos,
    cloning_repos,
    staging,
    committing,
    undoing_things,
    branches,
    merging_and_conflicts,
    github,
    collaboration,
    pre_commits,
)

SITE_CONTENTS = {
    "chapter_title": "Git and Github",
    "pages": tuple(
        itertools.chain(
            *[topic["pages"] for topic in TOPICS],
        ),
    ),
    "other": tuple(
        # "existing figures etc.",
        itertools.chain(
            *[topic["other"] for topic in TOPICS],
        ),
    ),
    "built": tuple(
        # "screencasts etc.",
        itertools.chain(
            *[topic["built"] for topic in TOPICS],
        ),
    ),
}
