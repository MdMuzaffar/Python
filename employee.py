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
