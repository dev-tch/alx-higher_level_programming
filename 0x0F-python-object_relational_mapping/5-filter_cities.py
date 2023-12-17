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
    mycursor.execute("SELECT cities.name  FROM cities\
                     INNER JOIN states ON cities.state_id = states.id\
                     WHERE states.name = %s\
                     ORDER BY cities.id ASC", (argv[4],))
    rows = mycursor.fetchall()
    res = ", ".join(map(lambda x: x[0], rows))
    print(res)
    mycursor.close()
    db.close()
