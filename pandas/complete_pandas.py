# Pandas Comprehensive Function Examples

'''
This notebook demonstrates:

Data Loading: Reading from CSV and creating DataFrames.
Data Selection: Using .iloc[], .loc[], and selecting columns.
Data Cleaning: Handling missing data, replacing values, and dropping columns.
Data Modification: Adding columns, renaming, and deleting columns.
Grouping and Aggregation: Using .groupby() and .agg().
Merging and Joining: Combining DataFrames.
Sorting: Sorting data by column or index.
Filtering: Filtering rows based on conditions.
Statistics: Summary statistics and value counts.
Pivot Tables: Creating pivot tables for grouped data.
Reshaping: Melting and pivoting data.
Handling Duplicates: Removing duplicates from a DataFrame.
Exporting Data: Exporting DataFrames to CSV.
'''

# Import pandas
import pandas as pd
import numpy as np

# 1. Data Loading
# Read a CSV file
# df = pd.read_csv('your_file.csv')

# Creating DataFrames directly (example)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

# 2. Data Selection
# Select a single column
print("\nSelect 'Name' column:\n", df['Name'])

# Select multiple columns
print("\nSelect 'Name' and 'Salary' columns:\n", df[['Name', 'Salary']])

# Select rows by index location (using iloc)
print("\nSelect first two rows (iloc):\n", df.iloc[:2])

# Select rows by index label (using loc)
print("\nSelect rows where Age > 30 (loc):\n", df.loc[df['Age'] > 30])

# 3. Data Cleaning
# Handling missing data
df_with_nan = df.copy()
df_with_nan.loc[1, 'Salary'] = np.nan
print("\nDataFrame with NaN:\n", df_with_nan)

# Drop rows with missing values
print("\nDrop rows with NaN:\n", df_with_nan.dropna())

# Fill missing values
print("\nFill NaN with mean salary:\n", df_with_nan.fillna(df_with_nan['Salary'].mean()))

# Replace specific values
print("\nReplace 'Alice' with 'Alicia':\n", df.replace({'Alice': 'Alicia'}))

# 4. Data Modification
# Adding new columns
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:\n", df)

# Dropping columns
df_dropped = df.drop(columns=['Bonus'])
print("\nDataFrame after dropping 'Bonus' column:\n", df_dropped)

# Renaming columns
df_renamed = df.rename(columns={'Name': 'Employee', 'Salary': 'Annual Salary'})
print("\nDataFrame with renamed columns:\n", df_renamed)

# 5. Grouping and Aggregation
# Group by 'Age' and calculate mean salary
grouped = df.groupby('Age').agg({'Salary': 'mean'})
print("\nGrouped by Age with mean Salary:\n", grouped)

# Apply multiple aggregate functions
agg_multi = df.groupby('Age').agg({'Salary': ['mean', 'sum', 'max']})
print("\nGrouped by Age with multiple aggregations:\n", agg_multi)

# 6. Merging and Joining DataFrames
# Creating another DataFrame for merge example
data2 = {'Employee': ['Alice', 'Bob', 'Eve', 'Frank'],
         'Department': ['HR', 'IT', 'Marketing', 'Sales']}
df2 = pd.DataFrame(data2)

# Merge the two DataFrames on 'Employee'
merged_df = pd.merge(df, df2, left_on='Name', right_on='Employee', how='left')
print("\nMerged DataFrame (left join on 'Employee'):\n", merged_df)

# 7. Sorting
# Sorting by column values
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame sorted by 'Salary' (descending):\n", sorted_df)

# Sorting by index
sorted_index_df = df.sort_index(ascending=False)
print("\nDataFrame sorted by index (descending):\n", sorted_index_df)

# 8. Filtering
# Filter rows where Salary > 60000
filtered_df = df[df['Salary'] > 60000]
print("\nFilter rows where Salary > 60000:\n", filtered_df)

# 9. Statistics
# Summary statistics for numerical columns
print("\nSummary statistics:\n", df.describe())

# Value counts for a specific column
print("\nValue counts for 'Age' column:\n", df['Age'].value_counts())

# 10. Pivot Tables
# Create a pivot table
pivot = df.pivot_table(values='Salary', index='Age', columns='Name', aggfunc='mean')
print("\nPivot Table:\n", pivot)

# 11. Reshaping
# Melting a DataFrame (long format)
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Salary'])
print("\nMelted DataFrame:\n", melted_df)

# Pivot back to wide format
pivoted_df = melted_df.pivot(index='Name', columns='variable', values='value')
print("\nPivoted DataFrame:\n", pivoted_df)

# 12. Handling Duplicates
# Adding duplicate data for demonstration
df_dup = df.append(df.iloc[0])
print("\nDataFrame with duplicate rows:\n", df_dup)

# Dropping duplicate rows
df_no_dup = df_dup.drop_duplicates()
print("\nDataFrame with duplicates removed:\n", df_no_dup)

# 13. Exporting Data
# Export DataFrame to CSV
# df.to_csv('exported_file.csv', index=False)

print("\nDataFrame can be exported to CSV with `df.to_csv('exported_file.csv')`")

