# import from CSV
import csv

import sqlite3

# create database object
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # get employee details
    employees = csv.reader(open("employees.csv", "r"))

    # create the table
    c.execute("CREATE TABLE employee(firstname TEXT, lastname TEXT)")

    # insert data into the table
    c.executemany("INSERT INTO employee VALUES (?, ?)", employees)
