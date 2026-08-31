# PCA Scree Plot --- Complete Learning Notes

## Table of Contents

1.  What is PCA?
2.  Why Do We Need Principal Components?
3.  What Is a Principal Component?
4.  Eigenvalues in PCA
5.  Relationship Between Components and Eigenvalues
6.  Example With 5 Features
7.  Total Eigenvalues vs Sum of Eigenvalues
8.  Explained Variance
9.  Explained Variance Ratio
10. Cumulative Explained Variance
11. What Is a Scree Plot?
12. What Does the X-Axis Represent?
13. What Does the Y-Axis Represent?
14. Why Does the Scree Plot Decrease?
15. What Is the Elbow / Point of Inflection?
16. How to Identify the Elbow
17. Interpreting the Given Scree Plot
18. Why the First Components Matter Most
19. Scree Plot and Dimensionality Reduction
20. Choosing the Number of Components
21. Scree Plot vs Kaiser Criterion
22. Scree Plot vs K-Means Elbow Method
23. Example: Selecting 2 Components
24. Example: Selecting 4 Components
25. Important Distinction: Calculated vs Retained Components
26. PCA in scikit-learn
27. Complete PCA Workflow
28. Common Confusions
29. Quick Revision Notes
30. Final Mental Model

------------------------------------------------------------------------

# 1. What is PCA?

PCA stands for **Principal Component Analysis**.

It is a dimensionality-reduction technique.

The main idea is:

> Transform the original features into a smaller set of new features
> called Principal Components while preserving as much important
> variance as possible.

Suppose the original dataset has:

``` text
Feature 1
Feature 2
Feature 3
Feature 4
Feature 5
```

PCA transforms them into:

``` text
PC1
PC2
PC3
PC4
PC5
```

The principal components are new directions in the data.

------------------------------------------------------------------------

# 2. Why Do We Need Principal Components?

Suppose we have many original features:

``` text
Age
Income
Spending
Education
Experience
...
```

Some features may contain overlapping information.

PCA tries to represent the important information using fewer dimensions.

For example:

``` text
10 Original Features
        ↓
       PCA
        ↓
10 Principal Components
        ↓
Keep only first 3
        ↓
3-dimensional representation
```

The goal is not simply to remove features randomly.

Instead, PCA creates **new combinations of the original features**.

------------------------------------------------------------------------

# 3. What Is a Principal Component?

A Principal Component is a new axis/direction created by PCA.

The components are ordered by the amount of variance they capture.

Generally:

``` text
PC1 → Maximum variance
PC2 → Second highest variance
PC3 → Third highest variance
PC4 → Fourth highest variance
...
```

PC2 is also constrained to be orthogonal to PC1.

Similarly, later components are orthogonal to the previous components.

Conceptually:

``` text
Original Features
       ↓
      PCA
       ↓
PC1 → most variance
PC2 → next most variance
PC3 → next
...
```

------------------------------------------------------------------------

# 4. Eigenvalues in PCA

Each principal component has a corresponding **eigenvalue**.

The eigenvalue tells us how much variance is associated with that
principal component.

For example:

``` text
PC1 → Eigenvalue = 4.2
PC2 → Eigenvalue = 2.1
PC3 → Eigenvalue = 0.8
```

PC1 captures more variance than PC2.

PC2 captures more variance than PC3.

Therefore:

``` text
Higher Eigenvalue
       ↓
More variance captured
       ↓
More important component
```

------------------------------------------------------------------------

# 5. Relationship Between Components and Eigenvalues

There is a one-to-one relationship:

``` text
PC1 ↔ λ1
PC2 ↔ λ2
PC3 ↔ λ3
PC4 ↔ λ4
PC5 ↔ λ5
```

Here:

``` text
λ = Eigenvalue
```

Therefore:

``` text
5 PCA Components
       ↓
5 Corresponding Eigenvalues
```

If PCA produces 5 components:

``` text
PC1 → λ1
PC2 → λ2
PC3 → λ3
PC4 → λ4
PC5 → λ5
```

------------------------------------------------------------------------

# 6. Example With 5 Features

Suppose we start with 5 original features:

``` text
F1
F2
F3
F4
F5
```

PCA can produce up to 5 principal components:

