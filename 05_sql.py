# try / except
import sqlite3

# connect to the db
with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    # insert data with try except

    try:
        # insert data
        cursor.execute(
            "INSERT INTO populations VALUES('NEW YORK', 'NY', 300000)")

        connection.commit()

    except sqlite3.OperationalError:
        print("Something went wrong!")
