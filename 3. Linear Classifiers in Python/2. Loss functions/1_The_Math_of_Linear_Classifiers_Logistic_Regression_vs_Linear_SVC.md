# The Math of Linear Classifiers

## Logistic Regression vs Linear SVC

Logistic Regression and Linear SVC are both **linear classifiers**. They use the same basic linear scoring equation:

$$
z = w^T x + b
$$

However, they are **not the same algorithm**.

The important difference is what they do with this score and how they learn the parameters $w$ and $b$.

---

## 1. The Grocery Cart Math: Dot Product

A dot product is simply a way of multiplying corresponding values and adding the results.

Imagine a grocery store:

- Prices: `[2, 1, 5]`
- Quantities: `[3, 4, 2]`

The total cost is:

```text
(2 x 3) + (1 x 4) + (5 x 2)
= 6 + 4 + 10
= 20
```

This is a dot product.

In Python:

```python
prices @ quantities
```

The `@` operator performs matrix or vector multiplication.

---

# 2. The Raw Model Output

A linear classifier uses the same idea.

The general equation is:

$$
z = w^T x + b
$$

where:

- $x$ = input features
- $w$ = learned coefficients or weights
- $b$ = intercept or bias
- $z$ = raw model output, also called a decision score or linear score

For example:

```text
Features:
x1 = 3
x2 = 4

Weights:
w1 = 2
w2 = 1

Intercept:
b = -5
```

Then:

$$
z = (2 x 3) + (1 x 4) - 5
$$

$$
z = 6 + 4 - 5
$$

$$
z = 5
$$

So the raw score is:

```text
z = 5
```

---

# 3. The Decision Boundary

The decision boundary is where the raw score is zero:

$$
w^T x + b = 0
$$

For two features:

$$
w_1x_1 + w_2x_2 + b = 0
$$

This equation represents a straight line.

For more than two features, it represents a hyperplane.

Therefore, Logistic Regression and Linear SVC can both create a **linear decision boundary**.

---

# 4. The Plus/Minus Rule

For a binary linear classifier, the sign of the raw score tells us which side of the decision boundary the point is on.

```text
z > 0  -> one class
z < 0  -> the other class
z = 0  -> exactly on the decision boundary
```

For example:

```text
z = +3   -> Class 1 side
z = +0.2 -> Class 1 side
z = 0    -> Decision boundary
z = -0.2 -> Class 0 side
z = -3   -> Class 0 side
```

This idea is especially direct for a Linear SVM.

For Logistic Regression, the same boundary appears when the default probability threshold is 0.5.

---

# 5. Logistic Regression: What Happens After z?

This is the important part.

Logistic Regression first calculates:

$$
z = w^T x + b
$$

Then it applies the **sigmoid function**:

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

The sigmoid converts the raw score into a value between 0 and 1.

This value is interpreted as the model's estimated probability for the positive class.

### Example

Suppose:

$$
z = 2
$$

Then:

$$
p = \sigma(2) \approx 0.881
$$

So the model estimates approximately:

```text
P(Class 1) = 88.1%
```

If:

$$
z = -2
$$

then:

$$
\sigma(-2) \approx 0.119
$$

So:

```text
P(Class 1) = 11.9%
```

---

# 6. Logistic Regression Prediction Pipeline

The complete idea is:

```text
Input Features
      |
      v
z = w^T x + b
      |
      v
Sigmoid
      |
      v
Probability
      |
      v
Threshold
      |
      v
Class
```

With the usual threshold of 0.5:

```text
Probability >= 0.5 -> Class 1
Probability <  0.5 -> Class 0
```

---

# 7. Why Does Logistic Regression Have the Same Decision Boundary as Linear SVC?

This is the key mathematical connection.

For Logistic Regression:

$$
p = \sigma(z)
$$

The default classification threshold is:

$$
p = 0.5
$$

The sigmoid has an important property:

$$
\sigma(0) = 0.5
$$

Therefore:

```text
z > 0 -> sigmoid(z) > 0.5 -> Class 1

z = 0 -> sigmoid(z) = 0.5 -> Decision boundary

z < 0 -> sigmoid(z) < 0.5 -> Class 0
```

So Logistic Regression can make its final binary decision simply by checking whether:

$$
z > 0
$$

