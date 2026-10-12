# Lesson 15.3 — Interpretability, Feature Importance and Limitations

## Local vs global questions
- **Global explanation:** what patterns generally influence this fitted model?
- **Local explanation:** why did the model assign this output to one sample under an explanation method?
- **Model-intrinsic simplicity:** a small linear model or shallow tree may be easier to inspect directly.
- **Post-hoc explanation:** a separate method approximates or probes the fitted model's behaviour.

## Common tools
- Coefficients: direct for some linear models but depend on feature scales, coding and correlation.
- Tree rules: visible in a small tree; a large forest is not simply explained by one path.
- Permutation importance: shuffle one feature and measure how evaluation score changes on chosen data. Correlated substitutes can hide importance.
- SHAP: a family of feature-attribution methods with assumptions and computational trade-offs. An attribution is not a causal effect.

## Explanations are not proof
An explanation tool can approximate model behaviour but does not establish that the model has learned a causal relationship, is fair, or should be trusted. Validate explanations against domain knowledge, counterexamples, data quality and the actual decision process.

## Responsible limitations
Consider who may be harmed by false positives/negatives, whether data represent the intended population, privacy, consent, disparate performance across groups, feedback loops and avenues for human review. High-impact decisions need careful legal, domain and governance review beyond this introductory ML course.

## Practice
1. Why do coefficient magnitudes need scale context?
2. What happens to permutation importance with correlated features?
3. Does a SHAP plot prove causality?
4. Name two questions that a high overall score doesn't answer.

**Answers:** different units scale coefficients; substitutes can preserve performance after a shuffle; no; whether subgroup errors differ, data are representative, predictions are calibrated or error costs acceptable.
