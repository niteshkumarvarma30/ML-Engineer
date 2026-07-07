# Chapter 3 : ε (Epsilon) and MinPts

Everything in DBSCAN depends on only **two parameters**.

```
ε (Epsilon)

and

MinPts
```

If these two values change,

the clusters produced by DBSCAN also change.

Think of them as the **hyperparameters** of the algorithm.

---

# Overview

Every point in the dataset asks two questions.

```
Question 1

↓

Who is close to me?

↓

Answer

ε (Epsilon)

----------------------------

Question 2

↓

How many nearby friends do I need?

↓

Answer

MinPts
```

Only after answering these questions can DBSCAN decide whether a point belongs to a cluster.

---

# 1. What is ε (Epsilon)?

Epsilon is simply a **radius**.

Imagine every point draws a circle around itself.

```
          ε

      *********
    **         **
   *      ●      *
    **         **
      *********
```

Everything inside the circle is considered a **neighbor**.

Everything outside is ignored.

---

# Mathematical Definition

For a point

```
P
```

its ε-neighborhood is

```
Nε(P)

=

All points

whose distance from P

≤ ε
```

Mathematically

```
Nε(P)

=

{Q | Distance(P,Q) ≤ ε}
```

---

# Example

Suppose

```
ε = 3
```

Dataset

```
A(2,3)

B(3,4)

C(5,6)

D(10,12)
```

Distance

```
Distance(A,B)

=

√[(3−2)²+(4−3)²]

=

√2

≈1.41
```

Since

```
1.41 < 3
```

B belongs to A's neighborhood.

---

Distance

```
Distance(A,C)

=

√[(5−2)²+(6−3)²]

=

√18

≈4.24
```

Outside ε.

---

Therefore

```
Nε(A)

=

{A,B}
```

---

# Intuition

Imagine standing in a park.

You ask

> "Who is standing within 10 meters of me?"

Those people become your neighbors.

DBSCAN asks exactly the same question.

---

# What Happens if ε is Too Small?

Suppose

```
● ● ● ● ●
```

Choose

```
ε = 0.1
```

Each circle becomes tiny.

```
●     ●     ●     ●
```

Nobody can see anyone.

Result

```
Noise

Noise

Noise

Noise
```

Almost every point becomes Noise.

---

# What Happens if ε is Too Large?

Suppose

```
● ● ●

           ▲ ▲ ▲
```

Choose

```
ε = 100
```

Huge circles.

Everyone becomes everyone's neighbor.

Result

```
One Giant Cluster
```

This is also incorrect.

---

# Choosing ε

A good ε should

- connect nearby points
- separate distant groups
- avoid merging unrelated clusters

Usually ε is selected using a **K-Distance Graph**, which we'll study later.

---

# 2. What is MinPts?

Now we know

how far to search.

Next question

```
How many neighbors

should be inside the circle?
```

That number is called

```
MinPts
```

---

# Example

Suppose

```
MinPts = 5
```

Point

```
A
```

has

```
6 neighbors
```

Then

```
6 ≥ 5
```

Good.

A has enough nearby friends.

---

Another point

```
B
```

has

```
2 neighbors
```

```
2 < 5
```

Not enough.

---

# Why Do We Need MinPts?

Imagine

```
●




●




●
```

If

```
MinPts = 1
```

Every point

becomes its own cluster.

That makes no sense.

Instead

```
MinPts = 4
```

Now isolated points

cannot form clusters.

Only genuinely dense regions become clusters.

---

# Effect of Small MinPts

```
MinPts = 2
```

Almost every point becomes a Core Point.

Many tiny clusters appear.

---

# Effect of Large MinPts

```
MinPts = 20
```

Only extremely dense regions survive.

Many points become Noise.

---

# Typical Values

General guideline

```
MinPts

≥

Dimensions + 1
```

Examples

| Dimensions | Suggested MinPts |
|------------|-----------------:|
| 2 | 3–5 |
| 3 | 4–6 |
| 5 | 6–10 |
| 10 | 11–20 |

Many practical datasets use

```
MinPts = 4

or

MinPts = 5
```

---

# ε and MinPts Work Together

Suppose

```
ε = 2

MinPts = 5
```

Point

```
A
```

draws a circle.

Neighbors

```
7
```

Since

