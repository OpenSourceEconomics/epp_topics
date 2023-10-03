from pathlib import Path

import pandas as pd

BLD = Path(__file__).parent / "bld"


def task_clean_data(data=Path("gapminder.arrow"), produces=BLD / "data.pkl"):
    data = pd.read_feather(data)
    data = data.rename(
        columns={
            "lifeExp": "life_exp",
            "gdpPercap": "gdp_per_cap",
        },
    )
    data = data.query("continent == 'Asia'")

    data.to_pickle(produces)
