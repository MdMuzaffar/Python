

# scopes
import random
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
import math
message = 'Muz'


def greet_first(name):
    global message
    message = 'a'


greet_first('muz')
print(message)


# xxargs into function

def multi_user(**user):
    print(user['name'])
    print(user)


multi_user(id=1, name='muzaffar', age=35)

# xargs into function


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
# default argument


def increament(number, by=3):
    return number + by


print(increament(5))

# how to pass argument in function


def greeting(first_name, second_name):
    print(f"Hi {first_name} {second_name}")
    print("Welcome on aboard")


greeting("Muzaffar", "Ahmed")
greeting("Afsar", "Ahmed")

# create basic function


def greet():
    print("Hello world")
    print("Learning Python")


greet()

# print("Hello World")
# x = 1
# y = 2
# Unit_Price = 3

# print("Hello World")

# course = "Python Programming"
# print(len(course))

# # For Loop

# for number in range(1, 4):
#     print("number", number + 1, (number + 1) * ".")

# # count even number under 10
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"we have {count} even numbers")


# String methods

x = 1
x = 1.1
x = 1+2j
print(10+3)
print(10-3)
print(10 % 3)
print(10 / 3)
print(10*3)

# working with numbers
print(round(2.9))
print(abs(-2.9))
print((2.0))
print(math.ceil(3.4))

# TYPE Cenversion
# x = input("x")

# y = x + 1

# cONTRIL fLOW
# Fundamentals of programming

# Comparison Operators
# Conditional Statements

templature = 15

if templature > 30:
    print("It's Warm")
    print("Drink water")
elif templature > 20:
    print("It's Nice")
else:
    print("It's Cold")
print("Done")

# Ternary Operator

age = 12

# if age > 18:
#     print("Eligable")
# else:
#     print("Not Eligable")

# age1 = 20
# if age1 > 18:
#     message = "Eligable1"
# else:
#     message = "Not Eligable1"

# message2 = "Eligable2" if age1 >= 18 else "Not Eligable2"

# print(message)
# print(message2)

# # Logical Operators

# high_income = False
# good_income = True
# student = False

# if (high_income and good_income) or not student:
#     print("Eligable")
# else:
#     print("Not Eligable")

# short-circuit Evaluation

# chaining comparition operator
# age should be bewteen 18 and 65
age = 16
# if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligable age")
# else:
#     print("Age Not_Eligable")

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# # For Loops

# for number in range(1, 3):
#     print("Attempt", number, number * ".")

# # For Else

# successfull = False
# for number in range(3):
#     print("Attempt")
#     if successfull:
#         print("successfull")
#         break
# else:
#     print("Attend 3 times successfully")

# Nested Loop

for x in range(5):
    for y in range(2):
        print(f"({x},{y})")


# Iterables

# for x in range(5):
# for x in "python":
for x in [1, 2, 3, 4]:
    print(x)
shopping_cart = ('apple', 'Car')
for item in shopping_cart:
    print(item)

# While loops

# number = 100
# while number > 0:
#     print(number)
#     number //= 2


command = ""

# while command != "quit":
#     command = input(">")
#     print(command)

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")

# -----------------Functions-------------------------

# Defining Function

# 1- Perform a task


def greet():
    print("Hi There")
    print("Welcome aboard")


greet()

# Arguments

# 2- Return a value


def get_greeet(first_name, last_name):
    print(f"{first_name} {last_name}")
    print(last_name)


get_greeet("Muzaffar", "Ahmed")

# Types of functions
# 1- Perform a task
# 2- Return a value

# Keyword Arguments


def increament(number, by):
    return number + by


# result =
print(increament(2, by=1))

# Default Arguments


def default_increament(number, by=1):
    return number + by


print(default_increament(3, 6))

# Xargs


def add_number(a, b):
    print(a+b)


result_fun = add_number(1, 6)
print(result_fun)
# print(result_fun * 5) -- with this we cannt use the this result_fun varialbe


def add_numbers(a, b):
    return a+b


result_return = add_numbers(1, 3)
print(result_return)
print(result_return * 2)

# ---------------return multiple variables | *Args------------------------------------------------


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return (total)


print(multiply(2, 3, 4, 5))

sum_multiply = multiply(2, 3, 4, 5)
print(sum_multiply * 2)


# --------------------**Args---------------------------------------------

def save_user(**User):
    print(User)


save_user(Name="Muzaffar", No=1, age=35)

# ---------------------------Scope------------------------------------

# -----------------------------Debugging---------------------------------

# -------------------------------VSCode Tricks(Windows)-------------

