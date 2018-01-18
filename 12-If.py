# For IF Statements, we need to understand Boolean values
print "1 == 1", 1 == 1
print "1 != 2", 1 != 2
print "1 < 2", 1 < 2
print "2 > 0", 2 > 0
print "2 == 1", 2 == 1
print "this == this ", "this" == "this"
print "this == that ", "this" == "that"
print "3.0 >= 3.0", 3.0 >= 3.0
print "3.1 >= 3.0", 3.1 >= 3.0
print "If 2 in [1,2,3]", 2 in [1,2,3]
print "If 2 in [3,4,5]", 2 in [3,4,5]

brothers = ["Shahid","Tahir","Sajid","Abid"]
cousins  = ["Javed", "Zafar", "Nasar", "Qaiser"]
name = "Zafri"
if name in brothers:
    print(name + " is one of brothers")
elif name in cousins:
    print(name + " is one of cousins")
else:
    print(name + " is not one of brothers or cousins")

# We can use IF based on bool(Expression) result
print bool("This") # Answer should be True
if "This":
    print("This is test for bool")
else:
    print("Result was False") 
