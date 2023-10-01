import pandas as pd
import plotly.express as px

from epp_topics.config import SITE_SOURCE_DIR

pd.options.plotting.backend = "plotly"


PRODUCT = (
    SITE_SOURCE_DIR
    / "pandas"
    / "inspecting_and_summarizing"
    / "screencast"
    / "public"
    / "lineplot.png"
)


def task_create_plot(produces=PRODUCT):
    df = px.data.gapminder()
    df = df.rename(
        columns={
            "lifeExp": "life_exp",
        },
    )
    fig = df.groupby("year")["life_exp"].mean().plot(template="plotly_dark")
    fig.write_image(produces)
