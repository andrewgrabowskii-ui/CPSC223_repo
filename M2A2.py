# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']

print(f"Here are the top Sega games:")
for game in range(0, len(g_list)):
    print(g_list[game])
g_list.remove(input("Which one do you think should be removed? "))
print(f"Here are the new top Sega games:")
for game in range(0, len(g_list)):
    print(g_list[game])