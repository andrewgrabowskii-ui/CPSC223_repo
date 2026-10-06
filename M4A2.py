# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment 2

food_dict = {}
for index in range(3):
    food = input(f"What is good to eat? ")
    country = input(f"What country is that from? ")
    food_dict[food] = country

dish = input("What dish do you like? ")
if dish in food_dict:
    print(f"{dish} is from {food_dict[dish]}")
else:
    print(f"{dish} is not in the dictionary.")