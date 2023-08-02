# Template for Flipped Classroom Courses Using Jupyter Book

## Purpose

This is a template repository for flipped classroom courses. It uses
[jupyter book](https://jupyterbook.org/en/stable/intro.html) to create an online
textbook with course materials built from markdown files and jupyter notebooks. It
allows to launch notebooks on JupyterHub.

## Usage

### Replace Placeholders

Find and replace the following placeholders in the entire directory.

| Placeholder                                           | Replacement Example                                                              |
| ----------------------------------------------------- | -------------------------------------------------------------------------------- |
| `COURSE_SLUG`                                         | `applied_micro`                                                                  |
| `COURSE_NAME`                                         | `Applied Microeconomics`                                                         |
| `COURSE_DESCRIPTION`                                  | `Ph.D. / M.Sc. course in Applied Microeconomics`                                 |
| `COURSE_URL`                                          | `https://www.wiwi.uni-bonn.de/gaudecker/_static/applied_micro/landing-page.html` |
|                                                       | (course website, not git repository)                                             |
| `https://github.com/iame-uni-bonn/course_jb_template` | `https://gitlab.iame.uni-bonn.de/hmg/applied_microeconomics`                     |
|                                                       | (no `.git` at the end)                                                           |
| `TEACHER_NAMES`                                       | `Hans-Martin von Gaudecker and Florian Zimmermann`                               |
| `AUTHOR_EMAIL`                                        | `hmgaudecker@uni-bonn.de`                                                        |
|                                                       | (just one e-mail address)                                                        |
| `COURSE_DATE`                                         | `Summer Term 2023`                                                               |

Rename the directory `./src/COURSE_SLUG`.

### Requirements

Create and activate the environment with

```console
$ conda/mamba env create
$ conda activate COURSE_SLUG
$ npm install
```

### Build Project

To build the project, execute

```console
$ pytask
```

### View Materials

To view the jupyter books with course materials, open

- `./student_book/index.html` (student version) or
- `./teacher_book/index.html` (teacher version) in a browser.

To view the screencast slides in the interactive version, run

```console
$ npx slidev book_source/teachers/[chapter]/screencast_[x]/slides.md
```

### Add New Chapters

1. Copy and paste `./src/COURSE_SLUG/chapter_template`, and rename according to
   `CHAPTER_NAMES` in `src/COURSE_SLUG/config.py`.
1. Append the folder name to CHAPTER_NAMES in `./src/COURSE_SLUG/config.py`.
1. Run `pytask` to build the book and work on the To-Do list that is shown on the
   landing page when opening the book.
1. Remove finished To-Dos from the list by deleting them in
   `./src/COURSE_SLUG/[chapter]/contents.md`.

### Add New To-Dos

You can add additional To-Dos in .md files as well as in markdown cells in .ipynb files.
For instance, add the following line to a markdown file:

````
```{todo}
A description of what needs to be done.
```
````

To-Dos will only show up in the teacher book.
