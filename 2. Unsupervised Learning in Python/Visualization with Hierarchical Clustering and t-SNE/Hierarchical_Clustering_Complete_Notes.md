# Hierarchical Clustering - Complete Notes

# Table of Contents

1. Introduction
2. Types of Hierarchical Clustering
3. Agglomerative (Bottom-Up) Clustering
4. Step 1 - Dataset
5. Step 2 - Compute Distance Matrix
6. Step 3 - Merge Closest Clusters
7. Why Linkage Methods are Needed
8. Single Linkage
9. Complete Linkage
10. Average Linkage
11. Ward Linkage
12. Dendrogram
13. Divisive (Top-Down) Clustering
14. Agglomerative vs Divisive
15. Hierarchical Clustering vs K-Means
16. Advantages
17. Disadvantages
18. Applications
19. Interview Questions
20. Key Takeaways

---

# 1. Introduction

Hierarchical Clustering is an **Unsupervised Machine Learning Algorithm**.

Its goal is to group similar data points into clusters while building a **tree-like hierarchy**.

Unlike K-Means,

- It does **not require specifying the number of clusters (K)** beforehand.
- It produces a **Dendrogram**, which shows how clusters are formed.

---

# 2. Types of Hierarchical Clustering

There are two approaches.

```
Hierarchical Clustering
          │
   ┌──────┴──────┐
   │             │
Agglomerative   Divisive
(Bottom-Up)     (Top-Down)
```

---

# 3. Agglomerative Clustering (Bottom-Up)

Agglomerative means

> Start with individual data points and keep merging them.

Workflow

```
Every Point
   │
   ▼
One Cluster per Point
   │
   ▼
Merge Closest Clusters
   │
   ▼
Repeat
   │
   ▼
One Big Cluster
```

Think of LEGO blocks.

```
□   □   □   □

↓

□□

↓

□□□□

↓

□□□□□
```

---

# 4. Step 1 - Dataset

Suppose we have

| Point | Value |
|-------|------:|
| A | 1 |
| B | 3 |
| C | 8 |
| D | 10 |

Initially

```
{A}

{B}

{C}

{D}
```

Every point is an individual cluster.

---

# 5. Step 2 - Compute Distance Matrix

We compute Euclidean distance.

For one-dimensional data,

```
Distance = |x - y|
```

Distances

```
A-B = |1-3| = 2

A-C = |1-8| = 7

A-D = |1-10| = 9

B-C = |3-8| = 5

B-D = |3-10| = 7

C-D = |8-10| = 2
```

Distance Matrix

| |A|B|C|D|
|---|---:|---:|---:|---:|
|A|0|2|7|9|
|B|2|0|5|7|
|C|7|5|0|2|
|D|9|7|2|0|

---

# 6. Step 3 - Merge Closest Clusters

Smallest distance

```
A-B = 2
```

Merge

```
{AB}

{C}

{D}
```

Now a new question arises.

How do we compute

```
Distance({AB}, C) ?
```

There are two distances.

```
A-C = 7

B-C = 5
```

Which one should we use?

This is where **Linkage Methods** come in.

---

# 7. Why Linkage Methods are Needed

After merging clusters,

one cluster may contain multiple points.

Example

```
Cluster 1

A
B

Cluster 2

C
```

There are multiple possible distances.

```
A-C

B-C
```

Which one represents the distance between clusters?

Different linkage methods answer this differently.

---

# 8. Single Linkage

## Mathematical Rule

Take the **minimum distance**.

Formula

```
Distance(Cluster1, Cluster2)

=

Minimum of all pairwise distances
```

Example

```
A-C = 7

B-C = 5
```

Minimum

```
5
```

Therefore

```
Distance({AB},C)=5
```

### Intuition

Single Linkage asks

> **"Are any two students from different groups close enough?"**

Only the closest pair matters.

### Advantage

Finds connected groups easily.

### Disadvantage

Produces long chain-like clusters.

(Chaining Effect)

---

# 9. Complete Linkage