The sigmoid is still part of the Logistic Regression probability model, but for a default 0.5 classification threshold, it does not change which side of the boundary the point belongs to.

---

# 8. Linear SVC: Does It Use Sigmoid?

No.

A basic Linear SVC does **not** use the sigmoid function to make its normal classification decision.

It calculates:

$$
z = w^T x + b
$$

and uses the decision score to determine the class.

Conceptually:

```text
z > 0 -> Class 1
z < 0 -> Class 0
```

There is no:

```text
z -> sigmoid(z)
```

step in the normal Linear SVC decision process.

---

# 9. Linear SVC Prediction Pipeline

The basic idea is:

```text
Input Features
      |
      v
z = w^T x + b
      |
      v
Decision Score
      |
      v
Sign / Threshold
      |
      v
Class
```

The value of `z` is a **decision score**, not a probability.

For example:

```text
z = +2.5
```

does NOT mean:

```text
Probability = 92.4%
```

That interpretation belongs to the sigmoid output of Logistic Regression.

---

# 10. Side-by-Side Example

Suppose both models have the same parameters:

$$
w = [2,3]
$$

and:

$$
b = -5
$$

For a particular input, suppose:

$$
z = 2
$$

### Logistic Regression

First:

$$
z = 2
$$

Then:

$$
p = \sigma(2) \approx 0.881
$$

Therefore:

```text
Probability = 88.1%
Class = 1
```

### Linear SVC

It directly uses:

```text
z = 2
```

Since:

```text
z > 0
```

the prediction is:

```text
Class = 1
```

So:

```text
Logistic Regression:
2 -> sigmoid -> 0.881 -> Class 1

Linear SVC:
2 -> decision score -> Class 1
```

The internal interpretation of the score is different, but the binary class decision can be the same.

---

# 11. Another Example: Negative Score

Suppose:

$$
z = -2
$$

### Logistic Regression

$$
\sigma(-2) \approx 0.119
$$

Therefore:

```text
Probability = 11.9%
Class = 0
```

### Linear SVC

It directly sees:

```text
z = -2
```

Since:

```text
z < 0
```

it predicts:

```text
Class = 0
```

Again, both make the same binary decision when they use the same $w$ and $b$.

---

# 12. The Important Correction: Are They Actually the Same?

No.

Logistic Regression and Linear SVC are **not the same algorithm**.

They share the same type of linear decision function:

$$
\boxed{z = w^T x + b}
$$

But they learn $w$ and $b$ differently.

This is the most important distinction.

---

# 13. Logistic Regression Uses Log Loss

Logistic Regression is based on probability modeling.

It uses the sigmoid:

$$
p = \sigma(z)
$$

and commonly minimizes **log loss**, also called logistic loss or cross-entropy loss.

For binary classification:

$$
L = -[y\log(p) + (1-y)\log(1-p)]
$$

The model is therefore encouraged to produce good probability estimates.

---

# 14. Linear SVM Uses Hinge Loss

Linear SVM focuses on classification and the **margin** between classes.

A common form of hinge loss is:

$$
L = \max(0, 1-yz)
$$

where:

$$
y \in \{-1,+1\}
$$

The SVM tries to classify points correctly while also creating a large margin around the decision boundary.

Conceptually:

```text
Class -1       Margin       Boundary       Margin       Class +1

   - - -           |             |             |            + + +
   - - -           |             |             |            + + +
                   |             |             |
              -1 margin          0         +1 margin
```

The exact optimization formulation also includes regularization.

---

# 15. Why Can Their Final Lines Look Similar?

Because both are trying to separate the classes using a linear boundary.

Both use:

$$
w^T x + b = 0
$$

But they optimize different objectives.

```text
Logistic Regression
        |
        v
     Log Loss
        |
        v
    Learn w, b


Linear SVM
        |
        v
    Hinge Loss
        |
        v
    Learn w, b
```

Therefore, the learned weights and intercepts are generally different.

So their actual trained boundaries can also be different.

---

# 16. What Does "Same Prediction Equation" Really Mean?

A statement such as:

> Logistic Regression and Linear SVM use the same prediction equation.

should be understood carefully.

The precise statement is:

> Both models use the same type of linear scoring function $w^T x+b$. If they happen to have the same weights and intercept, their decision boundary is the same.

