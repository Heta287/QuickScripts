# Libraries Overview Example for 
# 1. pandas
# 2. numpy
# 3. matplotlib

#This notebook covers:
#pandas: DataFrame creation, column selection, grouping, handling missing data.
#numpy: Array creation, reshaping, basic element-wise operations, and statistics.
#matplotlib: Line plot, bar chart, scatter plot, histogram, and heatmap.

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Section 1: pandas

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)

print("Pandas DataFrame Example:\n", df)

# Selecting a specific column
print("\nSelect 'Name' Column:\n", df['Name'])

# Grouping by and calculating mean salary by Age
mean_salary_by_age = df.groupby('Age')['Salary'].mean()
print("\nMean Salary by Age:\n", mean_salary_by_age)

# Handling missing data
df_with_nan = df.copy()
df_with_nan.loc[1, 'Salary'] = np.nan
print("\nDataFrame with NaN:\n", df_with_nan)
df_filled = df_with_nan.fillna(df_with_nan['Salary'].mean())
print("\nNaN Filled with Mean Salary:\n", df_filled)


# Section 2: numpy

# Create an array
arr = np.array([1, 2, 3, 4, 5])

print("\nNumpy Array:\n", arr)

# Reshape the array to 2x3
arr_reshaped = np.reshape(np.arange(6), (2, 3))
print("\nReshaped Array (2x3):\n", arr_reshaped)

# Element-wise operations
arr_squared = np.sqrt(arr)
print("\nElement-wise Square Root of Array:\n", arr_squared)

# Basic statistics
mean_arr = np.mean(arr)
std_arr = np.std(arr)
print("\nMean of Array:", mean_arr)
print("Standard Deviation of Array:", std_arr)


# Section 3: matplotlib

# Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)')
plt.title("Sine Function")
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.grid(True)
plt.legend()
plt.show()

# Bar Chart
plt.figure(figsize=(7, 5))
plt.bar(df['Name'], df['Salary'])
plt.title("Salary by Person")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

# Scatter Plot
x = np.random.random(100)
y = np.random.random(100)

plt.figure(figsize=(7, 5))
plt.scatter(x, y, c='r', label='Random Scatter')
plt.title("Random Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(7, 5))
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()

# Heatmap (using numpy data)
matrix = np.random.rand(10, 10)

plt.figure(figsize=(7, 5))
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.title("Heatmap Example")
plt.colorbar()
plt.show()
