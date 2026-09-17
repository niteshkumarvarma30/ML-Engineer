# XGBoost for Binary Classification

## Complete Notes with Worked Examples

XGBoost (Extreme Gradient Boosting) is a gradient boosting algorithm that builds decision trees sequentially.

For binary classification, XGBoost works with an internal real-valued **margin**. The margin is converted into a probability using the sigmoid function. Each new tree adds a correction to the current model.

This chapter covers:

- Initial prediction
- Log-odds
- Sigmoid
- Gradients and Hessians
- Pseudo-residual intuition
- Candidate split thresholds
- Split evaluation
- Gain
- Best split selection
- Leaf weights
- Learning rate
- Model updates
- Final probability
- Classification threshold
- Tree split threshold vs classification threshold

---

# Table of Contents

1. Introduction
2. Problem Statement
3. Dataset
4. Why XGBoost Classification Is Different from Regression
5. Stage 1 - Initial Prediction
6. Log-Odds
7. Sigmoid Function
8. Initial Prediction Table
9. Pseudo-Residual Intuition
10. Gradients and Hessians
11. Building the First Decision Tree
12. How Candidate Split Thresholds Are Generated
13. Evaluating a Split
14. Worked Example - Threshold 5.97
15. Worked Example - Threshold 6.67
16. Worked Example - Threshold 7.62
17. Worked Example - Threshold 8.87
18. Comparing All Candidate Splits
19. How the Best Threshold Is Selected
20. First Decision Tree
21. Computing Leaf Outputs
22. Learning Rate
23. Updating the Model
24. Converting Margin to Probability
25. Computing New Gradients and Hessians
26. Stage 2 and Further Trees
27. Final Prediction Formula
28. Classification Threshold
29. Tree Split Threshold vs Classification Threshold
30. Can the Classification Threshold Be Changed?
31. Regression vs Classification
32. Complete XGBoost Training Pipeline
33. Important Formulas
34. Important Corrections and Clarifications
35. Interview Questions
36. Final Intuition

---

# 1. Introduction

XGBoost stands for **Extreme Gradient Boosting**.

It is an ensemble learning algorithm that builds many decision trees sequentially.

The basic idea is:

```text
Tree 1
  |
  v
Current prediction
  |
  v
Tree 2 learns a correction
  |
  v
Updated prediction
  |
  v
Tree 3 learns another correction
  |
  v
...
  |
  v
Final model
```

Each new tree tries to improve the current model.

For binary classification, the target is usually:

```text
0 -> Negative class
1 -> Positive class
```

For example:

```text
0 -> Not Placed
1 -> Placed
```

---

# 2. Problem Statement

Suppose we want to predict whether a student gets placed.

Feature:

```text
CGPA
```

Target:

```text
Placed
```

where:

```text
1 = Yes
0 = No
```

---

# 3. Dataset

| Sample | CGPA | Actual `y` |
|---:|---:|---:|
| 1 | 5.70 | 0 |
| 2 | 6.25 | 1 |
| 3 | 7.10 | 0 |
| 4 | 8.15 | 1 |
| 5 | 9.60 | 1 |

There are:

```text
3 positive examples
2 negative examples
```

---

# 4. Why XGBoost Classification Is Different from Regression

## Regression

Regression predicts a continuous value.

Examples:

```text
Salary = 85000
House price = 4500000
Temperature = 31.5
```

## Binary Classification

Binary classification predicts one of two classes.

A convenient way to represent the model output is:

```text
Internal margin
      |
      v
   Sigmoid
      |
      v
Probability between 0 and 1
      |
      v
Class decision
```

The sigmoid is:

$$
p = \frac{1}{1 + e^{-F(x)}}
$$

where:

- `F(x)` = current model margin
- `p` = probability of class 1

---

# 5. Stage 1 - Initial Prediction

Before building the first tree, XGBoost needs an initial model.

There are:

```text
3 placed
2 not placed
```

Therefore, the initial positive-class probability is:

$$
p_0 = \frac{3}{5}=0.6
$$

So initially:

```text
Every sample -> probability 0.60
```

This is only the starting point.

The trees will improve it.

---

