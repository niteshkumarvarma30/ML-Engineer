# DBSCAN - Complete Notes

# Chapter 1 : Introduction to DBSCAN

# Table of Contents

1. What is Clustering?
2. What is DBSCAN?
3. Why was DBSCAN Developed?
4. Problems with K-Means
5. Problems with Hierarchical Clustering
6. Why Density Matters
7. Overview of DBSCAN
8. Key Takeaways

---

# 1. What is Clustering?

Clustering is an **Unsupervised Machine Learning** technique.

Unlike supervised learning, clustering does not have target labels.

Instead, the algorithm tries to find **natural groups** present in the dataset.

Example

Suppose we have customer purchase data.

```
Customer A

Customer B

Customer C

Customer D

Customer E
```

Without knowing anything about them,

the algorithm may discover

```
Cluster 1

High Spending Customers

Cluster 2

Medium Spending Customers

Cluster 3

Low Spending Customers
```

Notice

No labels were provided.

The algorithm discovered these groups automatically.

---

# Why Do We Need Clustering?

Clustering helps us

- Discover hidden patterns
- Understand customer behavior
- Detect fraud
- Compress data
- Organize documents
- Segment images
- Analyze biological data

---

# 2. What is DBSCAN?

DBSCAN is one of the most popular clustering algorithms.

DBSCAN stands for

**Density-Based Spatial Clustering of Applications with Noise**

Unlike K-Means,

DBSCAN does **not** search for centroids.

Unlike Hierarchical Clustering,

DBSCAN does **not** build a tree.

Instead,

DBSCAN searches for **dense regions** in the dataset.

---

# Main Idea

Suppose we have

```
● ● ● ● ●

● ● ● ●

● ● ●


                  ▲ ▲ ▲ ▲

                  ▲ ▲ ▲


                             X
```

DBSCAN sees

```
Cluster 1

● ● ● ●

Cluster 2

▲ ▲ ▲ ▲

Noise

X
```

Notice

The isolated point

```
X
```

is **not forced into any cluster**.

It is labeled as **Noise**.

This is one of DBSCAN's biggest advantages.

---

# 3. Why was DBSCAN Developed?

Earlier clustering algorithms had several limitations.

Researchers noticed that

many real-world datasets

contain

- Outliers
- Noise
- Arbitrary shaped clusters

Unfortunately,

traditional clustering algorithms struggled with these situations.

DBSCAN was proposed in 1996 by

Martin Ester,
Hans-Peter Kriegel,
Jörg Sander,
and Xiaowei Xu

to overcome these problems.

---

# 4. Problems with K-Means

Suppose we have

```
*************

● ● ● ● ●

● ● ● ●


                     ▲ ▲ ▲ ▲

                     ▲ ▲ ▲


                             X
```

K-Means asks

> "Where should I place K centroids?"

Every point must belong to a cluster.

Even

```
X
```

must be assigned somewhere.

But

```
X
```

is clearly an outlier.

K-Means cannot ignore it.

---

## Problem 1

Must specify

```
K
```

before training.

Sometimes

we don't know

how many clusters exist.

---

## Problem 2

Sensitive to Outliers

One extreme point

can shift the centroid.

---

## Problem 3

Assumes Circular Clusters

Suppose

```
**************

(long curved shape)
```

K-Means tries to divide it into circles.

Poor result.

---

# 5. Problems with Hierarchical Clustering

Hierarchical Clustering solves

the "unknown K"

problem.

However,

it has its own limitations.

---

## Problem 1

Expensive

Time complexity

approximately

```
O(n²)

or

O(n³)
```

depending on implementation.

---

## Problem 2

Sensitive to Noise

One noisy point

may influence

the dendrogram.

---

## Problem 3

Cannot Undo Mistakes

Once two clusters merge,

they can never separate again.

Wrong merge

↓

Wrong final clusters.

---

# 6. Why Density Matters

Suppose

```
🙂🙂🙂🙂🙂🙂🙂🙂

🙂🙂🙂🙂🙂🙂🙂🙂
```

Many people

living close together.

This area has

High Density.

---

Another area

```
🙂



          🙂

                     🙂
```

People

far apart.

This area has

Low Density.

---

DBSCAN thinks exactly like this.

Instead of asking

> "Which centroid is nearest?"

