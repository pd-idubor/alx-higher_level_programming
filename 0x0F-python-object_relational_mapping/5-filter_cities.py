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
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                state_id = states.id WHERE states.name = '{}'\
                ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    [print(row) for row in rows]

    cur.close()
    db.close()
