# Lists and Tuples in Python
# Declaring Lists

# list can contains any data type
my_grocery_list = ["Potatos","Apples",'Bananas',10,True,90.5]
print(my_grocery_list)

# Getting List Items
print my_grocery_list[2],"<=== Should give Bananas"

# The length of list is find by len(my_grocery_list)
print "Length of list:", len(my_grocery_list)

# Print the last item of the list
print "Last item of the list:" , my_grocery_list[len(my_grocery_list) - 1]
# This will also print last item of the list
print "Last item of the list: " , my_grocery_list[-1]

# Slicing the List - Sub-list
print "First three list items:", my_grocery_list[0:3]
print "First three list items:",my_grocery_list[:3]
print "Every list litem from 2nd:", my_grocery_list[1:]

# Printing Even and Odd Numbers
odd_numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print "Odd Numbers from 1-10:",odd_numbers_list[0::2]
print "Even Numbers from 1-10:",even_number_list[1::2]

# Mutable - Changeable List Items
print "my_grocery_list:", my_grocery_list
my_grocery_list[0] = "Tomatoes"
print "Changing First List Item from Potatos to Tomatoes:", my_grocery_list

# Append items to out list
my_grocery_list.append("Onion")
print(my_grocery_list)

my_grocery_list += ["Carrots","Cabbage","Oranges"]
print(my_grocery_list)

# Don't add items to list, just merge to list
print my_grocery_list + ["Fruits","Vegetables"]
print(my_grocery_list)

# Replacing List Items
my_grocery_list[3:6] = ["20",'False','190.0']
print my_grocery_list

# Removing List items
my_grocery_list[4:5] = []
my_grocery_list.remove("Tomatoes")
print my_grocery_list

# Removing last list item via pop method
my_grocery_list.pop()
print my_grocery_list
# Removing First list item via pop method
my_grocery_list.pop(0)
print my_grocery_list


# TUPLES INTRODUCTION
# Tuples are useful for pointing plots like x,y values
coordinates = (2.0, 3.0)
print "X coordinate:", coordinates[0]
print "Y coordinate:", coordinates[1]

# Exercise
# Write a script that will loop through a list of users
users = [
{ "name" : "Bri Mundy",     "admin" : True,  "active" : True },
{ "name" : "Brent Wells",   "admin" : True,  "active" : True },
{ "name" : "Abid Malik",    "admin" : True,  "active" : True },
{ "name" : "Same Evett",    "admin" : False, "active" : True },
{ "name" : "Mark Peglow",   "admin" : True,  "active" : True },
{ "name" : "Ted Boggs",     "admin" : False, "active" : False },
{ "name" : "Drew Mcmillan", "admin" : True,  "active" : False },
{ "name" : "Josh Huber",    "admin" : False, "active" : True },
{ "name" : "Craig Caroon",  "admin" : False, "active" : True },
{ "name" : "Cody Wilson",   "admin" : True,  "active" : True },
{ "name" : "Steve Gambino", "admin" : False, "active" : True },
{ "name" : "Dodd Jones",    "admin" : False, "active" : False },
]

line_number = 1
for user in users:
    if user["admin"] and user["active"]:
        print("%s ACTIVE - (ADMIN) %s" % (line_number,user["name"]))
    elif user["admin"]:
        print("%s (ADMIN) %s" % (line_number,user["name"]))
    elif user["active"]:
        print("%s ACTIVE - %s" % (line_number,user["name"]))
    else:
        print("%s %s" % (line_number,user["name"]))
    line_number = line_number +1
