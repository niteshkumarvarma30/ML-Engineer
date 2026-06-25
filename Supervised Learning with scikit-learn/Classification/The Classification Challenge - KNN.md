# The Classification Challenge - KNN

## 1. The classification challenge
Previously, we learned that supervised learning uses labels. Let's discuss how we can build a classification model, or classifier, to predict the labels of unseen data.

## 2. Classifying labels of unseen data
There are four steps. First, we build a classifier, which learns from the labeled data we pass to it. We then pass it unlabeled data as input, and have it predict labels for this unseen data. As the classifier learns from the labeled data, we call this the training data.

## 3. k-Nearest Neighbors
Let's build our first model! We'll use an algorithm called k-Nearest Neighbors, which is popular for classification problems. The idea of k-Nearest Neighbors, or KNN, is to predict the label of any data point by looking at the k, for example, three, closest labeled data points and getting them to vote on what label the unlabeled observation should have. KNN uses majority voting, which makes predictions based on what label the majority of nearest neighbors have.

## 4. k-Nearest Neighbors
Using this scatter plot as an example, how do we classify the black observation?

## 5. k-Nearest Neighbors
If k equals three, we would classify it as red. This is because two of the three closest observations are red.

## 6. k-Nearest Neighbors
If k equals five, we would instead classify it as blue.

## 7. KNN Intuition
To build intuition for KNN, let's look at this scatter plot displaying total evening charge against total day charge for customers of a telecom company. The observations are colored in blue for customers who have churned, and red for those who have not churned.

## 8. KNN Intuition
Here we have visualized the results of a KNN algorithm where the number of neighbors is set to 15. KNN creates a decision boundary to predict if customers will churn. Any customers in the area with a gray background are predicted to churn, and those in the area with a red background are predicted to not churn. This boundary would be used to make predictions on unseen data.

## 9. Using scikit-learn to fit a classifier
To fit a KNN model using scikit-learn, we import `KNeighborsClassifier` from `sklearn.neighbors`. We split our data into `X`, a 2D array of our features, and `y`, a 1D array of the target values - in this case, churn status. scikit-learn requires that the features are in an array where each column is a feature and each row a different observation. Similarly, the target needs to be a single column with the same number of observations as the feature data. We use the `.values` attribute to convert `X` and `y` to NumPy arrays. Printing the shape of `X` and `y`, we see there are 3333 observations of two features, and 3333 observations of the target variable. We then instantiate our `KNeighborsClassifier`, setting `n_neighbors` equal to 15, and assign it to the variable `knn`. Then we can fit this classifier to our labeled data by applying the classifier's `.fit()` method and passing two arguments: the feature values, `X`, and the target values, `y`.

```python
from sklearn.neighbors import KNeighborsClassifier
X = churn_df[["total_day_charge", "total_eve_charge"]].values
y = churn_df["churn"].values
print(X.shape, y.shape)
```
**Output:**
```text
(3333, 2), (3333,)
```

```python
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X, y)
```

## 10. Predicting on unlabeled data
Here we have a set of new observations, `X_new`. Checking the shape of `X_new`, we see it has three rows and two columns, that is, three observations and two features. We use the classifier's `.predict()` method and pass it the unseen data as a 2D NumPy array containing features in columns and observations in rows. Printing the predictions returns a binary value for each observation or row in `X_new`. It predicts 1, which corresponds to 'churn', for the first observation, and 0, which corresponds to 'no churn', for the second and third observations.

```python
X_new = np.array([[56.8, 17.5],
                  [24.4, 24.1],
                  [50.1, 10.9]])
print(X_new.shape)
```
**Output:**
```text
(3, 2)
```

```python
predictions = knn.predict(X_new)
print('Predictions: {}'.format(predictions))
```
**Output:**
```text
Predictions: [1 0 0]
```
