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
title: Effective Programming Practices for Economists
defaults:
  layout: center
---

### Effective Programming Practices for Economists

<br>

# Software engineering


### Reusing test functions

<br>


Janoś Gabler and Hans-Martin von Gaudecker



---

# Careful with "or"-style conditions

```python
def test_clean_agreement_scale_invalid_data():
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series(["-77", "typo"]))
```

<br/>

- Could solve by a careful check of message coming with ValueError
- Much clearer: Run once for each element of `["-77", "typo"]`

<br/>

---

# Reusing test functions

```python
@pytest.mark.parametrize("invalid_input", [-77, "typo"])
def test_clean_agreement_scale_invalid_data(invalid_input):
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series([invalid_input]))
```

- first argument is a string with the test function input
- second argument is an iterable
- test function will be run once for each element of the iterable
- could have more than one argument to test function
  - including expected output
  - see [documentation](https://docs.pytest.org/en/stable/how-to/parametrize.html#how-to-parametrize-fixtures-and-test-functions) for syntax

---

# One test function, two tests

<img src="run_parametrized.png" class="rounded" width="650"/>


---

# Countercheck fails as it is supposed to


<img src="run_fail_for_valid_element.png" class="rounded" width="650"/>
