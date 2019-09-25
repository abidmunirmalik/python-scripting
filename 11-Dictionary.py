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

 # More stuff
# Dictionary: Key-Value pairs, unordered, mutable
users = {"name": "Patricia" ,"title" : "Director, IT Operations",
     "city":"Mason" ,"state": "Ohio"}

# Using 'dict' keyword
dba = dict(name="Samy", title="Senior DBA", location="Norht California")
# Items
print(dba["name"])  
dba["email"] = "samy@python.net"
print(dba)

# dict keys, values
for key in dba.keys():
    print(key)
for value in dba.values():
    print(value)
for key,value in dba.items():
    print(key+':',value)    

# try exception
try:
    print(dba["name"])
except:
    print("Error")    
# Methods
del dba["location"]
print(dba)
dba.pop("email")
print(dba)
dba.popitem() #pop last item
print(dba)

# Merge/Upgrade Dictionaries
d1 = {"name": "Abed Malek", "title": "DBA"}
d2 = {"name": "Abid Malik", "email": "amalik@webassign.net"}
d1.update(d2)
print(d1)
# {'name': 'Abid Malik', 'title': 'DBA', 'email': 'amalik@webassign.net'}
