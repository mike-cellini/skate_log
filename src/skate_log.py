import argparse
from datetime import date
import sqlite3
import os

db_exists = False
if os.path.isfile('skatelog.db'):
    db_exists = True

con = sqlite3.connect('skatelog.db')
cur = con.cursor()

if not db_exists:
    cur.execute("CREATE TABLE person(name TEXT, birthdate TEXT)")
    cur.execute("""CREATE TABLE activity(
                        person TEXT,
                        date TEXT,
                        activity_type TEXT,
                        skate TEXT,
                        hours NUMERIC)""")
    con.commit()


parser = argparse.ArgumentParser(
                    prog='Skate Log',
                    description='Logs ice time to a local file')

parser.add_argument('-n', '--name')
parser.add_argument('-d', '--date')
parser.add_argument('-H', '--hours')
parser.add_argument('-s', '--skate')
parser.add_argument('-t', '--activity_type')
args = parser.parse_args()

d = date.fromisoformat(args.date)

person_exists = False
for row in cur.execute("SELECT name FROM person"):
    if row[0] == args.name:
        person_exists = True

if not person_exists:
    cur.execute("INSERT INTO person VALUES(?, ?)", (args.name, None))

cur.execute("INSERT INTO activity VALUES(?, ?, ?, ?, ?)",
            (
                args.name,
                args.date,
                args.activity_type,
                args.skate,
                args.hours))
con.commit()

for row in cur.execute("""SELECT date, activity_type, skate, hours
                          FROM activity"""):
    print(f"""{args.name} skated for {row[3]} hours on {row[0]} at {row[1]}""")
