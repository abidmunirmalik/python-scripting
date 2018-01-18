# Executing Shell Commands within Python
import subprocess
#code = subprocess.call(["ls","-ltr"])

# if code == 0: # mean successfully executed the command
    #print("command finished successfully")
# else:
#    print("failed with code %i" % code)

# Let's capture the output in a variable
#output = subprocess.check_output(["ls","-ltr"])
#print(output)

# Add Try/Except Block
try:
    output = subprocess.check_output(["ls name.txt"],stderr=subprocess.STDOUT)
except OSError as err:
    print("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    output = err

print(err)
