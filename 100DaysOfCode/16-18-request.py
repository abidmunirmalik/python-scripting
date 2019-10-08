import requests
from collections import Counter
import re

resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
words = [re.sub(r'\W+',r'',word) for word in words]
words = [word for word in words if word.strip() and word not in ['the','a','he','and','to','of','but']]
words = [word for word in words if word.strip() and word not in ['that','at','have','all','his','in','mr']]
words = [word for word in words if word.strip() and word not in ['was','it','had','as','i','on','be']]
cnt = Counter(words).most_common(5)
print(cnt)
