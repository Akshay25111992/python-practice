# Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"]
# #Expected output : [1, 2, 3, 4, 5]
strings = ["1", "2", "3", "4", "5"]
list_of_int = []
for s in strings:
    list_of_int.append(int(s))

# Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7]
# Expected output :[13, 16]

numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = []
for n in numbers:
    if n > 10:
        greater_than_10.append(n)

# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# Expected output :[1, 4, 9, 16, 25]
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened_list = []
for row in matrix:
    for item in row:
        flattened_list.append(item)

# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# Expected output : {'a': 1, 'b': 2, 'c': 3}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result_dict = {}
for i in range(len(keys)):
    result_dict[keys[i]] = values[i]

# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
# Expected output : {'Alice': 85, 'Charlie': 90}

scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
high_scorers = {}
for student, score in scores.items():
    if score > 80:
        high_scorers[student] = score
