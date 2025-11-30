# Given a list of numbers, find and print the maximum and minimum values.

nums = [1, 2, 3, 4, 5]
max_value = max(nums)
min_value = min(nums)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Given two lists below, merge the values from both lists to one and print

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
print(f"Merged List: {a}")

# From a list, print the number of times the value 3 appears in the list:

a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count_3 = a.count(3)

print(f"The value 3 appears {count_3} times in the list.")

# From below list, Sort the list and print

a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print(f"Sorted List: {a}")

# Given a set, add the element 6 to it and print the updated set.

a = {1, 2, 3, 4, 5}
a.add(6)
print(f"Updated Set: {a}")

# Given a set, remove the element 3 from it and print the updated set.

numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(f"Set after removing 3: {numbers}")

# Given two sets, find and print their intersection.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print(f"Intersection: {intersection}")

# Given a tuple, count and print the number of occurrences of the element 'apple'.

fruits = ('apple', 'banana', 'orange', 'apple', 'kiwi', 'apple')
apple_count = fruits.count('apple')
print(f"Number of occurrences of 'apple': {apple_count}")

# Given two tuples, concatenate them and print the result.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2
print(f"Concatenated Tuple: {concatenated_tuple}")

# Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
age = person["age"]
print(f"Age: {age}")

# Add new key,  gender to dictionary and assign “M” to it and print
person["gender"] = "M"
print(f"Updated Dictionary: {person}")

# Remove the key "city" from the above Dict and print
del person["city"]
print(f"Dictionary after removing city: {person}")

#  Given two dictionaries, merge them into one

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(f"Merged Dictionary: {dict1}")
