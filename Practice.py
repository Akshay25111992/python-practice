message = """Hello, 
World!"""

print(message.find("World"))
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)

print(f"Total even numbers between 1 and 9: {count}")
