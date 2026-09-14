# Chapter 6: Complete DBSCAN Algorithm — Step-by-Step

In the previous chapters, we learned the fundamental concepts of DBSCAN:

- **Epsilon (`ε`)**
- **MinPts**
- **Core Points**
- **Border Points**
- **Noise Points**
- **ε-Neighborhood**
- **Density-Reachable**
- **Density-Connected**

Now we will see how DBSCAN combines all these concepts to discover clusters.

---

# 1. Problem Statement

Consider the following dataset:

```text
                A

          B     C

      D   E   F

          G   H

                    I

                               J
```

We choose:

```text
ε = 2
MinPts = 4
```

### Goal

Find all the clusters and identify the noise points.

---

# 2. What Does DBSCAN Actually Try to Find?

DBSCAN does **not** try to find a centroid.

It does **not** calculate a mean.

It does **not** require us to specify the number of clusters beforehand.

Instead, DBSCAN asks:

> **Does this point have enough nearby points to be considered part of a dense region?**

The basic decision is:

```text
Enough nearby points?
        |
   +----+----+
   |         |
  Yes        No
   |         |
 Core      Border or Noise
```

A Core Point can expand a cluster.

A Border Point can join a cluster but cannot expand it.

A Noise Point belongs to no cluster.

---

# 3. Important Parameters

DBSCAN uses two main parameters.

## 3.1 Epsilon (`ε`)

`ε` defines how far we look around a point.

For example:

```text
ε = 2
```

means we consider points within distance `2` from the current point.

The set of points within this distance is called the **ε-neighborhood**.

---

## 3.2 MinPts

`MinPts` defines the minimum density required for a point to be considered a Core Point.

For example:

```text
MinPts = 4
```

means the point must have enough points inside its ε-neighborhood according to the MinPts convention being used.

> **Important:** Different explanations and implementations can count the point itself differently when defining MinPts. For example, scikit-learn's `min_samples` includes the point itself. Always check the convention being used.

---

# 4. Three Types of Points

DBSCAN classifies points into three categories.

| Point Type | Meaning | Can Expand Cluster? |
|---|---|---|
| Core | Has enough nearby points | Yes |
| Border | Not dense enough itself, but close to a Core Point | No |
| Noise | Not part of any dense region | No |

The most important rule is:

```text
Core   → Join + Expand
Border → Join
Noise  → Stay Outside
```

---

# 5. Core Point

A point is a **Core Point** if its ε-neighborhood contains enough points to satisfy `MinPts`.

For our example:

```text
MinPts = 4
```

Suppose point `A` has:

```text
B
C
E
F
```

inside its ε-neighborhood.

Therefore:

```text
Number of nearby points = 4
MinPts = 4

4 >= 4
```

So:

```text
A = Core Point
```

A Core Point is important because it can **expand a cluster**.

---

# 6. Border Point

A Border Point does not have enough neighbors to become a Core Point.

Suppose:

```text
MinPts = 4
```

and point `D` has only:

```text
B
E
G
```

Then:

```text
Number of neighbors = 3

3 < 4
```

Therefore:

```text
D is not a Core Point.
```

But suppose `D` is inside the ε-neighborhood of Core Point `B`.

Then `D` belongs to the same cluster as `B`.

Therefore:

```text
D = Border Point
```

A Border Point can **join a cluster**, but it cannot expand the cluster.

---

# 7. Noise Point

A point is Noise when:

1. It does not have enough neighbors to become Core.
2. It is not density-reachable from any Core Point.

For example:

```text
I
```

may have only two nearby points.

If no Core Point can reach `I`, then:

```text
I = Noise
```

Noise points remain outside all clusters.

---

# 8. Step 1 — Mark Every Point as Unvisited

Initially, DBSCAN has not examined any point.

Conceptually:

| Point | Visited | Cluster |
|---|---|---|
| A | No | None |
| B | No | None |
| C | No | None |
| D | No | None |
| E | No | None |
| F | No | None |
| G | No | None |
| H | No | None |
| I | No | None |
| J | No | None |

The algorithm will process these points one by one.

---

