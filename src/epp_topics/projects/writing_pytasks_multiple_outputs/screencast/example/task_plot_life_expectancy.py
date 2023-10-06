from pathlib import Path

import pandas as pd

pd.options.plotting.backend = "plotly"

BLD = Path(__file__).parent / "bld"


products = {
    "Asia": BLD / "life_expectancy_asia.svg",
    "Europe": BLD / "life_expectancy_europe.svg",
}


def task_plot_life_expectancy(
    data_file=BLD / "data.pkl",
    produces=products,
):
    df = pd.read_pickle(data_file)
    for region, fig_file in produces.items():
        fig = _plot_life_expectancy(df[df["continent"] == region])
        fig.write_image(fig_file)


def _plot_life_expectancy(df):
    return df.plot(
        x="year",
        y="life_exp",
        color="country",
        title="Life Expectancy",
    )
