# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 6 Assignment 3

def make_album(artist, album_title, numsongs='None'):
    album_dict = {'artist': artist, 'title': album_title, 'number of songs': numsongs}
    return album_dict

active = True
while active:
    album_str = input("What is the title of the album (or q for quit)? ")
    if album_str == 'q':
        break
    artist_str = input("What is the name of the artist? ")
    print(make_album(artist_str, album_str))