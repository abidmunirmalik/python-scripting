# Environmental Variables in Python
import os
# print all the environmental variables
for en in os.environ:
    print(en + " : " + os.environ[en])

print("Hello " + os.getenv("USER") + " Your home dir is " + os.getenv("PWD") )