``` text
Original Features
       ↓
      PCA
       ↓
 ┌─────┬─────┬─────┬─────┬─────┐
 PC1   PC2   PC3   PC4   PC5
  ↓     ↓     ↓     ↓     ↓
 λ1    λ2    λ3    λ4    λ5
```

Example eigenvalues:

  Component     Eigenvalue
  ----------- ------------
  PC1                  4.2
  PC2                  2.1
  PC3                  0.8
  PC4                  0.5
  PC5                  0.4

So:

``` text
Number of Components = 5
Number of Eigenvalues = 5
```

------------------------------------------------------------------------

# 7. Total Eigenvalues vs Sum of Eigenvalues

Be careful with terminology.

Suppose:

``` text
λ1 = 4.2
λ2 = 2.1
λ3 = 0.8
λ4 = 0.5
λ5 = 0.4
```

There are:

``` text
5 eigenvalues
```

The **sum** of the eigenvalues is:

``` text
4.2 + 2.1 + 0.8 + 0.5 + 0.4
= 8.0
```

So:

``` text
Number of eigenvalues = 5

Sum of eigenvalues = 8.0
```

These are different concepts.

The sum of eigenvalues corresponds to the total variance represented by
the covariance structure used in PCA.

Therefore:

``` text
Number of Eigenvalues
        ≠
Sum of Eigenvalues
```

------------------------------------------------------------------------

# 8. Explained Variance

An eigenvalue tells us the amount of variance captured by its component.

For example:

``` text
PC1 → Eigenvalue = 4.2
```

means PC1 captures more variance than:

``` text
PC2 → Eigenvalue = 2.1
```

If the total variance is represented by the sum:

``` text
Total = 8.0
```

then PC1 captures:

``` text
4.2
```

units of variance.

------------------------------------------------------------------------

# 9. Explained Variance Ratio

The **explained variance ratio** tells us the percentage/proportion of
total variance captured by a component.

Formula:

``` text
Explained Variance Ratio
=
Eigenvalue of Component
────────────────────────
Sum of All Eigenvalues
```

For PC1:

``` text
PC1 = 4.2
Total = 8.0
```

Therefore:

``` text
4.2 / 8.0
= 0.525
= 52.5%
```

So:

``` text
PC1 explains 52.5% of the variance.
```

For PC2:

``` text
2.1 / 8.0
= 0.2625
= 26.25%
```

Therefore:

``` text
PC2 explains 26.25%.
```

------------------------------------------------------------------------

# 10. Cumulative Explained Variance

Cumulative explained variance tells us how much variance is retained
when multiple components are combined.

Using:

``` text
PC1 = 52.5%
PC2 = 26.25%
PC3 = 10%
PC4 = 6.25%
PC5 = 5%
```

We get:

  Components Retained       Cumulative Variance
  ----------------------- ---------------------
  PC1                                    52.50%
  PC1 + PC2                              78.75%
  PC1 + PC2 + PC3                        88.75%
  PC1 + PC2 + PC3 + PC4                  95.00%
  All 5                                    100%

Therefore:

``` text
Keep PC1 + PC2
       ↓
Retain 78.75% of variance
```

or:

``` text
Keep PC1–PC4
       ↓
Retain 95% of variance
```

This is one of the main ways PCA is used for dimensionality reduction.

------------------------------------------------------------------------

# 11. What Is a Scree Plot?

A **Scree Plot** is a graph used in PCA to help decide how many
principal components should be retained.

It usually plots:

``` text
X-axis → Component Number
Y-axis → Eigenvalue
```

For example:

``` text
Component  Eigenvalue

PC1        4.2
PC2        2.1
PC3        0.8
PC4        0.5
PC5        0.4
```

The scree plot visualizes how the eigenvalues decrease across
components.

------------------------------------------------------------------------

# 12. What Does the X-Axis Represent?

The X-axis represents:

``` text
Component Number
```

For example:

``` text
1 → PC1
2 → PC2
3 → PC3
4 → PC4
5 → PC5
...
```

The components are ordered from highest eigenvalue to lowest eigenvalue.

Therefore:

``` text
PC1
PC2
PC3
...
```

are arranged according to the amount of variance they capture.

------------------------------------------------------------------------

# 13. What Does the Y-Axis Represent?

The Y-axis represents:

``` text
Eigenvalue
```

