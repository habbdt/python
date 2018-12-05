#!/usr/bin/env python3

import sys
import os

'''
   sys.argv[0] - name of the script
   sys.argv[1] - first arguments
   sys.argv[n] - nth arguments
'''
script_name = sys.argv[0]
script_name = script_name.strip("./")
print ("Name of the python script is: ", os.path.join(os.getcwd(), script_name))
print ("My name is :", sys.argv[1])
print ("My age is : ", sys.argv[2])
print ("The lenght of the arguments is: ", len(sys.argv))
print ("The arguments passed by the scripts {}".format(script_name), str(sys.argv))
