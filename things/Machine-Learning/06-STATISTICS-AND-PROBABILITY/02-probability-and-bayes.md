# Lesson 06.2 — Probability, Conditional Probability and Bayes' Theorem

## 1. Probability
Probability quantifies uncertainty under a defined model or experiment. It is between 0 and 1: 0 denotes impossible under the model, 1 denotes certain. For a fair six-sided die, probability of rolling a 4 is 1/6.

## 2. Conditional probability
P(A | B) means probability of A given that B occurred. For events with P(B)>0:
\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]
The condition changes the group of outcomes we are considering.

Example: in a class of 20 students, 8 study Python and 5 of those 8 also study ML. Given that a student studies Python, the probability they also study ML is 5/8 = 0.625.

## 3. Independent events
Two events A and B are independent if knowing B does not change the probability of A, formally P(A|B)=P(A) when the conditional probability is defined. Independence is an assumption to justify, not a default.

## 4. Bayes' theorem
\[
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
\]
It combines the prior P(A), likelihood P(B|A), and evidence probability P(B) to calculate an updated conditional probability.

### Why base rates matter
Suppose a rare condition affects 1% of people. A test is positive for 90% of people with the condition and has a 5% false-positive rate among people without it. Out of 10,000 people (expected counts):
- Condition present: 100; true positives: about 90.
- Condition absent: 9,900; false positives: about 495.
- Total positives: about 585.
- Among positives, about 90/585 ≈ 15.4% have the condition.

Even a fairly sensitive test can have a modest positive predictive value when the condition is rare. These are hypothetical numbers, not medical advice; real tests have context-specific estimates and a proper clinical process.

## 5. How this connects to Naive Bayes
Naive Bayes applies Bayes' rule to compare class probabilities using features. Its “naive” assumption is conditional independence of features given the class, which is often not exactly true. It can still be a useful fast baseline, especially for some text classification tasks.

## Practice
1. If 12 out of 30 records have a missing value, what fraction is missing?
2. If P(A∩B)=0.2 and P(B)=0.5, calculate P(A|B).
3. Why can a positive result have a modest posterior probability when a condition is rare?
4. What is the key assumption in basic Naive Bayes?

**Answers:** 0.4; 0.2/0.5=0.4; false positives from the much larger non-condition group can outnumber true positives; conditional independence of features given class.