It does **not** mean that their complete prediction pipelines are identical.

### Logistic Regression

```text
x
|
v
z = w^T x + b
|
v
sigmoid(z)
|
v
probability
|
v
threshold
|
v
class
```

### Linear SVC

```text
x
|
v
z = w^T x + b
|
v
decision score
|
v
class
```

Therefore:

```text
Same linear score equation
        !=
Same complete algorithm
```

---

# 17. The Geometric Interpretation

Imagine the decision boundary as a wall.

The equation:

$$
w^T x+b=0
$$

defines the wall.

```text
             Class 1
                |
                |
                |
----------------+----------------
                |
                |
                |
             Class 0
```

Changing $b$ shifts the boundary.

Changing the weights $w$ changes its orientation.

Therefore:

### Changing the intercept

Moves the boundary.

```text
Before:
-------------------

After:
        -------------------
```

### Changing the weights

Changes the orientation of the boundary.

```text
Before:
-------------------

After:
       /
      /
     /
```

---

# 18. Raw Score vs Probability

This distinction is extremely important.

## Logistic Regression

The sigmoid output can be interpreted as a probability:

$$
p = \sigma(z)
$$

Example:

```text
z = 2
p = 0.881
```

So approximately:

```text
88.1% estimated probability of Class 1
```

## Linear SVC

The raw decision score is not automatically a probability.

Example:

```text
z = 2
```

means the point has a positive decision score.

It does **not** mean:

```text
Probability = 88.1%
```

---

# 19. A Useful Mental Model

Think of `z` as a person's position relative to a boundary.

```text
                 Decision Boundary
                        |
                        v

Class 0             z = 0             Class 1

<---------------------|--------------------->
                     0
```

Logistic Regression asks:

> "Where are you relative to the boundary, and what probability should I assign?"

So it does:

```text
z -> sigmoid -> probability
```

Linear SVC asks:

> "Which side of the boundary are you on, and how large is the margin?"

So it does:

```text
z -> decision score -> class
```

---

# 20. The Most Important Mathematical Connection

Remember these four equations.

### Both start with

$$
\boxed{z=w^Tx+b}
$$

### Logistic Regression

$$
\boxed{p=\sigma(z)}
$$

with:

$$
\boxed{\sigma(z)=\frac{1}{1+e^{-z}}}
$$

### Logistic Regression boundary

$$
\boxed{p=0.5 \Longleftrightarrow z=0}
$$

### Linear SVC boundary

$$
\boxed{z=0}
$$

Therefore, with the same $w$ and $b$:

$$
\boxed{\text{Both have the same binary decision boundary}}
$$

---

# 21. Final Comparison

| Concept | Logistic Regression | Linear SVC |
|---|---|---|
| Linear score | $z=w^Tx+b$ | $z=w^Tx+b$ |
| Uses sigmoid | Yes, for probability modeling | No |
| Probability output | Yes | No, not inherently |
| Decision score | $z$ before sigmoid | $z$ directly |
| Default binary boundary | $z=0$ | $z=0$ |
| Main loss | Log loss | Hinge loss |
| Main idea | Probability modeling | Margin maximization |
| Regularization | Commonly used | Commonly used |
| Same algorithm? | No | No |
| Can have same boundary? | Yes, if $w,b$ are the same | Yes |
| Raw score is probability? | No, sigmoid output is the probability | No |

---

# 22. Final Takeaway

The easiest way to remember the difference is:

```text
                SAME START
                    |
                    v
             z = w^T x + b
                    |
          +---------+---------+
          |                   |
          v                   v
   Logistic Regression     Linear SVC
          |                   |
          v                   |
      sigmoid(z)              |
          |                   |
          v                   v
     probability         decision score
          |                   |
          v                   v
       class               class
```

And during training:

```text
Logistic Regression -> Log Loss -> learns w and b

Linear SVM          -> Hinge Loss + Margin -> learns w and b
```

So the correct statement is:

> **Logistic Regression and Linear SVC are both linear classifiers and use the same linear scoring equation $w^Tx+b$. Logistic Regression additionally uses the sigmoid to model probabilities, while Linear SVC directly uses the decision score. They are not the same algorithm because they use different loss functions and optimization objectives.**
