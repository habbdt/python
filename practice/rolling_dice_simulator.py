'''rolling dice simulator'''
'''https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/'''

import random

max_roll = 6
min_roll = 1

while True:
    user_input = input("Do you want to roll a dice?  (Y/N)")
    if user_input.lower() == "y":
        result = random.randint(min_roll,max_roll)
        print ("The output is {}".format(result))
    else:
        break
print ("exit")
