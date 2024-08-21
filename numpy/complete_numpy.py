# Numpy Comprehensive Function Examples

'''
Notebook contains:
Array Creation: Creating arrays using np.array(), np.zeros(), np.ones(), np.arange(), np.random().
Array Properties: Checking array shape, size, and data types.
Array Indexing and Slicing: Accessing array elements and sub-arrays.
Reshaping Arrays: Reshaping and flattening arrays.
Element-wise Operations: Applying mathematical operations element-wise.
Broadcasting: Demonstrating broadcasting of smaller arrays.
Mathematical Functions: Sum, mean, standard deviation, min/max, and more.
Matrix Operations: Dot product, transpose, and matrix inverse.
Random Functions: Creating arrays of random values and random integers.
Sorting and Searching: Sorting arrays and searching for values.
Linear Algebra: Solving linear equations.
Saving and Loading Data: Saving and loading numpy arrays.
'''


# Import numpy
import numpy as np

# 1. Array Creation
# Create a 1D array from a list
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr_1d)

# Create a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr_2d)

# Create an array of zeros
arr_zeros = np.zeros((2, 3))
print("\nArray of Zeros:\n", arr_zeros)

# Create an array of ones
arr_ones = np.ones((3, 3))
print("\nArray of Ones:\n", arr_ones)

# Create an array with a range of values
arr_range = np.arange(0, 10, 2)
print("\nArray with Range (0 to 10, step 2):\n", arr_range)

# Create an array of random values between 0 and 1
arr_random = np.random.random((3, 3))
print("\nRandom Array (3x3):\n", arr_random)

# 2. Array Properties
# Shape of the array
print("\nShape of arr_2d:", arr_2d.shape)

# Size of the array (number of elements)
print("Size of arr_2d:", arr_2d.size)

# Data type of the array
print("Data type of arr_2d:", arr_2d.dtype)

# 3. Array Indexing and Slicing
# Indexing in 1D array
print("\nElement at index 2 of arr_1d:", arr_1d[2])

# Indexing in 2D array
print("Element at row 1, column 2 of arr_2d:", arr_2d[1, 2])

# Slicing 1D array
print("\nSlicing arr_1d (from index 1 to 3):\n", arr_1d[1:4])

# Slicing 2D array
print("Slicing arr_2d (first two rows and first two columns):\n", arr_2d[:2, :2])

# 4. Reshaping Arrays
# Reshape a 1D array to 2D array
arr_reshaped = np.reshape(arr_1d, (5, 1))
print("\nReshaped 1D Array to 2D (5x1):\n", arr_reshaped)

# Flatten a 2D array to 1D array
arr_flattened = arr_2d.flatten()
print("\nFlattened 2D Array to 1D:\n", arr_flattened)

# 5. Element-wise Operations
# Add scalar to an array
arr_add = arr_1d + 5
print("\nAdd 5 to each element of arr_1d:\n", arr_add)

# Multiply scalar with array
arr_multiply = arr_1d * 2
print("Multiply arr_1d by 2:\n", arr_multiply)

# Element-wise addition of two arrays
arr_sum = arr_1d + np.array([5, 4, 3, 2, 1])
print("\nElement-wise addition of two arrays:\n", arr_sum)

# Element-wise square root
arr_sqrt = np.sqrt(arr_1d)
print("Element-wise square root of arr_1d:\n", arr_sqrt)

# 6. Broadcasting
# Broadcasting example: adding a scalar to a 2D array
arr_broadcast = arr_2d + 10
print("\nBroadcasting Example (adding 10 to arr_2d):\n", arr_broadcast)

# Broadcasting with different shapes
arr_broadcast_diff = arr_2d + np.array([1, 2, 3])
print("\nBroadcasting Example with different shapes:\n", arr_broadcast_diff)

# 7. Mathematical Functions
# Sum of all elements
sum_all = np.sum(arr_2d)
print("\nSum of all elements in arr_2d:", sum_all)

# Sum along a specific axis
sum_axis_0 = np.sum(arr_2d, axis=0)  # Column-wise sum
print("Sum along axis 0 (column-wise sum):\n", sum_axis_0)

sum_axis_1 = np.sum(arr_2d, axis=1)  # Row-wise sum
print("Sum along axis 1 (row-wise sum):\n", sum_axis_1)

# Mean of the array
mean_arr = np.mean(arr_2d)
print("\nMean of arr_2d:", mean_arr)

# Standard deviation
std_arr = np.std(arr_2d)
print("Standard deviation of arr_2d:", std_arr)

# Maximum and minimum values
max_value = np.max(arr_2d)
min_value = np.min(arr_2d)
print("\nMax value in arr_2d:", max_value)
print("Min value in arr_2d:", min_value)

# 8. Matrix Operations
# Dot product of two matrices
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr_a, arr_b)
print("\nDot Product of arr_a and arr_b:\n", dot_product)

# Transpose of a matrix
arr_transpose = np.transpose(arr_a)
print("Transpose of arr_a:\n", arr_transpose)

# Inverse of a matrix (using np.linalg.inv)
arr_square = np.array([[1, 2], [3, 4]])
arr_inverse = np.linalg.inv(arr_square)
print("\nInverse of arr_square:\n", arr_inverse)

# 9. Random Functions
# Random integers within a range
arr_randint = np.random.randint(0, 10, size=(3, 3))
print("\nRandom Integer Array (3x3) between 0 and 10:\n", arr_randint)

# Random values from a normal distribution
arr_normal = np.random.randn(3, 3)
print("\nRandom Array from Normal Distribution (3x3):\n", arr_normal)

# 10. Sorting and Searching
# Sorting an array
arr_unsorted = np.array([5, 2, 9, 1, 5, 6])
arr_sorted = np.sort(arr_unsorted)
print("\nSorted Array:\n", arr_sorted)

# Find indices of the sorted array
arr_sorted_indices = np.argsort(arr_unsorted)
print("Indices of the sorted array:\n", arr_sorted_indices)

# Searching for elements
search_index = np.where(arr_1d == 3)
print("\nIndex where arr_1d == 3:", search_index)

# Check conditions in an array
arr_conditional = np.where(arr_1d > 3, 'Greater', 'Lesser or Equal')
print("Conditional Check in arr_1d:\n", arr_conditional)

# 11. Linear Algebra
# Solving a system of linear equations
coefficients = np.array([[3, 1], [1, 2]])
constants = np.array([9, 8])
solution = np.linalg.solve(coefficients, constants)
print("\nSolution of linear equations:\n", solution)

# 12. Saving and Loading Data
# Save array to a file
np.save('array_file.npy', arr_1d)
print("\nArray saved to 'array_file.npy'")

# Load array from file
loaded_array = np.load('array_file.npy')
print("Loaded Array from file:\n", loaded_array)

