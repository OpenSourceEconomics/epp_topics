"""Create figure for this week's screencast."""

import shutil
import subprocess
from pathlib import Path

import pytask

from COURSE_SLUG.config import BOOK_SOURCE_DIR, SRC

THIS_DIR = Path(__file__).parent.resolve()
OUT_DIRS = {
    s_o_t: BOOK_SOURCE_DIR / s_o_t / THIS_DIR.parent.name / THIS_DIR.name
    for s_o_t in ("students", "teachers")
}
COPY_SCREENCAST_KWARGS = {
    "depends_on": {
        "slides.md": THIS_DIR / "slides.md",
        "package.json": SRC / "slidev_config" / "package.json",
        "style.css": SRC / "slidev_config" / "style.css",
    },
    "produces": {
        "slides.md": OUT_DIRS["teachers"] / "slides.md",
        "package.json": OUT_DIRS["teachers"] / "package.json",
        "style.css": OUT_DIRS["teachers"] / "style.css",
    },
}
SCREENCAST_DEPS = COPY_SCREENCAST_KWARGS["produces"]
SCREENCAST_PDFS = {
    s_o_t: BOOK_SOURCE_DIR / s_o_t / THIS_DIR.parent.name / f"{THIS_DIR.name}.pdf"
    for s_o_t in ("students", "teachers")
}


# Copy all sources for the screencast.


@pytask.mark.skipif(THIS_DIR.name == "chapter_template", reason="Template chapter.")
@pytask.mark.task(id=THIS_DIR.name, kwargs=COPY_SCREENCAST_KWARGS)
def task_copy_sources(depends_on, produces):
    """Copy sources for slidev presentation."""
    for k, v in depends_on.items():
        shutil.copy(v, produces[k])


# Export slides to pdf.


@pytask.mark.skipif(THIS_DIR.name == "chapter_template", reason="Template chapter.")
@pytask.mark.depends_on(SCREENCAST_DEPS)
@pytask.mark.produces(SCREENCAST_PDFS["teachers"])
def task_export_pdf(depends_on, produces):
    """Create slidev presentation and export to pdf."""
    subprocess.run(
        f"npx slidev export {depends_on['slides.md'].absolute()}"
        f" --output {produces.absolute()}",
        shell=True,
    )


# Copy pdf to students book.


@pytask.mark.skipif(THIS_DIR.name == "chapter_template", reason="Template chapter.")
@pytask.mark.task(
    id=THIS_DIR.name,
    kwargs={
        "depends_on": SCREENCAST_PDFS["teachers"],
        "produces": SCREENCAST_PDFS["students"],
    },
)
def task_copy_pdf_for_students(depends_on, produces):
    """Copy the pdf slides."""
    shutil.copy(depends_on, produces)
