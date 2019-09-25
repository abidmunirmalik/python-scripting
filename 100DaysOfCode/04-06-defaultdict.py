from collections import defaultdict

# defaultdict: Default 'value' of dictionary 'key' if that does not exists
somedict = {}
#somedict[3] # KeyError
#output: KeyError: 3
# Note: Since key 3 does not exist, we get error

somedict = defaultdict(int)
somedict[3]
print(somedict)
#output: defaultdict(<class 'int'>, {3: 0})
# Note: Since Key 3 does not exists, we defined defaultdict
# 3 picked up the default value as '0'