# -----------------------Exercise-------------------------


def fizz_buzz(number):
    # if number % 3 == 0:
    #     print("Fizz")
    # elif number % 5 == 0:
    #     print("Buzz")
    # elif number % 3 == 0 and number % 5 == 0:
    #     print("Fizz & Buzz")
    # else:
    #     print(number)

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return (number)


print(fizz_buzz(5))

# ----------------------- Data Structures (List,Tuples,Ser,Dictionaires)--------------------------------


# letters = ["a", "b", "c"]
# # number = [1, 2, 3]
# combined = letters + number
# print(combined)
# print(list(range(20)))
# print(len(combined))

# ---------------------------- Accesssing Items---------------------------------------------------

# letters[0] = "A"
# print(letters[0:2])
# print(letters)
# numbers = list(range(20))
# print(numbers[:: 3])


# ---------------------List Unpacking------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8]

first, second, *third = numbers

print(first)
# print(second)
print(third)

# -------------------Looping over Lists-----------------------------


letters = ["A", "B", "C"]
for letter in enumerate(letters):
    print(letter)
for index, letter in enumerate(letters):
    print(index, letter)


# --------------------- Adding/Removing Items--------------------------------
#  Add end of the list APPEND

letters.append("D")
print(letters)

# Add items for the specific index use INSERT
letters.insert(0, "-")
print(letters)

# Removing items from the list POP

letters.pop(0)
letters.remove("B")
del letters[0: 1]
letters.clear()
print(letters)

# -------------------------Finding Items from the List-------------------------
letters = ["A", "B", "C"]
print(letters.index("A"))
# print(letters)
if "D" in letters:
    print(letters.index("D"))

    # ----------------------------------Soriting List---------------------------------

numbers_sorts = [2, 5, 3, 7, 9, 1]
numbers_sorts.sort(reverse=True)
print(numbers_sorts)


items = [
    ("product0", 9),
    ("product2", 10),
    ("product1", 8),
    ("product3", 15)

]

items.sort()
print(items)

# -------------------------------------------------Map Function ----------------------------------------------


prices = []
for item in items:
    prices.append(item[0])

print(prices)

x = map(lambda item: item[1], items)
for item in x:
    print("mapping_function", item)

# ---------------------------------------- Filter Function ----------------------------------------------------------

x = list(filter(lambda item: item[1] >= 10, items))
print("Number grater then 10 :", x)

# ---------------------------------------List Comprehension --------------------------------
# -------------------------------- use both MAP and Filter Function------------------------------
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]


filter = list(filter(lambda item: item[1] >= 10, items))
filter = [item[1] for item in items if item[1] >= 10]

# --------------------------------------ZIP Function----------------------------------

list1 = (1, 3, 5)
list2 = (2, 5, 8)

print(list(zip(list1, list2)))
print(list(zip("abcd", list1, list2)))

# ----------------------------------Stack-----------------------------
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session[-1])

# ---------------------Queue-----------------------------

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# ----------------------------------------- tuple(is used for read only we cant modify)-----------------------------
li = [1, 2, 3, "PythonGeeks"]
print(li)  # Output: [1, 2, 3, 'PythonGeeks']

# tuple
tup = (1, 2, 3, "PythonGeeks")
print(tup)  # Output: (1, 2, 3, 'PythonGeeks')
# set
set_0 = {1, 2, 3, "PythonGeeks"}
print(set_0)  # Output: {1, 2, 3, 'PythonGeeks'}


point = [1, 2, 3]
print(point)

x, y, z = point
if 10 in point:
    print("existing")
else:
    print("Not existing")


# -------------------------------------------------------------- Swapping Variables---------------------------

x = 10
y = 11

z = x
x = y
y = z

# x, y = y, x
print("x", x)
print("y", y)
print("z", z)

# ----------------------------------------------List---------------------------------------------


num = array("i", [1, 2, 3, 4, 5])
print(num)
num.append(6)
num.insert(5, 9)
num.pop()
num.remove(2)
print(num)

# ---------------------------------------Sets--------------------------------------------


sets_numbers = [1, 1, 2, 2, 2, 4, 4, 5, 6, 5, 6, 7, 7]
unique = set(sets_numbers)
second = {1, 9}
print(unique)

print(unique | second)
print(unique & second)
print(unique - second)

# --------------------------------Dictionaries---------------------------------------------


points = {"x": 1, "y": 2}
points = dict(x=1, y=2)
points["x"] = 10
points["z"] = 20
if "a" in points:
    print(points["a"])
print(points.get("a", 0))
del points["x"]
print(points)
for x in points.items():
    print("Printing loop", x)
