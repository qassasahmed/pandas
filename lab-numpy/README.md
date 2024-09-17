
# Lab 6: NumPy

## Introduction
NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and functions to perform mathematical operations on these data structures efficiently. In this lab, you'll learn the basics of using NumPy to create and manipulate arrays.
---

## 1. **Importing NumPy**

Before using NumPy, you need to import it into your Python environment. It is common to import NumPy with the alias `np`.

### Example:
```python
import numpy as np
```

### Task:
- Write a Python program that imports the NumPy library using the alias `np`.

---

## 2. **Creating Arrays**

NumPy arrays are central to NumPy. They can be created using functions like `np.array()`, `np.zeros()`, `np.ones()`, and `np.arange()`.

### Example:
```python
# Create an array from a list
arr = np.array([1, 2, 3, 4])
print(arr)

# Create an array of zeros
zeros = np.zeros((2, 3))  # 2x3 array of zeros
print(zeros)

# Create an array with a range of numbers
arr_range = np.arange(10)
print(arr_range)
```

### Task:
- Write a Python program that creates a 3x3 array of ones using NumPy.

---

## 3. **Array Operations**

You can perform element-wise operations (addition, subtraction, multiplication, etc.) on NumPy arrays, just like you would with scalars.

### Example:
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
result = arr1 + arr2
print(result)  # Output: [5 7 9]
```

### Task:
- Write a Python program that multiplies two NumPy arrays element-wise.

---

## 4. **Indexing and Slicing**

You can access elements of a NumPy array using indexing and slicing, similar to Python lists.

### Example:
```python
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[2])  # Output: 30

# Slicing
print(arr[1:4])  # Output: [20 30 40]
```

### Task:
- Write a Python program that slices a 2D NumPy array to extract the first two rows.

---

## 5. **Reshaping Arrays**

The `reshape()` function allows you to change the shape of an array without changing its data.

### Example:
```python
arr = np.arange(12)  # Create an array of 12 numbers
reshaped_arr = arr.reshape(3, 4)  # Reshape to a 3x4 array
print(reshaped_arr)
```

### Task:
- Write a Python program that reshapes a 1D array of size 9 into a 3x3 matrix.

---

## 6. **Mathematical and Statistical Functions**

NumPy provides a variety of mathematical functions like `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, and more to perform calculations on arrays.

### Example:
```python
arr = np.array([1, 2, 3, 4, 5])

# Sum of all elements
print(np.sum(arr))  # Output: 15

# Mean of elements
print(np.mean(arr))  # Output: 3.0

# Maximum and Minimum
print(np.max(arr))  # Output: 5
print(np.min(arr))  # Output: 1
```

### Task:
- Write a Python program that calculates the mean and standard deviation of a NumPy array.
