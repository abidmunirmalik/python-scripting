from collections import Counter

words = """ My name is Abid Munir Malik and I am son of Muhammad
Munir Malik, I was born in Gujranwala city of Pakistan, I stayed
in my home town till I was 30 years old, then I first time fly
to Doha, Qatar and landed a Oralce programmer job.""".split()
print(words[:5])
# Find most common words
most_common_words = Counter(words).most_common(3)
print(most_common_words)
