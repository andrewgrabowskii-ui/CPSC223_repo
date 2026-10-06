mylist = ["hot dogs", "hamburgers", "pizza"]

for num in range(0, len(mylist)):
    print(f"Food number {num+1} is {mylist[num]}")

for num, food in enumerate(mylist, start=1):
    print(f"Food number {num} is {food}")