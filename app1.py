from pathlib import Path
import json
import sqlite3
# -------------------- Write Text from Json-------------------------

movies = json.loads(Path("Movies.json").read_text())

with sqlite3.connect("Movies.json") as conn:
    command = "INSERT INTO movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
# movies = [
#     {"id": 1, "Name": "Koila", "year": 1994},
#     {"id": 2, "Name": "DDLG", "year": 1990}
# ]

# data = json.dumps(movies)
# Path("Movies.json").write_text(data)

# Path("New_Movie.json").write_text(data)

# -------------------- Read Text from Json-------------------------
# data = Path("Movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["Name"])
