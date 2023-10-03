from pathlib import Path

import plotly.express as px

BLD = Path(__file__).parent / "bld"


def task_clean_data(produces=BLD / "data.pkl"):
    df = px.data.gapminder()
    df = df.rename(
        columns={
            "lifeExp": "life_exp",
            "gdpPercap": "gdp_per_cap",
        },
    )

    df = df.query("continent == 'Asia'")
    df.to_pickle(produces)
