
import sqlite3


conn = sqlite3.connect('tutorial.db')
cur = conn.cursor()

cur.execute("""
    INSERT INTO
    TUTORIAL(ID, DATA)
    VALUES
    (1, "Hello, SQLite!");
""")

conn.commit()

result = cur.execute("""
    SELECT *
    FROM TUTORIAL;
""")

# [(1, 'Hello, SQLite!')]
print(result.fetchall())

conn.close()
