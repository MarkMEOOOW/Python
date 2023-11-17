import sqlite3 as sq

with sq.connect('database.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")
