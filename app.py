

# scopes
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
