#!/usr/bin/python3

"""
states module
from database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM state BY id ASC")

    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)
