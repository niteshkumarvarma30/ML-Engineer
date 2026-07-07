# Hierarchical Clustering - Complete Notes

This condensed Markdown includes the updated matrices discussed.

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
