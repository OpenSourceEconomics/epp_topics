from pathlib import Path

import pandas as pd
import plotly.express as px
import pytask

pd.options.plotting.backend = "plotly"


@pytask.mark.try_first
def task_create_lineplot(produces=Path() / "public" / "lineplot.svg"):
    df = px.data.gapminder()
    df = df.rename(
        columns={
            "lifeExp": "life_exp",
        },
    )
    fig = df.groupby("year")["life_exp"].mean().plot(template="plotly_dark")
    fig.write_image(produces)


@pytask.mark.try_first
def task_create_scatterplot(produces=Path() / "public" / "scatterplot.svg"):
    df = px.data.gapminder()
    df = df.rename(
        columns={
            "lifeExp": "life_exp",
        },
    )
    fig = df.plot.scatter(
        x="year",
        y="life_exp",
        color="country",
        template="plotly_dark",
    )
    fig.write_image(produces)
