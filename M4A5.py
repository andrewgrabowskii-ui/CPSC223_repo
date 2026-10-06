# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }

for name, food in food_dict.items():
    if food == '':
        fav_food = input(f"What is {name}'s favorite food? ")
        food_dict[name] = fav_food

print("Here are the favorite foods:")
for name, food in food_dict.items():
    print(f"{name}'s favorite food is {food}")