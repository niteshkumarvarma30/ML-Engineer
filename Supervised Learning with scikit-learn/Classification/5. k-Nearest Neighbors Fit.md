# Exercise: k-Nearest Neighbors: Fit

In this exercise, you will build your first classification model using the `churn_df` dataset, which has been preloaded for the remainder of the chapter.

The target, `"churn"`, needs to be a single column with the same number of observations as the feature data. The feature data has already been converted into `numpy` arrays.

`"account_length"` and `"customer_service_calls"` are treated as features because account length indicates customer loyalty, and frequent customer service calls may signal dissatisfaction, both of which can be good predictors of churn.

### Instructions (100 XP)

* Import `KNeighborsClassifier` from `sklearn.neighbors`.
* Instantiate a `KNeighborsClassifier` called `knn` with `6` neighbors.
* Fit the classifier to the data using the `.fit()` method.

### Starter Code

```python
# Import KNeighborsClassifier
from ____.____ import ____

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values

# Create a KNN classifier with 6 neighbors
knn = ____(____=____)

# Fit the classifier to the data
knn.____(____, ____)
```
