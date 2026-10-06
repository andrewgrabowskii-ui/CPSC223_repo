for x in range(5):
    print(x)

count_int = 0
while count_int < 5:
    print(count_int)
    count_int += 1

print()
print()

mylist = []
user_input = input("What is the next food choice? (or quit to end) ")
while user_input != 'quit':
    mylist.append(user_input)
    user_input = input("What is the next food choice? (or quit to end) ")

print(mylist)

keep_going = True
while keep_going:
    
    print(user_input.upper())
    if len(user_input) < 2:
        break

print(f"Done with the loop")