# Script: File Systems

- Modern Operating Systems try to hide details of how and where files are stored from
  users.
- Try to find on your smartphone where your latest download is...
- What OS's do instead is to offer combination of
  - list of recent documents (what you typical want)
  - powerful search functionality which retrieves files from whereever they may be
    stored
- Obvious that reproducibility is impossible if you don't know where your files are
  stored.
- One of the main differences between MacOS

## Unix File Systems

MacOS is fairly similar, will point out one difference

- `/` is the root directory.
- `etc` is a directory under root that contains configuration files.
- `usr` is another directory under root, which contains several other directories,
  including `bin` (for executable files) and `lib` (for library files).
- `var` is a directory under root that contains variable data like system logging files,
  and log is a directory under var for log files.
- `home` is a directory under root that contains personal directories for users, such as
  `user_1` (called `Users` with capital U on MacOS)
- `user_1` has personal documents and download directories.
- `mambaforge` is a directory under `user_1` that contains the mamba package manager for
  creating Python environments.

Let's focus on the mambaforge directory.

The sequence `root` - `home` - `user_1` - `mambaforge` is called an **absolute path**.

### Different Representations

- Graphical User Interface
- Shell:
  - Start with the root note "/"
  - Forward slash is also the directory separator

## Windows File System

- `C:` is the root directory.
- `Program Files` is where applications are typically installed.
- `Users` is where user directories are located.
- `user_1` represents the `user_1`'s home directory with Documents and Download as
  typical examples of subdirectories
- `Windows` is where the operating system files are located.
- `System32` is a directory within `Windows` that contains important system files.
- `ProgramData` is used to store application and operating system data.
- `mambaforge` is where the mamba package manager is located if you choose to install
  that.
- Each disk (physical or virtual) gets its own directory tree.
- They are not connected, but you can jump between them using the drive letters.

### Different Representations

- Graphical User Interface
- Shell:
  - Start with the root note "C:"
  - Backward slash is also the directory separator
