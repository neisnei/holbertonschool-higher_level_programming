#!/usr/bin/python3

"""
states module
from database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost,
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states BY id ASC")
    states = cur.fetchall()

    for row in rows:
    print(row)
