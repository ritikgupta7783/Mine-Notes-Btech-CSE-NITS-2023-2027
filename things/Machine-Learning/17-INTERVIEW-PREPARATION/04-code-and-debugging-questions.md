# Interview Set 17.4 — Code Reading and Debugging

## Question 1: Target leakage
```python
X = data[["area", "bedrooms", "price"]]
y = data["price"]
```
**What's wrong?** The target price is included in X, letting the model read the answer. **Fix:** remove price from X. If a feature is a transformed form of target or recorded after outcome, it can cause the same problem.

## Question 2: Scaling before split
```python
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```
**What's wrong?** Scaler statistics used all rows, including the test set. **Fix:** split first and fit scaler/model in a Pipeline on training data. This prevents preprocessing from using held-out information.

## Question 3: Wrong shape
```python
X = np.array([1, 2, 3, 4])
print(X.shape)
```
Shape is (4,), a one-dimensional vector. A feature matrix with four samples and one feature is usually shape (4,1), e.g. np.array([1,2,3,4]).reshape(-1,1). The proper shape depends on the estimator's input contract.

## Question 4: Wrong metric
A classifier reports 99% accuracy for a rare positive class but detects no positive cases. **Diagnosis:** accuracy hides minority failure. **Next step:** define positive class, confusion matrix, recall/precision/PR curve and cost-aware threshold.

## Question 5: Cross-validation leak
A feature selector is fitted on all data before cross-validation. **Issue:** validation fold labels influence selected features. **Fix:** put selector and estimator into a Pipeline so each fold's training part fits its own selector.

## Question 6: Train/test rows overlap
Duplicate customer rows appear in both train and test, though deployment concerns new customers. **Issue:** the score may partly reflect the same entities. **Fix:** deduplicate if appropriate and use group-based split by customer ID, while ensuring the ID itself is not unintentionally a predictor.

## Question 7: Correlation mistake
A chart shows strong association between umbrella sales and rain. Does selling umbrellas cause rain? **No.** Rain influences both. Association is not proof of direction or intervention effect.

## Practice
For each snippet, give (1) the issue, (2) why it matters, (3) corrected approach, and (4) one test that verifies the fix. Avoid changing code without explaining the failure mechanism.
