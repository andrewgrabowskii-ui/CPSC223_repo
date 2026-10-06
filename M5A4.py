# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']
finished_list = []

while orders_list:
    order = orders_list.pop()
    print(f"I made your {order}")
    finished_list.append(order)

print("Here are all the sandwiches I made:")
for item in finished_list:
    print(item)