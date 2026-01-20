import itertools

from epp_topics.type_hints.advanced_patterns import SITE_CONTENTS as advanced_patterns
from epp_topics.type_hints.basic_syntax import SITE_CONTENTS as basic_syntax
from epp_topics.type_hints.collections_generics import (
    SITE_CONTENTS as collections_generics,
)
from epp_topics.type_hints.dataclasses_typing import SITE_CONTENTS as dataclasses_typing
from epp_topics.type_hints.introduction import SITE_CONTENTS as introduction
from epp_topics.type_hints.stringly_to_strongly import (
    SITE_CONTENTS as stringly_to_strongly,
)

TOPICS = (
    introduction,
    basic_syntax,
    collections_generics,
    dataclasses_typing,
    advanced_patterns,
    stringly_to_strongly,
)

SITE_CONTENTS = {
    "chapter_title": "Type Hints",
    "pages": tuple(itertools.chain(*[topic["pages"] for topic in TOPICS])),
    "other": tuple(itertools.chain(*[topic["other"] for topic in TOPICS])),
    "built": tuple(itertools.chain(*[topic["built"] for topic in TOPICS])),
}
