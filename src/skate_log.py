import argparse
from datetime import date
from database import Database

db = Database('skatelog.db')

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

db.add_person(args.name)
db.add_activity(args.name,
                args.date,
                args.activity_type,
                args.skate,
                args.hours)


for row in db.get_activities_by_person(args.name):
    print(f"""{args.name} skated for {row[4]} hours on {row[1]} at {row[2]}""")
