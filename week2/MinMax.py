# Find the Maximum and Minimum Values in a List
# numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
# Expected Output: Max = 79, Min = 1

numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
max_value = max(numbers)
min_value = min(numbers)


# Given a set of numbers, find the maximum and minimum values.
# setn = {5, 10, 3, 15, 2, 20}
# Expected Output: Max = 20, Min = 2

setn = {5, 10, 3, 15, 2, 20}
max_set = max(setn)
min_set = min(setn)


# Write a Python function that takes a list of strings as input and returns a tuple
# containing the shortest and longest word from the list, in that order.
# If there are multiple words of the same shortest or longest length,
# return the first shortest/longest word found.
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')

def find_shortest_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)


words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = find_shortest_longest(words)
print(result)

