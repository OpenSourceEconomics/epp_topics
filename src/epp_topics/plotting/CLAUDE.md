# Plotting with Plotly - Guidelines for AI Agents

This document provides guidance for AI coding agents creating visualizations using
plotly in this codebase. Follow these best practices to generate effective, clear, and
publication-ready plots.

## Overview

This chapter covers visualization using plotly with three interfaces:

1. **Pandas backend** - Quick plots via `df.plot()`
1. **plotly.express (px)** - High-level interface for rapid exploration
1. **plotly.graph_objects (go)** - Low-level interface for full customization

## Standard Imports and Setup

Always use these standard imports when working with plotly:

```python
import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set default template
pio.templates.default = "plotly_dark"

# Enable plotly as pandas plotting backend
pd.options.plotting.backend = "plotly"
```

______________________________________________________________________

## Goals and Workflow

### Two Types of Plots

1. **Exploratory plots** - For discovering patterns in data

   - Speed is essential
   - Interactivity is valuable
   - Clear labels help even for personal use
   - Use `plotly.express` or pandas backend

1. **Publication plots** - For communicating results

   - Must be self-explanatory
   - Aesthetics matter
   - Static format required for papers
   - May need `plotly.graph_objects` for fine control

### Recommended Workflow

1. Define what question the plot should answer
1. Sketch the plot on paper first
1. Find a similar plot in the plotly documentation/gallery
1. Create a quick plot to test your ideas
1. Refine and make it publication-ready
1. Verify the plot is self-explanatory (get feedback)

______________________________________________________________________

## Chart Type Selection

### Data Types and Recommended Charts

| Data Type                         | Recommended Chart                                  |
| --------------------------------- | -------------------------------------------------- |
| Raw continuous data               | Scatterplots                                       |
| Fractions of categorical/discrete | Bar charts (potentially stacked)                   |
| Levels/amounts                    | Bar charts (include zeros!), unless interval scale |
| Changes over time                 | Line charts                                        |
| Distributions                     | Histograms, box plots, violin plots                |

______________________________________________________________________

## Five Core Visualization Guidelines

Based on Schwabish's principles:

### 1. Show the Data

- DO: Let the data be visible and interpretable
- DON'T: Obscure data with excessive decoration

### 2. Reduce the Clutter

- DO: Remove unnecessary gridlines, borders, and decorations
- DON'T: Add elements that don't convey information

### 3. Integrate Graphics and Text

- DO: Label data directly on the plot when possible
- DO: Write titles like newspaper headlines (convey the insight)
- DO: Add explanatory annotations
- DON'T: Rely solely on legends when direct labels work better

### 4. Avoid the Spaghetti Chart

- DO: Use facets to separate groups (`facet_col`, `facet_row`)
- DO: Highlight specific lines of interest
- DON'T: Plot many overlapping lines without differentiation

### 5. Start with Grey

- DO: Use grey as the default color for most elements
- DO: Use accent colors only for the most important data points
- DON'T: Use many bright colors without purpose

______________________________________________________________________

## plotly.express Quick Reference

### Basic Line Plot

```python
fig = px.line(
    df,
    x="year",
    y="value",
    color="category",
    labels={"value": "Human-Readable Label"},
)
```

### Using Pandas Backend

```python
# After setting: pd.options.plotting.backend = "plotly"
fig = df.plot(x="year", y="value", color="category")
```

### Faceted Plots (Avoiding Spaghetti)

```python
fig = px.line(
    df,
    x="year",
    y="life_expectancy",
    color="country",
    facet_col="continent",  # Split into columns by continent
)
```

### Cleaning Up Facet Labels

```python
# Remove "variable=" prefix from facet titles
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
```

### Updating Layout

```python
fig.update_layout(
    title="Descriptive Title",
    showlegend=False,  # Remove legend when using direct labels
)
```

______________________________________________________________________

## plotly.graph_objects for Custom Plots

Use graph_objects when you need fine-grained control:

### Creating Subplots

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, subplot_titles=["Europe", "Americas"])
```

### Adding Traces

```python
fig.add_trace(
    go.Scatter(
        x=data["year"],
        y=data["value"],
        name="Series Name",
        mode="lines",
        line={"color": "darkgray"},
    ),
    row=1,
    col=1,
)
```

### Highlighting Specific Data

```python
# Add highlighted trace with thicker line and accent color
fig.add_trace(
    go.Scatter(
        x=data["year"],
        y=data["value"],
        name="Poland",
        mode="lines",
        line={"color": "red", "width": 5},
    ),
    row=1,
    col=1,
)
```

### Adding Annotations

```python
fig.add_annotation(
    x=1967,
    y=77,
    text="<b>Poland</b>",
    font={"size": 14, "color": "red"},
    showarrow=False,
    row=1,
    col=1,
)
```

### Synchronizing Axes Across Subplots

```python
fig.update_xaxes(matches="x")
fig.update_yaxes(matches="y")
```

______________________________________________________________________

## DO's and DON'Ts Summary

### DO

- Use `plotly.express` for exploratory analysis (fast iteration)
- Use `plotly.graph_objects` when you need full customization
- Use facets (`facet_col`, `facet_row`) to avoid spaghetti charts
- Use grey for background elements, accent colors for highlights
- Label axes with human-readable names using the `labels` parameter
- Write descriptive titles that convey insights
- Remove legends when direct labeling is clearer
- Clean up facet labels with `for_each_annotation`
- Ensure plots are self-explanatory
- Use `fig.update_layout()` to customize appearance
- Set a consistent template with `pio.templates.default`

### DON'T

- Create overly cluttered plots with too many overlapping lines
- Use many bright colors without clear purpose
- Rely on legends when direct labels would be clearer
- Start with colors - start with grey and add color purposefully
- Forget to include zeros in bar charts showing levels
- Create plots that require external explanation to understand
- Use plotly.express when you need precise control over every element
- Forget to make interactive plots static-export-ready for publications

______________________________________________________________________

## Static Export

For publication-quality static exports, plotly uses Kaleido:

```python
# First ensure Kaleido is set up (run once in environment):
# pixi run plotly_get_chrome

# Then export:
fig.write_image("figure.png")
fig.write_image("figure.pdf")
fig.write_image("figure.svg")
```

______________________________________________________________________

## Resources

- [Plotly Python Gallery](https://plotly.com/python/)
- [Line Charts Documentation](https://plotly.com/python/line-charts/)
- [Facet Plots Documentation](https://plotly.com/python/facet-plots/)
- Schwabish: "Better Data Visualizations"
- Cairo: "How Charts Lie", "The Functional Art"
- Bergstrom & West: "Calling Bullshit", Chapter 7
