
# Lab 4: Loops and Iterations

## Introduction
In this lab, you will learn how to use loops in Python to **repeat blocks of code**. Loops are essential for iterating over _sequences_ (like lists and  tuples) or repeating actions a specific number of times. The two main types of loops in Python are the `for` loop and the `while` loop.

## 1. **`for` Loop**

A `for` loop allows you to iterate over a sequence of elements, such as a list or a string.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Task:
- Write a Python program that prints each character of the string `"Python"`.

---

## 2. **`while` Loop**

A `while` loop continues to execute as long as the condition is `True`. If the condition becomes `False`, the loop will stop.

### Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Task:
- Write a Python program that prints numbers from 1 to 10 using a `while` loop.

---

## 3. **Iterating Over Different Data Structures**

Python's loops can be used to iterate over various types of data structures, such as lists, dictionaries, and sets.

### Example (Lists):
```python
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
```

### Example (Dictionaries):
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
```

### Task:
- Write a Python program to iterate over a dictionary and print both the keys and values.

---

## 4. **`break` and `continue` Statements**

You can use the `break` statement to exit a loop prematurely. The `continue` statement allows you to skip the rest of the current iteration and move on to the next one.

### Example (`break`):
```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

### Example (`continue`):
```python
for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)
```

### Task:
- Write a Python program that prints numbers from 1 to 10 but skips the number 5 using `continue`.

---

## 5. **`range()` Function**

The `range()` function generates a sequence of numbers, which is very useful for looping a specific number of times.

### Example:
```python
for number in range(5):
    print(number)
```

### Task:
- Write a Python program that prints the numbers from 0 to 9 using the `range()` function.

---

## 6. **Nested Loops**

You can place one loop inside another loop to create a **nested loop**. This is useful when dealing with matrices or multi-dimensional data.

### Example:
```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

### Task:
- Write a Python program that prints a 3x3 matrix using nested loops.
