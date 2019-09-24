# Lists: ordered, mutable, allows duplicate elements
fruits = ["Banana", "Cherry", "Apple"]
numbers = [10,20,30,40]
print(fruits)

# List can have mixed date types and allow duplicate elements
mixed_list = [1, True, "string", 56.7, None, True]
print(mixed_list)
print(mixed_list[-1], mixed_list[1])

# Iterate through List Items
for fruit in fruits:
    print("I like {}".format(fruit))

# Using 'in'
if "Apple" in fruits:
    print("Yes, Apple is in list!")
else:
    print("No")

# Sum up list items
print(sum(numbers))
max = max(numbers)
min = min(numbers)

# Max & Min
print("Max: {}".format(max), "Min: {}".format(min))

# Lenght of list members
print("Length: {}".format(len(numbers)))

# Append and Insert method
fruits.append("Orange")
print(fruits)

fruits.insert(0,"Grapes")
print(fruits)

# Remove item with pop/remove from list
fruits.pop()
print(fruits)

fruits.remove("Cherry")
print(fruits)

# Empty the list
numbers.clear()
print(numbers)

# Reverse the list
print(fruits)
fruits.reverse()
print(fruits)

# Sort the list
numbers = [100,90,80,60,70]
print(numbers)
numbers.sort()
print(numbers)
# if we do not want to change original list
new_list = sorted(numbers)
print(new_list)

# Create a list with '*'
five_zeros_list = [0] * 5
print(five_zeros_list)

# Combine two lists
two_list_combined = new_list + five_zeros_list
print(two_list_combined)

# List Slicing
# syntax: list[start_index:stop_index]
numbers = [1,2,3,4,5,6,7,8,9,10]
# Print first-five members of list
print(numbers[0:5])
# Print last-five members of list
print(numbers[5:])
# if we do not specify start-index, it starts from 0
print(numbers[:5])
# if we do not specify stop-index, it goes to end
print(numbers[5:])
# Print ODD members of list - using step index
print(numbers[0::2])
# Print EVEN members of list - using step index
print(numbers[1::2])

# Start from End to Begining
print(numbers[::-1])

# copy the list
fruits = ["Banana", "Cherry", "Apple"]
my_fruits = fruits.copy()
my_fruits.append("Lemon")
# Another way of copying list
your_fruits = list(my_fruits)
your_fruits.append("Grapes")
# Another way to copying list
our_fruits = your_fruits[:]
our_fruits.append("Mangos")
print(fruits)
print(my_fruits)
print(your_fruits)
print(our_fruits)

# List comprehension - elegant way creaing list
numbers = [1,2,3,4,5,6,7]
sqroot = [s*s for s in numbers]
power_of_three = [t*t*t for t in numbers]
print(sqroot)
print(power_of_three)
