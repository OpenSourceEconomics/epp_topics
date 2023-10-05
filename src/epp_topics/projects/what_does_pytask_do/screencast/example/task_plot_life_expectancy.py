from pathlib import Path

import pandas as pd

pd.options.plotting.backend = "plotly"

BLD = Path(__file__).parent / "bld"


def task_plot_life_expectancy(
    data_file=BLD / "data.pkl",
    produces=BLD / "life_expectancy.svg",
):
    df = pd.read_pickle(data_file)
    fig = _plot_life_expectancy(df)
    fig.write_image(produces)


def _plot_life_expectancy(df):
    return df.plot(
        x="year",
        y="life_exp",
        color="country",
        title="Life Expectancy",
    )
