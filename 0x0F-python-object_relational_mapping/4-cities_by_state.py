#!/usr/bin/python3
""" module to connect to database and select records with INNER JOIN
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3]
            )
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                     INNER JOIN states ON cities.id = states.id\
                     ORDER BY cities.id ASC")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
