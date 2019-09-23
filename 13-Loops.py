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

# FOR LOOP WITH CONTINUE & BREAK
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        print("We'r hit by Red Color, exiting....")
        break
    else:
        print(color)
        
# FOR LOOP IN LIST OF TUPLES
list_of_points = [ (1,2), (3,4), (5,6)]
for x,y in list_of_points:
    print(f"x: {x}, y:{y}")
    
# FOR LOOP OVER DICTIONARY
ages = {"Bob" : 54, "Sandy" : 50, "John" : 48, "Doe" : 46}
for name,age in ages.items():
    print "Name: " + name
    print "Age: "  + str(age)
    print "-" * 5
print ages.items()
print ages
