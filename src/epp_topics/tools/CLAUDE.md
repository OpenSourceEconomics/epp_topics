# CLAUDE.md - Shell and Terminal Usage Guidelines for AI Agents

This document provides guidance for AI coding agents on shell/terminal best practices
based on the "Tools" chapter of the Effective Programming Practices for Economists
course.

## Overview

The shell is a program used to run other programs. It provides a command-line interface
(CLI) that, while requiring more initial learning than graphical interfaces, offers
significant advantages for automation, precision, and efficiency.

______________________________________________________________________

## When to Use Shell vs. GUI

### DO use the shell for:

- **Package installation and environment management** - No GUI alternative exists; shell
  is required
- **Version control with git** - Shell is the recommended approach over Git GUIs or VS
  Code integrations
- **Running tests** for Python projects
- **Running automated research pipelines**

### Either shell or GUI is acceptable for:

- Debugging Python code (VS Code debugger is a valid alternative)
- Creating, copying, and deleting files (File Explorer is acceptable)
- Trying out code in a Python REPL (Jupyter Notebook is acceptable)

### DON'T use the shell for:

- Editing files with vim when a modern editor is available - use a modern editor instead

______________________________________________________________________

## File System Navigation

### Core Concepts

- Every shell session has a **present working directory (pwd)**
- By default, this is the user's home directory
- Most operations should be performed with pwd set to the project folder

### Unix/Linux/macOS File System

- Root directory is `/`
- Home directory is typically `/home/username` (Linux) or `/Users/username` (macOS)
- Path separator is forward slash: `/`
- Example path: `/home/user_1/mambaforge`

### Windows File System

- Drive letters serve as roots (e.g., `C:`, `D:`)
- Home directory is typically `C:\Users\username`
- Path separator is backslash: `\`
- Example path: `C:\Users\user_1\mambaforge`

______________________________________________________________________

## Essential Navigation Commands

### Unix/Linux/macOS Commands

| Command     | Purpose                                |
| ----------- | -------------------------------------- |
| `pwd`       | Print the current working directory    |
| `cd <path>` | Change directory to the specified path |
| `cd ..`     | Move to the parent directory           |
| `cd ~`      | Move to the home directory             |
| `ls`        | List contents of the current directory |

### Windows PowerShell Commands

| Command                                | Purpose                                |
| -------------------------------------- | -------------------------------------- |
| `Get-Location` (or `pwd`)              | Print the current working directory    |
| `Set-Location <path>` (or `cd <path>`) | Change directory to the specified path |
| `cd ..`                                | Move to the parent directory           |
| `Get-ChildItem` (or `ls`)              | List contents of the current directory |

______________________________________________________________________

## Best Practices for AI Agents

### DO:

1. **Always verify the current working directory** before executing commands that depend
   on relative paths - use `pwd` (Unix) or `Get-Location` (Windows)

1. **Use absolute paths** when precision is critical to avoid ambiguity about file
   locations

1. **Store projects close to the home directory** to minimize typing and simplify
   navigation. Recommended structure:

   ```
   /home/username/projects/
       project_1/
       project_2/
       course_name/
           exercises/
           assignments/
           final_project/
   ```

1. **Verify navigation with pwd** after using `cd` to confirm you are in the expected
   directory

1. **Use ls/Get-ChildItem** to inspect directory contents before operating on files

1. **Chain related commands** when automation is beneficial - this is a key advantage of
   CLI over GUI

1. **Be aware of the platform** - use appropriate path separators and commands for Unix
   vs. Windows systems

### DON'T:

1. **Don't assume the working directory** - always check with `pwd` when uncertain

1. **Don't mix path separators** - use `/` for Unix/macOS and `\` for Windows

1. **Don't use shell for tasks better suited to GUIs** when the user would benefit from
   visual feedback (e.g., complex file browsing)

1. **Don't forget that `cd ..`** moves to the parent directory, not a directory
   literally named `..`

1. **Don't neglect to use the shell** for git operations, environment management,
   running tests, and automated pipelines - these are the recommended use cases

______________________________________________________________________

## Cross-Platform Considerations

When writing commands that need to work on both Unix and Windows:

1. **Navigation**: `cd` works on both platforms
1. **List files**: `ls` works on both (PowerShell aliases it)
1. **Print directory**: `pwd` works on both (PowerShell aliases it)
1. **Path handling**: Be explicit about which platform's path format is expected

______________________________________________________________________

## Efficiency Tips

1. **The z command** (Unix) - Allows fuzzy matching to jump to frequently-used
   directories with minimal typing. Similar to fuzzy matching in VS Code. Only
   recommended for advanced users who use the shell frequently.

1. **Tab completion** - Use Tab to auto-complete file and directory names to reduce
   typing errors

1. **Command history** - Use up/down arrows to access previously executed commands

______________________________________________________________________

## Summary of Key Commands

### Navigation Workflow

```bash
# Check where you are
pwd

# List what's here
ls

# Go somewhere
cd /path/to/project

# Verify you arrived
pwd

# Go up one level
cd ..

# Go home
cd ~
```

This workflow of verify-navigate-verify ensures you always know your location in the
file system before executing commands.
