# 1. Define a class Person with attributes name and age.
# Create an instance of this class and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 25)
print(f"Name: {person.name}, Age: {person.age}")


# 2. Write a Python class named BankAccount with attributes like account_number,
# balance, and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance


account = BankAccount("123456", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()


# 3. Create a class Book with a class method from_string() that creates a Book instance
# from a string. And print both attributes of the class.
# book = Book.from_string("Python Programming, John Doe")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_string):
        title, author = book_string.split(", ")
        return cls(title, author)


book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}, Author: {book.author}")


# 4. Create a base class Animal with a method sound().
# Create subclasses Dog and Cat that overrides the sound() method and call those methods.

class Animal:
    def sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()


# 5. Write a code to perform multiple inheritance.

class Father:
    def skills(self):
        print("Gardening, Programming")


class Mother:
    def skills(self):
        print("Cooking, Art")


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports, Music")


child = Child()
child.skills()

