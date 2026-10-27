# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# MidtermExam2

book_list = []
polling_active = True

while polling_active:
    book = input(f"What is the next book to add to the list? (type 'q' to quit) ")
    if book == 'q':
        polling_active = False
    else:
        book_list.append(book)

print(f"The book list contains {book_list}")