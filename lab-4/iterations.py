# for loop
string = "Python"
for char in string:
    print(char)
# while loop
count = 1
while count <= 10:
    print(count)
    count += 1
# iterate over a collection
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# continue and break
for number in range(1, 11):
    if number == 5:
        continue
    print(number)

# range() function
for number in range(10):
    print(number)

# nested loop
for i in range(3):
    for j in range(3):
        print(f"{i}, {j}")
