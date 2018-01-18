# Standard Library: random & json
import random
import os
import json

count = os.getenv("FILE_COUNT") or 10
words = [word.strip() for word in open("names.txt").readlines()]

# range should give 1 to 99
for identifier in range(1,count+1):
    amount = random.uniform(1.0, 1000.0)
    content = {
    'topic': random.choice(words),
    'value': "%.2f" % amount
    }
    with open('./new/receipt-%s.json' % identifier, 'w') as f:
        json.dump(content, f)
