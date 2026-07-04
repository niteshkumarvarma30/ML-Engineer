# Concept

## Ensemble Learning & Voting Classifiers

Up until now, we have been training individual machine learning models (like a single Logistic Regression model, or a single Decision Tree) to make predictions.

But what if we combine them? This is called **Ensemble Learning**.

---

### 1. Why do we need to combine models? (The limits of CARTs)

To understand why Ensembles are so powerful, let's look at the strengths and weaknesses of Decision Trees (CARTs).

**The Good:**
* They are incredibly easy to interpret (you can literally draw the tree).
* They can capture non-linear, complex patterns.
* They don't require any feature scaling (no `StandardScaler` needed!).

**The Bad:**
* **Orthogonal Boundaries:** They can only draw rigid, rectangular boxes on a graph.
* **High Variance (Overfitting):** If you let a tree grow unconstrained, it will memorize the training data.
* **Extreme Sensitivity:** Decision trees are incredibly fragile. If you delete just one single row of data from your training set and retrain the tree, it might draw a completely different set of branches!

**The Fix:** We want to keep the awesome flexibility of a Decision Tree, but fix its fragility and high variance. We do this by using an Ensemble.

---

### 2. What is Ensemble Learning? (The Board of Directors)

Imagine a company run by a single CEO (a single Decision Tree). If that CEO has a bad day or makes a weird assumption, the entire company makes a terrible decision.

Ensemble Learning fires the single CEO and replaces them with a **Board of Directors** (a group of different models).

1. You train multiple different models on the exact same dataset.
2. Every model looks at a new data point and makes its own independent prediction.
3. A **"Meta-Model"** gathers all their answers and aggregates them into one final, highly robust prediction.

> [!NOTE]
> **The Golden Rule of Ensembles:** 
> For an ensemble to work, the models must be skillful, but they must be **different from each other**. If you have a Logistic Regression model, a KNN model, and a Decision Tree, they all use completely different math to make their guesses.

**Why this is magic:** If the Decision Tree makes a weird, fragile mistake on a specific patient, the Logistic Regression and KNN models will likely get it right, and they will overrule the tree! They compensate for each other's weaknesses.

---

### 3. The Voting Classifier (Hard Voting)

The simplest type of Meta-Model is a Voting Classifier using **Hard Voting**.

It works exactly like a democratic election:
* **Judge 1 (Logistic Regression):** Predicts "1" (Malignant).
* **Judge 2 (KNN):** Predicts "0" (Benign).
* **Judge 3 (Decision Tree):** Predicts "1" (Malignant).

The Meta-Model counts the votes. Since "1" got two votes and "0" only got one vote, the final prediction is 1 (Malignant).

When you do this in the real world, the Voting Classifier almost always scores a higher Accuracy than any of the individual models on their own!

---

### 4. Cheat Sheet: Scikit-Learn Code

Here is how you build a Voting Classifier in Python. You just build your individual models, put them in a list of tuples, and hand them to the `VotingClassifier`!

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 2. Instantiate the individual models
lr = LogisticRegression(random_state=1)
knn = KNeighborsClassifier()
dt = DecisionTreeClassifier(random_state=1)

# 3. Define the list of classifiers (A list of tuples: ("Name", model))
classifiers = [
    ('Logistic Regression', lr),
    ('K Nearest Neighbours', knn),
    ('Classification Tree', dt)
]

# 4. Instantiate the Meta-Model (The Voting Classifier)
vc = VotingClassifier(estimators=classifiers)

# 5. Fit the Meta-Model to the training data
vc.fit(X_train, y_train)

# 6. Evaluate the Meta-Model!
y_pred = vc.predict(X_test)
print(f"Voting Classifier Accuracy: {accuracy_score(y_test, y_pred)}")
```
