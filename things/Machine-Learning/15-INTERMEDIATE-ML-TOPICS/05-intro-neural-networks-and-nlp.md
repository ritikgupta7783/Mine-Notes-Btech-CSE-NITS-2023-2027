# Lesson 15.5 — First Look at Neural Networks and NLP

## Neural network
A simple neural network combines weighted inputs, adds a bias, then applies an activation function. Multiple layers compose these transformations. Training adjusts weights to reduce a loss, commonly using backpropagation to calculate gradients and an optimiser such as gradient descent to update parameters.

For one neuron:
\[
z=\mathbf{w}\cdot\mathbf{x}+b,\qquad a=f(z)
\]
The activation f can be a ReLU, sigmoid or another choice. This is a conceptual starting point; real networks can have many layers, batches, regularisation and numerical details.

## NLP and text classification
Natural Language Processing (NLP) studies computational processing of human language. A standard text-classification pipeline can:
1. define the target labels and the prediction moment;
2. split labelled messages into training and held-out sets;
3. convert text into numerical features (e.g. word counts or TF-IDF);
4. fit a classifier;
5. inspect precision/recall and failure cases.

Text preprocessing and vectorisation must be fitted on training text only. Tokenisation and vocabulary choices matter; simple bags of words lose word order and context.

## Example: TF-IDF and a linear classifier
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

messages = [
    "project meeting at noon",
    "please review the project notes",
    "claim your free prize now",
    "win free money now",
    "weekly study plan",
    "free cash reward",
]
labels = ["normal", "normal", "spam", "spam", "normal", "spam"]

model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
model.fit(messages, labels)
print(model.predict(["claim free money"])[0])
```

**Output for this tiny teaching corpus:** likely `spam`, but run the model and inspect it in your environment. A handful of sentences is not enough to build a robust spam filter; use a representative dataset and held-out evaluation for any real use.

## What to learn next
Deep Learning and modern NLP deserve their own course once Python, linear algebra, gradients, validation and traditional ML are solid. Do not conflate a short conceptual introduction with full mastery.