for key in points:
    print(key, points[key])

# ------------------------Dictionary comprehension-------------------------------

values = []

for x in range(5):
    res = values.append(x * 2)
    print(res)

valueDis = [x*3 for x in range(2)]
print(valueDis)
#  0000000000000000000000000----------------------SET-----------------------------------------------
valueSet = {x * 3 for x in range(5)}
print(valueSet)

#  0000000000000000000000000----------------------DICTIONARY-----------------------------------------------
# in dictionary we use key value pairs
valueDictionary = {x:  x * 2 for x in range(5)}
print(valueDictionary)

# ----------------------------------------Generator Expression---------------------------------------------

ValuesGeneratorWithoutExp = [x * 8 for x in range(3)]
for x in ValuesGeneratorWithoutExp:
    print("xxxx", x)

values_with_generator = (x * 3 for x in range(1000))
print("gen:", getsizeof(values_with_generator))
values_with_generator = [x * 3 for x in range(1000)]
print("List:", getsizeof(values_with_generator))


# ---------------------------------------- Unpacking Operator----------------------------------------------------

numbers_unpacking = [1, 2, 3]
# if we add star(*) or 3 Dots(...) before the variable then it will get unpacked
print(*numbers_unpacking)
print(1, 2, 3)

values_pack = list(range(10))
print(values_pack)
values_unpack = [*range(10), *"Hello World"]
print(values_unpack)

sentence = "This is Python practice"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)

pprint(char_frequency, width=1)
# ------------------how to sort--------------

pprint(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))


# ------------------------------------------Exceptions---------------------------------------------

# age = int(input("Age: "))

# ------------------------------- Handling exception-----------------------------------------------

# try:
#     Age_exception = int(input("Age:"))
# except ValueError as ex:
#     print("You didn't enter the correct or valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("Execution completed")
# print("Please continue")


# -----------------------------------------Handling different exception-------------------------
# In this zero cannot be divided
#  combine the same output in one output
# try:
#     print("")
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter the valid age")

#     # ------------or--------------------
# try:
#     print()
# except ValueError:
#     print("You didn't enter the valid age")
# except ZeroDivisionError:
#     print("You didn't enter the valid age")

# -------------------------Cleaning up-------------------------------------------
# in this we will closed the file after we finished so at the end we have to add finally with closed method
# try:
#     print()
#     file = open("app.py")
# except ValueError:
#     print("You didn't enter the valid age")
# except ZeroDivisionError:
#     print("You didn't enter the valid age")
# finally:
#     file.close()

# -----------------------------The with statement------------------------------------------
# use with to open the file as we use with then it dont requited the finally to write for closing file
#    try:
#         with open("app.py") as file:
#             print("File opened")
#     except:
#         print("Opened")


# --------------------------- Raising Exception----------------------------------------------

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can't be zero or Negative")
#     return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# -----------------------cost of raising exceptions----------------------------
# use pass for exception to execute the code in less time(Improving performance)


# def cal_age(age):
#     if age <= 0:
#         return None
#     return 10/age


# xfactor = cal_age(-1)
# if xfactor == None:
#     pass


# ------------------------------------Classes----------------------------------
# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))

# ------------------------------Constructor---------------------------------------

class Point:
    eye_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drow(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)
point.drow()

# -------------------------------- Class Vs Instance Attributes------------------------------------
eye_color = "Blue"

another = Point(3, 4)
another.eye_color = "Brown"
another.drow()
print(another.eye_color)

# -------------------------------- Class Vs Instance Methods------------------------------------


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"your current balance is {amount}")

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"you have insufficient amount{amount}")
        else:
            print(f"you have sufficient amount{amount}")


class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

# ---------------------------------------Magic methods--------------------------------------


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


point = Point(1, 2)
print(point)

# ------------------Comparing objects-----------------------


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other1):
        return self.x == other1.x and self.y == other1.y

    def __gt__(self, other1):
        return self.x > other1.x and self.y > other1.y

# -------------Arithmetic operations------------------------
    def __add__(self, other1):
        return Point(self.x + other1.x, self.y + other1.y)


point1 = Point1(10, 20)
other1 = Point1(1, 2)
print(point1 == other1)
print(point1 > other1)

# --------------------------------------Supporting Arithmetic operations---------------------------------

combined = point1 + other1
print(combined.x + combined.y)


# ----------------------------------Making custom container-----------------------

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag] = self.tags.get(tag, 0)+1


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)

# ---------------------------Private methods------------------------------------
# in private methods we use __tags to keep it private