# 6. Log-Odds

XGBoost's internal model output is not restricted to the range `[0, 1]`.

We can transform a probability into a real-valued log-odds score:

$$
F_0 = \log\left(\frac{p}{1-p}\right)
$$

For:

$$
p=0.6
$$

the odds are:

$$
\frac{0.6}{0.4}=1.5
$$

Therefore:

$$
F_0=\log(1.5)\approx0.405
$$

So:

```text
Initial probability = 0.60
Initial margin      = 0.405
```

Important:

```text
0.405 is NOT a probability.

0.405 is an internal model score.
```

---

# 7. Sigmoid Function

The sigmoid converts the margin back into a probability:

$$
p=\frac{1}{1+e^{-F(x)}}
$$

An equivalent form is:

$$
p=\frac{e^{F(x)}}{1+e^{F(x)}}
$$

For:

$$
F_0=0.405
$$

we get approximately:

$$
p=0.60
$$

Therefore:

```text
Margin / Log-Odds
        |
        v
     Sigmoid
        |
        v
Probability
```

---

# 8. Initial Prediction Table

| CGPA | Actual `y` | Initial Probability |
|---:|---:|---:|
| 5.70 | 0 | 0.60 |
| 6.25 | 1 | 0.60 |
| 7.10 | 0 | 0.60 |
| 8.15 | 1 | 0.60 |
| 9.60 | 1 | 0.60 |

The model initially treats every student equally.

The first tree will learn how CGPA should change the prediction.

---

# 9. Pseudo-Residual Intuition

A useful intuition for binary classification is:

$$
r=y-p
$$

For the first sample:

```text
Actual = 0
Probability = 0.60
```

Therefore:

$$
r=0-0.6=-0.6
$$

For the second sample:

```text
Actual = 1
Probability = 0.60
```

Therefore:

$$
r=1-0.6=0.4
$$

The table is:

| CGPA | Actual | Probability | `y - p` |
|---:|---:|---:|---:|
| 5.70 | 0 | 0.60 | -0.60 |
| 6.25 | 1 | 0.60 | +0.40 |
| 7.10 | 0 | 0.60 | -0.60 |
| 8.15 | 1 | 0.60 | +0.40 |
| 9.60 | 1 | 0.60 | +0.40 |

These are useful for intuition.

However, actual XGBoost tree construction uses **gradients and Hessians**, not ordinary residuals alone.

---

# 10. Gradients and Hessians

For binary logistic loss, the gradient for observation `i` is:

$$
g_i=p_i-y_i
$$

The Hessian is:

$$
h_i=p_i(1-p_i)
$$

For the initial probability:

$$
p=0.6
$$

we get:

$$
h=0.6(1-0.6)=0.24
$$

The initial values are:

| CGPA | `y` | `p` | Gradient `g = p - y` | Hessian `h = p(1-p)` |
|---:|---:|---:|---:|---:|
| 5.70 | 0 | 0.60 | +0.60 | 0.24 |
| 6.25 | 1 | 0.60 | -0.40 | 0.24 |
| 7.10 | 0 | 0.60 | +0.60 | 0.24 |
| 8.15 | 1 | 0.60 | -0.40 | 0.24 |
| 9.60 | 1 | 0.60 | -0.40 | 0.24 |

Notice:

$$
g=-(y-p)
$$

So:

```text
y - p -> intuitive correction direction
p - y -> actual gradient
```

---

# 11. Building the First Decision Tree

The tree learns how to split the feature values.

First, sort CGPA:

```text
5.70
6.25
7.10
8.15
9.60
```

The tree considers possible places where the data can be divided.

---

# 12. How Candidate Split Thresholds Are Generated

For a simple continuous-feature example, consider the midpoint between neighboring values.

### Between 5.70 and 6.25

$$
\frac{5.70+6.25}{2}=5.975
$$

Approximately:

```text
5.97
```

### Between 6.25 and 7.10

$$
\frac{6.25+7.10}{2}=6.675
$$

Approximately:

```text
6.67
```

### Between 7.10 and 8.15

$$
\frac{7.10+8.15}{2}=7.625
$$

Approximately:

