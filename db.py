import sqlite3 as sq

con = sq.connect ("data.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    jins INTEGER,
    name TEXT,
    level INTEGER,
    score INTEGER
    
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS games(
    id INTEGER,
    user_id INTEGER,
    score INTEGER,
    time INTEGER
)""")

con.close()
