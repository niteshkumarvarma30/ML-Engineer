# Course Notes: Machine Learning with Scikit-Learn

## 1. The Core Concepts of Machine Learning
Machine Learning (ML) is the process by which computers learn to make decisions from data without being explicitly programmed to do so. It generally falls into two main categories:

* **Unsupervised Learning**: The goal is to uncover hidden patterns and structures from unlabeled data. You don't know the categories in advance.
  * *Example*: Clustering customers into distinct groups based on their purchasing behavior, or grouping books based on their text.

* **Supervised Learning**: The goal is to build a model using data where the target answers are already known, so the model can accurately predict the outcomes for unseen data.
  * *Example*: Predicting a basketball player's position based on their points per game, or predicting if an email is spam based on its content.

## 2. Supervised Learning Categories & Terminology
Because this course focuses entirely on Supervised Learning, it is important to understand its two primary sub-types:

* **Classification**: Used to predict a specific category or label. If there are only two possible outcomes (e.g., a bank transaction is either "fraudulent" or "non-fraudulent"), it is called *binary classification*.
* **Regression**: Used to predict continuous, numeric values. An example is predicting the price of a property based on its size and the number of bedrooms.

### Naming Conventions
Data scientists use varying terminology for the inputs and outputs of a model. Scikit-learn standardizes this into "Features" and "Targets".

| Scikit-learn Term | Alternative Names | Definition |
| :--- | :--- | :--- |
| **Feature (X)** | Predictor variable, Independent variable | The input data points used to make a prediction. |
| **Target (y)** | Dependent variable, Response variable | The output value or category you are trying to predict. |

## 3. Prerequisites & The Scikit-Learn Workflow

### Before You Build a Model
You cannot simply feed raw data into a supervised learning model. You must first perform **Exploratory Data Analysis (EDA)** using pandas methods and visualizations to ensure your data meets these strict requirements:

1. It contains no missing values.
2. It is strictly in a numeric format.
3. It is stored properly as pandas DataFrames/Series or NumPy arrays.

### The Standard Scikit-Learn Workflow
Scikit-learn is highly popular because it uses a consistent, repeatable syntax for almost all of its supervised learning models. Here is the standard four-step process described in the transcript:

```python
# 1. Import the model algorithm from an sklearn module
from sklearn.neighbors import KNeighborsClassifier

# 2. Instantiate the model by assigning it to a variable
model = KNeighborsClassifier()

# 3. Fit the model to your training data so it can learn the patterns
# (X represents the array of features, y represents the target array)
model.fit(X, y)

# 4. Predict the target values for new, unseen data (X_new)
predictions = model.predict(X_new)
```

> **Note:** In the transcript's spam example, passing 6 new emails (`X_new`) into the `.predict()` method would return an array of 6 numbers, where `1` indicates the email is spam and `0` indicates it is not.

## 4. Understanding Labeled vs. Unlabeled Data
In machine learning, the concepts of labeled and unlabeled data act as the foundation for how a computer is going to learn. The easiest way to think about it is whether or not the data comes with an "answer key."

Here is a breakdown of what each term means:

### 1. Labeled Data (The Answer Key is Provided)
Labeled data is information that has been tagged with one or more identifying labels. You know exactly what the input is, and you know exactly what the expected output (the answer) should be.

* **How it works**: The data includes both the features (the characteristics of the data) and the target (the correct answer).
* **Real-world example**: Imagine a dataset of thousands of emails. In a labeled dataset, every single email has a tag attached to it that explicitly says either "Spam" or "Not Spam".
* **How AI uses it**: This data is used for **Supervised Learning**. Because the model has the answer key, it can practice making predictions, check its answers against the labels, and adjust its math until it gets highly accurate.

### 2. Unlabeled Data (No Answer Key Provided)
Unlabeled data is raw information that has not been tagged, categorized, or classified in any way. You have the inputs, but there is no specific target or "right answer" attached to them.

* **How it works**: The data includes only the features. There are no targets.
* **Real-world example**: Imagine receiving a massive folder of one million random emails. There are no tags telling you what they are. It is just raw text, senders, and subject lines.
* **How AI uses it**: This data is used for **Unsupervised Learning**. Because there is no answer key to practice with, the model's job is to explore the data and find hidden patterns or structures on its own (like grouping all the emails that look like promotional newsletters into one pile, and all the personal emails into another).

### Summary Comparison

| Feature | Labeled Data | Unlabeled Data |
| :--- | :--- | :--- |
| **Contains "Answers"?** | Yes (has Targets/Tags) | No (only Features) |
| **Human Effort** | High (humans usually have to manually tag the data) | Low (easy to collect raw data) |
| **Learning Type** | Supervised Learning | Unsupervised Learning |
| **Primary Goal** | Predicting outcomes for new data | Discovering hidden patterns or groups |

## 5. What is "Unseen Data"?
> *Supervised Learning: The goal is to build a model using data where the target answers are already known, so the model can accurately predict the outcomes for **unseen data**.*

In machine learning, "unseen data" simply means new, real-world data that the computer model has never encountered before during its training process.

The easiest way to understand this is to compare a machine learning model to a student taking a math class.

### The Student Analogy
* **Training Data (Seen Data)**: This is the homework and practice problems the teacher assigns, complete with an answer key at the back of the book. The student uses these to practice and learn how to solve the equations.
* **Unseen Data**: This is the final exam. The test contains brand-new questions the student has never looked at before.

If the student truly learned the underlying math concepts, they will be able to solve the new exam questions accurately. However, if the student just lazy-memorized the exact answers from the homework, they will fail the exam because the questions are slightly different.

### How it Works in Practice
When building a supervised learning model, data scientists never use 100% of their labeled data to train the AI. If they did, they would have no way to test if the AI actually learned anything or if it just memorized the dataset.

Instead, they split their data into two separate piles:

1. **The Training Set (Usually ~80% of the data)**: This is fed into the model. The model looks at the features and the target answers to figure out the patterns.
2. **The Testing Set (Usually ~20% of the data)**: This pile is hidden away. Once the model is finished training, the data scientist feeds it this unseen data—but without giving it the answers.

The data scientist then compares the model's predictions on the unseen data to the real answers. If the model is highly accurate on this unseen data, it proves the model is genuinely smart and ready to be used in the real world.
