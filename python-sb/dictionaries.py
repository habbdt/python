

"""python dictionary"""

car_model = {
    "make1": "Ford",
    "model1": "Mustang",
    "year1": 1964,
    "make": "BMW",
    "model": "M5 BMW",
    "year": "2019"
}

#print (car_model)

# print all values in the dict
#for x in car_model:
#    print (x)

# print all keys in the dict
#for x in car_model:
#    print (car_model[x])

# display key-value pair
#for x, y in car_model.items():
#    print (x, y)

# check if key exists
if "model" in car_model:
    print ("The model exists in the dictionary")
else:
    print ("The car model does not exists in the dictionary")