```text
7.62
```

### Between 8.15 and 9.60

$$
\frac{8.15+9.60}{2}=8.875
$$

Approximately:

```text
8.87
```

So our simple example has:

```text
Candidate thresholds:

5.97
6.67
7.62
8.87
```

Important:

> These are **tree split thresholds**. They are not the same as the final classification threshold of `0.5`.

---

# 13. Evaluating a Split

XGBoost evaluates candidate splits using gradient and Hessian statistics.

For a node:

$$
G=\sum_i g_i
$$

and:

$$
H=\sum_i h_i
$$

A common regularized node statistic is:

$$
Score=\frac{G^2}{H+\lambda}
$$

where:

- `G` = sum of gradients
- `H` = sum of Hessians
- `lambda` = L2 regularization

A common gain expression is:

$$
Gain=
\frac{1}{2}
\left(
\frac{G_L^2}{H_L+\lambda}
+
\frac{G_R^2}{H_R+\lambda}
-
\frac{G_P^2}{H_P+\lambda}
\right)
-\gamma
$$

where:

- `L` = left child
- `R` = right child
- `P` = parent
- `lambda` = L2 regularization
- `gamma` = minimum loss reduction required for a split

For our hand calculation, use:

$$
\lambda=0
$$

and:

$$
\gamma=0
$$

For comparing candidate splits, we can temporarily omit the common `1/2` factor. This does not change which candidate has the largest gain.

---

# 14. Worked Example - Threshold 5.97

Consider:

```text
CGPA < 5.97
```

The split is:

```text
                 CGPA < 5.97
                  /        \
                Yes         No
```

Left:

```text
5.70
```

Right:

```text
6.25
7.10
8.15
9.60
```

## Left Node

For `5.70`:

```text
gradient = +0.60
hessian  = 0.24
```

Therefore:

$$
G_L=0.60
$$

$$
H_L=0.24
$$

Score:

$$
Score_L=\frac{0.60^2}{0.24}
$$

$$
Score_L=\frac{0.36}{0.24}=1.5
$$

## Right Node

Gradients:

```text
-0.40
+0.60
-0.40
-0.40
```

Therefore:

$$
G_R=-0.60
$$

There are four observations:

$$
H_R=4(0.24)=0.96
$$

Score:

$$
Score_R=\frac{(-0.60)^2}{0.96}
$$

$$
Score_R=\frac{0.36}{0.96}=0.375
$$

## Parent Node

All gradients:

```text
+0.60
-0.40
+0.60
-0.40
-0.40
```

Therefore:

$$
G_P=0
$$

So:

$$
Score_P=0
$$

## Simplified Gain

$$
Gain^*=1.5+0.375-0
$$

$$
\boxed{Gain^*=1.875}
$$

Using the common `1/2` factor:

$$
Gain=0.5(1.875)=0.9375
$$

---

# 15. Worked Example - Threshold 6.67

Consider:

```text
CGPA < 6.67
```

Left:

```text
5.70
6.25
```

Right:

```text
7.10
8.15
9.60
```

## Left Node

Gradients:

```text
+0.60
-0.40
```

Therefore:

$$
G_L=0.20
$$

and:

$$
H_L=2(0.24)=0.48
$$

Score:

$$
Score_L=
\frac{0.20^2}{0.48}
$$

$$
Score_L\approx0.0833
$$

## Right Node

Gradients:

```text
+0.60
-0.40
-0.40
```

Therefore:

$$
G_R=-0.20
$$

and:

$$
H_R=3(0.24)=0.72
$$

Score:

$$
Score_R=
\frac{(-0.20)^2}{0.72}
$$

$$
Score_R\approx0.0556
$$

## Gain

$$
Gain^*
=
0.0833+0.0556
$$

$$
\boxed{Gain^*\approx0.1389}
$$

Using the `1/2` factor:

$$
\boxed{Gain\approx0.0694}
$$

---

# 16. Worked Example - Threshold 7.62

Consider:

```text
CGPA < 7.62
```

Left:

```text
5.70
6.25
7.10
```

Right:

```text
8.15
9.60
```

## Left Node

Gradients:

