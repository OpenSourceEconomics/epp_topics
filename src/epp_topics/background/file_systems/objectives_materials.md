(background-file_systems)=

# File Systems

## Learning Objectives

After working through this topic, you should be able to:

- describe how a file system is organised.
- explain the most important differences between Unix-based and Windows-based file
  systems.

## Materials

Before working through this material, it should be helpful to go through the background
material on the [history of operating systems](background-os_history) and
[graphs](background-graphs).

Here is the
[Screencast](https://player.uni-bonn.educast.nrw/7a1c2ae3-2614-4fc5-939e-6bde0663a83e).
These are the [slides](background-file_systems.pdf). Some verbal explanations are
reproduced below.

One important difference that is not mentioned in the screencast is that Unix-based file
systems are case-sensitive, whereas Windows-based file systems are not. This means that
`Documents` and `documents` are two different directories on Unix-based systems, but the
same directory on Windows. This can lead to subtle differences when running the same
code on different file systems; let alone sharing files via a cloud. E.g., Dropbox has
created a
[specific flag for that case](https://help.dropbox.com/en-en/organize/case-conflict).

### Unix File System

```{raw} html
<div class="mermaid">
graph LR
    A["/"] --- B["etc"]
    A["/"] --- C["usr"]
    C["usr"] --- D["bin"]
    C["usr"] --- E["lib"]
    A["/"] --- F["var"]
    F["var"] --- G["log"]
    A["/"] --- H["home"]
    H["home"] --- I["user_1"]
    I["user_1"] --- J["Documents"]
    I["user_1"] --- K["Downloads"]
    I["user_1"] --- L["mambaforge"]
</div>
```

- `/` is the root directory.
- `etc` is a directory under root that contains configuration files.
- `usr` is another directory under root, which contains several other directories,
  including `bin` (for executable files) and `lib` (for library files).
- `var` is a directory under root that contains variable data like system logging files,
  and log is a directory under var for log files.
- `home` is a directory under root that contains personal directories for users, such as
  `user_1`. On MacOS, `home` is called `Users` (with capital U).
- `user_1` has personal documents and download directories.
- `mambaforge` is a directory under `user_1` that contains the mamba package manager for
  creating Python environments (unless you choose to install the entire Anaconda Python
  distribution).

```{mermaid}
graph LR
    A[C:]
    A --> B["Program Files"]
    B --> C["Microsoft"]
    B --> D["Adobe"]
    A --> E["Users"]
    E --> F["user_1"]
    F --> H["Documents"]
    F --> I["Downloads"]
    F --> P["mambaforge"]
    A --> M["Windows"]
    M --> N["System32"]
    A --> O["ProgramData"]
    X["I:"] --> Z["Second Drive"]
```

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

## Further Reading

Your favourite search engine and Wikipedia will guide your way. There is lots of
accessible material around.
