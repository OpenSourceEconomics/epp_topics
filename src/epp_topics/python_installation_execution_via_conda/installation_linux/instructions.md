# Installing Python on Linux (conda/mamba)

```{warning}
This page is about the **conda** / **mamba** package manager. Since 2025, we recommend
using **pixi** instead, see the [updated chapter](python-installation-and-execution)
```


There are many different ways to install the Python language and Python packages. Below,
we provide one way that works well for everything we need in the class. Please stick
exactly to the instructions unless you know what you are doing and are absolutely sure
you will never need any help from us.

If you have previously installed Python in a different way you can either keep your
installation (if you know what you are doing) or uninstall it and do a fresh install
according to the instructions.

We will cover the following topics:

1. How to install **mamba**: Mamba is a fast package manager that will install
   everything else. We install it via miniforge.
1. How to create the **course environment**: The course environment is a collection of
   Python packages that we will need for the course.

## Installing mamba

Go to
[https://github.com/conda-forge/miniforge#download](https://github.com/conda-forge/miniforge#download)
and Download the Linux x86_64 version of the installer in your Downloads folder.

![0_download](0_download.png)

Open a Terminal in the directory to which you downloaded the installer. You can use
`pwd` to find out where you are and `ls` to verify that the installer is actually there.

![1_cd.png](1_cd.png)

Type `bash Miniforge3-Linux-x86_64.sh` and hit enter.

![2_bash.png](2_bash.png)

Then, you will have to hit enter several times more until you get to the license
agreement. Type `yes` and hit enter again.

![3_accept.png](3_accept.png)

Next, you can choose the location where miniforge should be installed. This should be a
path with no spaces or special characters in it. As long as your username does not
contain such characters, you should go with the default.

![4_location.png](4_location.png)

Next, you will be asked whether you want to run `conda init`. Type `yes` and hit enter.

![5_conda_init.png](5_conda_init.png)

After a while, your screen should look like this.

![6_done.png](6_done.png)

Before you can use mamba, **you need to restart your terminal!**. After the restart, you
can type `mamba info` to quickly check your installation. If it worked, you will see the
mamba logo.

![7_mamba_info.png](7_mamba_info.png)

## Creating the course environment

The course environment is a collection of packages that we need for the class. Some of
those packages are not included in the standard anaconda distribution.

Later in the course, you will learn many benefits of using virtual environments. Until
then, believe us they are a good idea.

You start by downloading the

```{eval-rst}
:download:`course environment <../environment.yml>`
```

As before, open your Terminal in the directory where you chose to save the course
environment. You can use `pwd` to find out where you are and `ls` to verify that the file
is where you expect it to be.

![8_show.png](8_show.png)

Execute `mamba env create -f environment.yml`. This will print a lot of things to your
terminal and take a while. Do not interrupt it or close the terminal.

![9_create.png](9_create.png)

When environment creation is finished, it will give you the commands to activate the
environment.

![10_done.png](10_done.png)

To check that everything worked, you can activate the environment once. You will have to
activate it again each time you start a new Terminal. More about that later.

![11_activate.png](11_activate.png)
