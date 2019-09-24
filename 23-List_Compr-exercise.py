# List Comprehensions in Python
import argparse
parser = argparse.ArgumentParser(description="Search for words including partial word")
parser.add_argument("snippet", help="Partial or complete string in words file")
args = parser.parse_args()
snippet = args.snippet.lower()
words = open("names.txt").readlines()
matches = []
for word in words:
    if snippet in word.lower():
        matches.append(word)
print(matches)
# OR following one line will produce the same result        
#print([word.strip() for word in words if snippet in word.lower()])
