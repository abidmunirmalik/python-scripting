import sys
import timeit
# Tuples are orderd, immutable, allows duplicate elements
intelcpu = ("3.2Gz", 2019, "genuine")
print(intelcpu)
# mytuple = ("max",) <= string, end with , to make it tuple

# Create tuple from list with 'tuple' keyword
user = tuple(["Max", 28, "Boston", "BS Computer Science", "WSU"])
print(user[-1], user[0], user[-2])
for tuple_itmes in user:
    print(tuple_itmes)

# Return number of occurance of a value in tuple    
print(user.count('Max'))

# search index place of a string within tuple
print(user.index('Boston',0,len(user)))

# Tuple does not support item assignment
# user[0] = "Bobby" <= will fail

# If item is in the tuple
if "Bobby" in user:
    print("Yes")
else:
    print("Bobby is not in tuple")    

# We can make list out of tuple
user_list = list(user)
print(type(user_list))
print(user_list)  
user_list.append('USA')
user = tuple(user_list)
print(user)  

# Variable 
(power, year, model) = intelcpu
print(power)

# Tuple & List Comparison
a_list = ["Apple", "Banana", "Mango", True, 0]
a_tuple = ("Apple", "Banana", "Mango", True, 0)
print(sys.getsizeof(a_list),"bytes")
print(sys.getsizeof(a_tuple),"bytes")
# Tuples are more efficient then list

# comparison based on timing
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000))
