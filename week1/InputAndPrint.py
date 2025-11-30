# Write a program that asks the user for their name and then prints a greeting   message using their name.

name = input("Please enter your name: ")

print(f"Hello, {name}!")

# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
multiplication_result = num1 * num2
division_result = num1 / num2

#  Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.

names_input = input("Enter names separated by commas: ")
names_list = names_input.split(",")
print("List of names:", names_list)

#  Ask the user to enter their age and check if they are eligible to vote based on their age.

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# For value = 3.14159, Using f-string print output for only up to 2 decimal places.

value = 3.14159
print(f"Value up to 2 decimal places: {value:.2f}")
