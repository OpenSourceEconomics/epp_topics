import pandas as pd
import pytest
from clean_data import _clean_agreement_scale, _clean_favorite_language


def test_clean_agreement_check_dtype():
    # Test with a series that contains "-77" and "-99"
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    result = _clean_agreement_scale(pd.Series([]))
    assert result.dtype == dtype


def test_clean_agreement_scale_known_missings():
    sr = pd.Series(["-77", "-99"])
    result = _clean_agreement_scale(sr)
    expected = pd.Series([pd.NA, pd.NA], dtype=result.dtype)
    pd.testing.assert_series_equal(result, expected)


def test_clean_agreement_scale_invalid_data():
    with pytest.raises(ValueError):
        _clean_agreement_scale(pd.Series([-77, "agree"]))


def test_clean_favorite_language_known_missings():
    sr = pd.Series(["-77", "-99"])
    result = _clean_favorite_language(sr)
    expected = pd.Series([pd.NA, pd.NA], dtype=result.dtype)
    pd.testing.assert_series_equal(result, expected)


def test_clean_favorite_language_expected_typos():
    sr = pd.Series(["ypthon", "python   ", "Python"])
    result = _clean_favorite_language(sr)
    expected = pd.Series(["python", "python", "python"], dtype=result.dtype)
    pd.testing.assert_series_equal(result, expected)
