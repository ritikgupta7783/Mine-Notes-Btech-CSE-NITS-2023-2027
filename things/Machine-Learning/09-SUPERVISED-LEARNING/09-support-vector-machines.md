# Algorithm 09.9 — Support Vector Machines (SVM)

## 1. Intuition
SVM attempts to separate classes using a decision boundary with a large margin—the gap between the boundary and nearby training points. Those influential nearby points are called support vectors. With a kernel, SVM can represent nonlinear boundaries without explicitly writing every transformed feature.

## 2. Linear boundary
A linear decision function can be written as:
\[
f(x)=w\cdot x+b
\]
For binary classification, the sign gives a class decision under the chosen label convention. Training balances a wide margin against violations through a regularised objective. In scikit-learn, C controls the trade-off: smaller C applies stronger regularisation; larger C penalises training mistakes more strongly under the hinge-loss formulation.

## 3. Example
```python
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=300, noise=0.15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1.0, gamma="scale"),
)
model.fit(X_train, y_train)
print("Accuracy:", round(accuracy_score(y_test, model.predict(X_test)), 3))
```

This synthetic example uses an RBF kernel to model a curved boundary. Run it for the score in your environment; the result depends on data, library implementation and chosen split.

## 4. Kernel intuition
A kernel acts like a similarity function that allows nonlinear boundaries to be represented in an implicit feature space. Common options include linear, polynomial and RBF. gamma in an RBF kernel controls how local the influence of an individual training point is: a very high gamma can create a highly wiggly boundary and overfit.

## 5. Strengths and weaknesses
**Strengths:** effective on some medium-sized/high-dimensional data; flexible boundaries through kernels; margin-based reasoning.  
**Weaknesses:** scaling is often important; parameter and kernel selection may be sensitive; large datasets can make training expensive; raw SVM outputs are not necessarily well-calibrated probabilities.

## Practice
1. What are support vectors?
2. What does C control intuitively?
3. Why place StandardScaler before SVC in the pipeline?
4. What risk can a very high RBF gamma create?

**Answers:** samples most influential to the boundary/margin; trade-off between margin regularisation and training violations; feature magnitudes affect the geometry; overfitting with a very local, complex boundary.
