# Create a SQLite3 database and table


# import sqlite3 library
import sqlite3

# create a new database if the databse doesn't exist already
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL commands
cur = conn.cursor()

# create a table
cur.execute("""CREATE TABLE population
            (city TEXT, state TEXT, population INT)
            """)

# close the connection
conn.close()
