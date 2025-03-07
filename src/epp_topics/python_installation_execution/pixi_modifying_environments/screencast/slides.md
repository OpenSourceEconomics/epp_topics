---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br/>

# Python Installation and Execution

### Modifying Pixi environments

<br/>


Janoś Gabler, Hans-Martin von Gaudecker, and Tim Mensinger

---

# The pyproject.toml file


<div class="grid grid-cols-[30%_70%] gap-5">
<div>

```toml
# pyproject.toml

[tool.pixi.project]
name = "toy-project"
channels = ["conda-forge"]
platforms = [
  "linux-64",
  "osx-64",
  "osx-arm64",
  "win-64",
]

[tool.pixi.dependencies]
python = ">=3.13"
numpy = ">=2.2.3"
```

</div>
<div>

- The `pyproject.toml` file can be used to configure pixi for the project

- Dependencies are tracked in the `[tool.pixi.dependencies]` table

- Will see two ways of changing this:

  - Using `pixi add [package]` in a shell

  - Modifying it directly in `pyproject.toml`


</div>
</div>


---

# What is in the environment?


```console{1,2,15,17}
$ pixi list
Package           Version    Build                 Size       Kind   Source
_libgcc_mutex     0.1        conda_forge           2.5 KiB    conda  _libgcc_mutex
_openmp_mutex     4.5        2_gnu                 23.1 KiB   conda  _openmp_mutex
bzip2             1.0.8      h4bc722e_7            246.9 KiB  conda  bzip2
ca-certificates   2025.1.31  hbcca054_0            154.4 KiB  conda  ca-certificates
ld_impl_linux-64  2.43       h712a8e2_4            655.5 KiB  conda  ld_impl_linux-64
libblas           3.9.0      31_h59b9bed_openblas  16.5 KiB   conda  libblas
libcblas          3.9.0      31_he106b2a_openblas  16.4 KiB   conda  libcblas
...
libstdcxx         14.2.0     h8f9b012_2            3.7 MiB    conda  libstdcxx
libuuid           2.38.1     h0b41bf4_0            32.8 KiB   conda  libuuid
libzlib           1.3.1      hb9d3cd8_2            59.5 KiB   conda  libzlib
ncurses           6.5        h2d0b736_3            870.7 KiB  conda  ncurses
numpy             2.2.3      py313h17eae1a_0       8.1 MiB    conda  numpy
openssl           3.4.1      h7b32b05_0            2.8 MiB    conda  openssl
python            3.13.2     hf636f53_101_cp313    31.7 MiB   conda  python
python_abi        3.13       5_cp313               6.1 KiB    conda  python_abi
readline          8.2        h8c095d6_2            275.9 KiB  conda  readline
tk                8.6.13     noxft_h4845f30_101    3.2 MiB    conda  tk
tzdata            2025a      h78e105d_0            120 KiB    conda  tzdata
```


---

# Adding dependencies

<div class="grid grid-cols-[40%_60%] gap-20">
<div>

```console
$ pixi add pandas
```

</div>
<div>

```toml
# pyproject.toml

[tool.pixi.project]
name = "toy-project"
channels = ["conda-forge"]
platforms = [
  "linux-64",
  "osx-64",
  "osx-arm64",
  "win-64",
]

[tool.pixi.dependencies]
python = ">=3.13"
numpy = ">=2.2.3"
pandas = ">=2.2.3,<3"
```

</div>
</div>

---

# Adding dependencies (2)


- You can change the `pyproject.toml` file directly:

  - Add dependencies to the `[tool.pixi.dependencies]` table

  - When calling `pixi run` or `pixi install`, pixi will install the dependencies



- **Version constraints**

  - pandas version 2.2 or higher: `pandas = ">=2.2"`

  - pandas version 2.2.x: `pandas = "~=2.2"`

  - pandas version 2.2.0: `pandas = "==2.2.0"`

  - most recent version *(that is compatible with other packages)*: `pandas = "*"`


---

# Adding PyPi dependencies

<div class="grid grid-cols-[40%_60%] gap-20">
<div>

```console
$ pixi add --pypi pdbp
```

</div>
<div>

```toml
# pyproject.toml

[tool.pixi.project]
name = "toy-project"
channels = ["conda-forge"]
platforms = [
  "linux-64",
  "osx-64",
  "osx-arm64",
  "win-64",
]

[tool.pixi.dependencies]
python = ">=3.13"
numpy = ">=2.2.3"
pandas = ">=2.2.3,<3"

[tool.pixi.pypi-dependencies]
pdbp = "*"
```

</div>
</div>
---

# The lock file

- Upon installation of dependencies, pixi creates the `pixi.lock` file

- The lock file contains the exact versions of the dependencies that were installed

- The lock file is automatically updated when any dependency is changed

- This ensures reproducibility of the environment / results

- The lock file **should** be committed to the repository
