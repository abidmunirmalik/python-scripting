# WHILE LOOP EXAMPLE CONTINUE
count = 0
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We are counting odd numbers: {count}")
    count += 1

# WHILE LOOP EXAMPLE BREAK
count = 1
while count <= 10:
    if count % 2 == 0:
        print("We hit by an Even number, exiting.....")
        break
    print(f"We are counting odd numbers: {count}")
    count += 1

# FOR LOOP
print "For Loop"
colors = ["Red", "Green", "Blue", "White"]
for color in colors:
    print(color)

print "=" * 10
points = (2.1, 3.5, 5.7, 10.8, 20)
for point in points:
    print(point)

print "=" * 10
ages = {"Bob" : 54, "Sandy" : 50, "John" : 48, "Doe" : 46}
for name,age in ages.items():
    print "Name: " + name
    print "Age: "  + str(age)
    print "-" * 5
print ages.items()
print ages
