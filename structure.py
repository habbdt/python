
""" python script to create tree structure"""

import os

# check if "python-sb" dir exists or not
if os.path.isdir("python-sb"):
    print ("python-sb exists")
else:
    os.mkdir("python-sb")

# check whether README.md file is empty or not
if os.stat("README.md").st_size == 0:
    f = open("README.md", "wt")
    f.write("\n # Python git repo")
    f.close()
else:
    print ("the file README.md is not empty")

# read README.md file
fread = open("README.md", "rt")
print (fread.read())

# delete test dir
if os.path.isdir("test"):
    os.rmdir("test")
else:
    print ("No test dir exists")

# chaneg cwd to python-sb

os.chdir("python-sb")

if os.path.exists("hello-world.py"):
    print ("the file exists")
else:
    fread1 = open("hello-world.py", "wt")
    fread1.write("\n print hello-world \n")
    fread1.close()

# read hello-world.py file
fread2 = open("hello-world.py", "rt")
print (fread2.read())

