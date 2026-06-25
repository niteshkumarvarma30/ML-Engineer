# Exercise

## Overfitting and underfitting
Interpreting model complexity is a great way to evaluate supervised learning performance. Your aim is to produce a model that can interpret the relationship between features and the target variable, as well as generalize well when exposed to new observations.

The training and test sets have been created from the `churn_df` dataset and preloaded as `X_train`, `X_test`, `y_train`, and `y_test`.

In addition, `KNeighborsClassifier` has been imported for you along with `numpy` as `np`.

### Instructions
* Create `neighbors` as a `numpy` array of values from `1` up to and including `12`.
* Instantiate a `KNeighborsClassifier`, with the number of neighbors equal to the `neighbor` iterator.
* Fit the model to the training data.
* Calculate accuracy scores for the training set and test set separately using the `.score()` method, and assign the results to the `train_accuracies` and `test_accuracies` dictionaries, respectively, utilizing the `neighbor` iterator as the index.

### Solution (script.py)
```python
# Create neighbors
neighbors = np.arange(1, 13)
train_accuracies = {}
test_accuracies = {}

for neighbor in neighbors:
  
    # Set up a KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=neighbor)
  
    # Fit the model
    knn.fit(X_train, y_train)
  
    # Compute accuracy
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

print(neighbors, '\n', train_accuracies, '\n', test_accuracies)
```
