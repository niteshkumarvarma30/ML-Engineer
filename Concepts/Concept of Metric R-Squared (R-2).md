# R² Score (Coefficient of Determination) - Complete Intuition

> One of the most misunderstood concepts in Machine Learning.

---

# What is R² Score?

R² (R-Squared) measures **how well a regression model explains the variation in the target variable.**

It tells us

> **How much of the variation (spread) in the target variable is explained by the regression model.**

It **does NOT** measure:

- Model accuracy (like classification accuracy)
- Individual feature importance
- Percentage contribution of each feature

Instead, it measures **how well the entire regression model explains the changes in the target variable.**

---

# Step 1 : What is Variation?

Variation simply means

> **How much the target values change or differ from one another.**

Example 1

| Student | Marks |
|---------|------:|
| A | 80 |
| B | 81 |
| C | 79 |
| D | 80 |
| E | 82 |

Here,

all marks are almost the same.

Variation is **Low**.

---

Example 2

| Student | Marks |
|---------|------:|
| A | 20 |
| B | 40 |
| C | 60 |
| D | 80 |
| E | 100 |

Here,

marks are spread over a large range.

Variation is **High**.

---

## Visual Intuition

### Low Variation

```
80 81 79 80 82
```

All values are close.

---

### High Variation

```
20      40      60      80      100
```

Values are spread out.

---

# Step 2 : Why Do We Need R²?

Suppose we want to predict student marks.

Features

```
Study Hours
Attendance
Assignments
```

Target

```
Marks
```

Question

Can our model explain **why** some students score 20 while others score 100?

That is exactly what R² measures.

---

# Step 3 : Perfect Model

Actual Marks

```
20
40
60
80
100
```

Predicted Marks

```
20
40
60
80
100
```

Perfect prediction.

The model explains **all** the variation.

Therefore

```
R² = 1
```

Meaning

> The model explains **100% of the variation** in the target variable.

---

# Step 4 : Bad Model

Actual Marks

```
20
40
60
80
100
```

Predicted Marks

```
55
55
55
55
55
```

The model predicts the same value for everyone.

It cannot explain why one student scored 20 and another scored 100.

Therefore

```
R² ≈ 0
```

Meaning

The model explains **almost none** of the variation.

---

# What Does "Explaining Variation" Mean?

Actual Marks

```
20

40

60

80

100
```

Good Model

```
22

39

61

79

98
```

Notice

The model follows the same increasing pattern.

It understands

why marks change.

Therefore

High R².

---

Bad Model

```
55

55

55

55

55
```

The model completely ignores the pattern.

Therefore

Low R².

---

# Intuition

Imagine the actual data forms a mountain.

```
Actual

100        *

80      *

60    *

40  *

20*
```

Good Model

```
Prediction

98        *

79      *

61    *

39  *

22*
```

It follows the mountain.

---

Bad Model

```
60 *********************
```

It ignores the mountain.

---

# What Does R² Actually Measure?

R² answers

> **How well did my regression model capture the pattern (variation) in the target variable?**

Not

> How accurate is my model?

---

# Relationship Between Variation and R²

Suppose

Total Variation

```
100 units
```

Your model explains

```
85 units
```

Remaining unexplained

```
15 units
```

Then

```
R²

=

85 / 100

=

0.85
```

Meaning

The model explains

**85% of the variation**.

---

# Mathematical Formula

The official formula is

```
R²

=

1 − SSE / SST
```

where

### SST (Total Sum of Squares)

```
SST

=

Σ(yi − ȳ)²
```

Measures

> Total variation present in the target variable.

---

### SSE (Sum of Squared Errors)

```
SSE

=

Σ(yi − ŷi)²
```

Measures

> Variation that the model failed to explain.

---

Therefore

```
Explained Variation

=

SST − SSE
```

Hence

```
R²

=

(SST − SSE)

/

SST
```

or

```
R²

=

Explained Variation

/

Total Variation
```

This is the easiest way to understand R².

---

# Example

Suppose

```
Total Variation

=

100
```

Model explains

```
90
```

Unexplained

```
10
```

Then

```
R²

=

90/100

=

0.90
```

Meaning

The model explains **90% of the variation**.

---

# Does R² Measure Feature Contribution?

No.

Suppose features are

```
Area

Bedrooms

Age

Location
```

Suppose

```
R² = 0.90
```

This does **NOT** mean

```
Area contributes 40%

Bedrooms contribute 20%

Age contributes 15%

Location contributes 15%
```

Wrong.

R² only evaluates the **entire model**.

It cannot tell which feature contributed the most.

---

# Then How Do We Measure Feature Importance?

Different models use different techniques.

Examples

- Linear Regression → Coefficients
- Decision Tree → Feature Importance
- Random Forest → Feature Importance
- XGBoost → Gain / Cover / Weight
- SHAP Values
- Permutation Importance

---

# R² Interpretation

| R² Score | Meaning |
|----------|---------|
| 1.0 | Perfect prediction |
| 0.95 | Excellent model |
| 0.80 | Good model |
| 0.60 | Moderate model |
| 0.30 | Weak model |
| 0 | No better than predicting the average |
| < 0 | Worse than predicting the average |

---

# Why Does R² = 0 Mean Predicting the Average?

Suppose actual marks are

```
20

40

60

80

100
```

Average

```
60
```

If we know nothing,

the safest prediction is

```
60

60

60

60

60
```

This prediction does not explain

why marks differ.

It simply predicts the average.

Therefore

```
R² ≈ 0
```

---

# Real-Life Analogy

Imagine you are a detective.

There are 100 clues.

A good detective explains

95 clues.

```
R² = 0.95
```

A poor detective explains

almost nothing.

```
R² = 0
```

The clues already exist.

The detective only explains them.

Similarly

The variation already exists in the data.

The regression model tries to explain it.

---

# Summary

Variation means

> How much the target values differ from one another.

R² means

> How much of that variation is successfully explained by the regression model.

Mathematically

```
R²

=

Explained Variation

/

Total Variation
```

or

```
R²

=

1 − SSE/SST
```

---

# Key Takeaways

- R² is used only for **Regression**.
- It measures **how well the model explains the variation** in the target variable.
- It is **not** classification accuracy.
- It does **not** measure feature importance.
- Higher R² generally indicates a better fit (though it should be interpreted alongside metrics like RMSE and MAE).
- R² = 0 means the model performs no better than predicting the average target value.
- R² < 0 means the model performs worse than simply predicting the average.

---

# One-Line Interview Answer

> **R² Score (Coefficient of Determination) measures the proportion of the total variation in the target variable that is explained by the regression model.**
