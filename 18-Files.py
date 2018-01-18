# Handling Files in Python
import os
# how to read a Files
xmen_file = open("xmen.txt")
print(xmen_file.read()) # This will give all file contents as one string
for line in xmen_file:
    print(line)
xmen_file.close()
# How to write to Files
# File Mode
# w = write (it will completely override the content of file)
# r = read (default mode)
# r+ = Read + Write
# a  = Append Mode
xmenn_file = open("xmen.txt","r+")
xmenn_file.seek(-1, os.SEEK_END)
xmenn_file.write("\nBeast\n")
xmenn_file.write("Phoenix\n")

#print(xmen_file.read())
xmenn_file.close()

# OR
x_file = open("xmen.txt","a")
x_file.writelines(['Morph\n', 'Rogue\n'])
x_file.close()
x_file = open("xmen.txt", "r")
print(x_file.read())
x_file.close()

# OR
with open("xmen.txt", "a") as xx_file:
    xx_file.write("Professor Xavier\n")
    
