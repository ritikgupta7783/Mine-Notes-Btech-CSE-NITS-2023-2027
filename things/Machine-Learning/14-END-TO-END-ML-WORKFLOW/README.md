# Module 14 — End-to-End ML Workflow

**Prerequisites:** Modules 00–13. This module combines problem definition, exploration, splitting, preprocessing, training, evaluation and saved inference.

## Lessons and files
1. [Workflow and design checklist](01-workflow-checklist.md)
2. [Train a complete pipeline](train_model.py)
3. [Load the saved pipeline for inference](predict.py)

## Workflow
Define the prediction task and prediction time → inspect data → separate X and y → choose a suitable split → establish a baseline → fit preprocessing/model pipeline → validate/tune → evaluate on held-out test → analyse errors and limitations → save the fitted pipeline → load and predict with the same feature contract.

## Reproducibility
The example uses scikit-learn's built-in diabetes dataset so it does not need a custom file download. It demonstrates regression only; it is not a medical diagnosis application. Train/test scores are outcomes of running the script and should not be invented in the documentation.

## Checkpoint
You should be able to explain every step, state which data was used to fit each operation, rerun training, load the saved artifact, and explain the feature order expected by inference.
