"""Set up the directories with source files for the books."""

import shutil
import subprocess
from pathlib import Path
from typing import Annotated, Any

import yaml
from deepdiff import DeepHash
from pybaum.tree_util import tree_just_flatten
from pytask import Product, PythonNode, task

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

    @task(id=c)
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

    for orig, prod in zip(
        tree_just_flatten(orig_sources),
        tree_just_flatten(
            {k: v for k, v in site_sources.items() if k != "built"},
        ),
        strict=True,
    ):

        @task(id=f"{orig.relative_to(SRC)}")
        def task_copy_chapter_source(
            orig: Path = orig,
            prod: Annotated[Path, Product] = prod,
        ):
            """Copy a source file for the book."""
            shutil.copy(orig, prod)

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

for fn in ["_config.yml", "landing-page.md", "ose-logo.png", "references.bib"]:
    all_orig_sources.append(orig := SRC / fn)
    all_site_sources.append(prod := SITE_SOURCE_DIR / fn)

    @task(id=fn)
    def task_copy_site_source(
        orig: Path = orig,
        prod: Annotated[Path, Product] = prod,
    ):
        """Copy the source files for the book."""
        if orig.name == "_config.yml":
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
            with orig.open(mode="r", encoding="utf-8") as d:
                config_file = yaml.safe_load(d)
            config_file.update(config_nb_exec)
            config_file["sphinx"]["config"].update(config_sphinx)
            with prod.open(mode="w", encoding="utf-8") as prod:
                yaml.safe_dump(
                    config_file,
                    stream=prod,
                    default_flow_style=False,
                    sort_keys=False,
                )
        else:
            shutil.copy(orig, prod)


# Main table of contents.
toc = {
    "format": "jb-book",
    "root": "landing-page",
    "chapters": toc_chapters,
}
toc_file = SITE_SOURCE_DIR / "_toc.yml"
all_site_sources.append(toc_file)


def task_create_toc(
    toc: Annotated[dict[str, Any], PythonNode(value=toc, hash=DeepHash)],
    toc_file: Annotated[Path, Product] = toc_file,
):
    """Main table of contents."""
    with toc_file.open(mode="w", encoding="utf-8") as f:
        yaml.dump(toc, stream=f, default_flow_style=False, sort_keys=False)


def task_compile_book(
    deps: list[Path] = all_site_sources,  # noqa: ARG001
    site_index: Annotated[Path, Product] = SITE_SOURCE_DIR  # noqa: ARG001
    / "_build"
    / "html"
    / "index.html",
):
    """Build the Jupyter book.

    Arguments are needed to make sure that the task is executed correctly.
    """
    subprocess.run(f"jb clean {SITE_SOURCE_DIR}", shell=True, check=True)
    result = subprocess.run(
        f"jb build {SITE_SOURCE_DIR} --nitpick --warningiserror",
        shell=True,
        check=True,
    )
    if result.returncode != 0:
        raise RuntimeError("Jupyter book compilation failed.")


def task_copy_book(
    site_index_local: Path = SITE_SOURCE_DIR / "_build" / "html" / "index.html",
    all_site_sources: list[Path] = all_site_sources,  # noqa: ARG001
    site_index_public: Annotated[Path, Product] = SITE_DIR / "index.html",
):
    """Copy the Jupyter book to location from where it is published.

    The arguments `all_site_sources` is needed to make sure that the task is executed
    correctly.
    """
    shutil.copytree(
        site_index_local.parent,
        site_index_public.parent,
        dirs_exist_ok=True,
    )
