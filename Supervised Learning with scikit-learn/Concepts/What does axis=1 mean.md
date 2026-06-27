# What does axis=1 mean?

When you look at a spreadsheet (DataFrame), there are two directions you can move: up/down (rows) or left/right (columns).

In programming, we use the `axis` parameter to tell the computer which direction we want it to move.

## The Simple Rule

* `axis=0` means **ROWS**. (Move vertically ↓)
* `axis=1` means **COLUMNS**. (Move horizontally →)

## Real-World Examples

Let's look at the two most common times you use `axis=1` during data preprocessing:

### 1. Dropping a Column

If you want to delete the "genre" column, you write:
```python
df.drop("genre", axis=1)
```

**Why `axis=1`?** Because you are telling the computer: *"Look across the columns (left to right) until you find the one named 'genre', and delete that entire column."*

*(If you used `axis=0`, the computer would look down the rows for a row named 'genre', which would cause an error).*

### 2. Gluing Data Together (Concatenating)

If you have two spreadsheets and you want to glue them together, you write:
```python
pd.concat([sheet1, sheet2], axis=1)
```

**Why `axis=1`?** Because you are telling the computer to glue them together side-by-side (adding new columns).

*(If you used `axis=0`, it would stack the second spreadsheet at the bottom of the first one, making it longer by adding new rows).*

## Summary Cheat Sheet

Whenever you see a function and you aren't sure which axis to use, ask yourself:

* Am I trying to mess with the **Rows**? Use `axis=0`.
* Am I trying to mess with the **Columns**? Use `axis=1`.
