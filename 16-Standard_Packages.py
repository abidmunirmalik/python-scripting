# Python Standard Library - All Packages in Standard Library are available when Python is installed
# From Standard Library, import the "time" package (class)
import time

start_time = time.localtime()
print("Timer started at %s " % time.strftime("%X", start_time))

# Wait for user input
raw_input("Please press Enter to continue...")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at %s " % time.strftime("%X", stop_time))
print("Total time: %s seconds" % difference)

# The same script can be written as
# We can just import the functions that we need from time package
from time import localtime, strftime, mktime

#Now we don't have to use time. notation but just function name

started_time = localtime()
print("Timer started at %s " % strftime("%X", started_time))

# Wait for user input
raw_input("Please press Enter to continue...")

stoped_time = localtime()
diff = mktime(stoped_time) - mktime(started_time)

print("Timer stopped at %s " % strftime("%X", stoped_time))
print("Total time: %s seconds" % diff)
