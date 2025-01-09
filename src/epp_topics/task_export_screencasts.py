"""Create figure for this subchapter's screencast."""

import shutil
import subprocess
from pathlib import Path
from typing import Annotated

from pytask import Product, task

from epp_topics.config import SITE_SOURCE_DIR, SLIDES_PDF_DIR, SRC


def find_screencasts():
    """Find all files matching screencast pattern, except for template chapter."""
    return [
        sc
        for sc in SRC.glob("**/screencast/slides.md")
        if SRC / "chapter_template" not in sc.parents
    ]


for screencast_md in find_screencasts():
    orig_dir = screencast_md.parent
    chapter_name = orig_dir.parent.parent.name
    topic_name = orig_dir.parent.name

    screencast_pdf_name = f"{chapter_name}-{topic_name}.pdf"

    screencast_pdf_built = SLIDES_PDF_DIR / screencast_pdf_name
    screencast_pdf_on_site = (
        SITE_SOURCE_DIR / orig_dir.parent.relative_to(SRC) / screencast_pdf_name
    )

    @task(id=screencast_pdf_name)
    def task_export_pdf(
        screencast_md: Path = screencast_md,
        screencast_pdf: Annotated[Path, Product] = screencast_pdf_built,
    ):
        """Create slidev presentation and export to pdf."""
        subprocess.run(
            f"npx slidev export {screencast_md.absolute()}"
            f" --output {screencast_pdf.absolute()}",
            shell=True,
            check=True,
        )

    @task(id=screencast_pdf_name)
    def task_copy_chapter_source(
        built: Path = screencast_pdf_built,
        on_site: Annotated[Path, Product] = screencast_pdf_on_site,
    ):
        """Copy a source file for the book."""
        shutil.copy(built, on_site)
