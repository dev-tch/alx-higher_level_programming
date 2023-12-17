#!/usr/bin/python3
""" module to connect to database and select records with filtering"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        if (len(argv) != 4):
            raise ValueError("missing arguments")
        db = MySQLdb.connect(
                host="localhost",
                user=argv[1],
                password=argv[2],
                database=argv[3]
                )
        sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        mycursor = db.cursor()
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if 'mycursor' in locals() and mycursor is not None:
            mycursor.close()
        if 'db' in locals() and db is not None:
            db.close()
