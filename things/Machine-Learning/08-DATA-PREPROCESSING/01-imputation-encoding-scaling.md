# Lesson 08.1 — Imputation, Encoding and Scaling

## 1. Missing values
**Imputation** fills missing feature values using a chosen rule, such as a median or most-frequent category. The rule should be selected based on feature meaning and missingness. Removing rows can discard useful data and may create bias if missingness is systematic.

A median is less affected by extreme numeric values than a mean. A missing category might be imputed with the most frequent value or with a meaningful explicit category when appropriate. Never blindly replace the missing target with a feature median for ordinary supervised learning.

## 2. Encode categorical features
Many models need numerical input.
- **One-hot encoding:** creates a 0/1 indicator column for each category.
- **Ordinal encoding:** maps categories to integer codes. Use it when a known order exists or when the modelling choice supports such encoding; arbitrary integer codes can falsely imply numeric order.
- **Text encoding:** methods such as bag-of-words/TF-IDF represent terms numerically; covered in the intermediate/text lesson.

Example: colour = red/blue/green can become columns colour_red, colour_blue and colour_green. A row with blue might be [0,1,0]. The numeric values indicate category membership, not amount.

## 3. Scaling
**Standardisation** subtracts the training mean and divides by training standard deviation:
\[
z=\frac{x-\mu_{train}}{\sigma_{train}}
\]
The resulting training feature has mean about 0 and standard deviation about 1 when the denominator is nonzero under the chosen convention.

**Min-max scaling** maps values using training minimum and maximum, often to [0,1]:
\[
x' = \frac{x-x_{min,train}}{x_{max,train}-x_{min,train}}
\]
If a training feature is constant, a library must handle the zero range safely. Values in held-out data can fall outside [0,1] when they exceed the training range.

## 4. Which models need scaling?
- KNN and K-means rely on distances, so large numeric scales can dominate.
- Logistic/linear models with gradient-based optimisation or regularisation often benefit from scale consistency.
- SVMs commonly benefit from scaling.
- Ordinary decision trees and tree ensembles are usually less sensitive to monotonic scale changes in numeric features.
- Scaling never fixes a leakage problem or makes bad features meaningful.

## Practice
1. Why might median imputation be chosen instead of mean?
2. What is wrong with mapping red=0, green=1, blue=2 if colours have no natural order?
3. Why fit a scaler only on training data?
4. Why is scaling often important for KNN but not required in the same way for decision trees?

**Answers:** median is more robust to extreme values; numeric codes may invent a false ordering; the test distribution must stay out of learned preprocessing; KNN distances depend on scale while tree split ordering typically does not.
