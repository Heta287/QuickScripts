# Matplotlib Comprehensive Function Examples

'''
Notebook contains:
Basic Line Plot: Simple line plot using plot().
Customizing Line Styles: Demonstrating different line styles, colors, and labels.
Bar Plot: Vertical bar plot with categories.
Horizontal Bar Plot: Horizontal bar chart.
Scatter Plot: Scatter plot of random data points.
Histogram: Histogram with bins and customized colors.
Pie Chart: Circular pie chart with labels and percentage.
Box Plot: Boxplot showing the distribution of data.
Subplots: Multiple plots in a single figure using subplot().
Heatmap: Visualizing a 2D matrix using imshow().
Contour Plot: Contour plot using contour().
3D Plot: 3D surface plot using Axes3D.
Plot Annotations: Adding annotations to a plot.
Logarithmic Scales: Logarithmic axes.
Polar Plot: Plotting data in polar coordinates.
'''


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# 1. Basic Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis (sin(x))")
plt.grid(True)
plt.show()

# 2. Customizing Line Styles
plt.figure(figsize=(8, 4))
plt.plot(x, y, linestyle='--', color='r', label='Dashed Red Line')
plt.plot(x, np.cos(x), linestyle='-', color='b', label='Solid Blue Line')
plt.title("Customized Line Styles")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 3. Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 8]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color='teal')
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()

# 4. Horizontal Bar Plot
plt.figure(figsize=(8, 4))
plt.barh(categories, values, color='orange')
plt.title("Horizontal Bar Plot")
plt.xlabel("Value")
plt.ylabel("Category")
plt.show()

# 5. Scatter Plot
x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)

plt.figure(figsize=(8, 4))
plt.scatter(x_scatter, y_scatter, c='purple')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 6. Histogram
data = np.random.randn(1000)

plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 7. Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightblue', 'lightgreen', 'lightcoral']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.show()

# 8. Box Plot
data_box = [np.random.rand(50) * 100, np.random.rand(50) * 80, np.random.rand(50) * 90]

plt.figure(figsize=(8, 4))
plt.boxplot(data_box)
plt.title("Box Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()

# 9. Subplots
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y, 'r')
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.bar(categories, values, color='b')
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.scatter(x_scatter, y_scatter, c='g')
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.hist(data, bins=20, color='m')
plt.title("Plot 4")

plt.tight_layout()
plt.show()

# 10. Heatmap
matrix = np.random.rand(10, 10)

plt.figure(figsize=(8, 4))
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap Example")
plt.show()

# 11. Contour Plot
x_contour = np.linspace(-3.0, 3.0, 100)
y_contour = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x_contour, y_contour)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(8, 4))
plt.contour(X, Y, Z)
plt.title("Contour Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 12. 3D Plot (requires mpl_toolkits)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot Example")
plt.show()

# 13. Plot Annotations
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Annotated Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis (sin(x))")
plt.annotate('Local Max', xy=(np.pi / 2, 1), xytext=(2, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.grid(True)
plt.show()

# 14. Logarithmic Scales
x_log = np.logspace(0.1, 2, 100)
y_log = np.log(x_log)

plt.figure(figsize=(8, 4))
plt.plot(x_log, y_log)
plt.xscale('log')
plt.yscale('log')
plt.title("Logarithmic Scale Plot")
plt.xlabel("Log X-axis")
plt.ylabel("Log Y-axis")
plt.grid(True)
plt.show()

# 15. Polar Plot
theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(2 * theta) * np.cos(2 * theta))

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r)
plt.title("Polar Plot Example")
plt.show()
