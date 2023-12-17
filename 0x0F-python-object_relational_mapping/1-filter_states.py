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
    sql = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    mycursor = db.cursor()
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
