# The Double Underscore Trick (__)

When you use `GridSearchCV` on a normal model, you can just pass the name of the parameter you want to change, like this:
```python
parameters = {"C": [0.1, 0.5, 1.0]}
```

### The Pipeline Problem

When you put your `LogisticRegression` model inside a `Pipeline`, `GridSearchCV` can no longer see it directly. If you just pass `"C"`, the Pipeline gets confused and says, *"I don't have a parameter called C! I only have steps!"*

### The Solution: Routing with `__`

To fix this, scikit-learn requires you to provide an "address" to the parameter using a double underscore.

Let's break down `"logreg__C"`:

* **`logreg`**: This is the exact name you gave your model in the pipeline steps earlier: 
  ```python
  steps = [("scaler", StandardScaler()), ("logreg", LogisticRegression())]
  ```
* **`__` (Double Underscore)**: This acts as a bridge. It tells the computer, *"Look inside the step I just named."*
* **`C`**: This is the actual hyperparameter belonging to Logistic Regression that you want to test.

**Translation**: *"Hey Pipeline, go to the step named 'logreg', look inside it, and test these values on its 'C' parameter."*
