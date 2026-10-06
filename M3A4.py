# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 3 Assignment 4

year_present = int(input("What year is it now? "))
year_born = int(input("What year were you born? "))

age_int = year_present - year_born
if (age_int % 2) == 0 and age_int < 50:
    print("This will be a great year")
elif (age_int % 2) != 0 and age_int < 50:
    print("This year will be tough")
elif age_int == 50:
    print("The future is unclear")
else:
    print("Death will come for you soon")