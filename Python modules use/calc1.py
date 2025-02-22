import numpy as np

# # Create a 1D array
# arr = np.array([1, 2, 3, 4, 5])

# # Print the array and its type
# print("Array:", arr)
# print("Type:", type(arr))

# # Perform operations on the array
# arr_squared = arr ** 2
# print("Squared Array:", arr_squared)

# # Accessing elements
# print("First element:", arr[0])
# print("Last element:", arr[-1])


# # Creating a 1D array
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# # Reshaping to a 2D array
# arr_reshaped = arr.reshape(3, 4)
# print("Reshaped Array:\n", arr_reshaped)

# rand_ints = np.random.randint(1, 100, size=10)
# print("Random Integers:", rand_ints)

# rand_floats = np.random.random(100)
# print("Random Floats:", rand_floats)

# rand_norm = np.random.randn(10)
# print("Random Numbers from Normal Distribution:", rand_norm)




# # Creating an array
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Applying a condition to filter elements
# filtered_arr = arr[arr > 5]
# print("Filtered Array (elements > 5):", filtered_arr)

# # Setting elements based on condition
# arr[arr > 5] = 0
# print("Array after setting elements > 5 to 0:", arr)


# Creating a 2D array
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing rows and columns
row_slice = arr_2d[1, :]
col_slice = arr_2d[:, 2]
sub_array = arr_2d[1:, 1:3]

print("Row Slice (2nd row):", row_slice)
print("Column Slice (3rd column):", col_slice)
print("Sub-array:\n", sub_array)
