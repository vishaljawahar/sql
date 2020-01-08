# exectuemany() method


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple data of cities
    cities = [
        ('Boston', 'MA', 6000000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    # insert data into the population table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