it asks

> "Where are many points packed closely together?"

---

# 7. Overview of DBSCAN

DBSCAN works using only two parameters.

```
ε (Epsilon)

↓

Search Radius
```

and

```
MinPts

↓

Minimum Required Neighbors
```

Workflow

```
Dataset
      │
      ▼
Choose ε
Choose MinPts
      │
      ▼
Draw Circle Around Every Point
      │
      ▼
Count Neighbors
      │
      ▼
Enough Neighbors?
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Core      Not Core
 │
 ▼
Expand Cluster
 │
 ▼
Visit Neighbors
 │
 ▼
Repeat
 │
 ▼
Final Clusters
```

---

# 8. Key Takeaways

- DBSCAN is an Unsupervised Learning Algorithm.
- It groups points based on **density**.
- It can automatically detect **noise**.
- It does **not require K**.
- It can discover clusters of arbitrary shapes.
- It is widely used for anomaly detection and spatial data analysis.

---

# Chapter 2 : Understanding the Name "DBSCAN"

Many students memorize the full form without understanding what each word means.

Let's understand every word.

---

# DBSCAN

```
Density

Based

Spatial

Clustering

of

Applications

with

Noise
```

Every word has a purpose.

---

# 1. Density

Density simply means

> How closely packed are the points?

Example

High Density

```
● ● ● ● ●

● ● ● ●

● ● ●
```

Many points

inside a small area.

---

Low Density

```
●



          ●



                   ●
```

Few points

inside a large area.

---

DBSCAN searches for

High Density Regions.

These become clusters.

---

## Intuition

Imagine entering a shopping mall.

You immediately notice

where most people are standing.

That crowd

is a dense region.

DBSCAN thinks exactly the same way.

---

# 2. Based

The word

"Based"

means

the algorithm makes decisions

using

Density.

It does **not** use

- Centroids
- Means
- Decision Trees
- Linear Equations

Everything depends on

Density.

---

# 3. Spatial

Spatial means

the data exists

inside a geometric space.

Example

```
(2,3)

(5,6)

(10,8)
```

These are points

inside a 2D coordinate system.

DBSCAN measures

distance

between these points.

Usually

Euclidean Distance.

---

# 4. Clustering

Once dense regions

are discovered,

DBSCAN groups them.

Example

```
● ● ● ●

● ● ●
```

↓

Cluster 1

---

```
▲ ▲ ▲

▲ ▲
```

↓

Cluster 2

---

# 5. Applications

The creators wanted

an algorithm

that could solve

many real-world problems.

Examples

Customer Segmentation

Image Segmentation

GPS Analysis

Medical Imaging

Fraud Detection

Astronomy

Biology

Social Networks

---

# 6. Noise

This is the most unique feature.

Suppose

```
● ● ● ●

● ● ●


                     X
```

K-Means

forces

```
X
```

into a cluster.

DBSCAN says

"No."

```
X
```

does not belong

to any cluster.

It becomes

Noise.

---

# Real-Life Analogy

Imagine a classroom.

```
🙂🙂🙂🙂🙂

🙂🙂🙂🙂
```

One student

sits alone

in another room.

```
🙂
```

Would you call

that student

part of the class discussion?

Probably not.

DBSCAN thinks exactly this way.

---

# Complete Meaning

Read the name again.

**Density-Based Spatial Clustering of Applications with Noise**

Meaning

> Find groups of densely packed points in space while leaving isolated points as Noise.

---

# DBSCAN vs K-Means Thinking

K-Means asks

> Where should I place K centroids?

Hierarchical Clustering asks

> Which clusters should I merge?

DBSCAN asks

> Where are dense regions of points?

This single question

is the foundation of the entire algorithm.

---

# Summary

DBSCAN stands for

**Density-Based Spatial Clustering of Applications with Noise.**

Meaning of each word

| Word | Meaning |
|------|---------|
| Density | Closely packed points |
| Based | Decisions are based on density |
| Spatial | Points exist in geometric space |
| Clustering | Group similar dense points |
| Applications | Useful in many domains |
| Noise | Isolated points remain unclustered |

---

# What's Next?

In **Chapter 3**, we'll study the two most important parameters in DBSCAN:

- ε (Epsilon)
- MinPts

These two values control **everything** the algorithm does.
