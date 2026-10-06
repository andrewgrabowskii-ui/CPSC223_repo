# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name? ")
score_int = int(input("What is their score? "))
grade_letter = 'n/a'

if score_int >= 90:
    grade_letter = 'A'
elif score_int >= 80:
    grade_letter = 'B'
elif score_int >= 70:
    grade_letter = 'C'
elif score_int >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'

if grade_letter == 'A' or grade_letter == 'F':
    print(f"{student_name} earned an {grade_letter}")
else:
    print(f"{student_name} earned a {grade_letter}")