# 9. Step 2 — Pick an Unvisited Point

Suppose DBSCAN starts with:

```text
A
```

DBSCAN marks:

```text
A = Visited
```

Now it needs to determine whether `A` belongs to a dense region.

---

# 10. Step 3 — Find the ε-Neighborhood

DBSCAN performs a neighborhood query around `A`.

Suppose the points within `ε = 2` are:

```text
B
C
E
F
```

Therefore:

```text
Neighborhood(A) = {B, C, E, F}
```

There are 4 neighboring points under the convention used in our example.

---

# 11. Step 4 — Compare With MinPts

We have:

```text
Number of neighbors = 4
MinPts = 4
```

Therefore:

```text
4 >= 4
```

So:

```text
A = Core Point
```

Because `A` is Core, DBSCAN can start a new cluster.

---

# 12. Step 5 — Create the First Cluster

DBSCAN creates:

```text
Cluster 1
```

and adds:

```text
A
```

Therefore:

```text
Cluster 1 = {A}
```

However, the cluster is not finished.

Since `A` is Core, DBSCAN must investigate its neighbors:

```text
B
C
E
F
```

This process is called **cluster expansion**.

---

# 13. Step 6 — Visit Neighbor B

DBSCAN examines:

```text
B
```

Suppose the ε-neighborhood of `B` contains:

```text
A
C
D
E
F
```

Therefore:

```text
Number of neighbors = 5
MinPts = 4

5 >= 4
```

So:

```text
B = Core Point
```

Since `B` is connected to `A`, it joins Cluster 1.

```text
Cluster 1 = {A, B}
```

Because `B` is Core, its neighbors must also be examined.

This allows the cluster to grow.

---

# 14. Step 7 — Expand the Cluster Through B

B has discovered:

```text
D
E
F
```

Suppose `D` has not been visited before.

DBSCAN now examines `D`.

This is how the cluster can expand beyond the immediate neighbors of `A`.

The important idea is:

> **A Core Point can introduce more points into the cluster expansion process.**

---

# 15. Step 8 — Visit D

Suppose `D` has the following neighbors:

```text
B
E
G
```

Therefore:

```text
Number of neighbors = 3
MinPts = 4

3 < 4
```

So:

```text
D is not Core.
```

Now DBSCAN checks whether `D` is close enough to an existing Core Point.

`D` is inside the ε-neighborhood of Core Point `B`.

Therefore:

```text
D = Border Point
```

So `D` is added to Cluster 1:

```text
Cluster 1 = {A, B, D, ...}
```

But because `D` is not Core:

```text
D cannot expand the cluster.
```

This is a very important DBSCAN rule.

---

# 16. Core vs Border

Consider:

```text
Core Point
    |
    | can expand
    v
More points
```

But:

```text
Border Point
    |
    | cannot expand
    X
```

Therefore:

> **Only Core Points expand clusters.**

Border Points simply become members of an existing cluster.

---

# 17. Step 9 — Visit C

Now DBSCAN examines `C`.

Suppose the ε-neighborhood of `C` contains:

```text
A
B
E
F
H
```

Therefore:

```text
Number of neighbors = 5
MinPts = 4

5 >= 4
```

So:

```text
C = Core Point
```

Since `C` is connected to Cluster 1:

```text
C → Cluster 1
```

Now:

```text
Cluster 1 = {A, B, C, D, ...}
```

Because `C` is Core, DBSCAN also examines its neighbors.

---

# 18. Step 10 — Continue Cluster Expansion

The same process continues.

Suppose:

```text
F = Core
H = Core
```

Then DBSCAN explores the neighborhoods of `F` and `H`.

This can cause additional points to become members of Cluster 1.

Eventually, the cluster might become:

```text
Cluster 1 = {A, B, C, D, E, F, G, H}
```

The important mechanism is:

```text
Core Point
    ↓
Find neighbors
    ↓
Find another Core Point
    ↓
Expand again
    ↓
Find more neighbors
    ↓
Repeat
```

This is how DBSCAN discovers a complete dense region.

---

# 19. Why Does the Cluster Keep Growing?

