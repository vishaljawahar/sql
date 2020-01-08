import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute(
        "update population set population = 9000000 where city='New York City'")

    c.execute("delete from population where city = 'Boston'")

    print("\n NEW DATA: \n")

    c.execute("select * from population")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
