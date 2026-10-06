# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 2 Assignment 3

uber_list = list(range(100, 201, 2))

start_num = int(input("What is the start of your slice? "))
end_num = int(input("What is the end of your slice? "))
data_list = uber_list[start_num : end_num]

total_int = 0
for num in range(0 , len(data_list)):
    total_int += data_list[num]

print(f"Your slice contains {len(data_list)} values and has an average value of {total_int / len(data_list)}")