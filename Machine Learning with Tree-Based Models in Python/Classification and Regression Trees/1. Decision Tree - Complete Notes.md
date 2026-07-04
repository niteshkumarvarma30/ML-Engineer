# Decision Tree - Complete Notes (README.md)

# Table of Contents

1. What is a Decision Tree?
2. Why is it called a Decision Tree?
3. Components of a Decision Tree
4. Classification vs Regression Tree
5. Decision Tree as a Non-Parametric Model
6. Why Splitting is Required?
7. Pure Node vs Impure Node
8. Gini Impurity
9. Derivation of Gini Formula
10. Why Probability is Squared?
11. Calculating Gini
12. Weighted Gini Impurity
13. Choosing the Best Split
14. Entropy
15. Information Theory Behind Entropy
16. Why Logarithm?
17. Why Negative Sign?
18. Derivation of Entropy Formula
19. Calculating Entropy
20. Information Gain
21. Numerical Example
22. Gini vs Entropy
23. Complete Decision Tree Algorithm

---

# 1. What is a Decision Tree?

Decision Tree is a **Supervised Machine Learning Algorithm** used for

- Classification
- Regression

Instead of learning an equation like

```
y = wx + b
```

Decision Tree learns a sequence of questions.

Example

```
Salary > 50000 ?

        Yes

          ↓

Credit Score >700 ?

        Yes

          ↓

Loan Approved
```

The model keeps asking questions until it reaches a final prediction.

---

# 2. Why is it Called a Decision Tree?

It looks like an upside-down tree.

```
                Root

            Salary?

          /         \

      High          Low

      /               \

 Credit?          Credit?

 /      \

Yes      No
```

Each branch represents a decision.

Hence the name

**Decision Tree**.

---

# 3. Components of a Decision Tree

## Root Node

The first question asked by the tree.

Example

```
Salary?
```

There is only one root node.

---

## Decision Node

A node that asks another question.

Example

```
Salary?

↓

Credit History?

↓

Age?
```

Decision nodes continue splitting the data.

---

## Leaf Node (Terminal Node)

No further questions.

Contains only the final prediction.

Example

```
Loan = Approved
```

or

```
Loan = Rejected
```

---

# 4. Classification vs Regression Tree

## Classification Tree

Predicts categories.

Examples

- Spam / Not Spam
- Pass / Fail
- Disease / No Disease

Output

```
+1

or

-1
```

---

## Regression Tree

Predicts continuous values.

Examples

- House Price
- Temperature
- Sales

Output

```
52 Lakhs

78 Lakhs

100 Lakhs
```

---

# 5. Why is Decision Tree called Non-Parametric?

Unlike Linear Regression,

there is no equation like

```
y = wx+b
```

There are

- No Weights
- No Bias
- No Gradient Descent

Instead,

Decision Tree stores

```
Question

↓

Question

↓

Question

↓

Prediction
```

Hence it is called a **Non-Parametric Model**.

---

# 6. Why Splitting is Required?

Suppose a node contains

```
+

-

+

-

+

-
```

Both classes are mixed.

Prediction becomes difficult.

We split the data.

Example

```
Salary?

       /        \

High            Low
```

Now each child node becomes more homogeneous.

Goal

Create nodes containing only one class.

---

# 7. Pure Node vs Impure Node

## Pure Node

```
+

+

+

+
```

All samples belong to one class.

Prediction is easy.

---

## Impure Node

```
+

-

+

-

+
```

Classes are mixed.

Prediction is uncertain.

Decision Tree tries to reduce impurity.

---

# 8. What is Gini Impurity?

Gini measures

> "How likely are we to classify a randomly selected sample incorrectly?"

Pure node

↓

Low impurity

Mixed node

↓

High impurity

Decision Trees always minimize Gini.

---

# 9. Derivation of Gini Formula

Suppose

```
P(+)=0.8

P(-)=0.2
```

Probability of correct prediction

```
0.8²

+

0.2²

=

0.68
```

Probability of wrong prediction

```
1−0.68

=0.32
```

Therefore

```
Gini

=

1−ΣPi²
```

General Formula

```
Gini

=

1−ΣPi²
```

---

# 10. Why Do We Square the Probabilities?

Suppose

```
P=1
```

Square

```
1²=1
```

Suppose

```
P=0.5
```

Square

```
0.25
```

Squaring rewards dominant classes.

As one class becomes stronger,

Gini decreases.

---

# 11. Calculating Gini

Example

```
8 Positive

2 Negative
```

Probabilities

```
0.8

0.2
```

Gini

```
1−(0.8²+0.2²)

=

1−(0.64+0.04)

=

0.32
```

Another example

```
9 Positive

1 Negative
```

```
1−(0.9²+0.1²)

=

1−(0.81+0.01)

=

0.18
```

Smaller Gini

↓

More Pure Node

---

# Maximum and Minimum Gini

Perfect Node

```
10 Positive

0 Negative
```

```
Gini=0
```

Maximum Impurity

```
5 Positive

5 Negative
```

```
Gini=0.5
```

(Binary Classification)

---

# 12. Weighted Gini Impurity

Suppose

Parent Node

```
20 Samples
```

Split into

Left Child

```
14 Samples

Gini=0.49
```

Right Child

```
6 Samples

Gini=0.44
```

Simply averaging is incorrect.

Large nodes should contribute more.

Weight

```
Left

14/20=0.70
```

Right

```
6/20=0.30
```

Weighted Gini

```
0.70×0.49

+

0.30×0.44

=

0.475
```

Formula

```
Weighted Gini

=

Σ

(Node Size / Parent Size)

×

Node Gini
```

---

# 13. Choosing the Best Split

Suppose

