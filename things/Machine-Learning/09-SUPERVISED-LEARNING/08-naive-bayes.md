# Algorithm 09.8 — Naive Bayes

## 1. Intuition
Naive Bayes uses Bayes' theorem to estimate which class is most plausible given the observed features. The “naive” part is the assumption that features are conditionally independent given the class. Text features often violate this assumption, but Naive Bayes can still be a strong, simple baseline.

## 2. Core calculation
For class C and features x1…xp, the class score is proportional to:
\[
P(C)\prod_j P(x_j\mid C)
\]
P(C) is the prior class probability and P(xj|C) is a likelihood under the class. The full denominator P(x) is the same across competing classes for one example, so class scores can be compared proportionally. Implementations use logarithms to avoid multiplying many tiny probabilities directly.

## 3. Common variants
- **GaussianNB:** models each numeric feature with a class-specific Gaussian distribution.
- **MultinomialNB:** commonly used for non-negative count-like features, including word counts.
- **BernoulliNB:** designed for binary feature presence/absence.

Choose based on how the feature representation is constructed; a distribution assumption should make sense for the data.

## 4. Simple text example
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

messages = [
    "win money now",
    "claim free prize",
    "team meeting tomorrow",
    "project meeting schedule",
]
labels = ["spam", "spam", "normal", "normal"]

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(messages, labels)
print(model.predict(["free money prize"])[0])
```

**Output:** `spam` for this tiny teaching example. With so few messages this is only a demonstration of API flow, not a reliable spam filter. Text vectorisation is part of the pipeline and is learned from the training corpus only.

## 5. Strengths and weaknesses
**Strengths:** fast, works well on some high-dimensional text tasks, supports useful probability scores, simple baseline.  
**Weaknesses:** conditional-independence assumption is often unrealistic; probability estimates can be poorly calibrated; performance depends heavily on data representation and tokenisation.

## Practice
1. Why is it called “naive”?
2. Why is CountVectorizer put inside the pipeline?
3. Which variant is common for non-negative word counts?
4. Why does four-message accuracy not establish production readiness?

**Answers:** conditional independence assumption; it must be learned only on training text and applied consistently; MultinomialNB; tiny dataset cannot establish generalisation across diverse real messages.
