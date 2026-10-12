# Lesson 06.3 — Distributions, Sampling and Statistical Reasoning

## 1. What is a distribution?
A distribution describes which values a variable takes and how often or how much probability is associated with them. A histogram is one empirical view of a numeric distribution.

Common examples:
- **Bernoulli:** one trial with two outcomes, often coded 0/1.
- **Binomial:** number of successes in a fixed number of independent trials with the same success probability.
- **Uniform:** equal probability density over a specified interval in the continuous case.
- **Normal:** symmetric bell-shaped distribution described by a mean and standard deviation.

Not every real dataset is normally distributed. Do not choose a statistical procedure solely because a bell curve is familiar.

## 2. Population and sample
A population is the full group of interest; a sample is the portion observed. Sampling bias occurs when the selection method makes the sample unrepresentative of the population for the question being asked.

Example: a survey about all students based only on students who attend an optional advanced coding club is unlikely to represent all students' study habits.

## 3. Law of large numbers and central limit theorem intuition
The law of large numbers says that under suitable assumptions, sample averages tend toward the expected value as the number of independent observations increases.

The central limit theorem, under suitable conditions, describes why the distribution of appropriately standardised sample means becomes approximately normal as sample size grows. It does not say that every raw dataset becomes normally distributed, and dependence/heavy tails can complicate the result.

## 4. Confidence intervals and significance
A confidence interval procedure describes uncertainty in an estimate. A 95% confidence procedure means that, across repeated samples under its assumptions, 95% of intervals produced this way would cover the fixed true parameter. It does not strictly mean there is a 95% probability the particular fixed parameter is inside a specific frequentist interval.

A hypothesis test provides evidence against a specified null model at a chosen threshold. Statistical significance is not the same as practical importance. Small effects can become statistically significant with huge sample sizes; large-looking estimates can be uncertain when samples are small.

## 5. Correlation is not causation
If ice-cream sales and swimming incidents rise together, a third factor such as hot weather may influence both. Correlation is useful for exploring associations and building predictive features, but it doesn't by itself establish what would happen if we intervened on one variable.

## ML connections
- Sampling and split strategy affect evaluation reliability.
- Skew and outliers affect scaling and model choice.
- Probability is central to Naive Bayes and probability estimates.
- Uncertainty makes small differences between models hard to interpret.
- Distribution shifts can reduce performance after deployment.

## Practice
1. Explain how sampling only from one class section can bias a student-score study.
2. Does the central limit theorem say all observed features become normal?
3. Distinguish statistical significance from business importance.
4. Give one reason correlation does not prove causation.

**Answers:** a selected section may differ systematically; no, it concerns a sampling distribution of means under assumptions; one describes evidence relative to a statistical model while the other concerns the size/usefulness of an effect; a confounder or reverse causality may explain the relationship.
