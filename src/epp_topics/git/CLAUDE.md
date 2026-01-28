# Git Best Practices for AI Coding Agents

This document provides guidance for AI coding agents on how to use git effectively,
based on the "Effective Programming Practices for Economists" course materials.

## Core Concepts

### What is Git?

- A distributed version control system
- Tracks changes in source code over time
- Creates snapshots (commits) you can return to later
- Repositories are stored locally on each developer's computer

### What is GitHub?

- A cloud-based platform for hosting git repositories
- Enables collaboration with coauthors
- Provides code review via pull requests
- NOT the same as git (git is local, GitHub is remote)

______________________________________________________________________

## Repository Management

### Creating Repositories

**DO:**

- Use `git init` to convert a normal folder into a git repository
- This creates a `.git` folder that tracks your project

**DON'T:**

- Assume `git init` uploads anything to GitHub (it does not)
- Create nested git repositories (avoid `git init` inside an existing repo)

### Cloning Repositories

**DO:**

- Use `git clone <URL>` to download a repository from GitHub
- Clone creates a linked copy that can be synchronized with the remote

**DON'T:**

- Download repositories as zip files (this loses the git history and remote link)
- Confuse cloning with downloading

______________________________________________________________________

## Staging and Committing

### The Staging Area

**DO:**

- Use `git status` to check which files are untracked, modified, or staged
- Use `git add <file>` to stage specific files for the next commit
- Use `git add .` to stage all changes (use with caution)
- Use `git reset` to unstage all staged files if needed

**DON'T:**

- Commit without first staging the relevant files
- Assume all modified files are automatically included in commits

### Making Commits

**DO:**

- Write descriptive commit messages that explain the "why" not just the "what"
- Use `git commit -m "Your message"` for simple commits
- Use `git commit -am "Your message"` to stage and commit all modified files in one step
- Create commits after making changes that belong together logically
- Use `git log` to inspect commit history

**DON'T:**

- Use `git commit -am` for untracked files (it only works for already-tracked files)
- Write vague commit messages like "fixed stuff" or "updates"
- Create commits automatically without user intent

### Commit Message Best Practices

**DO:**

- Start with a short summary line (50 characters or less)
- Use imperative mood ("Add feature" not "Added feature")
- Explain what changed and why

**DON'T:**

- Write overly long single-line messages
- Omit context that future readers will need

______________________________________________________________________

## Branches

### Working with Branches

**DO:**

- Use branches to try out changes without affecting the stable main branch
- Use `git branch <name>` or `git checkout -b <name>` to create new branches
- Use `git branch` (no arguments) to see which branch you are on
- Use `git checkout <branch>` to switch between branches
- Use `git branch -d <name>` to delete branches after merging

**DON'T:**

- Make experimental changes directly on the main branch
- Forget which branch you are working on before making commits
- Delete branches that have unmerged changes without warning

### Creating Feature Branches (Recommended Workflow)

1. `git checkout main` - Switch to main branch
1. `git pull` - Get latest changes from remote
1. `git checkout -b feature_branch` - Create and switch to new branch

______________________________________________________________________

## Merging and Conflict Resolution

### Merging Branches

**DO:**

- To merge branch `a` into branch `b`:
  1. `git checkout b` - Switch to the target branch
  1. `git merge a` - Merge the source branch into current branch
- Understand the difference between fast-forward and recursive merge strategies

**DON'T:**

- Merge without being on the correct target branch
- Panic if merge conflicts occur

### Resolving Merge Conflicts

**DO:**

- Modify the conflicting files manually to resolve conflicts
- After resolving, use `git add <file>` to stage the resolved files
- Then use `git commit` to complete the merge
- Read conflict markers carefully (`<<<<<<<`, `=======`, `>>>>>>>`)

**DON'T:**

- Use `git reset` to "fix" merge conflicts
- Expect a `git resolve conflict` command (it does not exist)
- Leave conflict markers in committed files

______________________________________________________________________

## Undoing Things

### Safe Operations

**DO:**

- Use `git checkout <commit-hash>` to browse earlier versions (safe, non-destructive)
- Use `git checkout main` to return from detached HEAD state
- Use `git revert <commit>` to create a new commit that undoes a specific commit

**DON'T:**

- Panic when in detached HEAD mode
- Type random git commands hoping to fix things

### Destructive Operations (Use with Extreme Caution)

