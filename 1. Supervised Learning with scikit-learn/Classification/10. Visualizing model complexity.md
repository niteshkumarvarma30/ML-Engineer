# Exercise

## Visualizing model complexity
Now you have calculated the accuracy of the KNN model on the training and test sets using various values of `n_neighbors`, you can create a model complexity curve to visualize how performance changes as the model becomes less complex!

The variables `neighbors`, `train_accuracies`, and `test_accuracies`, which you generated in the previous exercise, have all been preloaded for you. You will plot the results to aid in finding the optimal number of neighbors for your model.

### Instructions
* Add a title `"KNN: Varying Number of Neighbors"`.
* Plot the `.values()` method of `train_accuracies` on the y-axis against `neighbors` on the x-axis, with a label of `"Training Accuracy"`.
* Plot the `.values()` method of `test_accuracies` on the y-axis against `neighbors` on the x-axis, with a label of `"Testing Accuracy"`.
* Display the plot.

### Solution (script.py)
```python
# Add a title
plt.title("KNN: Varying Number of Neighbors")

# Plot training accuracies
plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy")

# Plot test accuracies
plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy")

plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")

# Display the plot
plt.show()
```
