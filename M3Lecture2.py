age = 20
if age != 21 or age == 19:
    print("age is 20")

toppings = ['mushrooms', 'onions', 'pineapple', 'peperoni', 'sausage']
request = input("What do you want on your pizza? ")
if request == "onions":
    print("Yum, onions")
elif request == 'pineapple':
    print("Awesome i don't care what people think about me anyway")
elif request == 'sausage':
    print("So spicy")
elif request in toppings:
    print("It's on the list")
else:
    print("No one loves me and I never get what I want I hate you")
