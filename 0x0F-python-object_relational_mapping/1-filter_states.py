#!/usr/bin/python3

"""
 a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]

    with MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database) as db:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cur.fetchall()
            for row in rows:
                if row[1][0] == 'N':
                    print(row)
