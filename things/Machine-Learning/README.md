# Machine Learning — Beginner-to-Intermediate Study Course

Welcome to a step-by-step Machine Learning course built around one rule: **understand the idea before memorising the algorithm**. Every module connects to skills introduced earlier and uses plain-English explanations, small datasets, Python code, interpretation, exercises and interview questions.

**Start here:** [Module 00 — ML Foundations](00-ML-FOUNDATIONS/README.md). Do not jump into algorithms before you understand features, targets, training, prediction and evaluation.

## Course roadmap

| Module | Main question | Study link |
|---|---|---|
| 00. ML foundations | What is ML and what problem does it solve? | [Start](00-ML-FOUNDATIONS/README.md) |
| 01. Python for ML | What Python do I need to work with data? | [Open](01-PYTHON-FOR-ML/README.md) |
| 02. NumPy | How do we represent numerical data efficiently? | [Open](02-NUMPY-AND-VECTORIZATION/README.md) |
| 03. Pandas | How do we inspect and prepare tables? | [Open](03-PANDAS-AND-DATA-HANDLING/README.md) |
| 04. Visualisation | What patterns and problems can plots reveal? | [Open](04-DATA-VISUALIZATION/README.md) |
| 05. Mathematics | What maths is behind model calculations? | [Open](05-MATHEMATICS-FOR-ML/README.md) |
| 06. Statistics and probability | How do we reason about variation and uncertainty? | [Open](06-STATISTICS-AND-PROBABILITY/README.md) |
| 07. ML fundamentals | How does a model learn and generalise? | [Open](07-ML-FUNDAMENTALS/README.md) |
| 08. Preprocessing | How do we prepare features without leakage? | [Open](08-DATA-PREPROCESSING/README.md) |
| 09. Supervised learning | How do we predict a known target? | [Open](09-SUPERVISED-LEARNING/README.md) |
| 10. Unsupervised learning | How do we find structure without labels? | [Open](10-UNSUPERVISED-LEARNING/README.md) |
| 11. Model evaluation | How do we judge predictions fairly? | [Open](11-MODEL-EVALUATION/README.md) |
| 12. Feature engineering | How can raw columns become more useful inputs? | [Open](12-FEATURE-ENGINEERING/README.md) |
| 13. Model improvement | How do we improve a baseline systematically? | [Open](13-MODEL-IMPROVEMENT/README.md) |
| 14. End-to-end workflow | How do the pieces fit together in a real task? | [Open](14-END-TO-END-ML-WORKFLOW/README.md) |
| 15. Intermediate topics | What else matters beyond basic model fitting? | [Open](15-INTERMEDIATE-ML-TOPICS/README.md) |
| 16. Projects | Can I build the workflow independently? | [Open](16-ML-PROJECTS/README.md) |
| 17. Interview preparation | Can I explain concepts, code and trade-offs? | [Open](17-INTERVIEW-PREPARATION/README.md) |
| 18. Revision and practice | What needs revision and where are the weak spots? | [Open](18-REVISION-AND-PRACTICE/README.md) |

## How to study a lesson
1. Read the problem and intuition before the formula.
2. Write down what each symbol and column means.
3. Predict the output before running the code.
4. Run examples locally and inspect intermediate results.
5. Attempt exercises before opening solutions.
6. Explain the idea out loud without reading.
7. Use the [Progress Tracker](PROGRESS-TRACKER.md) honestly—understanding is not the same as opening a file.

## Setup

Use Python 3.10+ where possible. Install dependencies from [requirements.txt](requirements.txt), then follow [How to Study](HOW-TO-STUDY.md) for environment commands. Core examples run on a normal laptop; no paid APIs or GPU are required.

## Install dependencies

From this folder, create and activate a virtual environment as described in [How to Study](HOW-TO-STUDY.md), then run:

```bash
python -m pip install -r requirements.txt
```

## Companion resources
- [Learning roadmap](LEARNING-ROADMAP.md)
- [How to study and run examples](HOW-TO-STUDY.md)
- [Progress tracker](PROGRESS-TRACKER.md)
- [Glossary](GLOSSARY.md)
- [Formula sheet](FORMULA-SHEET.md)
- [Interview master index](INTERVIEW-MASTER-INDEX.md)

## Important notes on accuracy
Code examples are labelled as runnable scripts or illustrative snippets. Expected outputs are stated where they are stable and meaningful. Model performance depends on data and setup; never treat an unexecuted score as a measured result. An evaluation score by itself does not prove a model is fair, causal, safe or useful in the real world.
