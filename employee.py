import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
# cursor.execute("""

# CREATE TABLE IF NOT EXISTS employee(
#     id INTIGER PRIMARY KEY AUTOINCREAMENT,
#     name TEXT NOT NULL,
#     department TEXT NOT NULL,

#                )

# """)

for i in range(5):
    print("Number:", i)


def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10, 2)

# your_age = int(input("Please enter your age :"))
# print(f"You said your age is {your_age}")
# print(your_age + 3)

age_text = input("Please enter you age :")

try:
    age_number = int(age_text)
    print(f"Next year, your age will be {age_number + 1}")

except ValueError:
    print("That was not a valid number")

print("Line 1\nMuzaffar Ahmed 2\t38yrs")