The eigenvalue indicates the amount of variance associated with each
principal component.

Therefore:

``` text
High eigenvalue
      ↓
More variance
      ↓
More information captured
```

A low eigenvalue means that the component contributes relatively little
variance.

------------------------------------------------------------------------

# 14. Why Does the Scree Plot Decrease?

PCA orders components from highest variance to lowest variance.

Therefore:

``` text
PC1 ≥ PC2 ≥ PC3 ≥ PC4 ≥ ...
```

in terms of explained variance/eigenvalue.

This creates a generally decreasing curve.

A typical scree plot looks like:

``` text
Eigenvalue
   ↑
   |
   | ●
   |  \
   |   \
   |    ●
   |     \
   |      ●
   |       \
   |        ●
   |         ●
   |          ●
   +----------------→ Component
```

The important question is not:

> "Where does the graph reach zero?"

Instead:

> "Where does the graph stop decreasing sharply and start flattening?"

------------------------------------------------------------------------

# 15. What Is the Elbow / Point of Inflection?

The **elbow** is the point where the curve changes from a steep decline
to a relatively flatter decline.

Conceptually:

``` text
Large decrease
     ↓
     ↓
     ↓
   ELBOW
     ↓
Small decreases
     ↓
     ↓
```

The idea is:

> Components before the elbow provide substantial additional variance,
> while components after the elbow provide relatively small additional
> variance.

Therefore, the elbow can be used as a practical criterion for deciding
how many components to retain.

------------------------------------------------------------------------

# 16. How to Identify the Elbow

Follow these steps.

### Step 1

Look at the first component.

Usually PC1 has a high eigenvalue.

### Step 2

Look for the large drop.

For example:

``` text
PC1 = 6.4
PC2 = 1.6
```

This is a very large decrease.

### Step 3

Check what happens afterward.

If:

``` text
PC2 = 1.6
PC3 = 1.4
PC4 = 1.15
PC5 = 1.0
...
```

the curve is becoming much flatter.

### Step 4

Identify where the transition happens.

That is the approximate elbow.

------------------------------------------------------------------------

# 17. Interpreting the Given Scree Plot

The given scree plot has approximately:

``` text
PC1 → 6.4
PC2 → 1.6
PC3 → 1.4
PC4 → 1.15
PC5 → 1.0
PC6 → 0.8
PC7 → 0.7
...
```

The most dramatic drop is:

``` text
PC1 → PC2
```

After PC2, the curve becomes much flatter.

Conceptually:

``` text
Eigenvalue
   ↑
6.4 ●
    |
    |
    |
    |
1.6 ●
     \
1.4   ●
       \
1.15    ●
          \
1.0        ●
            \
0.8          ●
0.7           ●
               ...
   +----------------→ Component
      1  2  3  4  5
```

Therefore, based on the visual scree/elbow criterion:

``` text
Approximate elbow ≈ PC2
```

So the scree plot suggests that the first **2 components** may capture
the most important structure before the curve starts flattening.

------------------------------------------------------------------------

# 18. Why the First Components Matter Most

Suppose:

``` text
PC1 → 6.4
PC2 → 1.6
PC3 → 1.4
PC4 → 1.15
...
```

PC1 has a very large eigenvalue.

Therefore PC1 captures a large amount of variance.

PC2 also contributes meaningful variance.

After that, the improvements become more gradual.

So:

``` text
PC1 + PC2
```

may provide a strong low-dimensional representation.

This is why the scree plot is useful.

------------------------------------------------------------------------

# 19. Scree Plot and Dimensionality Reduction

Suppose the original dataset has:

``` text
18 Features
```

PCA might produce:

``` text
PC1
PC2
PC3
...
PC18
```

You do not necessarily need all 18.

The scree plot may indicate:

``` text
Elbow ≈ PC2
```

Then you might investigate whether:

``` text
PC1 + PC2
```

provides enough useful variance.

The transformation becomes:

``` text
18 Original Features
        ↓
       PCA
        ↓
18 Principal Components
        ↓
Retain first 2
        ↓
2-Dimensional representation
```

This is dimensionality reduction.

------------------------------------------------------------------------

# 20. Choosing the Number of Components

There are several approaches.

## Method 1 --- Scree Plot

Look for the elbow.

