# Module 04 — Data Visualization

**Prerequisite:** Python basics and Pandas DataFrames. **Goal:** use plots to investigate data, spot possible issues and communicate evidence.

## Study these plot types
1. Histogram — how a numeric variable is distributed.
2. Bar chart — compare counts or summaries across categories.
3. Scatter plot — inspect the relationship between two numeric variables.
4. Line chart — show a sequence or time trend when order matters.
5. Box plot — summarise median, quartiles and points beyond whiskers under the chosen plotting convention.
6. Correlation heatmap — show pairwise numeric correlation estimates.
7. Prediction/residual plot — inspect how model errors vary.

## Example: histogram and scatter plot
```python
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "area": [45, 50, 60, 70, 85, 90, 100],
    "price": [110, 120, 138, 160, 190, 205, 225],
})

fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].hist(data["price"], bins=5)
axes[0].set_title("Price distribution")
axes[0].set_xlabel("Price")
axes[1].scatter(data["area"], data["price"])
axes[1].set_title("Area vs price")
axes[1].set_xlabel("Area")
axes[1].set_ylabel("Price")
fig.tight_layout()
plt.show()
```

This code opens two plots in a local Python environment; there is no fixed text output. The histogram shows the distribution of recorded prices; the scatter plot helps inspect whether area and price move together. These seven points cannot establish a general economic law or prove causation.

## Interpret plots carefully
- A histogram depends on bin choices.
- A bar chart's displayed summary can hide variation within groups.
- A scatter plot can hide overlapping points and confounders.
- Correlation is not causal proof.
- A box-plot “outlier” is a statistical flag under the plotting rule, not proof of a bad data entry.
- Always label axes and units; an unlabeled plot is harder to interpret.

## Practice
1. Which plot would you use first to inspect the distribution of exam marks?
2. Which plot helps inspect area/price association?
3. Why doesn't a high positive correlation prove that increasing area alone causes a higher price?
4. Modify the example to label the price unit and add a title.
