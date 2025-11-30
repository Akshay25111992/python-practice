# Write a program that takes the input from the user and checks if a number is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
string = input("Enter a string: ")
reversed_string = ""
for num in range(len(string) - 1, -1, -1):
    reversed_string = string[num] + reversed_string
print(f"Reversed string: {reversed_string}")

if string == reversed_string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
N = int(input("Enter the value of N: "))
fib_sequence = []
a, b = 0, 1
for _ in range(N):
    fib_sequence.append(a)
    a, b = b, a + b
print(f"First {N} numbers of the Fibonacci sequence: {fib_sequence}")

# From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]

nums = [1, 2, 3, 4, 5]
result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            result.append([nums[i], nums[j]])
print(f"Pairs that add up to 9: {result}")

# Print all even numbers between 1 and 20 using a while loop.
count = 1
even_numbers = []
while count <= 20:
    if count % 2 == 0:
        even_numbers.append(count)
    count += 1
print(f"Even numbers between 1 and 20: {even_numbers}")

# Find the first occurrence of a number in a list and stop further searching.
numbers = [10, 20, 30, 40, 50]
search_for = 30
for index in range(len(numbers)):
    if numbers[index] == search_for:
        print(f"First occurrence of {search_for} found at index: {index}")
        break

# Using continue statement, print only the odd numbers from 1 to 10.
odd_numbers = []
for num in range(1, 11):
    if num % 2 == 0:
        continue
    odd_numbers.append(num)
print(f"Odd numbers between 1 and 10: {odd_numbers}")

# What will be the output
# for i in range(5):
#     if i == 3:
#         pass
#     print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.

day = input("Enter a day of the week: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is a weekday.")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is a weekend.")
    case _:
        print("Invalid day entered.")

