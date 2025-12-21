# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10 numbers
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))


# 2. Write a generator function called infinite_multiples(n) that yields multiples
# of the given base value indefinitely.
# Input n=3
# Output:
# 3
# 6
# 9
# 12
# 15
# …

def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


multiples_gen = infinite_multiples(3)
for _ in range(5):
    print(next(multiples_gen))


# 3. Write a generator function called repeat_word(word, times) that yields
# the given character char a specified number of times.
# word = "hello"
# times = 5

def repeat_word(word, times):
    for _ in range(times):
        yield word


word = "hello"
times = 5

for w in repeat_word(word, times):
    print(w)

