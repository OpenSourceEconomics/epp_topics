import pandas as pd
import plotly.express as px

from epp_topics.config import SITE_SOURCE_DIR

pd.options.plotting.backend = "plotly"


LINEPLOT = (
    SITE_SOURCE_DIR
    / "pandas"
    / "inspecting_and_summarizing"
    / "screencast"
    / "public"
    / "lineplot.png"
)

SCATTERPLOT = (
    SITE_SOURCE_DIR
    / "pandas"
    / "inspecting_and_summarizing"
    / "screencast"
    / "public"
    / "scatterplot.png"
)


def task_create_lineplot(produces=LINEPLOT):
    df = px.data.gapminder()
    df = df.rename(
        columns={
            "lifeExp": "life_exp",
        },
    )
    fig = df.groupby("year")["life_exp"].mean().plot(template="plotly_dark")
    fig.write_image(produces)


def task_create_scatterplot(produces=SCATTERPLOT):
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
