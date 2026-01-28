# Pandas Best Practices for AI Coding Agents

This document provides guidance for AI coding agents on how to write pandas code
following the best practices established in this programming course. These guidelines
emphasize modern pandas features, functional programming patterns, and efficient data
manipulation.

## Modern Pandas Configuration

Always enable modern pandas features at the start of any script or notebook:

```python
import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
```

**DO:**

- Use pandas version 2.1 or higher
- Use pyarrow version 13.0 or higher
- Use `engine="pyarrow"` when loading CSV files for better dtypes

**DON'T:**

- Use the deprecated `inplace` argument
- Rely on implicit copies of DataFrames

## DataFrames and Series

### Mental Models

- **DataFrame as labeled matrix**: Think of DataFrames as 2D arrays with row and column
  labels
- **DataFrame as dict of columns**: Each column is a Series; useful for understanding
  performance characteristics

### Creating DataFrames

**DO:**

- Create small DataFrames for debugging and testing:
  ```python
  df = pd.DataFrame(data=[[1, "bla"], [3, "blubb"]], columns=["a", "b"], index=["c", "d"])
  ```
- Use tiny inputs to recreate and solve problems before applying to real data

**DON'T:**

- Only work with full datasets when debugging

### Index Alignment

**DO:**

- Understand that assignment is index-aligned:
  ```python
  sr = pd.Series([2.71, 3.14], index=["d", "c"])
  df["new_col"] = sr  # Aligns by index, not position
  ```
- Use meaningful indices (not just RangeIndex) for safer operations

**DON'T:**

- Use float values in indices
- Have duplicate values in indices when possible

## Columns and Indices

### Setting the Index

**DO:**

- Use `set_index` and `reset_index` for index manipulation:
  ```python
  df = df.set_index(["country", "year"])
  df = df.reset_index()
  ```
- Use meaningful indices containing actual data (e.g., country + year)

**DON'T:**

- Rely solely on RangeIndex when you have meaningful identifiers
- Drop and recreate indices carelessly (can cause subtle bugs)

### Renaming Columns

**DO:**

- Use dictionaries with `rename` for selective renaming:
  ```python
  new_names = {"life_exp": "life_expectancy", "country": "country_name"}
  df = df.rename(columns=new_names)
  ```
- Use functions for systematic renaming when appropriate

## Data Types

### Type Selection

**DO:**

- Set optimal dtypes explicitly:
  ```python
  better_dtypes = {
      "country": pd.CategoricalDtype(),
      "continent": pd.CategoricalDtype(),
      "year": pd.UInt16Dtype(),
      "life_exp": pd.Float64Dtype(),
  }
  df = df.astype(better_dtypes)
  ```
- Use `pd.CategoricalDtype()` for variables with a fixed, small set of values
- Use `pd.StringDtype()` for actual text data
- Choose appropriate numeric types based on data range

**DON'T:**

- Accept default dtypes without consideration
- Use strings when categoricals are more appropriate

### Working with Strings and Categoricals

**DO:**

- Use the `.str` accessor for string operations:
  ```python
  sr.str.lower()
  sr.str.strip()
  sr.str.replace("old", "new")
  ```
- Use the `.cat` accessor for categorical operations
- Define ordered categories when appropriate:
  ```python
  cat_type = pd.CategoricalDtype(
      categories=["low", "middle", "high"],
      ordered=True,
  )
  ```

## Loading and Saving Data

### File Formats

**DO:**

- Use `.pkl` (pickle) for intermediate files not shared with others
- Use `.arrow` (Apache Arrow) for files to share
- Use `engine="pyarrow"` when reading CSV files:
  ```python
  df = pd.read_csv("data.csv", engine="pyarrow")
  ```

**DON'T:**

- Use `.dta` unless sharing with Stata users
- Use `.fwf` (fixed-width format) unless absolutely necessary

### Recommended Pattern

```python
# Read
df = pd.read_csv("source.csv", engine="pyarrow")
# Save processed data
df.to_feather("processed.arrow")  # For sharing
df.to_pickle("processed.pkl")  # For internal use
```

## Selection

### Column Selection

**DO:**

- Use single brackets for Series: `df["column"]`
- Use double brackets for DataFrame: `df[["col1", "col2"]]`

### Row Selection

**DO:**

- Use `.loc` for label-based selection:
  ```python
  df.loc[1]  # Single row
  df.loc["Cuba"]  # By label
  df.loc[("Cuba", 2002)]  # MultiIndex
  df.loc[[1, 3], ["country", "year"]]  # Multiple rows and columns
  ```
- Use Boolean Series for filtering:
  ```python
  df[df["year"] >= 2005]
  ```
- Use `.query()` for readable conditions:
  ```python
  df.query("year >= 2005 & continent == 'Europe'")
  ```

**DON'T:**

- Use `.iloc` (position-based) unless absolutely necessary
- Mix up row and column selection syntax

## Creating Variables

### Vectorized Operations

**DO:**

- Use numpy functions for math operations:
  ```python
  df["log_life_exp"] = np.log(df["life_exp"])
  ```
- Use arithmetic between Series:
  ```python
  df["gdp_billion"] = df["gdp_per_cap"] * df["pop"] / 1e9
  ```
- Use `.replace()` for value recoding:
  ```python
  df["country_code"] = df["country"].replace({"Cuba": "CUB", "Spain": "ESP"})
  ```
- Use `.where()` for vectorized conditionals:
  ```python
  helper = pd.Series("rich", index=df.index)
  df["income_status"] = helper.where(
      cond=df["gdp_per_cap"] > 10000,
      other="not rich",
  )
  ```

### Looping Guidelines

**DO: Loop over columns**

