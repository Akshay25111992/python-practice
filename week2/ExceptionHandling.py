# Write a Python program that attempts to divide two numbers a = 10, b = 0
# and handles a ZeroDivisionError if the denominator is zero.
# Divide a by b and handle the exception and print the error.

a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")


# Apply exception handling to below code and handle an exception if the index is out of range.
# my_list = [1, 2, 3]
# print(my_list[5])

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}")


# Correct this below code with appropriate exception handlings.
# And finally print "Execution completed"
# def safe_divide(a,b):
#       result = a / b
#       print(f"Result: {result}")
# safe_divide(1,0)
# safe_divide(1,"a")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")

