
import sqlite3


if __name__ == '__main__':

    conn = sqlite3.connect('tutorial.db')

    conn.execute("""
        CREATE TABLE
        TUTORIAL(
            ID NUMBER NOT NULL PRIMARY KEY,
            DATA TEXT
        );
    """)

    conn.commit()
    conn.close()
