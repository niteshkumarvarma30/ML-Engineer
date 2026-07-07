# What is a Pandas DataFrame?

A DataFrame is the core data structure of the Pandas library (`import pandas as pd`). It is essentially a 2-dimensional table or spreadsheet.

Machine learning models in scikit-learn love DataFrames because they perfectly organize data into a mathematical grid.

## The Anatomy of a DataFrame

* **Rows (Index):** Run horizontally. In machine learning, every row is a single **Sample** (e.g., one specific customer, one specific flower, one specific fish).
* **Columns:** Run vertically. In machine learning, every column is a **Feature** (e.g., "Age", "Petal Length", "Weight").

## How do you "Initiate" one?

You can initiate an empty DataFrame, but usually, you initiate it by feeding it data. There are three main ways to do this:

1. **From a Dictionary:** You define the columns as "keys" and the rows as lists of "values". (Great for building small tables by hand).
2. **From a List of Lists:** You provide the raw rows of data, and then define the column names separately.
3. **From a CSV File:** This is what you will do 99% of the time in the real world. You just point Pandas to a file on your computer, and it automatically builds the spreadsheet for you!

```python
# Always import pandas first (usually aliased as 'pd')
import pandas as pd

# ==========================================
# METHOD 1: Initiating from a Dictionary
# ==========================================
# Keys become the Column headers.
# Lists become the Row data down that column.
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Purchased": ["Yes", "No", "Yes"]
}

# Initiate the DataFrame
df_from_dict = pd.DataFrame(data_dict)

print("--- Method 1: From Dictionary ---")
print(df_from_dict)
print("\n")


# ==========================================
# METHOD 2: Initiating from a List of Lists
# ==========================================
# Each inner list represents a single horizontal Row.
data_lists = [
    ["Alice", 25, "Yes"],
    ["Bob", 30, "No"],
    ["Charlie", 35, "Yes"]
]

# Initiate the DataFrame (and pass the column names manually)
df_from_lists = pd.DataFrame(data_lists, columns=["Name", "Age", "Purchased"])

print("--- Method 2: From List of Lists ---")
print(df_from_lists)
print("\n")


# ==========================================
# METHOD 3: Initiating from a CSV File (The Pro Way)
# ==========================================
# In the real world, your data is usually saved in a file.
# Pandas initiates the DataFrame and fills it automatically!

# df_from_csv = pd.read_csv("my_dataset.csv")

# print("--- Method 3: From CSV ---")
# print(df_from_csv.head()) # .head() prints just the first 5 rows 
```

## Basic DataFrame Operations

Once your DataFrame is initiated, you can manipulate it. Here are the most common operations you'll need:

```python
import pandas as pd

# ==========================================
# STEP 1: Initiate our starting DataFrame
# ==========================================
print("--- 1. The Original DataFrame ---")
data = {
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 45, 30, 50, 22],
    "Purchases": [5, 2, 10, 1, 8]
}
df = pd.DataFrame(data)
print(df)
print("\n")


# ==========================================
# STEP 2: Adding a New Column
# ==========================================
# Let's say every purchase averages $10. 
# We can create a "Total_Spent" column by multiplying the Purchases column by 10.
print("--- 2. Adding a 'Total_Spent' Column ---")
df["Total_Spent"] = df["Purchases"] * 10
print(df)
print("\n")


# ==========================================
# STEP 3: Filtering the Data (Asking Questions)
# ==========================================
# Let's find only the customers who are older than 30.
# The inner part (df["Age"] > 30) asks the True/False question.
# The outer brackets df[...] keep only the rows where the answer is True.
print("--- 3. Filtering: Customers older than 30 ---")
older_customers = df[df["Age"] > 30]
print(older_customers)
print("\n")


# ==========================================
# STEP 4: Dropping a Column
# ==========================================
# Let's say our machine learning model doesn't need the customer's name.
# We use .drop(). Remember: axis=1 means we are dropping a vertical COLUMN.
print("--- 4. Dropping the 'Customer' Column ---")
df_no_names = df.drop("Customer", axis=1)
print(df_no_names)
print("\n")


# ==========================================
# STEP 5: Dropping a Row
# ==========================================
# Let's delete Bob's row. Bob is at index 1.
# We use .drop() again, but this time axis=0, meaning drop a horizontal ROW.
print("--- 5. Dropping Row Index 1 (Bob) ---")
df_no_bob = df.drop(1, axis=0)
print(df_no_bob)
print("\n")


# ==========================================
# STEP 6: Selecting Specific Columns
# ==========================================
# If you only want to look at a few specific columns, you pass a list of column names.
# Notice the double brackets [[...]]!
print("--- 6. Selecting only Age and Total_Spent ---")
subset = df[["Age", "Total_Spent"]]
print(subset)
```
