#!/usr/bin/python3
"""
Module takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Function takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    """

    # Connecting to a MySQL database.
    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # Making cursor obj for execution.
    cur = cnx.cursor()

    # Executing query.
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]))

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        if row[1][0] == sys.argv[4][0]:
            print(row)

    # Close cursor.
    cur.close()

    # Close connection to database.
    cnx.close()
