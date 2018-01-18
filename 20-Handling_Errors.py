# Handling Errors
import sys
import argparse

parser = argparse.ArgumentParser(description="PURPOSE: Read a file to read in reverse")
parser.add_argument("filename", help="The file to be read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version","-v" ,action="version", version="%(prog)s ver 1.0")

args = parser.parse_args()

try:
    f = open(args.filename) #Try to open this file
except IOError as err:
    print("Error: '%s' not found" % args.filename)
else:
    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::1])

finally: #This piece always run
    print("\nWe're finished\n")