``` text
Sharp decrease
      ↓
Elbow
      ↓
Flattening
```

For your graph:

``` text
Approximate elbow ≈ PC2
```

------------------------------------------------------------------------

## Method 2 --- Explained Variance

Instead of relying only on visual inspection, calculate cumulative
explained variance.

For example:

``` text
PC1 + PC2 → 78.75%
PC1 + PC2 + PC3 → 88.75%
PC1–PC4 → 95%
```

You might choose enough components to reach a desired threshold such as
90% or 95%, depending on the application.

------------------------------------------------------------------------

## Method 3 --- Combine Both

A practical approach is:

``` text
Scree Plot
    +
Cumulative Explained Variance
    ↓
Choose number of components
```

This is often more informative than using only one criterion.

------------------------------------------------------------------------

# 21. Scree Plot vs Kaiser Criterion

These are different methods.

## Scree Plot

Look for:

``` text
Elbow
```

The elbow indicates where additional components begin contributing
relatively little additional variance.

------------------------------------------------------------------------

## Kaiser Criterion

A common rule is:

``` text
Keep components with:

Eigenvalue > 1
```

This criterion is often discussed when PCA is based on standardized
variables/correlation structure.

For your graph, if the eigenvalues are approximately:

``` text
PC1 = 6.4
PC2 = 1.6
PC3 = 1.4
PC4 = 1.15
PC5 = 1.0
PC6 = 0.8
...
```

then the Kaiser rule would suggest retaining roughly the components
whose eigenvalues are above 1.

That can give a different answer from the scree plot.

Therefore:

``` text
Scree Plot
→ Elbow-based decision

Kaiser Criterion
→ Eigenvalue > 1 rule
```

Do not confuse them.

------------------------------------------------------------------------

# 22. Scree Plot vs K-Means Elbow Method

These two graphs can look similar, but they are used for different
purposes.

## PCA Scree Plot

``` text
X-axis → Component Number
Y-axis → Eigenvalue
```

Question:

> How many principal components should I retain?

------------------------------------------------------------------------

## K-Means Elbow Plot

``` text
X-axis → Number of Clusters K
Y-axis → Inertia / WCSS
```

Question:

> How many clusters should I create?

Therefore:

``` text
PCA
↓
Scree Plot
↓
Choose Number of Components


K-Means
↓
Elbow Plot
↓
Choose Number of Clusters
```

They are conceptually related because both look for diminishing returns,
but they are not the same procedure.

------------------------------------------------------------------------

# 23. Example: Selecting 2 Components

Suppose:

``` text
5 Original Features
```

PCA produces:

``` text
PC1 → λ = 4.2
PC2 → λ = 2.1
PC3 → λ = 0.8
PC4 → λ = 0.5
PC5 → λ = 0.4
```

Total:

``` text
8.0
```

Explained variance:

``` text
PC1 = 4.2 / 8.0 = 52.5%

PC2 = 2.1 / 8.0 = 26.25%
```

Cumulative:

``` text
PC1 + PC2
= 78.75%
```

If the scree plot also shows an elbow around PC2, then:

``` text
Keep PC1 and PC2
```

You would reduce:

``` text
5 dimensions
      ↓
2 dimensions
```

while retaining about:

``` text
78.75% variance
```

in this illustrative example.

------------------------------------------------------------------------

# 24. Example: Selecting 4 Components

Suppose the cumulative explained variance is:

``` text
PC1 → 52.5%
PC1 + PC2 → 78.75%
PC1 + PC2 + PC3 → 88.75%
PC1–PC4 → 95%
```

If your application requires approximately 95% variance retention:

``` text
Keep PC1–PC4
```

Then:

``` text
5 Original Features
        ↓
PCA
        ↓
5 PCs
        ↓
Keep 4
        ↓
95% variance retained
```

So the number selected does not have to be determined by the scree plot
alone.

------------------------------------------------------------------------

# 25. Important Distinction: Calculated vs Retained Components

This is a very common source of confusion.

Suppose you have 5 original features.

PCA may produce:

``` text
PC1
PC2
PC3
PC4
PC5
```

Therefore there are:

``` text
5 components
5 eigenvalues
```

But you might decide to retain only:

``` text
PC1
PC2
```

That means:

``` text
Calculated:
PC1 PC2 PC3 PC4 PC5

Retained:
PC1 PC2
```

