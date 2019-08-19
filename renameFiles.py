# remove numeric values from .txt file names
#
# all .txt files
# 124tokoy.txt, chicago55.txt, newyork44.txt, sandiago50.txt
# tokoy.txt, chicago.txt, newyork.txt, sandiago.txt
#

import os
import re
all_files = os.listdir(".") # path is current dir
for file_name in all_files:
    if '.txt' in file_name:
        new_name =  re.sub('[0-9]','',file_name)
        os.rename(file_name,new_name)
