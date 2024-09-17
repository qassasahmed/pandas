# Example of a List
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'apple']

# Modifying the list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple']

# Example of a Tuple
coordinates = (10, 20, 30, 10)
print(coordinates)  # Output: (10, 20, 30, 10)

# Tuples are immutable, so the following line will raise an error:
# coordinates[1] = 50  # Uncommenting this line will raise a TypeError

# Example of a Set
numbers = {1, 2, 3, 1, 4}
print(numbers)  # Output: {1, 2, 3, 4} (duplicate "1" is automatically removed)

# Adding and removing items from a set
numbers.add(5)
print(numbers)  # Output: {1, 2, 3, 4, 5}

numbers.remove(2)
print(numbers)  # Output: {1, 3, 4, 5}

# Example of a Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing and modifying values
print(person["name"])  # Output: Alice
person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

