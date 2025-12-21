# Using below list and enumerate(), print index followed by value.
# Input: fruits = ["apple", "banana", "cherry"]
# Output:
# 0 apple
# 1 banana
# 2 cherry

fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)


# Using below dict and enumerate, print key followed by value.
# Input: person = {"name": "Alice", "age": 30, "city": "New York"}
# Output:
# name: Alice
# age: 30
# city: New York

person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")


# Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"],
# use enumerate() to create a list of tuples where each tuple contains the index
# and the corresponding fruit, but only for even indices.
# Output: [(2, 'banana'), (4, 'date')]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
even_index_fruits = [(index, fruit) for index, fruit in enumerate(fruits, start=1) if index % 2 == 0]
print(even_index_fruits)

