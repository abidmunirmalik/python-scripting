import sys
# Numbers in Python 2
# There are 4 types of numbers in Python 2
# Types of numbers: int, long, float, complex
# Whole numbers: int, long
a = 28 # This is a perfect number
print(type(a))
# What is the max limit of a integer value
print(sys.maxint)
b = 9223372036854775807
print(type(b))

c = 9223372036854775808 # We just changed the last digit from 7 to 8
print(type(c)) # it will turn to long automatically
# No need to worry converting from int to long, it is automatically

# Floats  - These are numbers with decimal values
f = 4.56789
print"f is of type: ", type(f)

# Complex Numbers - They have real part and an imaginary part

# Arithmetic in Python 2
# Four Arithmetic operators: +, -, *, /
a = 2   # int
b = 3L  # long
c = 6.0 # Float
d = 12 + 0j # complex number
# Addition
print (a + b)
print(b + c)
print(a + d)

# Subtraction
print ( c - b)
print (b -a )

# Multiplication
print (a * b)

#Division
print (c / a)
