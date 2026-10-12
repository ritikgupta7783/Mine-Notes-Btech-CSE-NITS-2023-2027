# Lesson 00.3 — From Raw Data to a Prediction

This lesson demonstrates the shape of an ML workflow without using an ML library yet. The model below is deliberately hand-written, so it is **not** machine learning. It lets us understand inputs, outputs and prediction before the learning algorithms arrive.

## 1. A rule-based baseline

```python
def estimate_price(area):
    # A hand-written rule, not a trained ML model.
    return 2.0 * area + 20

print(estimate_price(50))
print(estimate_price(70))
```

**Output**
```text
120.0
160.0
```

The function always applies the same formula. A person supplied the weight 2.0 and bias 20; the program did not learn them from examples.

## 2. What would learning change?

Given training pairs such as (area, sale price), a regression algorithm can estimate the weight and bias to reduce an error objective. In the next modules we learn arrays, loss functions and model fitting, then use a library to fit a model from examples.

The main workflow terms:
1. **Raw records:** the available historical data.
2. **Feature definition:** decide what information is available at prediction time.
3. **Target definition:** clarify what quantity or category should be predicted and for which time/event.
4. **Data split:** reserve samples for evaluation before fitting data-dependent preprocessing.
5. **Fit:** estimate model parameters using training data.
6. **Evaluate:** compare predictions with held-out target values using appropriate metrics.
7. **Inference:** apply the saved fitted pipeline to new examples.

## 3. Why the task definition matters
- If sale prices are recorded in different currencies without conversion, target values are inconsistent.
- If a feature contains the price determined after the house is sold, it leaks the answer.
- If training examples come only from one neighborhood, results may transfer poorly to another.
- If a model is judged only on its training data, memorisation can look like success.

## Practice
Write three sentences defining the input, target and evaluation plan for a student-score predictor. State which inputs would genuinely be known before the exam result. Avoid using the final score itself as an input.

**Example answer:** Inputs could include number of practice questions completed before the exam and previous-term marks; target is the next exam score. Split historical records into training and held-out test samples, ensuring all input variables were available before the target event. Evaluate numeric predictions with an error metric such as MAE, then inspect whether test records represent the students the model will be used for.

## What comes next
Module 01 introduces the Python language needed to express these ideas as small, testable programs.
