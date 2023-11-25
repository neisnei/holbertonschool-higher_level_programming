#!/usr/bin/python3
"""
This module is about the lists all states
from database htbtn_0e_0_usa.
"""

import MySQLdb
import sys import argv

if __name__ == "__main__":
    """
    Acess database and get states
    from database
    """

    db = MySQLdb.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
