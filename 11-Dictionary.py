# Dictionaries are key-value pair values
# Kevin is key, 59 is value , Bob = Key, 39=value
ages = {"Kevin" : 59, "Bob" : 39, "Alex" : 28}
brothers =  dict(Shahid=52, Tahir=50, Sajid=48, Abid=46)
color_choice = dict([("Abid","Green"), ("Sajid","White")])
print ages
print brothers
print color_choice
# Dictionaries are not in order list
print " Key ages[Kevin] and its value:", ages["Kevin"]
print " Key ages['Bob'] and its value:", ages['Bob']

# Modify Dictionaries
ages["Kevin"] = 29

# Append to Dictionaries
ages["Sam"] = 61
ages["Josh"] = 44
ages["Abid"] = 46
ages["Briana"] = 40
ages["Brent"] = 50

print "Dictionary before purging:", ages
# Deleting Dictionaries
del ages["Kevin"]
del ages["Bob"]
del ages["Alex"]
ages.pop("Brent") # By using pop method

print "Dictionary after purging:", ages

# Print the Values,Keys, Items of Dictionary
print "ages Keys:",ages.keys()
print "ages Values:",ages.values()
print "ages Items:",ages.items()

print "=" * 10

# Exercise - If user is an admin, print Admin, if user is Active, print Active, otherwise only print name
user = {"name" : "abid", "admin" : False, "active" : False}
if user["admin"] and user["active"]:
    print("ACTIVE - (ADMIN) %s" % user["name"])
elif user["admin"]:
    print("(ADMIN) %s" % user["name"])
elif user["active"]:
    print("ACTIVE - %s" % user["name"])
else:
    print(user["name"])
