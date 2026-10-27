# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# MidtermExam3

def make_book(book_title, book_author, book_length=100):
    book_dict = {'title':book_title, 'author':book_author, 'length':book_length}
    return book_dict

print(make_book("Ulysses","James Joyce",762))
print(make_book(book_title="The Odyssey",book_author="Homer"))