---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: Effective Programming Practices for Economists
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Installation and execution

### Environment files

<br/>


Janoś Gabler and Hans-Martin von Gaudecker

---

# Environment files vs. environments

- **environment.yml**:
    - A recipe to create environments
    - Under version control
    - Shared with team members
- **environment**:
    - A collection of python packages stored on your computer
    - Independent of other environments you might have
- You get from environment files to environments by using

`mamba env create -f environment.yml`

---

# Anatomy of `environment.yml`

<div class="flex gap-4">
<div>

```yaml
name: mini-env
channels: [conda-forge, nodefaults]
dependencies:
  - python==3.11
  - pandas
  - pip:
      - pdbp
```

</div>
<div>

- Name can be anything (not containing spaces)
- Channels: You rarely need more than conda-forge
- Dependencies: List of Python packages and python
  - Can have equality or inequality constraints on versions
  - Only use pip for packages that are not conda/mamba installable
- Environment files should be hand-written and maintained

</div>
</div>


---

# Dependencies are installed automatically

<div class="flex gap-4">
<div>

<br/>
<br/>

- The mini environment from above will contain the following packages
- Many are low-level dependencies you don't have to care about
- Some exact versions are OS specific
- Listing all of them would create a non-portable environment



</div>
<div>

```txt
_libgcc_mutex    0.1
_openmp_mutex    4.5
bzip2            1.0.8
ca-certificates  2023.11.17
ld_impl_linux-64 2.40
libblas          3.9.0
libcblas         3.9.0
libffi           3.4.2
libgcc-ng        13.2.0
libgfortran-ng   13.2.0
libgfortran5     13.2.0
libgomp          13.2.0
liblapack        3.9.0
libnsl           2.0.1
libopenblas      0.3.25
libsqlite        3.44.2
libstdcxx-ng     13.2.0
libuuid          2.38.1
libzlib          1.2.13
ncurses          6.4
```


</div>

<div>


```txt
numpy            1.26.2
openssl          3.2.0
pandas           2.1.4
pdbp             1.5.0
pip              23.3.1
pygments         2.17.2
python           3.11.0
python-dateutil  2.8.2
python-tzdata    2023.3
python_abi       3.11
pytz             2023.3.post1
readline         8.2
setuptools       68.2.2
six              1.16.0
tabcompleter     1.3.0
tk               8.6.13
tzdata           2023c
wheel            0.42.0
xz               5.2.6
```

</div>


</div>



---

# How to add a package

- Just installing packages into an environment from the shell is not reproducible
- Instead:
  - Add the package to `environment.yml`
  - Use `mamba env update -f environment.yml`
- If you have any problem:
  - `mamba env remove --name mini-env`
  - `mamba env create -f environment.yml`
