import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"


def _clean_agreement_scale(sr):
    known_missings = {"-77", "-99"}
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    if invalid_values := set(sr.unique()) - set(categories) - known_missings:
        msg = f"Unexpected values in agreement scale: {invalid_values}"
        raise ValueError(msg)
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.replace(dict.fromkeys(known_missings, pd.NA)).astype(dtype)


def _clean_favorite_language(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    sr = sr.str.lower().str.strip()
    sr = sr.replace("ypthon", "python")
    return sr.astype(pd.CategoricalDtype())
