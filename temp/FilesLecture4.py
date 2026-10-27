#try:
#    var1 = 5 / 0
#except ZeroDivisionError:
#    print(f"Tried to divide by zero")
#    var1 = 0
#else:
#    print(f"var1 worked fine")

import os.path
filename = "temp/junk.txt"

try:
    with open(filename) as file_object:
        text = file_object.read()
except FileNotFoundError:
    pass
else:
    print(text)

if os.path.exists(filename):
    with open(filename) as file_object:
        text = file_object.read()
    print(text)