```text
+0.60
-0.40
+0.60
```

Therefore:

$$
G_L=0.80
$$

and:

$$
H_L=3(0.24)=0.72
$$

Score:

$$
Score_L=
\frac{0.80^2}{0.72}
$$

$$
Score_L\approx0.8889
$$

## Right Node

Gradients:

```text
-0.40
-0.40
```

Therefore:

$$
G_R=-0.80
$$

and:

$$
H_R=2(0.24)=0.48
$$

Score:

$$
Score_R=
\frac{(-0.80)^2}{0.48}
$$

$$
Score_R\approx1.3333
$$

## Gain

$$
Gain^*
=
0.8889+1.3333
$$

$$
\boxed{Gain^*\approx2.2222}
$$

Using the `1/2` factor:

$$
\boxed{Gain\approx1.1111}
$$

This is larger than the previous candidate gains.

---

# 17. Worked Example - Threshold 8.87

Consider:

```text
CGPA < 8.87
```

Left:

```text
5.70
6.25
7.10
8.15
```

Right:

```text
9.60
```

## Left Node

Gradients:

```text
+0.60
-0.40
+0.60
-0.40
```

Therefore:

$$
G_L=0.20
$$

and:

$$
H_L=4(0.24)=0.96
$$

Score:

$$
Score_L=
\frac{0.20^2}{0.96}
$$

$$
Score_L\approx0.0417
$$

## Right Node

For `9.60`:

```text
gradient = -0.40
hessian  = 0.24
```

Therefore:

$$
G_R=-0.40
$$

$$
H_R=0.24
$$

Score:

$$
Score_R=
\frac{(-0.40)^2}{0.24}
$$

$$
Score_R=
\frac{0.16}{0.24}
\approx0.6667
$$

## Gain

$$
Gain^*
=
0.0417+0.6667
$$

$$
\boxed{Gain^*\approx0.7084}
$$

---

# 18. Comparing All Candidate Splits

Using the simplified gain without the common `1/2` factor:

| Candidate Threshold | Simplified Gain |
|---:|---:|
| 5.97 | 1.8750 |
| 6.67 | 0.1389 |
| 7.62 | **2.2222** |
| 8.87 | 0.7084 |

Therefore:

```text
5.97 -> 1.8750
6.67 -> 0.1389
7.62 -> 2.2222  <- highest
8.87 -> 0.7084
```

---

# 19. How the Best Threshold Is Selected

This is the key idea.

XGBoost does not simply choose a threshold based on the feature value.

It evaluates candidate splits.

The process is:

```text
Sort feature values
       |
       v
Generate candidate split thresholds
       |
       v
5.97, 6.67, 7.62, 8.87
       |
       v
Calculate gradients and Hessians
       |
       v
Calculate Gain for each split
       |
       v
Compare Gains
       |
       v
Choose the best valid split
```

In our example:

$$
Gain(5.97)=1.875
$$

$$
Gain(6.67)=0.139
$$

$$
Gain(7.62)=2.222
$$

$$
Gain(8.87)=0.708
$$

Therefore:

$$
\boxed{\text{Best split threshold}=7.62}
$$

because it produces the largest gain in this simplified example.

The word **best** here means:

> Best according to the objective improvement calculated by the tree-building algorithm, subject to the model's constraints and regularization.

---

# 20. First Decision Tree

The selected split is:

```text
             CGPA < 7.62
              /        \
            Yes         No
             /           \
        5.70, 6.25, 7.10  8.15, 9.60
```

The leaves do not simply output `0` or `1`.

They contain a **leaf weight**, which is a correction to the current model margin.

---

# 21. Computing Leaf Outputs

The standard second-order XGBoost leaf weight is:

$$
w_j=-\frac{G_j}{H_j+\lambda}
$$

where:

- `G_j` = sum of gradients in the leaf
- `H_j` = sum of Hessians in the leaf
- `lambda` = L2 regularization

For this simplified example:

$$
\lambda=0
$$

## Left Leaf

Samples:

```text
5.70
6.25
7.10
```

Gradient sum:

$$
G_L=0.60-0.40+0.60=0.80
$$

Hessian sum:

