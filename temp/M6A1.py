# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 6 Assignment 1

def favorite_book(book_title):
    print(f"One of my favortie books is {book_title}")

for item in range(3):
    title = input("What is your favorite book? ")
    favorite_book(title)