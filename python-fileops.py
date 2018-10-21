
""" python file ops"""

import os

f = open ("README.md", "at")
f.write ("\n #Python script repository\n")
f.close()

f = open("README.md", "rt")
print (f.read())

# check if hello-world.py existis

if os.path.exists("hello-world.py"):
    os.remove("hello-world.py")
else:
    print ("The file does not exists")

if os.path.isdir("new-code"):
    os.rmdir("new-code")
else:
    print ("the dir does not exists")
