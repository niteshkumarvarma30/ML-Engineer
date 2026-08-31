# Exercise

## Train/test split + computing accuracy
It's time to practice splitting your data into training and test sets with the `churn_df` dataset!

NumPy arrays have been created for you containing the features as `X` and the target variable as `y`.

### Instructions
* Import `train_test_split` from `sklearn.model_selection`.
* Split `X` and `y` into training and test sets, setting `test_size` equal to 20%, `random_state` to `42`, and ensuring the target label proportions reflect that of the original dataset.
* Fit the `knn` model to the training data.
* Compute and print the model's accuracy for the test data.

### Solution (script.py)
```python
# Import the module
from sklearn.model_selection import train_test_split

X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

knn = KNeighborsClassifier(n_neighbors=5)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))
```
