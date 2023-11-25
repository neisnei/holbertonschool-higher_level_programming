#!/usr/bin/python3

"""
all states module
from database htbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Acess database and get states
    from database
    """

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states BY id ASC")
    states = cur.fetchall()

    for state in state:
        print(state)
        db.close()
