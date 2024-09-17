# Python Collections

In Python, collections are used to store multiple items in a single variable. Python provides four main types of collections: **Lists**, **Tuples**, **Dictionaries**, and **Sets**. Each of these collections has its own characteristics in terms of mutability, ordering, and uniqueness.

## 1. Lists
- **Definition**: Lists are ordered, mutable collections of items. Items in a list can be of any data type, and lists can contain duplicates.
- **Syntax**: `[]`

```python
my_list = ["apple", "banana", "cherry"]
```

### Characteristics:
- **Mutable**: Yes, you can modify, add, or remove items from a list.
- **Ordered**: Yes, items have a defined order, and the order will not change unless explicitly modified.
- **Unique**: No, lists can contain duplicate values.

---

## 2. Tuples
- **Definition**: Tuples are ordered, immutable collections of items. Like lists, items in a tuple can be of any data type, and tuples can contain duplicates.
- **Syntax**: `()`

```python
my_tuple = ("apple", "banana", "cherry")
```

### Characteristics:
- **Mutable**: No, once a tuple is created, you cannot change its content.
- **Ordered**: Yes, items in a tuple maintain their order.
- **Unique**: No, tuples can contain duplicate values.

---

## 3. Dictionaries
- **Definition**: Dictionaries store data as key-value pairs, where each key must be unique. Values, however, can be duplicated. Dictionaries are mutable and unordered (prior to Python 3.7, where they became ordered).
- **Syntax**: `{}`

```python
my_dict = {"name": "Alice", "age": 25}
```

### Characteristics:
- **Mutable**: Yes, you can modify, add, or remove key-value pairs.
- **Ordered**: Yes (as of Python 3.7+). In earlier versions, dictionaries were unordered.
- **Unique**: Keys must be unique, but values can be duplicated.

---

## 4. Sets
- **Definition**: Sets are unordered collections of unique items. They are mutable but do not allow duplicate values.
- **Syntax**: `{}`

```python
my_set = {1, 2, 3}
```

### Characteristics:
- **Mutable**: Yes, you can modify a set (e.g., add or remove items), but it cannot contain duplicates.
- **Ordered**: No, sets are unordered.
- **Unique**: Yes, sets do not allow duplicate values.

---

## Summary Table

| Collection  | Mutable | Ordered | Unique |
|-------------|---------|---------|--------|
| **List**    | Yes     | Yes     | No     |
| **Tuple**   | No      | Yes     | No     |
| **Dictionary** | Yes  | Yes*    | Keys: Yes, Values: No |
| **Set**     | Yes     | No      | Yes    |

\*Dictionaries are ordered as of Python 3.7+.

---

Understanding these characteristics will help you choose the right collection type for your data needs.

