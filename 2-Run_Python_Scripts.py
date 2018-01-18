How to Create and Run Python Scripts

We can run the Python script by passing it as an command line argument to python command line utility as:

abidmalik$ touch hello.py
abidmalik$ echo 'print("Hello from Python!")' > hello.py
abidmalik$ python hello.py
Hello from Python!

But if we want to turn this into a executable script by shell, we need to save it as:

abidmalik$ touch hello.py
abidmalik$ echo '#! /usr/bin/python' > hello.py
abidmalik$ echo 'print("Hello from Python!")' >> hello.py
abidmalik$ chmod u+x hello.py
abidmalik$ ./hello.py
Hello from Python!
