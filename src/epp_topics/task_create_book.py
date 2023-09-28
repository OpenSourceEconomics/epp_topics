"""Set up the directories with source files for the books."""

import shutil
import subprocess
from pathlib import Path
from typing import Annotated

import pytask
from pytask import PythonNode, Product
import yaml
from pybaum.tree_util import tree_just_flatten

from epp_topics.config import (
    CHAPTER_NAMES,
    SITE_DIR,
    SITE_SOURCE_DIR,
    SRC,
    get_chapter_title,
    get_sources_for_chapter,
)

toc_chapters = []
all_orig_sources = []
all_site_sources = []

for c in CHAPTER_NAMES:
    # Relevant source files
    orig_sources = get_sources_for_chapter(
        chapter_name=c,
        os_o_ss="orig_source",
    )
    site_sources = get_sources_for_chapter(
        chapter_name=c,
        os_o_ss="site_source",
    )
    # Skip entire chapter if empty, order is important here.
    if not site_sources and not orig_sources:
        continue
    else:
        chapter_config = SRC / c / "config.py"
        all_orig_sources.append(chapter_config)

        chapter_index_file = SITE_SOURCE_DIR / c / "index.md"
        all_site_sources.append(chapter_index_file)

        all_orig_sources.append(orig_sources)

    def task_create_chapter_toc(
        title: Annotated[str, PythonNode(value=get_chapter_title(c), hash=True)],
        index_file: Annotated[Path, Product] = chapter_index_file,
        ):
        """Create the toc file for the book."""
        index_file.write_text(
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
        breakpoint()
        @pytask.mark.task(
            id=f"{c}, {depends_on.relative_to(SRC)}",
            kwargs={
                "depends_on": depends_on,
                "produces": produces,
            },
        )
        def task_copy_chapter_source(depends_on, produces):
            """Copy the source files for the book."""
            shutil.copy(depends_on, produces)

    all_site_sources.append(site_sources)

    def _rel_path_for_toc(bs):
        return str(
            (bs.relative_to(SITE_SOURCE_DIR).parent / bs.stem).as_posix(),
        )

    toc_chapters.append(
        {
            "file": _rel_path_for_toc(bs=chapter_index_file),
            "sections": [
                {
                    "file": _rel_path_for_toc(bs=bs),
                }
                for bs in tree_just_flatten(site_sources["toc_sources"])
            ],
        },
    )

# Background files at the book level
all_kwargs = [
    {
        "depends_on": SRC / f,
        "produces": SITE_SOURCE_DIR / f,
    }
    for f in ["landing-page.md", "_config.yml", "ose-logo.png", "references.bib"]
]
all_orig_sources.extend(
    [v for kv in all_kwargs for k, v in kv.items() if k == "depends_on"],
)
all_site_sources.extend(
    [v for kv in all_kwargs for k, v in kv.items() if k == "produces"],
)

for kwargs in all_kwargs:

    @pytask.mark.task(id=f"{kwargs['produces'].name}", kwargs=kwargs)
    def task_copy_site_source(depends_on, produces):
        """Copy the source files for the book."""
        if depends_on.name == "_config.yml":
            config_nb_exec = {
                "execute": {
                    "execute_notebooks": "force",
                    "only_build_toc_files": True,
                    "timeout": -1,
                },
            }
            config_sphinx = {
                "todo_include_todos": False,
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
toc_file = SITE_SOURCE_DIR / "_toc.yml"
all_site_sources.append(toc_file)


@pytask.mark.task(
    id="create_toc",
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
site_index = SITE_SOURCE_DIR / "_build" / "html" / "index.html"


@pytask.mark.task(
    id="compile_book",
    kwargs={
        "depends_on": all_site_sources,
        "produces": site_index,
    },
)
def task_compile_book(produces, depends_on):  # noqa: ARG001
    """Build the Jupyter book."""
    subprocess.run(f"jb clean {SITE_SOURCE_DIR}", shell=True, check=True)
    result = subprocess.run(
        f"jb build {SITE_SOURCE_DIR} --nitpick --warningiserror",
        shell=True,
        check=True,
    )
    if result.returncode != 0:
        raise RuntimeError("Jupyter book compilation failed.")


# Copy the site to relevant locations.
@pytask.mark.task(
    id="copy_book",
    kwargs={
        "depends_on": (site_index, all_site_sources),
        "produces": SITE_DIR / "index.html",
    },
)
def task_copy_book(produces, depends_on):
    """Copy the Jupyter book so it is easily accessible."""
    shutil.copytree(depends_on[0].parent, produces.parent, dirs_exist_ok=True)