# -------------------------------------Properties--------------------------------


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(120)
print(product.price)


# -------------------------------------Inheritance-----------------------------
# ---------------Method OverRiding-------------------------
class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
# m.eat()
# print(m.age)
print(m.age)
print(m.weight)

# ---------------------------------------Multilevel Inhertance--------------------------------


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# ------------------------------ Practice Leaning-----------------


class StreamAlreadyOpen(Exception):
    pass


class Stream:
    def __init__(self):
        self.Opened = False

    def open(self):
        if self.Opened:
            raise StreamAlreadyOpen("Already opened")
        self.Opened = True

    def close(self):
        if not self.Opened:
            raise StreamAlreadyOpen("Its closed")
        self.Opened = False


class FileStream(Stream):
    def read(self):
        print("File has been opened")


class NetworkStream(Stream):
    def read(self):
        print("Network has been opened")


file_stream = FileStream()
file_stream.open()
# file_stream.open()
file_stream.read()
file_stream.close()
# file_stream.close()


# ----------------------------------------Method Overriding-----------------------------

# -------------------------------------Practice---------------------------------
# -------------Basic Calculator(Variable , Input/Output, Basic arthmetic)-----------------------/


# num1 = float(input("please enter the number :"))
# num2 = float(input("please enter the number :"))
# operation = input("choose operation(+,-,*,%):")
# if operation == '+':
#     print("Result", num1+num2)
# elif operation == '-':
#     print("Result", num1-num2)
# elif operation == '*':
#     print("Result", num1 * num2)
# else:
#     print("Invalid number")

# -------------------------------Number guessing Game(Loops, COnditionals,Random Module)--------------


# secret = random.randint(1, 10)
# guess = 0
# while guess != secret:
#     guess = int(input("Enter the number bewteen(1-10) :"))
#     if guess < secret:
#         print("Too Low")
#     elif guess > secret:
#         print("Too High")
# print("Matching the number")

# -------------------------------------- Intermediate Projects-------------------------------
# ----------------To-Do List----------------

# tasks = []


# def show_tasks():
#     for i, task in enumerate(tasks, 1):
#         print(f"{i}. {task}")


# while True:
#     choice = input("Add/Remove/Show/Exit: ").lower()
#     if choice == "add":
#         choice = input("Enter task: ")
#         tasks.append(choice)
#     elif choice == "remove":
#         show_tasks()
#         idx = int(input("Enter the task number to remove: ")) - 1
#         tasks.pop(idx)
#     elif choice == "show":
#         show_tasks()
#     elif choice == "exit":
#         break

# start with empty list

# tasks = []


# def show_tasks():
#     if not tasks:
#         print("There is no tasks")
#     else:
#         for i, task in enumerate(tasks, 1):
#             print(f"{i},{task}")


# while True:
#     print("\nOptions: Add / Remove / pop /  sort / Clear / Show / String / Exit")
#     choice = input("Enter the choice: ").lower()

#     if choice == "add":
#         task = input("Enter task: ")
#         tasks.append(task)
#         print(f"successfully added{task}")
#     elif choice == "remove":
#         show_tasks()
#         task = input("which task you want to remove: ")
#         if task in tasks:
#             tasks.remove(task)
#             print(f"Removed task {task}")
#         else:
#             print(f"you have selected invalid task {task}")
#     elif choice == "pop":
#         show_tasks()
#         idx = print(int("Which task you want to remove"))-1
#         if 0 <= idx < int(tasks):
#             removed = tasks.pop(idx)
#             print(f"Task has been removed{removed}")
#         else:
#             print("Invalid task")
#     elif choice == "sort":
#         tasks.sort()
#         print("Tasks has been sorted")
#     elif choice == "clear":
#         tasks.clear()
#         print("All the tasks has bee cleared")


# class Task:
#     def __init__(self, name, priority="Medium", deadline=None):
#         self.name = name
#         self.priority = priority
#         self.deadline = deadline
#         self.completed = False

#     def mark_complete(self):
#         self.completed = True

#     def __str__(self):
#         status = "Done" if self.completed else "Pending"
#         if self.deadline:
#             return f"{self.nake} (priority:{self.priority},deadline:{self.deadline})"
#         else:
#             return f"{self.name}(priority:{self.priority},status:{status})"


# ------------------------------------ Add BankAccount-------------------------------------

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError(f"you have insufficient balance {self.balance}")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be positive")
        self.balance += amount
        print(
            f"amount{self.amount} has been added and current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"you account has less amount")
        self.balance -= amount


account = BankAccount("Muzaffar", 500)
print(account.balance)