You are NOT creating new components.

You are selecting the most useful components from the ones already
calculated.

Similarly, you are not creating new eigenvalues.

The corresponding eigenvalues already exist:

``` text
PC1 ↔ λ1
PC2 ↔ λ2
PC3 ↔ λ3
PC4 ↔ λ4
PC5 ↔ λ5
```

------------------------------------------------------------------------

# 26. PCA in scikit-learn

Example:

``` python
from sklearn.decomposition import PCA

pca = PCA()

X_pca = pca.fit_transform(X)
```

The explained variance ratios can be obtained using:

``` python
pca.explained_variance_ratio_
```

For example:

``` python
print(pca.explained_variance_ratio_)
```

Might return:

``` text
[0.525, 0.2625, 0.10, 0.0625, 0.05]
```

The cumulative explained variance can be calculated using:

``` python
import numpy as np

cumulative_variance = np.cumsum(
    pca.explained_variance_ratio_
)

print(cumulative_variance)
```

Output:

``` text
[0.525, 0.7875, 0.8875, 0.95, 1.0]
```

The eigenvalues themselves are available through:

``` python
pca.explained_variance_
```

------------------------------------------------------------------------

# 27. Complete PCA Workflow

``` text
Original Dataset
       ↓
Original Features
       ↓
Standardize Features
       ↓
PCA
       ↓
Calculate Principal Components
       ↓
Calculate Eigenvalues
       ↓
Calculate Explained Variance Ratio
       ↓
Create Scree Plot
       ↓
Look for Elbow
       ↓
Check Cumulative Explained Variance
       ↓
Choose Number of Components
       ↓
Retain Selected PCs
       ↓
Reduced Dataset
```

For example:

``` text
18 Original Features
        ↓
       PCA
        ↓
18 Components
        ↓
18 Eigenvalues
        ↓
Scree Plot
        ↓
Elbow around PC2
        ↓
Check explained variance
        ↓
Retain suitable number of PCs
```

------------------------------------------------------------------------

# 28. Common Confusions

## Confusion 1

### "If I have 5 components, do I have 5 eigenvalues?"

Yes.

``` text
5 Components
↓
5 Corresponding Eigenvalues
```

------------------------------------------------------------------------

## Confusion 2

### "Does 5 eigenvalues mean their sum is 5?"

No.

Example:

``` text
Eigenvalues:

4.2
2.1
0.8
0.5
0.4
```

There are:

``` text
5 eigenvalues
```

but their sum is:

``` text
8.0
```

------------------------------------------------------------------------

## Confusion 3

### "If I retain only 2 components, do I only have 2 eigenvalues?"

Not necessarily.

The PCA calculation may have produced 5 components and 5 eigenvalues.

You are simply retaining:

``` text
PC1
PC2
```

and their corresponding eigenvalues.

------------------------------------------------------------------------

## Confusion 4

### "Does the scree plot show explained variance percentage?"

Not necessarily.

A standard scree plot typically shows:

``` text
Y-axis → Eigenvalue
```

If the graph explicitly uses explained variance ratio, then the Y-axis
would represent that quantity instead.

Always check the axis label.

------------------------------------------------------------------------

## Confusion 5

### "Does the scree plot tell us exactly how many components to use?"

Not always.

It provides a visual criterion.

You should also consider:

``` text
Cumulative explained variance
+
Application requirements
+
Possibly other criteria
```

------------------------------------------------------------------------

## Confusion 6

### "Is Scree Plot the same as K-Means Elbow?"

No.

``` text
PCA Scree Plot
→ Choose components

K-Means Elbow Plot
→ Choose clusters
```

------------------------------------------------------------------------

# 29. Quick Revision Notes

## PCA

``` text
PCA = Principal Component Analysis
```

Used mainly for:

``` text
Dimensionality Reduction
```

------------------------------------------------------------------------

## Principal Component

A new direction/feature created by PCA.

``` text
PC1 → Maximum variance
PC2 → Second highest
PC3 → Third highest
...
```

------------------------------------------------------------------------

## Eigenvalue

Measures the variance associated with a principal component.

``` text
Higher Eigenvalue
→ More variance
→ More important component
```

------------------------------------------------------------------------

## Components and Eigenvalues

