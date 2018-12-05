#!/usr/bin/env python3

'''simple ticketing system in python'''
import math
import sys
import argparse

# constant
TICKET_PRICE = 10

# for every transactions this service charge would be applied
SERVICE_CHARGE = 2

ticket_remaining = 100


# refactor code to meet business need
def calculate_cost(number_of_tickets):
    return  math.ceil(int(number_of_tickets) * TICKET_PRICE) + SERVICE_CHARGE

# run the code continiously until we ran out of tickets
while ticket_remaining >= 1:
    # output how many tickets are remaining using the ticket_remaining variable
    print ("There are {} tickets remaining".format(ticket_remaining))

    # gather the user's name and assign it to a new variable
    user_name = str(input("Please enter your Name: "))
    print ("Welcome to Superbads Ticket Booking Systems")
    print ("Hello {}".format(user_name), " ",  "Welcome Back!!!")

    # prompt the user by name and ask how many ticket they would like to purchase
    ticket_number_input = input("How many tickets you want to purchase, {}?   ".format(user_name))
    try:
        ticket_number = int(ticket_number_input)
        # Raise a ValueError if the request is for more tickets than available
        if ticket_number > int(ticket_remaining):
            raise ValueError("The number of available ticket is {}".format(ticket_remaining))
    except ValueError as err:
        print ("Please enter a valid a number. {}".format(err))
    else:
        # calculate the ticket cost
        total_cost = calculate_cost(ticket_number)
#        total_cost = math.ceil(int(ticket_number) * TICKET_PRICE)
        print ("The total cost of the ticket is ${}".format(total_cost))

        # prompt user if they want to proceed Y/N
        get_go = str(input("Do you want to proceed in placing orders? (Y/N) "))

        # if they want to proceed
        if get_go.upper() == "Y":
            print ("SOLD!!!!!")
            ticket_remaining -=  ticket_number
            print ("The number of ticket remaining is {}".format(ticket_remaining))
        else:
            print ("Thank you for your business".format(user_name))
            sys.exit()
print ("The tickets are sold out")