**DO:**

- Use `git reset --hard` only when you truly want to permanently delete commits
- Understand that `git reset --hard` deletes commits and resets local files

**DON'T:**

- Use `git reset --hard` without understanding the consequences
- Use destructive commands on shared branches
- Modify commit history after pushing to a shared remote

### Frequency Guide for Undoing

| Action                                              | Frequency  |
| --------------------------------------------------- | ---------- |
| Undo changes before committing (`git reset --hard`) | Common     |
| Browse earlier versions via checkout                | Very often |
| Use `git revert` to undo a specific commit          | Rare       |
| Use `git reset` to undo recent commits              | Rare       |

______________________________________________________________________

## GitHub and Collaboration

### Syncing with Remote

**DO:**

- Use `git pull` to download changes from the remote repository
- Use `git push` to upload your local commits to the remote
- Always pull before starting new work to get the latest changes
- Verify changes on the GitHub page after pushing

**DON'T:**

- Push without pulling first (may cause conflicts)
- Assume local changes are automatically synced

### Pull Requests

**DO:**

- Open pull requests to propose changes for review
- Push additional commits to update an open pull request
- Use pull requests for code review before merging

**DON'T:**

- Close and recreate pull requests just to add changes
- Merge without review on collaborative projects

### Workflow for Updating Remote

1. `git add <file>` - Stage the changed file
1. `git commit -m "Descriptive message"` - Create a commit
1. `git push` - Upload to remote

______________________________________________________________________

## Pre-commit Hooks

### Understanding Pre-commit Hooks

Pre-commit hooks automate code quality checks before commits:

- **black**: Automatically formats Python code
- **ruff**: Lints code and identifies problems
- **Line-ending fixers**: Ensure cross-platform compatibility

### Working with Pre-commit Hooks

**DO:**

- Run `pre-commit install` once after cloning a repository with hooks
- Use `git commit -am "message"` to stage and commit (important because hooks run on
  staged files)
- If the first commit fails, simply try again (hooks may have auto-fixed issues)
- If the second commit fails, carefully read error messages and fix manually
- Re-add files after hooks modify them

**DON'T:**

- Panic when pre-commit hooks fail
- Look for ways to disable pre-commit hooks
- Skip reading error messages when commits fail repeatedly

### Pre-commit Hook Workflow

1. Make changes to files
1. `git commit -am "Your message"` (or `git add` then `git commit`)
1. If hooks fail and auto-fix, run the same commit command again
1. If hooks fail again, read errors and fix manually, then commit

______________________________________________________________________

## Command Reference

### Essential Commands

| Command                  | Purpose                            |
| ------------------------ | ---------------------------------- |
| `git init`               | Create a new repository            |
| `git clone <url>`        | Download a repository from GitHub  |
| `git status`             | Check repository state             |
| `git add <file>`         | Stage files for commit             |
| `git commit -m "msg"`    | Create a commit                    |
| `git commit -am "msg"`   | Stage and commit modified files    |
| `git log`                | View commit history                |
| `git branch`             | List branches / see current branch |
| `git branch <name>`      | Create a new branch                |
| `git checkout <branch>`  | Switch branches                    |
| `git checkout -b <name>` | Create and switch to new branch    |
| `git merge <branch>`     | Merge branch into current branch   |
| `git pull`               | Download changes from remote       |
| `git push`               | Upload changes to remote           |
| `git revert <commit>`    | Undo a commit (safely)             |

### Commands to Use Carefully

| Command                     | Purpose                               | Warning          |
| --------------------------- | ------------------------------------- | ---------------- |
| `git reset --hard`          | Discard all uncommitted changes       | Destructive      |
| `git reset --hard <commit>` | Delete commits after specified commit | Destructive      |
| `git push --force`          | Overwrite remote history              | Very destructive |

______________________________________________________________________

## Summary of Best Practices

1. **Always check status** before committing (`git status`)
1. **Write meaningful commit messages** that explain the why
1. **Use branches** for new features and experiments
1. **Pull before starting work** to stay synchronized
1. **Never force push** to shared branches
1. **Read error messages** carefully when things fail
1. **Prefer `git revert`** over `git reset` when collaborating
1. **Install pre-commit hooks** after cloning repositories that use them
1. **Keep commits atomic** - each commit should represent one logical change
1. **Don't panic** - most git situations are recoverable
