#!/usr/bin/env python3

import os

def dir_contains(root_fs, list_fs):
    for root, dir, files in os.walk(root_fs):
        for name in files:
            file_const = os.path.join(root, name)
            path_validator = os.path.exists(file_const)
            print (path_validator)

    for element in list_fs:
        file_const1 = os.path.join(root_fs, element)
        path_validator1 = os.path.exists(file_const1)
        print (path_validator1)

        if path_validator == path_validator1:
            print (True)
        else:
            print (False)



dir_contains("/Users/hbustam/code/python/python-sb", ["os-walk.py", "while-loop.py", "nanometer.txt"])

