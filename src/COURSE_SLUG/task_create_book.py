"""Set up the directories with source files for the books."""

import shutil
import subprocess
from pathlib import Path

import nbformat
import pytask
import yaml
from pybaum.tree_util import tree_just_flatten

from COURSE_SLUG.config import (
    BOOK_DIR,
    BOOK_SOURCE_DIR,
    CHAPTER_NAMES,
    JUPYTERHUB_REPO_DIR,
    SRC,
    filter_student_lectures,
    get_chapter_title,
    get_sources_for_chapter,
)
from COURSE_SLUG.process_notebook import process_notebook

# Filter relevant materials
sources_both_books = {
    "students": [
        (n, CHAPTER_NAMES[n])
        for n in sorted(CHAPTER_NAMES)
        if filter_student_lectures(n)
    ],
    "teachers": [(n, CHAPTER_NAMES[n]) for n in sorted(CHAPTER_NAMES)],
}

for s_o_t, all_chapters in sources_both_books.items():
    toc_chapters = []
    all_orig_sources = []
    all_book_sources = []

    for _n, c in all_chapters:
        # Relevant source files
        orig_sources = get_sources_for_chapter(
            chapter_name=c,
            s_o_t=s_o_t,
            os_o_bs="orig_source",
        )
        book_sources = get_sources_for_chapter(
            chapter_name=c,
            s_o_t=s_o_t,
            os_o_bs="book_source",
        )
        # Skip entire chapter if empty, order is important here.
        if not book_sources and not orig_sources:
            continue
        else:
            chapter_config = SRC / c / "config.py"
            all_orig_sources.append(chapter_config)

            chapter_index_file = BOOK_SOURCE_DIR / s_o_t / c / "index.md"
            all_book_sources.append(chapter_index_file)

            all_orig_sources.append(orig_sources)

        # The chapter's toc file
        @pytask.mark.task(
            id=f"{s_o_t}, {c}",
            kwargs={
                "depends_on": chapter_config,
                "produces": chapter_index_file,
                "title": get_chapter_title(c),
            },
        )
        def task_create_chapter_toc(depends_on, produces, title):  # noqa: ARG001
            """Create the toc file for the book."""
            produces.write_text(
                f"""# {title}

```{{tableofcontents}}
```
""",
                encoding="utf-8",
            )

        for depends_on, produces in zip(
            tree_just_flatten(orig_sources),
            tree_just_flatten(
                {k: v for k, v in book_sources.items() if k != "built"},
            ),
            strict=True,
        ):
            if depends_on.suffix == ".ipynb":

                @pytask.mark.task(
                    id=f"{s_o_t}, {c}, {produces.name}",
                    kwargs={
                        "depends_on": depends_on,
                        "produces": produces,
                    },
                )
                def task_preprocess_copy_notebook(depends_on, produces):
                    """Preprocess notebook."""
                    nb_raw = nbformat.read(depends_on, as_version=nbformat.NO_CONVERT)
                    ex_o_sol = (
                        "solution"
                        if produces.parent.parent.name == "teachers"
                        else "exercise"
                    )

                    nb_processed = process_notebook(nb_raw=nb_raw, ex_o_sol=ex_o_sol)

                    nbformat.write(nb_processed, produces)

                if s_o_t == "students":
                    # Use the product of previous task as dependency for copying to
                    # Jupyterhub repo.
                    @pytask.mark.task(
                        id=f"{c}, {produces.name}",
                        kwargs={
                            "depends_on": produces,
                            "produces": JUPYTERHUB_REPO_DIR / c / produces.name,
                        },
                    )
                    def task_copy_notebook_jupyterhub(depends_on, produces):
                        """Copy some file to Jupyterhub repo."""
                        shutil.copy(depends_on, produces)

            else:

                @pytask.mark.task(
                    id=f"{s_o_t}, {c}, {depends_on.relative_to(SRC)}",
                    kwargs={
                        "depends_on": depends_on,
                        "produces": produces,
                    },
                )
                def task_copy_chapter_source(depends_on, produces):
                    """Copy the source files for the book."""
                    shutil.copy(depends_on, produces)

        all_book_sources.append(book_sources)

        def _rel_path_for_toc(bs, s_o_t):
            return str(
                (bs.relative_to(BOOK_SOURCE_DIR / s_o_t).parent / bs.stem).as_posix(),
            )

        toc_chapters.append(
            {
                "file": _rel_path_for_toc(bs=chapter_index_file, s_o_t=s_o_t),
                "sections": [
                    {
                        "file": _rel_path_for_toc(bs=bs, s_o_t=s_o_t),
                    }
                    for bs in tree_just_flatten(book_sources["toc_sources"])
                ],
            },
        )

    # Background files at the book level
    all_kwargs = [
        {
            "depends_on": SRC / f"landing-page_{s_o_t}.md",
            "produces": BOOK_SOURCE_DIR / s_o_t / "landing-page.md",
        },
        *[
            {
                "depends_on": SRC / f,
                "produces": BOOK_SOURCE_DIR / s_o_t / f,
            }
            for f in ["_config.yml", "uni-bonn-blue.jpg", "references.bib"]
        ],
    ]
    all_orig_sources.extend(
        [v for kv in all_kwargs for k, v in kv.items() if k == "depends_on"],
    )
    all_book_sources.extend(
        [v for kv in all_kwargs for k, v in kv.items() if k == "produces"],
    )

    for kwargs in all_kwargs:

        @pytask.mark.task(id=f"{s_o_t}, {kwargs['produces'].name}", kwargs=kwargs)
        def task_copy_book_source(depends_on, produces):
            """Copy the source files for the book."""
            if depends_on.name == "_config.yml":
                config_nb_exec = {
                    "execute": {
                        "execute_notebooks": "force"
                        if produces.parent.name == "teachers"
                        else "off",
                        "only_build_toc_files": True,
                        "timeout": -1,
                    },
                }
                config_sphinx = {
                    "todo_include_todos": produces.parent.name == "teachers",
                }
                with depends_on.open(mode="r", encoding="utf-8") as d:
                    config_file = yaml.safe_load(d)
                config_file.update(config_nb_exec)
                config_file["sphinx"]["config"].update(config_sphinx)
                with produces.open(mode="w", encoding="utf-8") as produces:
                    yaml.safe_dump(
                        config_file,
                        stream=produces,
                        default_flow_style=False,
                        sort_keys=False,
                    )
            else:
                shutil.copy(depends_on, produces)

    # Main table of contents.
    toc = {
        "format": "jb-book",
        "root": "landing-page",
        "chapters": toc_chapters,
    }
    toc_file = BOOK_SOURCE_DIR / s_o_t / "_toc.yml"
    all_book_sources.append(toc_file)

    @pytask.mark.task(
        id=s_o_t,
        kwargs={
            "depends_on": all_orig_sources,
            "produces": toc_file,
            "toc": toc,
        },
    )
    def task_create_toc(depends_on, produces, toc):  # noqa: ARG001
        """Main table of contents."""
        with produces.open(mode="w", encoding="utf-8") as f:
            yaml.dump(toc, stream=f, default_flow_style=False, sort_keys=False)

    # Compile the book.
    book_index = BOOK_SOURCE_DIR / s_o_t / "_build" / "html" / "index.html"

    @pytask.mark.task(
        id=s_o_t,
        kwargs={
            "depends_on": all_book_sources,
            "produces": book_index,
            "s_o_t": s_o_t,
        },
    )
    def task_compile_book(produces, depends_on, s_o_t):  # noqa: ARG001
        """Build the Jupyter book."""
        subprocess.run(f"jb clean {BOOK_SOURCE_DIR / s_o_t}", shell=True)
        result = subprocess.run(
            f"jb build {BOOK_SOURCE_DIR / s_o_t} --nitpick --warningiserror",
            shell=True,
        )
        if result.returncode != 0:
            raise RuntimeError("Jupyter book compilation failed.")

    # Copy the book to relevant locations.
    @pytask.mark.task(
        id=s_o_t,
        kwargs={
            "depends_on": (book_index, all_book_sources),
            "produces": BOOK_DIR[s_o_t] / "index.html",
        },
    )
    def task_copy_book(produces, depends_on):
        """Copy the Jupyter book so it is easily accessible."""
        shutil.copytree(depends_on[0].parent, produces.parent, dirs_exist_ok=True)

    if s_o_t == "students" and (website := Path("/home/hmg/admin/website")).exists():

        @pytask.mark.task(
            id="copy_locally_to_website",
            kwargs={
                "depends_on": (
                    book_index,
                    all_book_sources,
                    BOOK_DIR[s_o_t] / "index.html",
                ),
                "produces": website / "_static" / "fsp" / "index.html",
            },
        )
        def task_copy_book_to_website(depends_on, produces):
            """Copy the Jupyter book (locally) to website."""
            shutil.copytree(depends_on[0].parent, produces.parent, dirs_exist_ok=True)
