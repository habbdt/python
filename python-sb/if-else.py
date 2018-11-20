
""" if-else python"""




try:
    while True:
        x = int(input("Please enter first number: "))
        y = int(input("Please enter the second number: "))
        if x > y:
            print ("x is greater than y")
        elif x <y:
            print ("x is less than y")
        else:
            print ("x and y is equal")

except KeyboardInterrupt:
    print ('interrupted')