$$
H_L=3(0.24)=0.72
$$

Leaf weight:

$$
w_L=-\frac{0.80}{0.72}
$$

$$
\boxed{w_L\approx-1.11}
$$

## Right Leaf

Samples:

```text
8.15
9.60
```

Gradient sum:

$$
G_R=-0.40-0.40=-0.80
$$

Hessian sum:

$$
H_R=2(0.24)=0.48
$$

Leaf weight:

$$
w_R=-\frac{-0.80}{0.48}
$$

$$
\boxed{w_R\approx+1.67}
$$

The tree is:

```text
                 CGPA < 7.62
                  /        \
                 /          \
            -1.11           +1.67
```

These are **margin corrections**, not probabilities.

---

# 22. Learning Rate

XGBoost scales each tree's contribution using the learning rate:

$$
\eta
$$

Suppose:

$$
\eta=0.3
$$

Then:

$$
F_{new}(x)
=
F_{old}(x)
+
\eta T(x)
$$

where `T(x)` is the leaf weight produced by the tree.

For the left leaf:

$$
0.3(-1.11)\approx-0.333
$$

So only part of the full correction is applied.

A smaller learning rate generally means each tree makes a smaller update.

---

# 23. Updating the Model

Consider:

```text
CGPA = 5.70
```

This sample belongs to the left leaf.

Initial margin:

$$
F_0=0.405
$$

Leaf weight:

$$
w_L=-1.11
$$

Learning rate:

$$
\eta=0.3
$$

Update:

$$
F_1
=
0.405+0.3(-1.11)
$$

$$
F_1
\approx0.072
$$

Therefore:

```text
Old margin ≈ 0.405
New margin ≈ 0.072
```

The model moved the margin downward.

That is sensible because this sample has actual class `0`.

---

# 24. Converting Margin to Probability

Now convert the updated margin to a probability.

$$
p_1=
\frac{1}{1+e^{-F_1}}
$$

Using:

$$
F_1\approx0.072
$$

we get approximately:

$$
\boxed{p_1\approx0.518}
$$

Before the tree:

```text
Probability = 0.600
```

After the tree:

```text
Probability ≈ 0.518
```

---

## Another Example: CGPA = 8.15

This sample belongs to the right leaf.

Initial margin:

$$
F_0=0.405
$$

Right leaf weight:

$$
w_R=1.67
$$

Learning rate:

$$
\eta=0.3
$$

Update:

$$
F_1
=
0.405+0.3(1.67)
$$

$$
F_1\approx0.906
$$

Probability:

$$
p_1=
\frac{1}{1+e^{-0.906}}
$$

Approximately:

$$
\boxed{p_1\approx0.712}
$$

So:

```text
Before: 0.600
After:  0.712
```

The model increased the probability for this higher-CGPA group.

---

# 25. Computing New Gradients and Hessians

After the model is updated, XGBoost calculates new probabilities.

Then it calculates new gradients and Hessians.

For logistic loss:

$$
g_i=p_i-y_i
$$

$$
h_i=p_i(1-p_i)
$$

Example:

```text
Actual y = 0
New probability p = 0.518
```

Gradient:

$$
g=0.518-0=0.518
$$

Hessian:

$$
h=0.518(1-0.518)
$$

$$
h\approx0.250
$$

For:

```text
Actual y = 1
New probability p = 0.712
```

Gradient:

$$
g=0.712-1=-0.288
$$

The next tree uses the new gradients and Hessians.

---

# 26. Stage 2 and Further Trees

The second tree uses the updated model.

The general process is:

```text
Current model
      |
      v
Current probabilities
      |
      v
Calculate gradients
      |
      v
Calculate Hessians
      |
      v
Try candidate splits
      |
      v
Calculate Gain
      |
      v
Choose best valid split
      |
      v
Calculate leaf weights
      |
      v
Apply learning rate
      |
      v
Update model margin
```

Then the same process continues:

```text
Tree 3
Tree 4
Tree 5
...
```

Each tree adds another correction.

---

# 27. Final Prediction Formula

After `n` trees:

