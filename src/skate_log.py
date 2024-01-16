import argparse
from datetime import date
from database import Database


def manage_person(args):
    if args.birthdate is not None:
        bd = date.fromisoformat(args.birthdate)
        if bd is None:
            raise Exception("Must provide a valid birthdate")

        if db.get_person(args.name) is None:
            db.add_person(args.name, args.birthdate)
        elif args.update:
            db.update_person(args.name, args.birthdate)

    if args.list:
        for person in db.get_persons():
            print(f"{person.name}\t\t{person.birthdate}")


def add_activity(args):
    d = date.fromisoformat(args.date)
    if d is None:
        raise Exception("Must provide a valid date")

    db.add_person(args.name)
    db.add_activity(args.name,
                    args.date,
                    args.activity_type,
                    args.skate,
                    args.hours)

    for a in db.get_activities_by_person(args.name):
        print(f"""{args.name} skated for {a.hours} hours on {a.date} at {a.activity_type}""")


db = Database('skatelog.db')

parser = argparse.ArgumentParser(
                    prog='Skate Log',
                    description='Logs ice time to a local file')

parser.add_argument('-n', '--name')
parser.add_argument('-d', '--date')
parser.add_argument('-H', '--hours')
parser.add_argument('-s', '--skate')
parser.add_argument('-t', '--activity_type')
parser.set_defaults(func=add_activity)

subparsers = parser.add_subparsers()
person_parser = subparsers.add_parser('person')
person_parser.add_argument('-u', '--update', action='store_true')
person_parser.add_argument('-l', '--list', action='store_true')
person_parser.add_argument('-n', '--name')
person_parser.add_argument('-b', '--birthdate')
person_parser.set_defaults(func=manage_person)

args = parser.parse_args()
args.func(args)