Consider the following simplified relationship:

```text
A → B → C → F → H
```

Suppose:

```text
A = Core
B = Core
C = Core
F = Core
H = Core
```

Then DBSCAN can continue expanding:

```text
A
↓
B
↓
C
↓
F
↓
H
```

Each Core Point can contribute more neighboring points.

This is the basis of **density-reachability**.

---

# 20. Density-Reachability

A point can be reached through a chain of Core Points.

For example:

```text
A → B → C → D
```

Suppose:

```text
A = Core
B = Core
C = Core
D = Border
```

Then `D` can belong to the same cluster because it is reachable from the dense region through Core Points.

The important idea is:

> **A Border Point may be part of a cluster even though it cannot expand the cluster itself.**

---

# 21. Cluster Expansion Stops

Eventually, DBSCAN reaches a point where there are no more unprocessed points that can expand the current dense region.

For example:

```text
Cluster 1

A
B
C
D
E
F
G
H
```

At this point:

```text
No more reachable points
```

Therefore:

```text
Cluster 1 is complete.
```

DBSCAN then goes back to the dataset and searches for another unvisited point.

---

# 22. Step 11 — Examine I

Now DBSCAN reaches:

```text
I
```

Suppose `I` has only:

```text
2 neighbors
```

We have:

```text
2 < MinPts
2 < 4
```

Therefore:

```text
I is not Core.
```

Now DBSCAN checks whether `I` is close enough to a Core Point.

Suppose it is not.

Therefore:

```text
I = Noise
```

---

# 23. Step 12 — Examine J

Now DBSCAN examines:

```text
J
```

Suppose:

```text
J has 0 neighbors.
```

Therefore:

```text
0 < 4
```

So `J` is not Core.

It is also not connected to a Core Point.

Therefore:

```text
J = Noise
```

---

# 24. Final Result

The final clustering is:

```text
Cluster 1:
A
B
C
D
E
F
G
H
```

And:

```text
Noise:
I
J
```

So conceptually:

```text
Cluster 1 = {A, B, C, D, E, F, G, H}

Noise = {I, J}
```

---

# 25. What Actually Happened?

DBSCAN did **not** ask:

```text
Where is the centroid?
```

It did **not** calculate:

```text
mean
```

It did **not** minimize:

```text
distance to centroid
```

Instead, it repeatedly asked:

```text
Does this point have enough nearby points?
```

If yes:

```text
Core
  ↓
Expand
```

If no:

```text
Not Core
  ↓
Is it near a Core Point?
  ↓
Yes → Border
No  → Noise
```

That is the central idea of DBSCAN.

---

# 26. Complete DBSCAN Flow

The complete process can be summarized as:

```text
Choose an unvisited point
        ↓
Mark it as visited
        ↓
Find its ε-neighborhood
        ↓
Does it satisfy MinPts?
        ↓
   ┌────┴────┐
   │         │
  Yes        No
   │         │
   ↓         ↓
 Core    Temporarily Noise
   │
   ↓
Create a cluster
   │
   ↓
Add its neighbors
   │
   ↓
Examine each neighbor
   │
   ↓
Is the neighbor Core?
   │
   ┌───┴───┐
   │       │
  Yes      No
   │       │
   ↓       ↓
Expand   Border
   │
   ↓
Repeat
   │
   ↓
No more reachable points
   │
   ↓
Cluster finished
   │
   ↓
Find next unvisited point
   │
   ↓
Repeat until all points are processed
```

---

# 27. Complete Pseudocode

A simplified version of DBSCAN is:

```text
for each point P:

    if P is already visited:
        continue

    mark P as visited

    neighbors = regionQuery(P)

    if neighbors do not satisfy MinPts:

        mark P as Noise

    else:

        create a new cluster

        expandCluster(P)
```

The important work happens inside `expandCluster()`.

---

# 28. expandCluster()

Simplified pseudocode:

```text
expandCluster(P):

    add P to the current cluster

    for every neighbor Q of P:

        if Q is not visited:

            mark Q as visited

            new_neighbors = regionQuery(Q)

            if Q satisfies MinPts:

                add new_neighbors
                to the expansion process

        if Q does not belong to any cluster:

            add Q to the current cluster
```

