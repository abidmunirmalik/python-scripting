# Control Flow - Logic Operations in Python
# "not" is a keyword in Python
print bool(1) # Should print True
if not bool(1):
    print "False"
else:
    print("True") #This should print True

name = "Abid Munir Malik"
if not len(name) > 25:
    print("Name is normal")
else:
    print("Name has too many characters")
print "=" * 10
# "is" a keyword in Python
if 10 is 10:
    print "True"
else:
    print "False"
print "=" * 10
user_input = 10
if user_input is 10:
    print str(user_input) + " is integer"
else:
    print str(user_input) + " is string"

print "=" * 10

# AND & OR operators in Python
print "AND"
print 1 and 2 # it will return last value if both True
print 0 and 1 # it will return first false value if one is True
print bool(0) # Should return False
print bool(1) # Should return True
print "OR"
print 1 or 2 # should print 1
print 0 or 2 # should print 2
