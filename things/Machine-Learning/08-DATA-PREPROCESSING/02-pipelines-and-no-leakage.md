# Lesson 08.2 — Pipelines and Leakage-Safe Preprocessing

## 1. Separate learning from applying
A transformer may learn values from data. For example, SimpleImputer learns a fill value and StandardScaler learns the training mean and standard deviation. Call fit (or fit_transform on training inputs) only on training data. Later, transform validation/test inputs using those same learned values.

Incorrect approach: fit the scaler on all X, then split. It exposes the test feature distribution to training preprocessing. Correct approach: split first; place preprocessing and estimator together in a Pipeline.

## 2. ColumnTransformer
Real data often has numeric and categorical columns requiring different preprocessing. ColumnTransformer lets you apply one pipeline to numeric columns and another to categorical columns, then combine the results.

## 3. Complete example
The sample rows below are illustrative synthetic data. The program does not claim a measured performance result for a real-world dataset.

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = pd.DataFrame({
    "age": [22, 31, 25, 45, 52, 28, 39, 33, 48, 23, 41, 56],
    "income": [30, 55, None, 80, 90, 38, 65, 52, 88, 32, 72, 95],
    "channel": ["web", "store", "web", "store", "web", "app",
                "app", "store", "web", "app", "store", "web"],
    "churn": [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
})

X = data[["age", "income", "channel"]]
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

numeric_features = ["age", "income"]
categorical_features = ["channel"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features),
])

model = Pipeline([
    ("preprocess", preprocess),
    ("classifier", LogisticRegression(max_iter=1000)),
])
model.fit(X_train, y_train)
print("Train rows:", len(X_train))
print("Test rows:", len(X_test))
print("Prediction for first test row:", int(model.predict(X_test.iloc[[0]])[0]))
```

The train/test row counts should be 9 and 3. The specific predicted class comes from the fitted model and this tiny sample; it is not a trustworthy performance claim. Inspect class probabilities and evaluate appropriate metrics on a larger representative dataset before treating any prediction as useful.

## 4. Why the pipeline works
- The split occurs before imputation/scaling/encoding are fitted.
- Numeric columns use median imputation and standardisation.
- Categorical data uses most-frequent imputation and one-hot encoding.
- The classifier is fitted after the transformations.
- Calling model.predict on a raw DataFrame with the expected columns repeats the fitted transformations automatically.
- handle_unknown="ignore" prevents an unseen test category from causing encoder failure; it does not make the new category semantically known.

## 5. Common mistakes
- Fitting preprocessing on the entire dataset before splitting.
- Encoding categories separately on train and test so columns don't match.
- Imputing values that are actually meaningful zeros.
- Leaking the target through a feature.
- Changing a fitted transformer after training and forgetting to refit the model.
- Saving the estimator without the preprocessing needed to interpret raw inputs.

## Practice
1. In the sample, where is the median for income learned?
2. What does handle_unknown="ignore" do?
3. What should be passed to model.predict in this example?
4. Why is the three-row test set unsuitable for claiming robust generalisation?

**Answers:** from X_train within the pipeline; unseen categories are encoded without raising that unknown-category error; a DataFrame with columns age/income/channel in the expected meanings; three observations have high statistical uncertainty and may not represent deployment data.