The critical condition is:

```text
if Q satisfies MinPts:
    expand from Q
```

Therefore:

```text
Core Point   → expansion
Border Point → no expansion
```

---

# 29. Important Detail: Noise Can Be Temporary

Suppose DBSCAN examines a point:

```text
X
```

and initially finds that it does not satisfy MinPts.

It may temporarily mark:

```text
X = Noise
```

Later, DBSCAN may discover that `X` is inside the ε-neighborhood of a Core Point.

Then:

```text
X
↓
was temporarily Noise
↓
found near Core Point
↓
becomes Border Point
↓
joins the cluster
```

Therefore, an implementation should not necessarily treat the first Noise assignment as permanently final.

---

# 30. The Most Important Rule

Remember this:

```text
Core Point
    ↓
Can start or expand a cluster

Border Point
    ↓
Can join a cluster
but cannot expand it

Noise Point
    ↓
Does not belong to a cluster
```

Or simply:

```text
CORE   → JOIN + EXPAND
BORDER → JOIN
NOISE  → IGNORE
```

---

# 31. DBSCAN vs K-Means

DBSCAN and K-Means approach clustering differently.

## K-Means

K-Means focuses on centroids.

Conceptually:

```text
Choose centroids
      ↓
Assign points to closest centroid
      ↓
Update centroids
      ↓
Repeat
```

K-Means therefore relies heavily on distance from cluster centers.

---

## DBSCAN

DBSCAN focuses on density.

Conceptually:

```text
Find dense region
      ↓
Find Core Points
      ↓
Expand through Core Points
      ↓
Attach Border Points
      ↓
Leave isolated points as Noise
```

DBSCAN does not need centroids.

---

# 32. Why DBSCAN Can Find Irregular Shapes

Consider a curved cluster:

```text
● ● ● ●
      ●
      ●
      ● ● ●
```

A centroid-based approach may have difficulty representing such a shape.

DBSCAN can follow the dense region because it does not require the cluster to have a particular geometric shape.

The algorithm is fundamentally based on:

```text
local density
+
connectivity
```

rather than:

```text
distance to a center
```

---

# 33. Density-Based Thinking

The easiest mental model for DBSCAN is:

> **Find crowded areas and connect those crowded areas together.**

Imagine every point is a person.

If many people are standing close together:

```text
Person Person Person
   Person Person
Person Person Person
```

that is a dense region.

A person slightly outside the crowd might still belong to the group:

```text
Crowd Crowd Crowd
Crowd Crowd Crowd

       Person
```

That person is similar to a Border Point.

But a person standing far away:

```text
Crowd Crowd Crowd


                         Person
```

may be Noise.

---

# 34. Why Border Points Cannot Expand

Suppose:

```text
B = Core
D = Border
```

and:

```text
D has only 3 neighbors
MinPts = 4
```

D is not dense enough.

If DBSCAN allowed Border Points to expand clusters, a sparse chain could incorrectly connect separate dense regions.

Therefore:

```text
Core → allowed to expand
Border → not allowed to expand
```

This helps DBSCAN preserve the concept of a dense cluster.

---

# 35. Complexity Analysis

Suppose:

```text
n = number of data points
```

A straightforward DBSCAN implementation may compare each point with many or all other points when searching for neighbors.

Therefore, the worst-case time complexity can be:

```text
O(n²)
```

---

# 36. Faster Neighborhood Search

DBSCAN can use spatial data structures such as:

- KD-Tree
- Ball Tree
- Spatial indexes

These structures can make neighborhood queries substantially faster for suitable datasets.

For low-dimensional data, practical performance can often be much better than a naive `O(n²)` implementation.

However, the exact complexity depends on:

- Data dimensionality
- Distribution of points
- Distance metric
- Index structure
- Implementation

So it is better to remember:

```text
Naive DBSCAN → O(n²) worst case
Spatial indexing → potentially much faster
```

rather than assuming DBSCAN is always `O(n log n)`.

