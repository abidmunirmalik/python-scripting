# Command line arguments - positional arguments
import sys

print("First Argument: %s " % sys.argv[0])
#The 2nd is what we pass to script from Command-line
# print("2nd argument: %s " % sys.argv[1])

import argparse

parser = argparse.ArgumentParser(description="PURPOSE: Read a file to read in reverse")
parser.add_argument("filename", help="The file to be read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version","-v" ,action="version", version="%(prog)s ver 1.0")

args = parser.parse_args()
# print(args)
# abidmac:PYTHON abidmalik$ python 19-Command_Line_Param.py abid.txt --limit 5
# output will be ('abid.txt', 5)
# print(args.filename, args.limit)

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::1])
