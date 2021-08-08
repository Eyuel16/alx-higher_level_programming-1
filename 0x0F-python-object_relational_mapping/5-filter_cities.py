#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM states \
                    INNER JOIN cities ON states.id = cities.state_id \
                    WHERE Binary states.name=%s \
                    ORDER BY cities.id ASC", (argv[4],))
    for row in cursor.fetchall():
        print(row.cities.name)
    cursor.close()
    db.close()
