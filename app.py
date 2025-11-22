

# scopes
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

if age > 18:
    print("Eligable")
else:
    print("Not Eligable")

age1 = 20
if age1 > 18:
    message = "Eligable1"
else:
    message = "Not Eligable1"

message2 = "Eligable2" if age1 >= 18 else "Not Eligable2"

print(message)
print(message2)

# Logical Operators

high_income = False
good_income = True
student = False

if (high_income and good_income) or not student:
    print("Eligable")
else:
    print("Not Eligable")

# short-circuit Evaluation

# chaining comparition operator
# age should be bewteen 18 and 65
age = 16
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligable age")
else:
    print("Age Not_Eligable")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# For Loops

for number in range(1, 3):
    print("Attempt", number, number * ".")

# For Else

successfull = False
for number in range(3):
    print("Attempt")
    if successfull:
        print("successfull")
        break
else:
    print("Attend 3 times successfully")

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
