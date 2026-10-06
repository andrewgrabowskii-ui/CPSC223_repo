# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 5 Assignment 2

start = int(input("Enter the start of the loop: "))
limit = int(input("Enter the limit of the loop: "))

current_val = start
print(f"The current value is {current_val}")
while current_val <= limit:
    current_val *= 2
    if current_val > limit:
        current_val = int(current_val / 2)
        break
    else:
        print(f"The current value is {current_val}")
print(f"The last value of current that was less than {limit} was {current_val}")