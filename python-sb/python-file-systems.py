#!/usr/bin/env python3

import os

def absolute(path_string, root_string):
    value_path = os.path.isabs(str(path_string))
#    value_root = os.path.isabs(str(root_string))
    if value_path == False:
        print (root_string + path_string)
    else:
        print (path_string)


absolute("projects/python_basics/", "/")
absolute("/home/kenneth/django", "C:\\")