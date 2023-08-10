"""Definitions of source files for the current chapter."""


BOOK_CONTENTS = {
    "chapter_title": "Placeholder: Title as displayed in book",
    "students": {
        "prep": (
            "objectives.md",
            "preparation.md",
            # "All .md or .ipynb files",
            # "for preparation phase",
        ),
        "in_class": (
            "in_class_exercise.ipynb",
            # "All .md or .ipynb files",
            # "for in-in_class",
        ),
        "post": (
            # "All .md or .ipynb files",
            # "for post-in_class phase",
        ),
    },
    "teachers": (
        "contents.md",
        "objectives.md",
        "preparation.md",
        "in_class_exercise.ipynb",
        # "All files included in 'students'",
        # "key above, plus all files",
        # "that students should not see",
    ),
    "other": (
        # "existing figures etc.",
    ),
    "built": (
        # "screencast slides etc.",
        # "everything that is built",
    ),
}
