# Chapter 6 : Complete DBSCAN Algorithm (Step-by-Step)

Until now we know

- ε (Epsilon)
- MinPts
- Core Points
- Border Points
- Noise Points
- ε-Neighborhood
- Density-Reachable
- Density-Connected

Now we'll see how DBSCAN uses all these concepts together.

---

# Problem Statement

Suppose we have the following dataset.

```
                A

          B     C

      D   E   F

          G   H

                    I


                               J
```

Choose

```
ε = 2

MinPts = 4
```

Goal

```
Find all clusters.
```

---

# Step 1 : Mark Every Point as Unvisited

Initially

```
Visited = No

Cluster = None
```

for every point.

| Point | Visited | Cluster |
|--------|----------|---------|
| A | No | None |
| B | No | None |
| C | No | None |
| D | No | None |
| E | No | None |
| F | No |None |
| G | No |None |
| H | No |None |
| I | No |None |
| J | No |None |

---

# Step 2 : Pick Any Unvisited Point

Suppose DBSCAN starts with

```
Point A
```

Mark

```
Visited = Yes
```

---

# Step 3 : Find ε-Neighborhood

Draw a circle around A.

```
        *************

      **           **

     *      A        *

      **           **

        *************
```

Neighbors

```
B

C

E

F
```

Total

```
4 neighbors
```

---

# Step 4 : Compare with MinPts

```
Neighbors

=

4

MinPts

=

4
```

Since

```
4 ≥ 4
```

A becomes

```
Core Point
```

---

# Step 5 : Create First Cluster

DBSCAN says

```
Cluster 1

↓

{A}
```

Now

look at every neighbor.

```
B

C

E

F
```

---

# Step 6 : Visit Neighbor B

Mark

```
Visited
```

Find B's neighbors.

Suppose

```
A

C

D

E

F
```

Neighbors

```
5
```

Since

```
5 ≥ 4
```

B is also

```
Core Point
```

Add

```
B

↓

Cluster 1
```

---

# Step 7 : Expand Again

Since B is Core,

DBSCAN now visits

all neighbors of B.

```
D

E

F
```

Notice

```
D
```

was not previously discovered.

Add

```
D

↓

Cluster 1
```

---

# Step 8 : Visit D

Draw ε around D.

Suppose

Neighbors

```
B

E

G
```

Total

```
3
```

Compare

```
3 < 4
```

Not enough.

Therefore

```
D

↓

Not Core
```

But

D lies inside B's neighborhood.

Therefore

```
Border Point
```

Add

```
D

↓

Cluster 1
```

Notice

Border Points

cannot expand clusters.

So

DBSCAN stops expanding from D.

---

# Step 9 : Visit C

Neighbors

```
A

B

E

F

H
```

Total

```
5
```

```
5 ≥ 4
```

Core Point.

Add

```
C

↓

Cluster 1
```

Now expand from C.

---

# Step 10 : Continue Expansion

Suppose

```
F
```

also becomes Core.

Then

visit F's neighbors.

Suppose

```
H
```

becomes Core.

Visit H.

Eventually

the cluster grows.

```
Cluster 1

↓

A

B

C

D

E

F

G

H
```

---

# Step 11 : Finish Cluster

Eventually

every reachable point

has been visited.

Cluster expansion stops.

Current result

```
Cluster 1

↓

A B C D E F G H
```

---

# Step 12 : Continue Searching

DBSCAN now scans

the remaining points.

```
I

J
```

Suppose

I

has

```
2 neighbors
```

Not enough.

Also

no Core Point reaches I.

Therefore

```
Noise
```

---

Visit

```
J
```

Neighbors

```
0
```

Noise.

---

# Final Result

```
Cluster 1

↓

A

B

C

D

E

F

G

H

--------------------

Noise

↓

I

J
```

---

# What Actually Happened?

Notice

DBSCAN never searched for

centroids.

It never computed

means.

It never minimized

distances.

Instead

it simply asked

```
Does this point

have enough nearby friends?
```

If

Yes

↓

Core

↓

Expand

Otherwise

↓

Border

or

Noise

---

# Complete Flowchart

```
Start
   │
   ▼
Choose an Unvisited Point
   │
   ▼
Mark as Visited
   │
   ▼
Find ε-Neighborhood
   │
   ▼
Neighbors ≥ MinPts ?
   │
 ┌───────────────┐
 │               │
Yes              No
 │               │
 ▼               ▼
Core         Temporarily Noise
 │
 ▼
Create New Cluster
 │
 ▼
Add All Neighbors
 │
 ▼
Visit Every Neighbor
 │
 ▼
Neighbor is Core?
 │
 ┌───────────────┐
 │               │
Yes              No
 │               │
 ▼               ▼
Expand       Border Point
Cluster
 │
 ▼
Repeat
 │
 ▼
No More Reachable Points
 │
 ▼
Cluster Finished
 │
 ▼
Search Next Unvisited Point
 │
 ▼
Repeat Until Every Point is Visited
```

---

# Complete Pseudocode

```
for each point P

    if P already visited

        continue

    mark P visited

    neighbors = regionQuery(P)

    if neighbors < MinPts

        mark as Noise

    else

        create new cluster

        expandCluster(P)
```

---

# expandCluster()

```
Add P to Cluster

for every neighbor Q

    if Q not visited

        mark visited

        new_neighbors = regionQuery(Q)

        if new_neighbors ≥ MinPts

            neighbors += new_neighbors

    if Q not assigned

        add Q to Cluster
```

Notice

Only

```
Core Points

↓

expand the cluster.
```

Border Points

simply join.

Noise Points

remain outside.

---

# Complexity Analysis

Suppose

```
n

=

number of points
```

Without optimization

Every point

checks

every other point.

```
Time

=

O(n²)
```

With

KD-Tree

or

Ball Tree

Nearest-neighbor search becomes faster.

Average complexity

```
O(n log n)
```

for low-dimensional datasets.

---

# Complete Algorithm Summary

```
Dataset
      │
      ▼
Choose ε
Choose MinPts
      │
      ▼
Mark Every Point Unvisited
      │
      ▼
Pick an Unvisited Point
      │
      ▼
Find ε-Neighborhood
      │
      ▼
Enough Neighbors?
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Core      Noise
 │
 ▼
Create Cluster
 │
 ▼
Visit Neighbors
 │
 ▼
Neighbor is Core?
 │
 ┌────┴─────┐
 │          │
 ▼          ▼
Yes      Border
 │
 ▼
Expand Again
 │
 ▼
Repeat
 │
 ▼
Cluster Completed
 │
 ▼
Repeat for Remaining Points
 │
 ▼
Final Clusters
```

---

# Key Takeaways

- DBSCAN starts with **all points unvisited**.
- It visits one point at a time.
- If a point has at least **MinPts neighbors within ε**, it becomes a **Core Point**.
- A Core Point starts a **new cluster**.
- The cluster grows by visiting neighboring **Core Points**.
- **Border Points** join a cluster but **never expand** it.
- **Noise Points** remain outside every cluster.
- The algorithm repeats until **every point has been visited**.

---

# Next Chapter

In **Chapter 7**, we'll learn **how to choose the best values for ε and MinPts**.

We'll cover:

- K-Distance Graph
- Elbow Method
- Practical parameter selection
- Effects of choosing ε too small or too large
- Effects of choosing MinPts too small or too large

This is the most important practical topic for using DBSCAN effectively.
