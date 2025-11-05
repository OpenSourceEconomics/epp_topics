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
title: EPP — Pre-commit hooks
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Version Control and collaboration with Git and Github

### Pre-commit hooks

<br>

Janoś Gabler and Hans-Martin von Gaudecker


---

# What are pre-commit hooks

- We saw the importance of following style guides
- Pre-commit hooks are tools to help you automate style guides
- Examples of pre-commit hooks are:
  - The black formatter that automatically formats your code
  - The ruff linter that tells you about problems and fixes some of them
  - Line-ending fixers for better compatibility across platforms
- Save a lot of time but have a learning curve


---

# Activating pre-commit hooks

- Open a terminal
- Install the `pre_commit` python package
  - `pixi global install pre-commit`
- Change directory to the root of your repository
- Execute `pre-commit install`

Just needs to be done once after cloning the repository


---

# Configuring pre-commit hooks


<div class="flex gap-12">
<div>

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black
        language_version: python3.11
```

</div>
<div>

- Pre-commit hooks are configured in `.pre-commit-config.yaml`
- Typically inherited from the project templates or copy it from another project
- Example shows just the black formatter


</div>
</div>


---

# A useful git command

- `git commit -am "Your message."` stages and commits all modified files
- Does not work for untracked files
- Important because pre-commit hooks run over staged files!

---

# A badly formatted python file

```python
def clean_data(raw):
    df = pd.DataFrame(index=raw.index)
    df["coding_genius"]=clean_agreement_scale(raw['Q001'])
    df['learned_a_lot']=clean_agreement_scale(

      raw['Q002'])
    df['favorite_language'] = clean_favorite_language(raw['Q003'])
    return df

def clean_agreement_scale(sr):
    sr = sr.replace({'-77': pd.NA,'-99':pd.NA})
    categories = ['strongly disagree',
     'disagree',
'neutral', 'agree',
      'strongly agree'         ]
    dtype = pd.CategoricalDtype(categories=categories,
    ordered=True)
    return sr.astype(dtype)

```

---

# Git status

<img src="/git_status.png" class="rounded" width="700"/>

---

# First commit fails

<img src="/first_commit.png" class="rounded" width="700"/>


---

# Second commit works

<img src="/second_commit.png" class="rounded" width="700"/>
