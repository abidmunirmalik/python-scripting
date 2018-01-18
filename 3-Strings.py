import string
# Strings in Python
# Strings in Python can be expressed in several ways. Strings can be enclosed in single quotes or double quotes with the same output.
# We can use \ in string to use escape quotes.

# String Quotations
print ""
print("Strings in single & double quotes:")
myname = 'Abid Malik' # single quoted string
print("String in single quote:" + myname)
myname = "Abid Malik" # double quoted string
print("String in double quotes :" + myname)

escape_single_quote = 'it doesn\'t matter'  #escape the single quote
print("Escape in Single Quote :" + escape_single_quote)

escape_double_quote = "it doesn\'t matter"  #escape double quote
print("Escape in Double Quote :" + escape_double_quote)

print_backspace = '"Isn\'t," she said.'
print("Print quotes :" + print_backspace)

# new-line and \r characters
print ""
three_lines_name = "Abid\nMunir\nMalik" #\n is the new line character
print("The name will be printed in 3 lines:")
print(three_lines_name)
print ""
print("The name will print in one line:")
same_line_name = r"Abid\nMunir\nMalik" # By using \r, we can skip interpreting special character
print(same_line_name)
print ""

# Multiple lines string literals
print("Priting string in multiple lines:")
help_usage = """\
Usage: command args [OPTIONS]
       -v            Display version and quite
       -H hostname   Hostname to connect
       -u username   User Name
       -p password   Password
"""
print(help_usage)

# String Concatination
first_name = "Abid"
middle_name = "Munir"
last_name = "Malik"
full_name = first_name + ' ' + middle_name + ' ' + last_name
print("Full Name: " + full_name)
print ""

# String Repitition
print("print 5 times Ha")
print("Ha" * 5)

# Strings can be indexed, first character is at index 0
# There is no separate character type; a character is simply a string of size one.
print ""
language = "Python"
print("Language = Python")
print("character at index 0 :" + language[0])
print("character at index 1 :" + language[1])
print("character at index 2 :" + language[2])
print("character at index 3 :" + language[3])
print("character at index 4 :" + language[4])
print("character at index 5 :" + language[5])

# Search Strong within string by using find() method
print(language.find("th")) # Search 'P' within Python

# Sub-String within String
word = "Python"
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[4:6]) # characters from position 4 (included) to 6 (excluded)

# Slices in String
# In Slices how to start is always included, and the end always excluded.
# s[:i] + s[i:] is always equal to s.
print("word = Python")
print("characters from the beginning to position 2 (excluded) - should print 'Py'")
print(word[ :2 ])
print("characters from position 4 (included) to the end - should print 'on'")
print(word[ 4: ])
print("characters from second-last (included) to the end - should print 'on'")
print(word[ -2: ])

# String Length
print("The length of string 'Python' is: ")
print( len(word) )

# Converting Strings to Lower and Upper case
hostname = "wilma"
url = "WWW.GOOGLE.COM"
print( string.upper(hostname) )
print( string.lower(url))
