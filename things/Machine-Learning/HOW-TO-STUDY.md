# How to Study This ML Repository

## 1. Environment setup

Use Python 3.10 or newer. Create a virtual environment in a working directory, then install the packages used in later modules.

### Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib scikit-learn jupyter
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib scikit-learn jupyter
```

To start a notebook interface, run python -m jupyter lab. For scripts, run python path/to/script.py. If package installation fails, record the full error and check the Python version and active environment first.

## 2. Use a repeatable lesson routine

1. **Question:** State the problem the technique solves.
2. **Intuition:** Explain it without maths.
3. **Vocabulary:** Define every new term.
4. **Small example:** Work through a tiny example manually.
5. **Formula:** Define every symbol and calculate a numerical case.
6. **Code:** Run the smallest useful implementation.
7. **Interpret:** Explain what outputs mean and what they do not mean.
8. **Failure mode:** Identify a common way the method can mislead you.
9. **Practice:** Solve one guided and one independent task.
10. **Teach back:** Explain the concept in 60 seconds without reading.

## 3. Script versus notebook
- Use a **Python script** for a repeatable example with clear inputs and outputs.
- Use a **Jupyter notebook** when the learner should inspect tables, draw plots, or change one value and observe its effect.
- Keep core calculations in small functions when reuse or testing helps.
- Do not commit large generated datasets unless they are needed and licensed appropriately.

## 4. Reproducibility
For random demonstrations, use an explicitly stated seed such as random_state=42 where supported. Record package versions for a project when results depend on implementation details. A fixed seed makes many experiments repeatable; it does not make data or model assumptions correct.

## 5. How to read ML API calls
- fit(X, y): learn model parameters or preprocessing settings from supplied training data.
- predict(X): produce predictions for supplied samples.
- predict_proba(X): estimate class probabilities for estimators that support it.
- transform(X): apply a previously learned transformation.
- fit_transform(X): fit and apply a transformer, often on training data.
- train_test_split(...): divide data into subsets; choose stratification when the task requires preserving class proportions.
- Cross-validation: repeatedly fit and validate on different folds.
- Hyperparameter search: compare configuration choices under a specified validation procedure.

These method names are common conventions, but not every estimator supports every method.

## 6. Avoid these traps
- Do not scale or impute the full dataset before splitting; that leaks information into evaluation.
- Do not use the test set repeatedly to choose features or hyperparameters.
- Do not assume correlation proves a causal effect.
- Do not interpret a high accuracy as proof of a good model on imbalanced data.
- Do not report a score from code that you have not executed.
- Do not save a fitted model without documenting its feature order, preprocessing and required library versions.
