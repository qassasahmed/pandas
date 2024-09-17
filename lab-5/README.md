
# Lab 5: Functions

## Introduction
Functions are _reusable_ blocks of code that perform a specific task. They help make your code modular, easier to understand, and reduce repetition. In this lab, you will learn how to define and use functions in Python.

## 1. **Defining a Function**

Functions in Python are defined using the `def` keyword. A function may take inputs (arguments) and may return a result using the `return` statement.

### Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Output: Hello, John!
```

### Task:
- Write a function `square(number)` that returns the square of the number passed to it.

---

## 2. **Positional and Keyword Arguments**

When calling functions, you can pass arguments by position or by keyword.

### Example:
```python
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old.")

introduce("Alice", 25)                # Positional arguments
introduce(age=30, name="Bob")          # Keyword arguments
```

### Task:
- Write a function `calculate_area(length, width)` that returns the area of a rectangle.

---

## 3. **Return Values**

Functions can return values using the `return` statement. If no `return` is specified, the function returns `None` by default.

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Task:
- Write a function `is_even(number)` that returns `True` if the number is even, and `False` otherwise.

---

## 4. **Default Parameters**

You can specify default values for function arguments. These default values are used if no value is passed during the function call.

### Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()            # Output: Hello, Guest!
greet("Alice")     # Output: Hello, Alice!
```

### Task:
- Write a function `power(base, exponent=2)` that returns the value of `base` raised to the power of `exponent`. If no exponent is provided, the function should return the square of the base.

---

## 5. **Variable-Length Arguments**

Python functions can accept a variable number of arguments using `*args` (for positional arguments) and `**kwargs` (for keyword arguments).

### Example (`*args`):
```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10
```

### Example (`**kwargs`):
```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")
```

### Task:
- Write a function `multiply_all(*numbers)` that returns the product of all the numbers passed as arguments.

---

## 6. **Lambda Functions**

Lambda functions (anonymous functions) are small, one-line functions that don't require a `def` keyword. They are commonly used for short, simple operations.

### Example:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

### Task:
- Write a lambda function `add` that takes two numbers and returns their sum. Use it to add `10` and `20`.
