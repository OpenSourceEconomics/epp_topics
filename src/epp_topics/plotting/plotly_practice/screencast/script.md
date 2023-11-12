# Script: Plotting practical

## Plot entire data

- Start with:

```py
px.line(
    all_countries,
    x="year",
    y="lifeExp",
    title='Life Expectancy by Continent and Country',
)
```

- add `color="country"` only later

## Creating subplots by facet columns

- Copy from previous cell, insert

```py
facet_col="continent",
```

- Show interactivity by clicking on countries.

## Restrict data to Canada and Poland

- Move towards publication-style
- Copy first cell again

## Changing overall appearance

- Copy from previous cell, insert

```py
    # some templates: "plotly", "plotly_dark", "ggplot2", "seaborn", "simple_white"
    template="plotly_dark",
```

## Graph objects

- For publication-level graphs often not enough to use out-of-the-box functionality
- Purpose: Show these exist, idea of what you can do with them