## Mathematical Rule

Take the **maximum distance**.

Formula

```
Distance(Cluster1, Cluster2)

=

Maximum of all pairwise distances
```

Example

```
A-C = 7

B-C = 5
```

Maximum

```
7
```

Therefore

```
Distance({AB},C)=7
```

### Intuition

Complete Linkage asks

> **"How far apart are the two farthest students from different groups?"**

Every member should be close before merging.

### Advantage

Produces compact clusters.

### Disadvantage

Sensitive to outliers.

---

# 10. Average Linkage

## Mathematical Rule

Take the average distance.

Formula

```
Distance

=

Sum of all pairwise distances

/

Number of pairs
```

Example

```
A-C = 7

B-C = 5
```

Average

```
(7+5)/2

=

6
```

### Intuition

Average Linkage asks

> **"On average, how far apart are students from the two groups?"**

It balances Single and Complete Linkage.

### Advantage

More stable clustering.

---

# 11. Ward Linkage

Ward Linkage is different.

It does **not directly compare distances**.

Instead,

it asks

> **"If I merge these two clusters, how much will the variance (WCSS) increase?"**

The merge with the **smallest increase in WCSS** is chosen.

---

## WCSS Formula

```
WCSS

=

Σ(Point − Centroid)²
```

---

### Example

Suppose

```
2

3
```

Centroid

```
(2+3)/2

=

2.5
```

WCSS

```
(2−2.5)²

+

(3−2.5)²

=

0.25

+

0.25

=

0.5
```

Now suppose another merge

```
2

10
```

Centroid

```
6
```

WCSS

```
(2−6)²

+

(10−6)²

=

16

+

16

=

32
```

Ward chooses

```
Merge

2

3
```

because

```
0.5

<

32
```

---

### Intuition

Ward Linkage asks

> **"If we combine these two groups, will the new group still stay tightly packed?"**

It always tries to keep clusters compact.

---

# 12. Dendrogram

A dendrogram is a tree showing the sequence of merges.

Example

```
             ABCD
            /    \
         AB        CD
        /  \      /  \
       A    B    C    D
```

Merge heights

```
              5
             / \
           2     2
          / \   / \
         A   B C   D
```

Height represents the distance at which clusters merged.

Cutting the dendrogram at different heights gives different numbers of clusters.

---

## Initial Distance Matrix

| |A|B|C|D|
|---|---:|---:|---:|---:|
|A|0|2|7|9|
|B|2|0|5|7|
|C|7|5|0|2|
|D|9|7|2|0|

## Single Linkage
Rule: Minimum distance.

Updated Matrix after merging A,B:

| |AB|C|D|
|---|---:|---:|---:|
|AB|0|5|7|
|C|5|0|2|
|D|7|2|0|

Final Matrix:

| |AB|CD|
|---|---:|---:|
|AB|0|5|
|CD|5|0|

Intuition: Are any two students from different groups close enough?

## Complete Linkage
Updated Matrix:

| |AB|C|D|
|---|---:|---:|---:|
|AB|0|7|9|
|C|7|0|2|
|D|9|2|0|

Final Matrix:

| |AB|CD|
|---|---:|---:|
|AB|0|9|
|CD|9|0|

Intuition: How far apart are the two farthest students?

## Average Linkage
Updated Matrix:

| |AB|C|D|
|---|---:|---:|---:|
|AB|0|6|8|
|C|6|0|2|
|D|8|2|0|

Final Matrix:

| |AB|CD|
|---|---:|---:|
|AB|0|7|
|CD|7|0|

Intuition: On average, how far apart are students?

## Ward Linkage
Uses increase in WCSS instead of pairwise distance.

| |A|B|C|D|
|---|---:|---:|---:|---:|
|A|-|0.5|32|50|
|B|0.5|-|24.5|40.5|
|C|32|24.5|-|2|
|D|50|40.5|2|-|

Ward merges the pair with the smallest increase in WCSS.


# 13. Divisive Clustering (Top-Down)

