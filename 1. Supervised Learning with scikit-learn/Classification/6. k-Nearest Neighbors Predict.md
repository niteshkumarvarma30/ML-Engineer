# Exercise: k-Nearest Neighbors: Predict

Now you have fit a KNN classifier, you can use it to predict the label of new data points. All available data was used for training, however, fortunately, there are new observations available. These have been preloaded for you as `X_new`.

The model `knn`, which you created and fit the data in the last exercise, has been preloaded for you. You will use your classifier to predict the labels of a set of new data points:

```python
X_new = np.array([[30.0, 17.5],
                  [107.0, 24.1],
                  [213.0, 10.9]])
```

### Instructions (100 XP)

* Create `y_pred` by predicting the target values of the unseen features `X_new` using the `knn` model.
* Print the predicted labels for the set of predictions.

### Starter Code

```python
# Predict the labels for the X_new
y_pred = ____

# Print the predictions
print("Predictions: {}".format(____))
```