``` text
PC1 ↔ λ1
PC2 ↔ λ2
PC3 ↔ λ3
...
```

Therefore:

``` text
N Components
→ N Eigenvalues
```

------------------------------------------------------------------------

## Sum of Eigenvalues

``` text
λ1 + λ2 + λ3 + ... + λn
```

represents the total variance represented by the PCA covariance
structure.

------------------------------------------------------------------------

## Explained Variance Ratio

``` text
Eigenvalue of PC
────────────────────
Sum of Eigenvalues
```

------------------------------------------------------------------------

## Cumulative Explained Variance

``` text
EVR(PC1)
+
EVR(PC2)
+
EVR(PC3)
+ ...
```

Shows how much variance is retained by the first N components.

------------------------------------------------------------------------

## Scree Plot

``` text
X-axis → Component Number
Y-axis → Eigenvalue
```

Used to help determine how many components to retain.

------------------------------------------------------------------------

## Elbow

Look for:

``` text
Sharp decrease
      ↓
Elbow
      ↓
Flattening
```

Your provided plot:

``` text
Approximate elbow ≈ PC2
```

------------------------------------------------------------------------

## Kaiser Criterion

Common rule:

``` text
Eigenvalue > 1
```

Keep those components.

This can produce a different result from the scree-plot elbow.

------------------------------------------------------------------------

# 30. Final Mental Model

The complete concept can be remembered as:

``` text
Original Features
       ↓
      PCA
       ↓
Principal Components
       ↓
Each Component has an Eigenvalue
       ↓
Eigenvalue tells variance captured
       ↓
Calculate Explained Variance Ratio
       ↓
Calculate Cumulative Explained Variance
       ↓
Create Scree Plot
       ↓
Look for Elbow
       ↓
Choose Number of Components
       ↓
Retain Selected Components
       ↓
Reduced-Dimension Dataset
```

## Example

Suppose:

``` text
5 Original Features
```

PCA produces:

``` text
PC1 → λ1 = 4.2
PC2 → λ2 = 2.1
PC3 → λ3 = 0.8
PC4 → λ4 = 0.5
PC5 → λ5 = 0.4
```

Then:

``` text
5 Components
↓
5 Eigenvalues
```

Total:

``` text
4.2 + 2.1 + 0.8 + 0.5 + 0.4
= 8.0
```

Explained variance:

``` text
PC1 = 52.5%
PC2 = 26.25%
PC3 = 10%
PC4 = 6.25%
PC5 = 5%
```

Cumulative:

``` text
PC1              → 52.5%
PC1 + PC2        → 78.75%
PC1 + PC2 + PC3  → 88.75%
PC1–PC4          → 95%
PC1–PC5          → 100%
```

If the scree plot shows an elbow around PC2:

``` text
Elbow ≈ PC2
```

you would investigate whether retaining:

``` text
PC1 + PC2
```

is sufficient for your task.

------------------------------------------------------------------------

# 🔥 Most Important Things to Remember

``` text
1. PCA transforms original features into principal components.

2. Every principal component has a corresponding eigenvalue.

3. If PCA produces 5 components, there are 5 corresponding eigenvalues.

4. Eigenvalue tells how much variance is associated with that component.

5. Higher eigenvalue → more variance captured.

6. Sum of eigenvalues represents total variance under the corresponding PCA formulation.

7. Explained variance ratio tells the percentage of total variance captured.

8. Cumulative explained variance tells how much variance is retained by the first N components.

9. Scree Plot = Component Number vs Eigenvalue.

10. The Scree Plot is used to identify an approximate elbow.

11. The elbow indicates where additional components begin contributing relatively little additional variance.

12. Your provided scree plot has a prominent elbow approximately around PC2.

13. Scree Plot and K-Means Elbow Method are different:
    PCA → choose components
    K-Means → choose clusters

14. Calculating 5 components does not mean you must retain all 5.

15. You may calculate 5 components/eigenvalues and retain only the first 2, 3, or 4 depending on the evidence and task.

16. The Scree Plot is a decision aid, not an absolute mathematical rule.
```

# One-Line Memory Trick

``` text
PCA
↓
Components
↓
Eigenvalues
↓
Variance
↓
Scree Plot
↓
Find Elbow
↓
Choose Components
↓
Reduce Dimensions
```
