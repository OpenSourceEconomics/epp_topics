# Installing Python with Windows Subsystem for Linux (WSL2)

## Why this Guide

One way to circumvent the problems with Windows Shell and other issues of compatibility
between Windows and Python is to install on Windows a Virtual Machine (VM) for Linux.
Virtual machines are programs that allow you to run a different operating system (OS)
than the one you have installed on your computer.

The easiest way to set up a virtual machine in Windows is to use Windows Subsystem for
Linux (WSL2). This page will guide you through the installation of WSL2 and how to set
up VSCode to use it.

We recommend this approach to those of you who are already familiar with Shells and Linux,
or to those who are willing to learn and use them by putting in some extra effort.
Given potential unexpected complications with Virtual Machines, we may not manage to
provide support to you in all cases, and you will need to be able (and patient enough)
to sort out problems on your own. The upside of doing this will be that you will have
 a Unix-based system like Linux on your Windows installation to run your
programs, which is generally easier and more effective once you get used to it. Linux
tends to have less compatibility issues than Windows with various python libraries;
additionally, having a separate VM for work will allow you to keep your Windows
installation "clean", which can be useful if you use it for other activities (e.g.
video games).

## What is WSL 2
Windows Subsystem for Linux 2 (WSL2) is a new version of the Windows Subsystem for Linux
 architecture that powers the Windows Subsystem for Linux to run ELF64 Linux binaries on
 Windows. Its primary goals are to increase file system performance, as well as adding
 full system call compatibility.

In laymen terms, this means that it is a tool that lets
you install a Linux distribution on your Windows machine, and run programs through it.
The advantage of using WSL2 compared to other virtual machines is that it is very easy
to set up, since it is already built into Windows 10, and it is well integrated with
VSCode.

## Installing WSL2

###

### Choosing a Linux Distribution


## Setting up and using WSL2 with VSCode
