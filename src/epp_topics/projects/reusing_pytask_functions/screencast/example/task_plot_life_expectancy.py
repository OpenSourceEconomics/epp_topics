from pathlib import Path

import pandas as pd
from pytask import task

pd.options.plotting.backend = "plotly"

BLD = Path(__file__).parent / "bld"


for region in ("Asia", "Europe"):

    @task(id=region)
    def task_plot_life_expectancy(
        data_file=BLD / "data.pkl",
        produces=BLD / f"life_expectancy_{region.lower()}.svg",
        region=region,
    ):
        df = pd.read_pickle(data_file)
        fig = _plot_life_expectancy(df[df["continent"] == region])
        fig.write_image(produces)

    def _plot_life_expectancy(df):
        return df.plot(
            x="year",
            y="life_exp",
            color="country",
            title="Life Expectancy",
        )