```
7 ≥ 5
```

A satisfies both conditions.

---

Point

```
B
```

Neighbors

```
2
```

```
2 < 5
```

Not enough.

---

# Real-Life Analogy

Imagine a discussion group in a classroom.

Teacher says

> "A discussion group must have at least **5 students** sitting within **2 meters** of one another."

Here

```
2 meters

↓

ε
```

```
5 students

↓

MinPts
```

Students sitting alone are not considered a group.

Exactly DBSCAN.

---

# Complete Workflow

```
Choose ε
      │
      ▼
Draw Circle Around Every Point
      │
      ▼
Count Neighbors
      │
      ▼
Neighbors ≥ MinPts?
```

The answer to this question determines whether a point can become the center of a cluster.

---

# Chapter Summary

ε determines

```
How far to search.
```

MinPts determines

```
How many nearby neighbors are required.
```

Together they decide whether a point belongs to a dense region.

---

# Chapter 4 : Core Point, Border Point and Noise Point

Now that every point knows

- its neighbors
- the value of ε
- the value of MinPts

DBSCAN classifies every point into one of **three categories**.

```
Dataset
      │
      ▼
Count Neighbors
      │
      ▼
Compare with MinPts
      │
 ┌────┼─────┐
 ▼    ▼     ▼

Core Border Noise
```

---

# 1. Core Point

A Core Point is the **heart of a cluster**.

Definition

A point is called a Core Point if

```
Neighbors ≥ MinPts
```

---

# Example

Suppose

```
ε = 2

MinPts = 5
```

Dataset

```
           ●

      ● ● ●

   ● ● A ●

      ● ●

           ●
```

Neighbors around A

```
8
```

Since

```
8 ≥ 5
```

A is a

```
Core Point
```

---

# Intuition

Imagine a crowded railway station.

```
🙂🙂🙂🙂🙂

🙂🙂A🙂🙂

🙂🙂🙂🙂🙂
```

A is surrounded by many people.

Clearly

A belongs to a crowd.

---

# 2. Border Point

Now consider

```
      ● ● ●

         B
```

Neighbors around B

```
2
```

Since

```
2 < MinPts
```

B is **not** a Core Point.

However

B lies inside the ε-neighborhood of a Core Point.

Therefore

B becomes a

```
Border Point
```

---

# Intuition

Imagine standing at the edge of a crowd.

You are still part of the crowd,

but you are not surrounded by many people.

That is exactly a Border Point.

---

# 3. Noise Point

Suppose

```
● ● ● ●




               X
```

Neighbors around X

```
0
```

Also

X does not lie inside any Core Point's neighborhood.

Therefore

X becomes

```
Noise
```

---

# Intuition

Imagine one person sitting alone in a park.

That person is not part of any crowd.

DBSCAN ignores that point.

---

# Important Difference

| Property | Core | Border | Noise |
|----------|------|--------|-------|
| Enough neighbors | ✅ | ❌ | ❌ |
| Inside Core's neighborhood | Yes | Yes | No |
| Starts a cluster | ✅ | ❌ | ❌ |
| Expands a cluster | ✅ | ❌ | ❌ |
| Belongs to a cluster | ✅ | ✅ | ❌ |

---

# Cluster Expansion

Suppose

```
A

↓

Core
```

DBSCAN creates

Cluster 1.

Now

visit all neighbors.

Suppose

```
B
```

is also Core.

Expand again.

Then

```
C
```

is Core.

Expand again.

Eventually

```
Entire Cluster
```

is discovered.

---

# Fire Analogy

Imagine lighting a match.

```
🔥
```

Nearby wood catches fire.

```
🔥🔥🔥
```

Then

more wood catches fire.

```
🔥🔥🔥🔥🔥
```

The fire spreads until

nothing else can burn.

Core Points spread the cluster exactly the same way.

---

# Summary

Core Point

> Has enough nearby neighbors.

Border Point

> Does not have enough neighbors but is connected to a Core Point.

Noise Point

> Has too few neighbors and is not connected to any Core Point.

---

# What's Next?

In **Chapter 5**, we'll study the mathematical backbone of DBSCAN:

- ε-Neighborhood
- Directly Density-Reachable
- Density-Reachable
- Density-Connected

These concepts explain exactly **how DBSCAN grows clusters mathematically**.
