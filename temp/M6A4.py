# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 6 Assignment 4

def show_messages(message_list):
    while message_list:
        print(message_list.pop())

my_messages = []
active = True
while active:
    message = input("What is the next message? (type 'q' to quit) ")
    if message == 'q':
        active = False
    else:
        my_messages.append(message)

print("First time calling function")
show_messages(my_messages[:])
print("Second time calling function")
show_messages(my_messages[:])