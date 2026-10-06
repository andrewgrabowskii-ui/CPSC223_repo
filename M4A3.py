# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment 3

games_dict = {}
for num in range(3):
    game = input(f"What is a great game? ")
    system = input(f"What system can I play that on? ")
    games_dict[game] = system

print(f"That's too many, let's get rid of one")
game_remove = input(f"What game should we remove? ")
if game_remove in games_dict:
    del games_dict[game_remove]
else:
    print(f"{game_remove} is not in the dictionary")

print("The new dictionary is:")
for games, systems in games_dict.items():
    print(f"You can play {games} on {systems}")