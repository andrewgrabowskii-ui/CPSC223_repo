# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 6 Assignment 5

def comp_avg(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def comp_max(*numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

def comp_min(*numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min