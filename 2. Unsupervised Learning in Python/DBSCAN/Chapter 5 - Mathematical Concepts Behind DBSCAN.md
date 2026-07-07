# Chapter 5 : Mathematical Concepts Behind DBSCAN

Until now we know

- ε (Epsilon)
- MinPts
- Core Point
- Border Point
- Noise Point

Now we will learn the mathematical concepts that explain **how DBSCAN grows clusters**.

These concepts are

```
ε-Neighborhood
        │
        ▼
Directly Density-Reachable
        │
        ▼
Density-Reachable
        │
        ▼
Density-Connected
        │
        ▼
Final Cluster
```

These four concepts are the mathematical backbone of DBSCAN.

---

# 1. ε-Neighborhood

This is the easiest concept.

Suppose we have a point

```
P
```

Draw a circle of radius

```
ε
```

around P.

Everything inside the circle becomes P's neighborhood.

Example

```
          ε

      *********
    **         **
   *      P      *
    **         **
      *********
```

---

## Mathematical Definition

The ε-Neighborhood of a point P is

```
Nε(P)

=

{Q | Distance(P,Q) ≤ ε}
```

Meaning

```
All points

whose distance

from P

is less than or equal to ε.
```

---

## Example

Suppose

```
ε = 3
```

Dataset

```
A (2,3)

B (3,4)

C (5,6)

D (10,12)
```

### Distance(A,B)

```
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

### Distance(A,C)

```
√[(5−2)²+(6−3)²]

=

√18

≈4.24
```

Outside ε.

---

### Distance(A,D)

Very far.

Outside ε.

---

Therefore

```
Nε(A)

=

{A,B}
```

---

## Visual

```
             B


       ***********
     **           **
    *      A        *
     **           **
       ***********


                C




                         D
```

Only

```
A

and

B
```

are inside the circle.

---

## Intuition

ε-Neighborhood simply answers

> **"Who are my nearby friends?"**

Nothing more.

---

# 2. Directly Density-Reachable

Now suppose

```
ε = 2

MinPts = 5
```

Dataset

```
            B

      C  A  D

        E F

            G
```

Suppose

A has

```
6 neighbors.
```

Therefore

```
A

↓

Core Point
```

Now ask

Can B be reached from A?

Yes.

Because

```
B

lies inside

A's ε-Neighborhood.
```

---

## Mathematical Definition

A point

```
Q
```

is **Directly Density-Reachable**

from

```
P
```

if

```
Q ∈ Nε(P)

AND

P is a Core Point.
```

Notice

Only

```
Core Points
```

can directly reach other points.

---

## Visual

```
             B


      ************
    **            **
   *       A        *
    **            **
      ************
```

Arrow

```
A

↓

B
```

Valid.

---

Can

```
B

↓

A
```

always happen?

No.

Suppose

```
B

↓

Border Point
```

Border Points

cannot expand clusters.

Therefore

Directly Density-Reachable

is **NOT symmetric**.

---

## Real-Life Analogy

Teacher

↓

Students

Teacher can call students.

Students

cannot call

the whole class.

Exactly the same idea.

---

# 3. Density-Reachable

Suppose

```
A

↓

B

↓

C

↓

D
```

A reaches B.

B reaches C.

C reaches D.

Although

```
A

cannot directly

reach D,
```

A reaches D

through

```
B

and

C
```

This is called

Density-Reachable.

---

## Mathematical Definition

A point

```
Q
```

is Density-Reachable

from

```
P
```

if there exists a chain

```
P₁

↓

P₂

↓

P₃

↓

...

↓

Pn
```

such that

every point

is directly density reachable

from the previous one.

---

## Example

```
A ---- B ---- C ---- D
```

Suppose

A

B

C

are Core Points.

D is Border.

Then

```
A

↓

B

↓

C

↓

D
```

Therefore

```
D

is Density-Reachable

from A.
```

---

## Intuition

Imagine dominoes.

```
□ □ □ □
```

Push the first one.

```
↓

□□□□
```

Eventually

the last domino falls.

Exactly

Density-Reachable.

---

## Important

Density-Reachable

is also

**NOT symmetric**.

Core reaches Border.

Border

cannot reach back.

---

# 4. Density-Connected

This is the final concept.

Suppose

```
A

↓

B

↓

C

↓

D
```

Now another point

```
E
```

```
A

↓

B

↓

C

↑

E
```

Notice

Both

```
D

and

E
```

are connected

through

```
C
```

Therefore

they belong

to the same cluster.

---

## Mathematical Definition

Two points

```
P

and

Q
```

are Density-Connected

if

there exists

another point

```
O
```

such that

```
P

and

Q
```

are both

Density-Reachable

from O.

---

## Visual

```
            A

          /   \

         B     C

        /       \

       D         E
```

A reaches

everyone.

Therefore

all belong

to one cluster.

---

## Intuition

Imagine cousins.

Two cousins

may not know each other directly.

But

they have

the same grandparents.

Therefore

they belong

to the same family.

Exactly

Density-Connected.

---

# Relationship Between All Concepts

```
Choose Point
      │
      ▼
Find ε-Neighborhood
      │
      ▼
Enough Neighbors?
      │
      ▼
Core Point
      │
      ▼
Directly Density-Reachable
      │
      ▼
Density-Reachable
      │
      ▼
Density-Connected
      │
      ▼
Same Cluster
```

---

# Complete Example

Suppose

```
ε = 2

MinPts = 4
```

Dataset

```
A ---- B ---- C ---- D

             |

             E
```

Suppose

A

B

C

are Core Points.

D

and

E

are Border Points.

---

Step 1

```
A

↓

B
```

Directly Density-Reachable.

---

Step 2

```
B

↓

C
```

Directly Density-Reachable.

---

Step 3

```
C

↓

D
```

Directly Density-Reachable.

---

Now

```
A

↓

B

↓

C

↓

D
```

Therefore

```
D

is Density-Reachable

from A.
```

Similarly

```
C

↓

E
```

Therefore

```
D

and

E
```

are Density-Connected.

Hence

they belong

to the same cluster.

---

# Summary Table

| Concept | Meaning | Condition |
|----------|---------|-----------|
| ε-Neighborhood | Nearby points inside ε radius | Distance ≤ ε |
| Directly Density-Reachable | Direct neighbor of a Core Point | Source must be Core |
| Density-Reachable | Reachable through a chain of Core Points | Chain exists |
| Density-Connected | Two points belong to the same cluster | Common Core ancestor |

---

# Key Takeaways

- ε-Neighborhood finds nearby points.
- Directly Density-Reachable is only possible from a Core Point.
- Density-Reachable allows clusters to grow through chains of Core Points.
- Density-Connected determines whether two points belong to the same cluster.
- These four concepts form the mathematical foundation of the DBSCAN algorithm.

---

# Next Chapter

In **Chapter 6**, we will simulate the **entire DBSCAN algorithm step by step** on a real dataset.

You will see exactly how DBSCAN:
- Visits each point
- Finds neighbors
- Identifies Core, Border, and Noise points
- Expands clusters
- Produces the final clustering result

This is the chapter where the complete algorithm comes together.
