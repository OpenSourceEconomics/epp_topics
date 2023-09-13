"""Create figure for this subchapter's screencast."""

import shutil
import subprocess
from pathlib import Path

import pytask

from epp_topics.config import SITE_SOURCE_DIR, SRC

THIS_DIR = Path(__file__).parent.resolve()
OUT_DIRS = {
    p_o_i: SITE_SOURCE_DIR
    / p_o_i
    / THIS_DIR.parent.parent.name
    / THIS_DIR.parent.name
    / THIS_DIR.name
    for p_o_i in ("public", "internal")
}
COPY_SCREENCAST_KWARGS = {
    "depends_on": {
        "slides.md": THIS_DIR / "slides.md",
        "package.json": SRC / "slidev_config" / "package.json",
        "style.css": SRC / "slidev_config" / "style.css",
    },
    "produces": {
        "slides.md": OUT_DIRS["internal"] / "slides.md",
        "package.json": OUT_DIRS["internal"] / "package.json",
        "style.css": OUT_DIRS["internal"] / "style.css",
    },
}
SCREENCAST_DEPS = COPY_SCREENCAST_KWARGS["produces"]
SCREENCAST_PDFS = {
    p_o_i: d.parent / f"{d.parent.parent.name}-{d.parent.name}.pdf"
    for p_o_i, d in OUT_DIRS.items()
}


# Copy all sources for the screencast.


@pytask.mark.skipif(
    THIS_DIR.parent.parent.name == "chapter_template",
    reason="Template chapter.",
)
@pytask.mark.task(id=THIS_DIR.name, kwargs=COPY_SCREENCAST_KWARGS)
def task_copy_sources(depends_on, produces):
    """Copy sources for slidev presentation."""
    for k, v in depends_on.items():
        shutil.copy(v, produces[k])


# Export slides to pdf.


@pytask.mark.skipif(
    THIS_DIR.parent.parent.name == "chapter_template",
    reason="Template chapter.",
)
@pytask.mark.depends_on(SCREENCAST_DEPS)
@pytask.mark.produces(SCREENCAST_PDFS["internal"])
def task_export_pdf(depends_on, produces):
    """Create slidev presentation and export to pdf."""
    subprocess.run(
        f"npx slidev export {depends_on['slides.md'].absolute()}"
        f" --output {produces.absolute()}",
        shell=True,
        check=True,
    )


# Copy pdf to students book.


@pytask.mark.skipif(
    THIS_DIR.parent.parent.name == "chapter_template",
    reason="Template chapter.",
)
@pytask.mark.task(
    id=THIS_DIR.name,
    kwargs={
        "depends_on": SCREENCAST_PDFS["internal"],
        "produces": SCREENCAST_PDFS["public"],
    },
)
def task_copy_pdf_for_students(depends_on, produces):
    """Copy the pdf slides."""
    shutil.copy(depends_on, produces)