Divisive works in the opposite direction.

Workflow

```
One Big Cluster
      │
      ▼
Split
      │
      ▼
Split Again
      │
      ▼
Repeat
      │
      ▼
Individual Points
```

Example

```
ABCDEFG
```

↓

```
ABC

DEFG
```

↓

```
A

BC

DE

FG
```

↓

```
A

B

C

D

E

F

G
```

Think of cutting a large tree into smaller branches.

---

# 14. Agglomerative vs Divisive

| Agglomerative | Divisive |
|---------------|----------|
| Bottom-Up | Top-Down |
| Starts with one point per cluster | Starts with one cluster containing all points |
| Merge clusters | Split clusters |
| Most commonly used | Rarely used |
| Implemented in scikit-learn | Not directly available |

---

# 15. Hierarchical Clustering vs K-Means

| Hierarchical | K-Means |
|--------------|---------|
| No need to specify K initially | Must specify K |
| Produces Dendrogram | Produces final clusters only |
| Computationally expensive | Faster |
| Suitable for small/medium datasets | Suitable for large datasets |
| Highly interpretable | Less interpretable |

---

# 16. Advantages

- No need to choose K initially.
- Produces a dendrogram.
- Easy to interpret.
- Reveals nested cluster relationships.

---

# 17. Disadvantages

- Slow for large datasets.
- Memory intensive.
- Sensitive to noise.
- Agglomerative merges cannot be undone.

---

# 18. Applications

- Customer Segmentation
- Gene Expression Analysis
- Document Clustering
- Image Segmentation
- Social Network Analysis
- Product Recommendation
- Marketing Analytics

---

# 19. Interview Questions

### Q1. What is Hierarchical Clustering?

An unsupervised learning algorithm that builds a hierarchy of clusters.

---

### Q2. What is a Dendrogram?

A tree showing how clusters merge or split.

---

### Q3. Difference between Agglomerative and Divisive?

Agglomerative merges clusters.

Divisive splits clusters.

---

### Q4. Which linkage method is most commonly used?

Ward Linkage.

---

### Q5. Why is Ward Linkage popular?

Because it minimizes the increase in WCSS and produces compact clusters.

---

# 20. Summary of Linkage Methods

## Single Linkage

Question it asks:

> **"Are any two students from different groups close enough?"**

Uses

```
Minimum Distance
```

---

## Complete Linkage

Question it asks:

> **"How far apart are the two farthest students from different groups?"**

Uses

```
Maximum Distance
```

---

## Average Linkage

Question it asks:

> **"On average, how far apart are students from the two groups?"**

Uses

```
Average Distance
```

---

## Ward Linkage

Question it asks:

> **"If we combine these two groups, will the new group still stay tightly packed?"**

Uses

```
Minimum Increase in WCSS (Variance)
```

---

# Complete Workflow

```
Dataset
     │
     ▼
Compute Distance Matrix
     │
     ▼
Choose Linkage Method
(Single / Complete / Average / Ward)
     │
     ▼
Agglomerative
Merge Closest Clusters
OR
Divisive
Split Largest Cluster
     │
     ▼
Update Cluster Structure
     │
     ▼
Repeat
     │
     ▼
Build Dendrogram
     │
     ▼
Cut Dendrogram
     │
     ▼
Final Clusters
```

---

# Final Key Takeaways

- Hierarchical Clustering builds a **tree of clusters** instead of directly producing final clusters.
- **Agglomerative** starts with individual points and merges them (**Bottom-Up**).
- **Divisive** starts with one cluster and repeatedly splits it (**Top-Down**).
- **Single Linkage** uses the **minimum** distance between clusters.
- **Complete Linkage** uses the **maximum** distance.
- **Average Linkage** uses the **average** distance.
- **Ward Linkage** chooses the merge that causes the **smallest increase in WCSS (variance)**.
- The **Dendrogram** helps visualize the entire clustering process and decide the final number of clusters by selecting a cut height.
# Hierarchical Clustering - Complete Notes


