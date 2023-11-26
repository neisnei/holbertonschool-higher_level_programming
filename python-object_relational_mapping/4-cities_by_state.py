#!/usr/bin/python3
"""
Module list all cities from database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """Function that lists all cities database hbtn_0e_4_usa"""

    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    cur = cnx.cursor()

    cur.execute

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()

    cnx.close()
