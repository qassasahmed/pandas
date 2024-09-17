# simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Output: Hello, John!


# positional and keyword args
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old.")

introduce("Alice", 25)                # Positional arguments
introduce(age=30, name="Bob")          # Keyword arguments


# return values
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


# default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()            # Output: Hello, Guest!
greet("Alice")     # Output: Hello, Alice!


# variable length args
## *args
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10


## **kwargs
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")


# lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25
