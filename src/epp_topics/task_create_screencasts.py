"""Create figure for this subchapter's screencast."""

import shutil
import subprocess
from pathlib import Path
from typing import Annotated

from pytask import Product, task

from epp_topics.config import SITE_SOURCE_DIR, SRC


def find_orig_screencasts():
    """Find all files matching screencast pattern, except for template chapter."""
    return [
        sc
        for sc in SRC.glob("**/screencast/slides.md")
        if sc.parent.parent.parent.name != "chapter_template"
    ]


for orig_screencast in find_orig_screencasts():
    orig_dir = orig_screencast.parent
    screencast_dir = SITE_SOURCE_DIR / orig_dir.relative_to(SRC)
    screencast_md = screencast_dir / orig_screencast.name

    chapter_name = orig_dir.parent.parent.name
    topic_name = orig_dir.parent.name
    screencast_pdf = screencast_dir.parent / f"{chapter_name}-{topic_name}.pdf"

    @task(id=f"{chapter_name}, {topic_name}")
    def task_copy_style_css(
        orig: Path = SRC / "slidev_config" / "style.css",
        prod: Annotated[Path, Product] = screencast_dir / "style.css",
    ):
        """Copy style.css for slidev presentation."""
        shutil.copy(orig, prod)

    @task(id=f"{chapter_name}, {topic_name}")
    def task_copy_slides_md(
        orig: Path = orig_screencast,
        prod: Annotated[Path, Product] = screencast_md,
    ):
        """Copy slides.md for slidev presentation."""
        shutil.copy(orig, prod)

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
