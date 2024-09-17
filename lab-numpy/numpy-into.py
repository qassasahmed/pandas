import numpy as np

# creating arrays
ones_array = np.ones((3, 3))
print(ones_array)

# array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# element-wise multiplication
result = arr1 * arr2
print(result)  # Output: [4 10 18]

#indexinn and slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# slicing to extract the first two rows
sliced_arr = arr[:2, :]
print(sliced_arr)

# reshaping arrays
arr = np.arange(9)  # Create an array with elements 0 to 8
reshaped_arr = arr.reshape(3, 3)
print(reshaped_arr)

arr = np.array([1, 2, 3, 4, 5])

# calculate mean and standard deviation
mean = np.mean(arr)
std_dev = np.std(arr)

print(f"Mean: {mean}, Standard Deviation: {std_dev}")