---

# 37. Complete Algorithm Summary

The entire DBSCAN algorithm can be remembered as:

```text
Dataset
   ↓
Choose ε
   ↓
Choose MinPts
   ↓
Mark all points unvisited
   ↓
Pick an unvisited point
   ↓
Find its ε-neighborhood
   ↓
Does it satisfy MinPts?
   ↓
 ┌─┴─┐
Yes  No
 ↓    ↓
Core  Temporarily Noise
 ↓
Create cluster
 ↓
Examine neighbors
 ↓
Is neighbor Core?
 ↓
 ┌───┴───┐
Yes      No
 ↓        ↓
Expand   Border
 ↓
Repeat
 ↓
No more reachable points
 ↓
Cluster finished
 ↓
Search for next unvisited point
 ↓
Repeat
 ↓
Final clusters + noise
```

---

# 38. DBSCAN in One Sentence

> **DBSCAN finds dense regions by identifying Core Points and expanding clusters through neighboring Core Points, while Border Points join clusters and isolated points become Noise.**

---

# 39. Key Takeaways

### 1. DBSCAN starts with unvisited points

Every point initially has:

```text
Visited = False
Cluster = None
```

### 2. DBSCAN examines one point at a time

For every unvisited point:

```text
Mark visited
     ↓
Find ε-neighborhood
```

### 3. Core Points have enough nearby points

If the point satisfies `MinPts`:

```text
Point → Core
```

### 4. Core Points can expand clusters

A Core Point causes DBSCAN to investigate its neighbors.

```text
Core
 ↓
Neighbors
 ↓
More Core Points
 ↓
More neighbors
```

### 5. Border Points can join but cannot expand

```text
Border → Cluster member
Border → No expansion
```

### 6. Noise points stay outside

If a point is not Core and cannot be reached from a Core Point:

```text
Point → Noise
```

### 7. DBSCAN does not need centroids

Unlike K-Means, DBSCAN does not require:

```text
Centroids
Means
```

### 8. DBSCAN does not require the number of clusters beforehand

You provide:

```text
ε
MinPts
```

and DBSCAN discovers the clusters from the density structure.

### 9. DBSCAN can find irregularly shaped clusters

Because it is based on:

```text
Density
+
Connectivity
```

rather than distance to a centroid.

---

# 40. Final Mental Model

If you remember nothing else, remember this:

```text
              DBSCAN

        "Are there enough
         points nearby?"
                 |
        +--------+--------+
        |                 |
       YES                NO
        |                 |
      CORE          "Is it near
        |            a Core?"
        |                 |
        |          +------+------+
        |          |             |
        |         YES            NO
        |          |             |
        ↓          ↓             ↓
     EXPAND      BORDER        NOISE
        |
        ↓
   Find more Core
      Points
        |
        ↓
    Keep expanding
```

The complete logic is:

```text
CORE
  → dense region
  → can expand

BORDER
  → near a dense region
  → can join
  → cannot expand

NOISE
  → not dense
  → not connected to a dense region
  → stays outside
```

---

# 41. What Comes Next?

The DBSCAN algorithm depends heavily on choosing good values for:

```text
ε
MinPts
```

Choosing them poorly can produce very different clustering results.

In the next chapter, we will learn how to choose these parameters using:

- **K-Distance Graph**
- **Elbow Method**
- Practical `ε` selection
- Practical `MinPts` selection
- What happens when `ε` is too small
- What happens when `ε` is too large
- What happens when `MinPts` is too small
- What happens when `MinPts` is too large

This is one of the most important practical parts of using DBSCAN.

---

# Quick Revision

```text
ε
→ Defines the neighborhood radius.

MinPts
→ Defines the required density.

Core
→ Enough nearby points.

Border
→ Not dense enough itself, but reachable from a Core Point.

Noise
→ Not part of any cluster.

Density-Reachable
→ A point can be reached through a chain of Core Points.

Cluster Expansion
→ Continues through Core Points.

DBSCAN
→ Density-based clustering algorithm.
```

> **Core Points expand. Border Points join. Noise Points stay outside.**
