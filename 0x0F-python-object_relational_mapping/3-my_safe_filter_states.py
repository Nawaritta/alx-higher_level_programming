#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, and
that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                    ORDER BY states.id ASC", {'name': sys.argv[4]})
    [print(state) for state in cursor.fetchall()]
