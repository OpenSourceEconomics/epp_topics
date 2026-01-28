# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in
this repository.

## Project Overview

This repository contains source materials for the "Effective Programming Practices for
Economists" course website (https://effective-programming-practices.vercel.app/). It
builds a Jupyter Book from screencasts, notebooks, and quizzes organized by chapter and
topic.

## Build Commands

```bash
# Build the entire site (compiles slides, copies files, builds Jupyter Book)
pixi run pytask

# Lint and format code
pixi run ruff check src/
pixi run ruff format src/

# Run pre-commit hooks
pixi run pre-commit run --all-files
```

## Command Rules

Always use these command mappings:

- **Python**: Use `pixi run python` instead of `python` or `python3`
- **Type checker**: Use `pixi run ty` instead of running ty/mypy/pyright directly
- **Tests**: Use `pixi run tests` instead of `pytest` directly
- **Linting/formatting**: Use `prek run --all-files` instead of `ruff` directly
- **All quality checks**: Use `prek run --all-files`

Before finishing any task that modifies code, always run:

1. `pixi run ty` (type checker)
1. `pixi run tests` (tests)
1. `prek run --all-files` (quality checks)

## Architecture

### Directory Structure

```
src/epp_topics/
├── config.py                    # Global config: CHAPTER_NAMES, paths
├── task_create_book.py          # Pytask tasks for building Jupyter Book
├── task_export_screencasts.py   # Pytask tasks for exporting slides to PDF
├── {chapter_name}/              # Each chapter (e.g., software_engineering/)
│   ├── config.py                # Chapter config: aggregates topic SITE_CONTENTS
│   ├── CLAUDE.md                # Chapter-specific AI guidelines
│   └── {topic_name}/            # Each topic within a chapter
│       ├── config.py            # Topic config: pages, other files, built PDFs
│       ├── objectives_materials.ipynb  # Main content notebook
│       └── screencast/
│           └── slides.md        # Slidev presentation source
```

### Adding New Content

1. **New topic in existing chapter**: Create directory under
   `src/epp_topics/{chapter}/`, add `config.py` with `SITE_CONTENTS`,
   `objectives_materials.ipynb`, and optionally `screencast/slides.md`

1. **Topic config.py format**:

```python
SITE_CONTENTS = {
    "pages": ("objectives_materials.ipynb",),
    "other": (),  # Additional files to copy
    "built": ("{chapter}-{topic}.pdf",),  # Generated PDF from slides
}
```

3. **Chapter config.py**: Import each topic's `SITE_CONTENTS` and combine into chapter's
   `SITE_CONTENTS` with `chapter_title`

1. **Register new chapters**: Add to `CHAPTER_NAMES` list in `src/epp_topics/config.py`

### Screencast Slides

- Written in Slidev markdown format (slides.md)
- Exported to PDF via `npx slidev export`
- PDF naming convention: `{chapter}-{topic}.pdf`
- PDFs built to `.slides_pdf/` then copied to site source

### Chapter-Specific Guidelines

Each chapter has a `CLAUDE.md` file with domain-specific coding guidelines (e.g.,
`software_engineering/CLAUDE.md` contains comprehensive Python best practices). Consult
these when working on chapter content.

## Key Configuration

- **Python version**: 3.14 (see `pyproject.toml`)
- **Ruff target**: py314
- **Jupyter Book**: \<2.0
- **Quiz utilities**: `epp_topics.quiz_utilities.display_quiz`
