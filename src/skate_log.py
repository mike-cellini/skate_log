import argparse
from datetime import date

parser = argparse.ArgumentParser(
                    prog='Skate Log',
                    description='Logs ice time to a local file')

parser.add_argument('-n', '--name')
parser.add_argument('-d', '--date')
parser.add_argument('-H', '--hours')
parser.add_argument('-t', '--type')
args = parser.parse_args()

d = date.fromisoformat(args.date)

print(f"{args.name} skated for {args.hours} hours on {d} at {args.type}")
