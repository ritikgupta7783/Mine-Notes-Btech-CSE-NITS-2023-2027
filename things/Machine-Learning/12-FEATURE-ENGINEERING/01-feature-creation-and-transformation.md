# Lesson 12.1 — Feature Creation, Transformation and Interactions

## 1. What is feature engineering?
Feature engineering creates or transforms input variables so a model can use them more effectively. It combines knowledge of the data with validation. It differs from selecting a model: it changes the representation of the input, while model selection chooses the learning method/configuration.

## 2. Examples
- **Ratio:** amount_spent / days_active can represent average daily spend, provided denominator-zero handling is defined.
- **Date features:** extract month, day of week or time since an event, only from timestamps available at prediction time.
- **Log transformation:** can reduce the influence of a long right tail, but interpretation changes and zero/negative values need explicit handling.
- **Interaction:** product of two features can represent that the effect of one variable depends on another.
- **Polynomial:** x² lets a linear model express curvature.
- **Missing indicator:** an indicator can preserve information that a value was absent, if missingness has meaningful predictive context.

## 3. Example
```python
import numpy as np
import pandas as pd

data = pd.DataFrame({
    "amount": [100, 240, 0],
    "days_active": [10, 12, 0],
})

data["average_daily_amount"] = np.where(
    data["days_active"] > 0,
    data["amount"] / data["days_active"],
    np.nan,
)
data["has_active_days"] = (data["days_active"] > 0).astype(int)
print(data[["average_daily_amount", "has_active_days"]].to_dict("records"))
```

**Output**
```text
[{'average_daily_amount': 10.0, 'has_active_days': 1}, {'average_daily_amount': 20.0, 'has_active_days': 1}, {'average_daily_amount': nan, 'has_active_days': 0}]
```

Zero active days makes the ratio undefined here, so we represent it as missing instead of dividing by zero or silently asserting an average of zero. A later preprocessing pipeline can impute the ratio according to a documented rule.

## 4. Do feature engineering inside a valid pipeline
Any transformation whose values are learned from data—such as a scaler, imputer, target encoder or feature selector—must be fit on the training data only. Deterministic feature creation can be applied consistently, but the feature still must be available at the intended prediction moment. Time-derived features can leak future information if timestamps represent events after the outcome.

## Practice
1. Add cost_per_item = total_cost / item_count. What will you do when item_count=0?
2. Give one interaction feature for area and age of a building.
3. Why is customer_id often not a meaningful generalisable predictor by itself?
4. A churn prediction feature stores the cancellation timestamp. Explain the leakage risk.

**Answers:** define zero-denominator behaviour such as missing/flag; area × age or a justified transform; IDs can encourage memorisation of entities and have no stable meaning for new customers; cancellation occurs after the target event and reveals the answer.
