#!/usr/bin/python3
"""
    Displays valies with name matches
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states ON\
                state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    cities = ""

    for row in rows:
        if row[4] == sys.argv[4]:
            cities += row[2] + ", "

    print(cities[:-2])
    cur.close()
    db.close()