```python
clean = pd.DataFrame()
for var in varlist:
    clean[var] = clean_variable(df[var])
```

**DON'T: Loop over rows**

- Avoid `df.iterrows()`, `df.apply()` row-wise, list comprehensions over rows
- These are just Python loops in disguise and are slow
- Use vectorized operations instead

## Merging Datasets

### Concatenation

**DO:**

- Use `pd.concat` for stacking DataFrames:
  ```python
  # Vertical (default)
  pd.concat([top, bottom])

  # Horizontal
  pd.concat([left, right], axis="columns")
  ```
- Ensure indices are compatible before concatenation

**DON'T:**

- Use `pd.concat` with non-meaningful indices (can silently produce wrong results)

### Merging

**DO:**

- Always specify merge keys explicitly:
  ```python
  pd.merge(left, right, on=["country", "year"])
  ```
- Choose the appropriate join type:
  ```python
  pd.merge(left, right, on=["country", "year"], how="left")  # Keep all left rows
  pd.merge(left, right, on=["country", "year"], how="outer")  # Keep all rows
  pd.merge(left, right, on=["country", "year"], how="inner")  # Only matching
  ```
- Check data before and after merging
- Verify expected number of observations

**DON'T:**

- Leave merge arguments at defaults without consideration
- Assume inner join (default) is what you want

## Functional Data Cleaning

### The Three Rules

1. **Start with an empty DataFrame**
1. **Touch every variable just once**
1. **Touch with a pure function**

### Implementation Pattern

**DO:**

```python
def clean_data(raw):
    df = pd.DataFrame(index=raw.index)
    df["coding_genius"] = clean_agreement_scale(raw["Q001"])
    df["learned_a_lot"] = clean_agreement_scale(raw["Q002"])
    df["favorite_language"] = clean_favorite_language(raw["Q003"])
    return df


def clean_agreement_scale(sr):
    sr = sr.replace({"-77": pd.NA, "-99": pd.NA})
    categories = ["strongly disagree", "disagree", "neutral", "agree", "strongly agree"]
    dtype = pd.CategoricalDtype(categories=categories, ordered=True)
    return sr.astype(dtype)


def clean_favorite_language(sr):
    sr = sr.str.lower().str.strip()
    sr = sr.replace("ypthon", "python")
    return sr.astype(pd.CategoricalDtype())


# Usage
raw_survey = pd.read_csv("survey.csv")
cleaned_survey = clean_data(raw_survey)
cleaned_survey.to_feather("bld/survey_cleaned.feather")
```

**DON'T (Imperative approach):**

```python
# Avoid this pattern
df = pd.read_csv("survey.csv")
df = df.rename(columns=new_names)
for var in ["coding_genius", "learned_a_lot"]:
    df[var] = df[var].replace({"-77": pd.NA, "-99": pd.NA})
    # ... more modifications
df["favorite_language"] = df["favorite_language"].str.lower()
# ... variables in invalid intermediate states
```

### Why Functional Approach

- Function names document what the code does (better than comments)
- No intermediate invalid states
- Code cannot be executed in wrong order
- Functions are reusable and testable
- Easy to find what a variable contains (search for `variable_name =`)
- Clear separation of data management and analysis

### Handling Simple Cases

If you just need to rename a variable without cleaning:

```python
df["sensible_name"] = raw["sxn3"]  # Identity function is a pure function
```

## Complex Data Structures

### Three Principles (Normal Forms)

1. **Values have no internal structure** (First Normal Form)

   - Store atomic values only
   - Example: Store first and last names separately

1. **No redundant information** (Second Normal Form)

   - Store time-constant characteristics in separate tables
   - Avoid duplication across rows

1. **Variable names have no structure** (Long format preferred)

   - Use long format for data management
   - Convert to wide only when needed for specific analyses

### Long vs Wide Format

**Prefer long format:**

```text
# Long format (preferred for data management)
| country | year | gdp_per_cap | pop      |
|---------|------|-------------|----------|
| Cuba    | 2002 | 6341        | 11226999 |
| Cuba    | 2007 | 8948        | 11416987 |
```

**Avoid wide format for data management:**

```text
# Wide format (only for specific analyses)
| country | gdp_per_cap_2002 | gdp_per_cap_2007 | pop_2002   | pop_2007   |
|---------|------------------|------------------|------------|------------|
| Cuba    | 6341             | 8948             | 11226999   | 11416987   |
```

## Inspecting and Summarizing Data

### Quick Inspection

**DO:**

- Use `.describe()` for summary statistics:
  ```python
  df[["life_exp", "pop", "gdp_per_cap"]].describe()
  ```
- Use `.head()` and `.tail()` to view subsets
- Use `.dtypes` to check column types
- Use `.value_counts()` for categorical data:
  ```python
  df["country"].value_counts()
  ```
- Use `.unique()` to see distinct values

### Quick Plotting

**DO:**

```python
pd.options.plotting.backend = "plotly"
df.groupby("year")["life_exp"].mean().plot()  # Line plot
df.plot.scatter(x="year", y="life_exp")  # Scatter plot
sr.hist()  # Histogram
```

## Summary Checklist

When writing pandas code, ensure you:

- [ ] Enable modern pandas options at the start
- [ ] Use `engine="pyarrow"` when reading CSV files
- [ ] Set appropriate dtypes (categoricals for fixed sets, proper numeric types)
- [ ] Use meaningful indices
- [ ] Use `.loc` for label-based selection
- [ ] Use vectorized operations instead of row loops
- [ ] Follow the three rules of functional data cleaning
- [ ] Use pure functions for data transformations
- [ ] Check data before and after merges
- [ ] Specify merge keys and join types explicitly
- [ ] Prefer long format for data management
- [ ] Never modify source data files