$$
F(x)
=
F_0(x)
+
\eta T_1(x)
+
\eta T_2(x)
+
\cdots
+
\eta T_n(x)
$$

where:

- `F_0(x)` = initial margin
- `T_1(x), T_2(x), ...` = tree leaf contributions
- `eta` = learning rate

The final probability is:

$$
\boxed{
p(x)=\frac{1}{1+e^{-F(x)}}
}
$$

This is the predicted probability of class 1.

---

# 28. Classification Threshold

Now we reach another meaning of **threshold**.

Suppose the final XGBoost model produces:

$$
p=0.72
$$

We need a rule to convert this probability into a class.

The common default threshold is:

$$
\boxed{0.5}
$$

The rule is:

```text
p >= 0.5 -> Class 1
p <  0.5 -> Class 0
```

Therefore:

```text
Final probability = 0.72
             |
             v
       0.72 >= 0.50
             |
             v
          Class 1
```

For:

```text
Final probability = 0.31
```

we get:

```text
0.31 < 0.50
     |
     v
Class 0
```

---

# 29. Tree Split Threshold vs Classification Threshold

This distinction is extremely important.

There are two different thresholds.

## A. Tree Split Threshold

Example:

```text
CGPA < 7.62
```

Purpose:

```text
Divide the training samples into child nodes.
```

It is selected by evaluating candidate feature splits and their gains.

```text
5.97
6.67
7.62
8.87
  |
  v
Calculate Gain
  |
  v
Best valid split
  |
  v
7.62
```

## B. Classification Threshold

Example:

```text
Probability >= 0.5
```

Purpose:

```text
Convert final probability into a class.
```

```text
Final probability
       |
       v
Compare with 0.5
       |
   +---+---+
   |       |
 >= 0.5   < 0.5
   |       |
   v       v
Class 1  Class 0
```

These thresholds happen at different stages and have different purposes.

---

# 30. Can the Classification Threshold Be Changed?

Yes.

The default threshold of `0.5` is a common choice, but it is not a mathematical requirement.

For example, suppose the model outputs:

```text
0.35
```

With threshold `0.50`:

```text
0.35 < 0.50
-> Class 0
```

With threshold `0.30`:

```text
0.35 >= 0.30
-> Class 1
```

Changing the classification threshold changes the final class decision.

It does **not** retrain the XGBoost trees.

The appropriate threshold depends on the application and the relative importance of false positives and false negatives.

Common threshold-selection approaches include:

- Precision-recall analysis
- ROC analysis
- F1-score optimization
- Cost-sensitive decision rules
- Domain-specific requirements

For example, if detecting a rare but important positive case is more important than minimizing false positives, a lower threshold may be considered.

The threshold should be selected using appropriate validation data rather than tuning it on the test set.

---

# 31. Regression vs Classification

| Concept | Regression | Binary Classification |
|---|---|---|
| Target | Continuous value | 0 or 1 |
| Internal prediction | Real-valued | Real-valued margin |
| Probability | Not required | Obtained using sigmoid |
| Gradient | Depends on objective | `p - y` for logistic loss |
| Hessian | Depends on objective | `p(1-p)` for logistic loss |
| Tree output | Objective-dependent leaf weight | Margin correction |
| Split selection | Objective-based | Gradient/Hessian-based |
| Final output | Numeric prediction | Probability, then class if thresholded |

---

# 32. Complete XGBoost Training Pipeline

The complete process can be visualized as:

```text
                       DATASET
                          |
                          v
                 Initial probability
                          |
                          v
                   Initial margin
                    / log-odds
                          |
                          v
                 Current probability
                          |
                          v
                Calculate gradients
                          |
                          v
                 Calculate Hessians
                          |
                          v
                 Build decision tree
                          |
                          v
             Generate candidate splits
                          |
                          v
                  Calculate Gain
                          |
                          v
               Choose best valid split
                          |
                          v
                Calculate leaf weights
                          |
                          v
                 Apply learning rate
                          |
                          v
                  Update model margin
                          |
                          v
              Convert margin to probability
                          |
                          v
              Calculate new gradients
                 and Hessians
                          |
                          v
                    Next tree
                          |
                          v
                       Repeat
                          |
                          v
                   Final margin
                          |
                          v
                       Sigmoid
                          |
                          v
                 Final probability
                          |
                          v
             Classification threshold
                    (default 0.5)
                          |
                          v
                 Predicted class
```

