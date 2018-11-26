#!/usr/bin/env python3

'''guess the number'''

# random library to generate random numbers
# sys library to utilize sys.exit()
import random
import sys

# guess a number between 1 to 10 - constant
LOWER_THRESHOLD = 1
UPPER_THRESHOLD = 10

print ("Welcome to Guess the Number Game!!!\n")
print ("You have to guess a number between 1 to 10\n")

# function to find the high or low value
def high_low(user_input_val, rand_number):
    diff_number = abs(int(rand_number) - int(user_input))
    print (diff_number)
    if diff_number >= 5:
        print ("The number you have guessed is too high!!!")
    else:
        print ("The number you have guessed is too low!!!!")

while True:
    try:
        user_input = int(input("Guess the number? "))
        rand_number = random.randint(LOWER_THRESHOLD, UPPER_THRESHOLD)
        if (user_input <= 0):
            raise ValueError ("Please enter a number greater than zero")
    except ValueError as err:
        print ("ERROR!!!! {}".format(err))
    else:
        if user_input == rand_number:
            print("You guessed right number\n")
            print("Exiting!!!")
            sys.exit()
        else:
            high_low(user_input, rand_number)