# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulating the Restaurant Sales Data
# We will create a dataset with sales of dishes for each day of the week.
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Pasta': np.random.randint(10, 50, size=7),
    'Pizza': np.random.randint(20, 60, size=7),
    'Burger': np.random.randint(15, 55, size=7),
    'Salad': np.random.randint(5, 30, size=7),
    'Steak': np.random.randint(10, 40, size=7)
}

df = pd.DataFrame(data)
print("Restaurant Sales Data")
print(df)

# 2. Understanding the Data with Pandas
# Viewing basic information about the dataset
print("\nDataset Info:")
df.info()

# Summary statistics of the dataset
print("\nSummary Statistics:")
print(df.describe())

# Accessing columns
print("\nSales of Pasta:")
print(df['Pasta'])

# Filtering data: What were the sales on Saturday?
print("\nSaturday's Sales:")
print(df[df['Day'] == 'Saturday'])

# Adding a Total Sales column
df['Total Sales'] = df[['Pasta', 'Pizza', 'Burger', 'Salad', 'Steak']].sum(axis=1)
print("\nData with Total Sales Column:")
print(df)

# 3. Using Numpy for Analysis
# Calculate the average sales of each dish over the week
average_sales = np.mean(df[['Pasta', 'Pizza', 'Burger', 'Salad', 'Steak']].values, axis=0)
print("\nAverage Sales of Each Dish Over the Week:")
print("Pasta: ", average_sales[0])
print("Pizza: ", average_sales[1])
print("Burger: ", average_sales[2])
print("Salad: ", average_sales[3])
print("Steak: ", average_sales[4])

# Maximum and Minimum Sales
max_sales = np.max(df['Total Sales'])
min_sales = np.min(df['Total Sales'])
print("\nMax Sales in a Day: ", max_sales)
print("Min Sales in a Day: ", min_sales)

# 4. Visualizing Data with Matplotlib
# Plotting the sales of each dish across the days of the week
plt.figure(figsize=(10, 6))
for dish in ['Pasta', 'Pizza', 'Burger', 'Salad', 'Steak']:
    plt.plot(df['Day'], df[dish], marker='o', label=dish)

plt.title("Daily Sales of Dishes")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Sales")
plt.legend()
plt.grid(True)
plt.show()

# 5. Bar Plot: Comparing Total Sales for Each Day
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Total Sales'], color='skyblue')
plt.title("Total Sales per Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Sales")
plt.show()

# 6. Pie Chart: Distribution of Sales Among Different Dishes Over the Week
total_dish_sales = df[['Pasta', 'Pizza', 'Burger', 'Salad', 'Steak']].sum().values
labels = ['Pasta', 'Pizza', 'Burger', 'Salad', 'Steak']

plt.figure(figsize=(7, 7))
plt.pie(total_dish_sales, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title("Proportion of Sales by Dish Over the Week")
plt.show()

# 7. Moving Average with Pandas for Trend Analysis
df['7-Day Moving Average'] = df['Total Sales'].rolling(window=7).mean()
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Total Sales'], label='Total Sales', marker='o')
plt.plot(df['Day'], df['7-Day Moving Average'], label='7-Day Moving Average', linestyle='--')
plt.title("Sales Trend with Moving Average")
plt.xlabel("Day of the Week")
plt.ylabel("Total Sales")
plt.legend()
plt.show()
