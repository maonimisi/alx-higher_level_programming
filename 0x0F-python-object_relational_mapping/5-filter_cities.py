#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    city_list = []

    with MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database) as db:
        with db.cursor() as cur:
            cur.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states on cities.state_id = states.id
            WHERE states.name=%s ORDER BY id ASC""", (state,))
            cities = cur.fetchall()
            for city in cities:
                city_list.append(city[1])
            print(', '.join(city_list))
