
# Lab 3: Python Conditions

## Introduction
In this lab, you'll learn how to use Python's conditional statements to execute certain blocks of code only when specific conditions are met. The primary conditionals in Python are `if`, `elif`, and `else`. We'll also cover the **ternary operator**, which is a shorthand way of writing conditional statements.

## Objectives
- Learn to use `if` statements for decision-making.
- Understand the use of `elif` for multiple conditions.
- Implement `else` to execute a block of code when no other conditions are met.
- Learn to use the **ternary operator** for concise conditionals.

---

## 1. **Basic `if` Statement**

The `if` statement allows you to run code only if a certain condition is true.

### Example:
```python
age = 18

if age >= 18:
    print("You are an adult.")
```

### Task:
- Write a Python program that checks if a number is positive. If the number is positive, print `"This is a positive number."`.

---

## 2. **`if`-`else` Statement**

The `else` statement allows you to execute a block of code when the `if` condition is false.

### Example:
```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Task:
- Write a Python program that checks if a number is positive or negative. If the number is positive, print `"Positive number"`. If it is negative, print `"Negative number"`.

---

## 3. **`if`-`elif`-`else` Statement**

The `elif` (short for "else if") allows you to check multiple conditions sequentially. If one of the conditions is true, its block of code will be executed, and the rest will be ignored.

### Example:
```python
grade = 85

if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
else:
    print("You got a C.")
```

### Task:
- Write a Python program that assigns a letter grade based on the following rules:
  - `A` if the grade is 90 or above.
  - `B` if the grade is between 80 and 89.
  - `C` if the grade is between 70 and 79.
  - `D` if the grade is between 60 and 69.
  - `F` if the grade is below 60.

---

## 4. **Multiple Conditions Using Logical Operators**

Sometimes, you might want to check multiple conditions in the same `if` statement using logical operators like `and`, `or`, and `not`.

### Example:
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")
```

### Task:
- Write a Python program that checks if a person is eligible for a driver's license:
  - The person must be at least 18 years old **and** have a driving test score of 70 or more.

---

## 5. **Nested `if` Statements**

You can also nest `if` statements inside each other to check more detailed conditions.

### Example:
```python
age = 18
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")
```

### Task:
- Write a Python program that checks if a number is positive or negative, and if positive, also check if it's greater than 100.

---

## 6. **Ternary Operator (Conditional Expression)**

The **ternary operator** is a shorthand way to write simple `if-else` conditions in a single line. The syntax is:
```python
value_if_true if condition else value_if_false
```

### Example:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

### Task:
- Write a Python program that checks whether a number is odd or even using a ternary operator.

### Task Example:
```python
number = 5
result = "Even" if number % 2 == 0 else "Odd"
print(result)  # Output: Odd
```

