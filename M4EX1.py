# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment EX1

cities_list = []

cities_list.append({
    'name': 'Anaheim',
    'pop': 100000,
    'state': 'California',
    'teams': ['Ducks', 'Angels']
})

cities_list.append({
    'name': 'Toronto',
    'pop': 250000,
    'state': 'Ontario',
    'teams': ['Maple Leafs', 'Blue Jays']
})

cities_list.append({
    'name': 'Los Angeles',
    'pop': 500000,
    'state': 'California',
    'teams': ['Dodgers', 'Kings', 'Lakers']
})

fav_team = input("What is your favorite team? ")
for cities in cities_list:
    for teams in cities['teams']:
        if teams == fav_team:
            print(f"If you like the {fav_team} you should move to {cities['name']}.")