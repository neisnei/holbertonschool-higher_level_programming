#!/usr/bin/python3
"""
This module is about the lists all states
from database htbtn_0e_0_usa.
"""

import MySQLdb

def main():
    # Get the username, password and database name from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = connection.cursor()

    # Get all the states from the database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Get the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()
