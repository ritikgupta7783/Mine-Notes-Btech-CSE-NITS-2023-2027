"""Project 3: text classification demonstration using a tiny toy corpus.

Install: python -m pip install scikit-learn
The data are illustrative only and not sufficient to build a real spam filter.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


def main():
    messages = [
        "win a free prize now",
        "claim your free reward",
        "urgent win cash today",
        "limited offer free money",
        "team meeting at noon",
        "please review the project notes",
        "class starts at ten",
        "can we schedule the meeting",
        "free prize claim now",
        "send the homework notes",
        "congratulations win money",
        "the project meeting moved",
        "claim cash offer",
        "please submit the assignment",
        "free reward claim",
        "review the class timetable",
    ]
    labels = [
        "spam", "spam", "spam", "spam",
        "normal", "normal", "normal", "normal",
        "spam", "normal", "spam", "normal",
        "spam", "normal", "spam", "normal",
    ]

    X_train, X_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.25, random_state=42, stratify=labels
    )
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions, zero_division=0))
    print("New message:", model.predict(["claim free money"])[0])


if __name__ == "__main__":
    main()
