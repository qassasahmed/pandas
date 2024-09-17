# Basic if
age = 18

if age >= 18:
    print("You are an adult.")

# if else
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else
grade = 85

if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
else:
    print("You got a C.")

# Multiple conditions
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")

# Nested if
age = 18
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")

# Tenrary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