---

# 33. Important Formulas

## 33.1 Odds

$$
Odds=\frac{p}{1-p}
$$

## 33.2 Log-Odds

$$
F=\log\left(\frac{p}{1-p}\right)
$$

## 33.3 Sigmoid

$$
p=\frac{1}{1+e^{-F}}
$$

## 33.4 Gradient

For binary logistic loss:

$$
\boxed{g_i=p_i-y_i}
$$

## 33.5 Hessian

$$
\boxed{h_i=p_i(1-p_i)}
$$

## 33.6 Gradient Sum

$$
G_j=\sum_{i\in j}g_i
$$

## 33.7 Hessian Sum

$$
H_j=\sum_{i\in j}h_i
$$

## 33.8 Node Score

A common regularized statistic is:

$$
Score_j=
\frac{G_j^2}{H_j+\lambda}
$$

## 33.9 Split Gain

A common XGBoost formulation is:

$$
\boxed{
Gain=
\frac{1}{2}
\left(
\frac{G_L^2}{H_L+\lambda}
+
\frac{G_R^2}{H_R+\lambda}
-
\frac{G_P^2}{H_P+\lambda}
\right)
-\gamma
}
$$

## 33.10 Leaf Weight

$$
\boxed{
w_j=-\frac{G_j}{H_j+\lambda}
}
$$

## 33.11 Model Update

$$
\boxed{
F_{new}(x)=F_{old}(x)+\eta T(x)
}
$$

## 33.12 Final Margin

$$
\boxed{
F(x)=F_0(x)+\eta T_1(x)+\eta T_2(x)+\cdots+\eta T_n(x)
}
$$

## 33.13 Final Probability

$$
\boxed{
p(x)=\frac{1}{1+e^{-F(x)}}
}
$$

## 33.14 Classification Rule

Using the default threshold:

$$
\boxed{
p\ge0.5\rightarrow Class\ 1
}
$$

and:

$$
\boxed{
p<0.5\rightarrow Class\ 0
}
$$

---

# 34. Important Corrections and Clarifications

## 34.1 `y - p` Is an Intuitive Residual

It is common to explain binary boosting using:

$$
y-p
$$

as a correction signal.

But the actual gradient for XGBoost's logistic objective is:

$$
p-y
$$

Therefore:

$$
g=-(y-p)
$$

Both ideas can appear in explanations, but they should not be treated as the same quantity.

---

## 34.2 XGBoost Uses Gradient and Hessian

Actual XGBoost tree construction uses:

```text
Gradient
+
Hessian
```

This is why XGBoost is commonly described as using **second-order gradient boosting**.

---

## 34.3 Leaf Output Is a Margin Correction

A leaf weight such as:

```text
-1.11
```

does not mean:

```text
Probability = -1.11
```

It is a correction to the model's internal margin.

After applying the learning rate, the margin is updated and then passed through the sigmoid.

---

## 34.4 The Classification Threshold Is Separate

The tree can learn a split such as:

```text
CGPA < 7.62
```

and the final prediction can use:

```text
Probability >= 0.5
```

These are completely different thresholds.

---

## 34.5 Residuals Do Not Have to Become Exactly Zero

XGBoost does not normally train until every residual is exactly zero.

Training can stop based on:

- Number of boosting rounds
- Maximum tree depth
- Minimum loss reduction
- Regularization
- Learning rate
- Early stopping
- Validation performance

The goal is to minimize the objective while maintaining good generalization.

---

## 34.6 Candidate Thresholds in Real XGBoost

The midpoint calculation in this chapter is a simple way to understand tree splitting.

Real XGBoost can use more sophisticated methods for finding candidate split points, including quantile-based approaches and histogram-based algorithms, especially for large datasets.

---

# 35. Interview Questions

## Q1. What is XGBoost?

XGBoost is an optimized gradient boosting algorithm that builds decision trees sequentially, with each new tree improving the current model.

