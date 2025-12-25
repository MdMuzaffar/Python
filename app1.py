import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import string
import random
from datetime import datetime
from pathlib import Path
import json
import sqlite3

# --------------------------Import Browser-------------------------

import webbrowser

print("Deployment completed")
webbrowser.open("https://www.google.com/")

# ------------------- Sending emails-------------------------


message = MIMEMultipart()
message["from"] = "Muzaffar Ahmed"
message["to"] = "Muzaffarahmed4u@gmail.com"
message["subject"] = "Angular email testing"


message.attach(MIMEText("Body"))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("smtp.gmail.com", "12345pw")
    smtp.send_message(message)
    print("Sent...")
# -------------------- Write Text from Json-------------------------

movies = json.loads(Path("movies.json").read_text())
print(movies)

# with sqlite3.connect("movies.db") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute("INSERT INTO movies VALUES(?, ?, ?)",
#                      tuple(movie.values()))
#     conn.commit()

with sqlite3.connect("movies.db") as conn:
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            title TEXT,
            director TEXT,
            year INTEGER
        )
    """)

    # Insert JSON data into the table
    for movie in movies:
        cursor.execute("INSERT INTO movies VALUES (?, ?, ?)",
                       tuple(movie.values()))

    conn.commit()


dt = datetime(2025, 12, 20)
dt = datetime.now()
print(dt)

random_key = ("".join(random.choices(
    f"{string.ascii_letters}{string.digits}", k=8)))
print(random_key)

numbers = [2, 3, 6, 7, 8]
random.shuffle(numbers)
print(numbers)
# movies = [
#     {"id": 1, "Name": "Koila", "year": 1994},
#     {"id": 2, "Name": "DDLG", "year": 1990}
# ])

# data = json.dumps(movies)
# Path("Movies.json").write_text(data)

# Path("New_Movie.json").write_text(data)

# -------------------- Read Text from Json-------------------------
# data = Path("Movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["Name"])
