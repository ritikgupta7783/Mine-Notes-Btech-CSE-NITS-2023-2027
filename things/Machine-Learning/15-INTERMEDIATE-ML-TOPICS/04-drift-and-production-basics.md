# Lesson 15.4 — Drift, Monitoring and Production Basics

## Model persistence
Saving a fitted pipeline allows consistent inference, but persist the complete required preprocessing/model pipeline and record the expected feature schema, package versions and training data version. Joblib/pickle files should be loaded only from trusted sources because deserialisation can execute code.

## Data drift and concept drift
- **Data drift:** the distribution of input features changes over time.
- **Concept drift:** the relationship between inputs and targets changes.
These are useful high-level distinctions. Shifts can be subtle, and monitoring a feature-distribution change does not directly prove model performance changed. Labeled outcome data may arrive later and be needed to assess actual errors.

## Monitoring checklist
- input schema/column order/type changes;
- missingness, invalid values and out-of-range inputs;
- prediction distribution shifts;
- data drift indicators;
- delayed true-outcome metrics and subgroup performance where appropriate;
- service latency, failures, model version and fallback behaviour;
- retraining criteria, owner and rollback plan.

## Deployment is not just saving a model
A production system includes data validation, serving interface, access control, logging without unnecessary private information, monitoring, resource limits, versioning, recovery and human oversight when decisions matter. The model file itself is only one component.

## Practice
1. Define data drift in one sentence.
2. Why doesn't a feature-distribution shift alone prove worse accuracy?
3. Why save preprocessing with the model?
4. What should be checked before retraining?

**Answers:** input distribution changed; the target relationship or predictive signal may remain stable, so outcomes must be checked; training and inference transformations must match; data validity, true outcome metrics, validation protocol and rollback plan.
