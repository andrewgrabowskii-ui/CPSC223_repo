# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment EX2

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

food_count = {}
popular_food_count = 0
for food in food_dict.values():
    if food in food_count:
        food_count[food] += 1
    else:
        food_count[food] = 1

    if food_count[food] > popular_food_count:
        popular_food_count += 1
        popular_food = food

print(f"The most popular food is {popular_food}")