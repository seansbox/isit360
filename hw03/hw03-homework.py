import sqlite3

con = sqlite3.connect("hw03-homework.sqlite3")
cur = con.cursor()

try:
    # Attempt to read a single value from our database
    cur.execute("SELECT id FROM homework LIMIT 1")
except:
    # Initialize the database since it couldn't be read from
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS homework (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            due DATE
        )
        """
    )
    cur.execute("INSERT INTO homework (name, due) VALUES (:name, :due)", {"name": "HW01", "due": "2024-04-16"})
    cur.execute("INSERT INTO homework (name, due) VALUES (:name, :due)", {"name": "HW02", "due": "2024-04-17"})
    con.commit()

print("ALL HOMEWORK:")
for row in cur.execute("SELECT id, name, due FROM homework"):
    print(f"  Homework {row[1]} ({row[0]}) is due on {row[2]}")

print("REMAINING HOMEWORK:")
for row in cur.execute("SELECT id, name, due FROM homework WHERE due > date('now')"):
    print(f"  Homework {row[1]} ({row[0]}) is due on {row[2]}")
