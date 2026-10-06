# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 4 Assignment 1

g_list = []

for num in range(3):
    game = input(f"What is your number {num + 1} favorite PlayStation game? ")
    g_list.append(game)

for index, value in enumerate(g_list):
    print(f"Your number {index + 1} favorite game was {value}")