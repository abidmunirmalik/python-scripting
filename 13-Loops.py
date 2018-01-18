# Looping in Python - Iteration
counter = 1
go = True
while go:
    print "Counter is: " + str(counter)
    counter = counter + 1
    if counter == 11:
        print "Clock Over, Exist Now"
        go = False
        counter = 1
while counter <= 10:
    print "Counter: " + str(counter)
    counter += 1

print "=" * 10
# For Loop
print "For Loop"
colors = ["Red", "Green", "Blue", "White"]
for color in colors:
    print(color)

print "=" * 10
points = (2.1, 3.5, 5.7, 10.8, 20)
for point in points:
    print(point)

print "=" * 10
ages = {"Shahid" : 54, "Tahir" : 50, "Sajid" : 48, "Abid" : 46}
for name,age in ages.items():
    print "Name: " + name
    print "Age: "  + str(age)
    print "-" * 5
print ages.items()
print ages