## Q2. What does XGBoost predict internally for binary classification?

It maintains a real-valued model margin. The margin is converted to a probability using the sigmoid function.

## Q3. Why use log-odds?

Probability is restricted to `(0, 1)`, while the log-odds can take any real value:

$$
(-\infty,+\infty)
$$

This makes additive tree updates convenient.

## Q4. What is the sigmoid function?

The sigmoid converts a real-valued margin into a number between 0 and 1:

$$
p=\frac{1}{1+e^{-F(x)}}
$$

## Q5. What is the gradient for logistic classification?

For XGBoost's logistic objective:

$$
g=p-y
$$

## Q6. What is the Hessian?

For logistic classification:

$$
h=p(1-p)
$$

It is the second derivative of the loss with respect to the model margin.

## Q7. How does XGBoost choose the best split?

It:

1. Generates candidate feature splits.
2. Calculates gradient and Hessian statistics.
3. Calculates gain for each candidate.
4. Selects the best valid split according to the objective and constraints.

## Q8. How are candidate thresholds generated in a simple example?

For sorted continuous values:

```text
5.70
6.25
7.10
8.15
9.60
```

midpoints give:

```text
5.97
6.67
7.62
8.87
```

## Q9. How is the best threshold selected?

Calculate gain for every candidate.

For example:

```text
Threshold   Simplified Gain
5.97        1.875
6.67        0.139
7.62        2.222
8.87        0.708
```

The largest gain is associated with:

```text
7.62
```

Therefore, in this simplified example:

```text
Best split = CGPA < 7.62
```

## Q10. What is a leaf weight?

A common regularized leaf-weight formula is:

$$
w_j=-\frac{G_j}{H_j+\lambda}
$$

It represents a correction to the current model margin.

## Q11. Why use a learning rate?

The learning rate controls how much of each tree's correction is added to the model:

$$
F_{new}=F_{old}+\eta T(x)
$$

## Q12. What is the final probability?

After all trees:

$$
p=\frac{1}{1+e^{-F(x)}}
$$

## Q13. What is the default classification threshold?

For a standard binary probability-to-class decision, the common default is:

```text
0.5
```

Therefore:

```text
p >= 0.5 -> Class 1
p <  0.5 -> Class 0
```

## Q14. Is the classification threshold always 0.5?

No.

It can be changed based on the application, evaluation metric, and relative costs of false positives and false negatives.

## Q15. Is `7.62` the same type of threshold as `0.5`?

No.

```text
7.62 -> tree split threshold

0.50 -> final classification threshold
```

The first divides training samples inside a tree. The second converts the final probability into a class.

---

# 36. Final Intuition

The entire process can be remembered like this:

```text
                         DATA
                           |
                           v
                  Initial probability
                           |
                           v
                    Initial margin
                           |
                           v
                 Gradient + Hessian
                           |
                           v
                  Try feature splits
                           |
                           v
                    Calculate Gain
                           |
                           v
                  Choose best split
                           |
                           v
                 Calculate leaf weight
                           |
                           v
                  Apply learning rate
                           |
                           v
                   Update margin
                           |
                           v
                      Sigmoid
                           |
                           v
                 New probability
                           |
                           v
              New gradient + Hessian
                           |
                           v
                      Next tree
                           |
                           v
                        Repeat
                           |
                           v
                   Final probability
                           |
                           v
               Compare with 0.5
                           |
                           v
                    Class 0 or 1
```

## The Three Most Important Ideas

### 1. Model margin

XGBoost builds an additive model:

$$
F(x)=F_0(x)+\eta T_1(x)+\eta T_2(x)+\cdots
$$

### 2. Tree split threshold

Example:

$$
\boxed{CGPA<7.62}
$$

It is selected by comparing candidate splits using gain.

### 3. Classification threshold

Example:

$$
\boxed{P\ge0.5}
$$

It converts the final probability into a class.

Therefore:

```text
7.62 -> decides WHERE THE TREE SPLITS THE DATA

0.50 -> decides HOW THE FINAL PROBABILITY BECOMES A CLASS
```

That distinction is essential for understanding binary classification with XGBoost.