| Feature | Weighted Gini |
|----------|---------------|
| Salary | 0.48 |
| Age | 0.36 |
| Credit History | 0.18 |

Decision Tree chooses

```
Credit History
```

because

```
0.18
```

is the smallest.

Decision Rule

```
Choose

Minimum Weighted Gini
```

---

# 14. What is Entropy?

Entropy measures

> "How much uncertainty exists inside a node?"

Pure Node

↓

Entropy = 0

Mixed Node

↓

High Entropy

Entropy is based on Information Theory.

---

# 15. Information Theory

Imagine

Someone tells you

```
Tomorrow the Sun will rise.
```

No surprise.

Information

```
≈0
```

Now

Someone says

```
Tomorrow your college is closed.
```

Huge surprise.

More information.

Entropy measures

How uncertain we are before knowing the answer.

---

# 16. Why Logarithm?

Information should satisfy

| Probability | Information |
|--------------|-------------|
|1|0|
|0.5|1|
|0.25|2|
|0.125|3|

This naturally follows

```
log₂
```

Therefore

Information of one event

```
-log₂(P)
```

---

# 17. Why Negative Sign?

For

```
0<P<1
```

Logarithm is negative.

Example

```
log₂(0.5)

=-1
```

Information cannot be negative.

Therefore

Multiply by

```
-1
```

Exactly like Negative Log Likelihood in Logistic Regression.

---

# 18. Derivation of Entropy Formula

Suppose

```
80%

Positive

20%

Negative
```

Information for Positive

```
-log₂(0.8)
```

Weighted Information

```
0.8

×

(-log₂0.8)
```

Similarly

Negative

```
0.2

×

(-log₂0.2)
```

Total

```
Entropy

=

-ΣPi log₂Pi
```

---

# 19. Calculating Entropy

Example

```
8 Positive

2 Negative
```

Probabilities

```
0.8

0.2
```

Entropy

```
-(0.8log₂0.8

+

0.2log₂0.2)

≈0.722
```

Perfect Node

```
Entropy=0
```

Maximum Binary Entropy

```
5 Positive

5 Negative

Entropy=1
```

---

# 20. What is Information Gain?

Suppose

Parent Entropy

```
0.971
```

After splitting

Weighted Child Entropy

```
0.648
```

Information Gain

```
0.971

−

0.648

=

0.323
```

Formula

```
Information Gain

=

Parent Entropy

−

Weighted Child Entropy
```

Meaning

How much uncertainty was removed by the split.

---

# 21. Numerical Example

Dataset

| Outlook | Play |
|----------|------|
|Sunny|No|
|Sunny|No|
|Overcast|Yes|
|Rain|Yes|
|Rain|Yes|
|Rain|No|
|Overcast|Yes|
|Sunny|No|
|Sunny|Yes|
|Rain|Yes|

Parent

```
6 Yes

4 No
```

Entropy

```
0.971
```

Split by Outlook

Sunny

```
Entropy=0.811
```

Overcast

```
Entropy=0
```

Rain

```
Entropy=0.811
```

Weighted Entropy

```
0.648
```

Information Gain

```
0.971−0.648

=

0.323
```

---

# 22. Gini vs Entropy

| Gini | Entropy |
|------|----------|
| Measures impurity | Measures uncertainty |
| No logarithm | Uses logarithm |
| Faster | Slightly slower |
| Used in CART | Used in ID3, C4.5 |

Decision Rule

Gini

↓

Minimum Weighted Gini

Entropy

↓

Maximum Information Gain

Both aim to produce the purest child nodes.

---

# 23. Complete Decision Tree Algorithm

```
Start with Entire Dataset
            │
            ▼
Calculate Parent Impurity
(Gini or Entropy)
            │
            ▼
Try Every Feature
(Salary, Age, Credit History...)
            │
            ▼
Split Dataset Using One Feature
            │
            ▼
Calculate Child Gini
or
Child Entropy
            │
            ▼
Compute

Weighted Gini

OR

Weighted Entropy
            │
            ▼
If using Entropy

Information Gain

=

Parent Entropy

−

Weighted Child Entropy
            │
            ▼
Compare Every Feature
            │
            ▼
Choose

Smallest Weighted Gini

OR

Largest Information Gain
            │
            ▼
Create Decision Node
            │
            ▼
Repeat the Same Process
for Every Child Node
            │
            ▼
Stop When

• Node Becomes Pure

OR

• Maximum Depth Reached

OR

• Minimum Samples Reached
            │
            ▼
Create Leaf Node
            │
            ▼
Final Prediction
```

---

# Final Summary

```
Dataset
      │
      ▼
Decision Tree
      │
      ▼
Ask Questions
      │
      ▼
Split Dataset
      │
      ▼
Measure Impurity

(Gini)

OR

Measure Uncertainty

(Entropy)
      │
      ▼
Calculate

Weighted Gini

OR

Information Gain
      │
      ▼
Choose Best Feature
      │
      ▼
Repeat Recursively
      │
      ▼
Pure Leaf Nodes
      │
      ▼
Final Classification / Regression Prediction
```

# Key Takeaways

- Decision Trees split data by asking questions.
- A **Root Node** is the first question.
- **Decision Nodes** continue splitting the data.
- **Leaf Nodes** contain the final prediction.
- **Gini Impurity** measures the probability of misclassification.
- **Entropy** measures uncertainty using Information Theory.
- **Weighted Gini** evaluates the quality of an entire split.
- **Information Gain** measures the reduction in uncertainty after splitting.
- Decision Trees choose the feature with the **lowest Weighted Gini** or the **highest Information Gain**.
- The process repeats recursively until stopping criteria are met, producing a complete Decision Tree.
