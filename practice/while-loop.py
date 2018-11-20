
import sys

MY_PASSWORD = 'redhat'
password = input("Please enter the secret password:  ")
attempt_count = 1

while password != MY_PASSWORD:
    if attempt_count > 3:
        sys.exit("Invalid password entered too many times")
    password = input("Invalid password, try again:  ")
    attempt_count = attempt_count + 1
print ("Success")