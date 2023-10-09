import pandas as pd
from clean_data import _clean_agreement_scale, _clean_favorite_language


def test_clean_agreement_scale_check_dtype():
    expected = pd.CategoricalDtype(
        categories=[
            "strongly disagree",
            "disagree",
            "neutral",
            "agree",
            "strongly agree",
        ],
        ordered=True,
    )
    actual = _clean_agreement_scale(pd.Series([])).dtype
    assert expected == actual


def test_clean_agreement_scale_known_missings():
    result = _clean_agreement_scale(pd.Series(["-77", "-99"]))
    expected = pd.Series([pd.NA, pd.NA], dtype=result.dtype)
    pd.testing.assert_series_equal(result, expected)


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
