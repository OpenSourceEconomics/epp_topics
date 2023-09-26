"""Definitions of source files for the current chapter."""
import itertools

from epp_topics.git.branches import SITE_CONTENTS as BRANCHES
from epp_topics.git.collaboration import SITE_CONTENTS as COLLABORATION
from epp_topics.git.committing import SITE_CONTENTS as COMMITTING
from epp_topics.git.creating_repos import SITE_CONTENTS as CREATING_REPOS
from epp_topics.git.github import SITE_CONTENTS as GITHUB
from epp_topics.git.how_git_works import SITE_CONTENTS as HOW_GIT_WORKS
from epp_topics.git.installing_git import SITE_CONTENTS as INSTALLING_GIT
from epp_topics.git.introduction import SITE_CONTENTS as INTRODUCTION
from epp_topics.git.merging_and_conflicts import SITE_CONTENTS as MERGING_AND_CONFLICTS
from epp_topics.git.staging import SITE_CONTENTS as STAGING
from epp_topics.git.undoing_things import SITE_CONTENTS as UNDOING_THINGS
from epp_topics.git.why_git import SITE_CONTENTS as WHY_GIT

TOPICS = [
    INTRODUCTION,
    WHY_GIT,
    INSTALLING_GIT,
    HOW_GIT_WORKS,
    CREATING_REPOS,
    STAGING,
    COMMITTING,
    UNDOING_THINGS,
    BRANCHES,
    MERGING_AND_CONFLICTS,
    GITHUB,
    COLLABORATION,
]

SITE_CONTENTS = {
    "chapter_title": "Git and Github",
    "public": tuple(
        itertools.chain(
            ("content_objectives.md",),
            *[topic["public"] for topic in TOPICS],
        ),
    ),
    "internal": tuple(
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
        itertools.chain(
            (
                "internal_overview.md",
                "content_objectives.md",
            ),
            *[topic["internal"] for topic in TOPICS],
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
