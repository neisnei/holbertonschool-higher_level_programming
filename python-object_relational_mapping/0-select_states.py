#!/usr/bin/python3

"""
lists all states module
from database htbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Acess database and get states
    from database
    """

    db = MySQLdb.connect(host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states BY id ASC")
    for i in res:
        print(1)
        db.close()
