#!/usr/bin/python3
""" module to connect to database and select records with filtering"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3]
            )
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    sql = query.format(argv[4])
    mycursor = db.cursor()
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
