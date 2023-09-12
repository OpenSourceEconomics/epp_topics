"""Set up the directories with source files for the books."""

import shutil
import subprocess
from pathlib import Path

import nbformat
import pytask
import yaml
from pybaum.tree_util import tree_just_flatten

from epp_topics.config import (
    CHAPTER_NAMES,
    JUPYTERHUB_REPO_DIR,
    SITE_DIR,
    SITE_SOURCE_DIR,
    SRC,
    get_chapter_title,
    get_sources_for_chapter,
)
from epp_topics.process_notebook import process_notebook

for p_o_i in ("public", "internal"):
    toc_chapters = []
    all_orig_sources = []
    all_site_sources = []

    for c in CHAPTER_NAMES:
        # Relevant source files
        orig_sources = get_sources_for_chapter(
            chapter_name=c,
            p_o_i=p_o_i,
            os_o_ss="orig_source",
        )
        site_sources = get_sources_for_chapter(
            chapter_name=c,
            p_o_i=p_o_i,
            os_o_ss="site_source",
        )
        # Skip entire chapter if empty, order is important here.
        if not site_sources and not orig_sources:
            continue
        else:
            chapter_config = SRC / c / "config.py"
            all_orig_sources.append(chapter_config)

            chapter_index_file = SITE_SOURCE_DIR / p_o_i / c / "index.md"
            all_site_sources.append(chapter_index_file)

            all_orig_sources.append(orig_sources)

        # The chapter's toc file
        @pytask.mark.task(
            id=f"{p_o_i}, {c}",
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
                {k: v for k, v in site_sources.items() if k != "built"},
            ),
            strict=True,
        ):
            if depends_on.suffix == ".ipynb":

                @pytask.mark.task(
                    id=f"{p_o_i}, {c}, {produces.parent.name}/{produces.name}",
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
                        if produces.parent.parent.parent.name == "internal"
                        else "exercise"
                    )

                    nb_processed = process_notebook(nb_raw=nb_raw, ex_o_sol=ex_o_sol)

                    nbformat.write(nb_processed, produces)

                if p_o_i == "public":
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
                    id=f"{p_o_i}, {c}, {depends_on.relative_to(SRC)}",
                    kwargs={
                        "depends_on": depends_on,
                        "produces": produces,
                    },
                )
                def task_copy_chapter_source(depends_on, produces):
                    """Copy the source files for the book."""
                    shutil.copy(depends_on, produces)

        all_site_sources.append(site_sources)

        def _rel_path_for_toc(bs, p_o_i):
            return str(
                (bs.relative_to(SITE_SOURCE_DIR / p_o_i).parent / bs.stem).as_posix(),
            )

        toc_chapters.append(
            {
                "file": _rel_path_for_toc(bs=chapter_index_file, p_o_i=p_o_i),
                "sections": [
                    {
                        "file": _rel_path_for_toc(bs=bs, p_o_i=p_o_i),
                    }
                    for bs in tree_just_flatten(site_sources["toc_sources"])
                ],
            },
        )

    # Background files at the book level
    all_kwargs = [
        {
            "depends_on": SRC / f"landing-page_{p_o_i}.md",
            "produces": SITE_SOURCE_DIR / p_o_i / "landing-page.md",
        },
        *[
            {
                "depends_on": SRC / f,
                "produces": SITE_SOURCE_DIR / p_o_i / f,
            }
            for f in ["_config.yml", "ose-logo.png", "references.bib"]
        ],
    ]
    all_orig_sources.extend(
        [v for kv in all_kwargs for k, v in kv.items() if k == "depends_on"],
    )
    all_site_sources.extend(
        [v for kv in all_kwargs for k, v in kv.items() if k == "produces"],
    )

    for kwargs in all_kwargs:

        @pytask.mark.task(id=f"{p_o_i}, {kwargs['produces'].name}", kwargs=kwargs)
        def task_copy_site_source(depends_on, produces):
            """Copy the source files for the book."""
            if depends_on.name == "_config.yml":
                config_nb_exec = {
                    "execute": {
                        "execute_notebooks": "force"
                        if produces.parent.name == "internal"
                        else "off",
                        "only_build_toc_files": True,
                        "timeout": -1,
                    },
                }
                config_sphinx = {
                    "todo_include_todos": produces.parent.name == "internal",
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
    toc_file = SITE_SOURCE_DIR / p_o_i / "_toc.yml"
    all_site_sources.append(toc_file)

    @pytask.mark.task(
        id=p_o_i,
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
    site_index = SITE_SOURCE_DIR / p_o_i / "_build" / "html" / "index.html"

    @pytask.mark.task(
        id=p_o_i,
        kwargs={
            "depends_on": all_site_sources,
            "produces": site_index,
            "p_o_i": p_o_i,
        },
    )
    def task_compile_book(produces, depends_on, p_o_i):  # noqa: ARG001
        """Build the Jupyter book."""
        subprocess.run(f"jb clean {SITE_SOURCE_DIR / p_o_i}", shell=True, check=True)
        result = subprocess.run(
            f"jb build {SITE_SOURCE_DIR / p_o_i} --nitpick --warningiserror",
            shell=True,
            check=True,
        )
        if result.returncode != 0:
            raise RuntimeError("Jupyter book compilation failed.")

    # Copy the site to relevant locations.
    @pytask.mark.task(
        id=p_o_i,
        kwargs={
            "depends_on": (site_index, all_site_sources),
            "produces": SITE_DIR[p_o_i] / "index.html",
        },
    )
    def task_copy_book(produces, depends_on):
        """Copy the Jupyter book so it is easily accessible."""
        shutil.copytree(depends_on[0].parent, produces.parent, dirs_exist_ok=True)

    if p_o_i == "public" and (website := Path("/home/hmg/admin/website")).exists():

        @pytask.mark.task(
            id="copy_locally_to_website",
            kwargs={
                "depends_on": (
                    site_index,
                    all_site_sources,
                    SITE_DIR[p_o_i] / "index.html",
                ),
                "produces": website / "_static" / "epp_topics" / "index.html",
            },
        )
        def task_copy_book_to_website(depends_on, produces):
            """Copy the Jupyter book (locally) to website."""
            shutil.copytree(depends_on[0].parent, produces.parent, dirs_exist_ok=True)
