"""Create figure for this subchapter's screencast."""

import subprocess
from pathlib import Path
from typing import Annotated

from pytask import Product, task

from epp_topics.config import SITE_SOURCE_DIR, SRC


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
    screencast_pdf = (
        SITE_SOURCE_DIR
        / orig_dir.parent.relative_to(SRC)
        / f"{chapter_name}-{topic_name}.pdf"
    )

    @task(id=f"{chapter_name}, {topic_name}")
    def task_export_pdf(
        screencast_md: Path = screencast_md,
        screencast_pdf: Annotated[Path, Product] = screencast_pdf,
    ):
        """Create slidev presentation and export to pdf."""
        subprocess.run(
            f"npx slidev export {screencast_md.absolute()}"
            f" --output {screencast_pdf.absolute()}",
            shell=True,
            check=True,
        )
