# Script: Setting up a project

There are no slides, just live demo

## Motivation (show title slide)

Give a brief motivation what cookiecutter helps to do:

- Select the correct version of the example
- Configure the settings according to taste (e.g. license, ...)
- Use the project name (slug) for folder names, etc.

## Where to get help (show docs)

[Documentation of the cookiecutter dialogue](https://econ-project-templates.readthedocs.io/en/stable/getting_started/index.html#customising-the-template-for-your-needs)

## Create a github repo

- Create an empty github repo and copy the link
- Explain that they should select to not have a license or readme

## Install cookiecutter

Need to install into the base environment (else might get nested envs)

`pip install cookiecutter`

(could also use conda at home)

## Do the setup (show shell)

- no pre-commits yet!
- Do show connection to git repo

## Verify the setup (show file explorer)

- Show the project folder named like their project slug
- Run pytask and show that it finds tasks
- Do not discuss directory structure yet
